from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import datetime





class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        try:
            user_detail = UserDetail.objects.get(user = self)
            return user_detail.__str__()
        except:
            return str(self.email)

    def get_user_detail(self):
        user_detail = UserDetail.objects.get(user = self)
        return user_detail

class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name) + '-' + str(self.location)


class Role(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    def get_permissions_of_role(self):
        role_wise_permission = RoleWisePermission.objects.get(role = self)
        return role_wise_permission.permission.all()


class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    def get_permissions_of_group(self):
        group_wise_permission = GroupWisePermission.objects.get(group = self)
        return group_wise_permission.permission.all()


class Permission(models.Model):
    SECTION_LIST = [
    ('-1', 'others'),
    ('0', 'profile'),
    ('1', 'setting'),
    ('2', 'driver'),
    ('3', 'vehicle'),
    ('4', 'journey'),
    ('5', 'hsse'),
    ('6', 'reports'),
    ]
    section = models.CharField(max_length = 10,choices = SECTION_LIST,default = '0')
    parent = models.ForeignKey('Permission', null=True,blank=True, on_delete=models.SET_NULL)
    url_name = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.get_section_display())+ '-' + str(self.url_name).replace('_', ' ')

    def get_section(self):
        return self.section


class RoleWisePermission(models.Model):
    # TODO should change role and group in below model to OneToOneField in future to avoid conflicts
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ManyToManyField('Permission', related_name='role_permissions')

    def __str__(self):
        return str('permissions of Role: ' + self.role.name)

    def get_permissions_of_role(self, role):
        permission_list = []
        roles_wise_permission = RoleWisePermission.objects.get(role = role)
        permissions = roles_wise_permission.permission.all()
        for each in permissions:
            permission_list.append(each)
        return permission_list

    def get_urls_of_role_as_list(self, role):
        url_list = []
        permission_list = get_permissions_of_role(self, role)
        for each in permission_list:
            url_list.append(each.url_name)
        return url_list


class GroupWisePermission(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ManyToManyField('Permission', related_name='group_permissions')

    def __str__(self):
        return str('permissions of Group: ' + self.group.name)

    def get_permissions_of_group(self, group):
        permission_list = []
        groups_wise_permission = GroupWisePermission.objects.get(group = group)
        permissions = groups_wise_permission.permission.all()
        for each in permissions:
            permission_list.append(each)
        return permission_list

    def get_urls_of_group_as_list(self, group):
        url_list = []
        permission_list = get_permissions_of_group(self, group)
        for each in permission_list:
            url_list.append(each.url_name)
        return url_list


class UserDetail(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    mobile_number = models.CharField(max_length = 10)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    role = models.ManyToManyField('Role', related_name='roles')
    group = models.ManyToManyField('Group', related_name='groups')
    custom_permission = models.ManyToManyField('Permission', related_name='custom_permissions')


    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    def can_access_setting_section(self):
        roles_wise_permission = RoleWisePermission.objects.filter(role__in = self.role.all())
        status = False
        for each in roles_wise_permission:
            permissions = each.permission.all()
            for each2 in permissions:
                # 1 is for setting section
                if each2.section == '1':
                    status = True
        return status

    def can_access_driver_section(self):
        roles_wise_permission = RoleWisePermission.objects.filter(role__in = self.role.all())
        status = False
        for each in roles_wise_permission:
            permissions = each.permission.all()
            for each2 in permissions:
                # 2 is for driver section
                if each2.section == '2':
                    status = True
        return status

    def can_access_vehicle_section(self):
        roles_wise_permission = RoleWisePermission.objects.filter(role__in = self.role.all())
        status = False
        for each in roles_wise_permission:
            permissions = each.permission.all()
            for each2 in permissions:
                # 3 is for vehicle section
                if each2.section == '3':
                    status = True
        return status

    def can_access_journey_section(self):
        roles_wise_permission = RoleWisePermission.objects.filter(role__in = self.role.all())
        status = False
        for each in roles_wise_permission:
            permissions = each.permission.all()
            for each2 in permissions:
                # 4 is for journey section
                if each2.section == '4':
                    status = True
        return status

    def can_access_hsse_section(self):
        roles_wise_permission = RoleWisePermission.objects.filter(role__in = self.role.all())
        status = False
        for each in roles_wise_permission:
            permissions = each.permission.all()
            for each2 in permissions:
                # 5 is for journey section
                if each2.section == '5':
                    status = True
        return status

    def get_all_roles(self):
        return self.role.all()

    def get_all_groups(self):
        return self.group.all()

    def get_all_custom_permissions(self):
        return self.custom_permission.all()


class Task(models.Model):
    task = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    task_for_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='task_for_users')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    STATUS_LIST = [
    ('0', 'Pending'),
    ('1', 'In Progress'),
    ('2', 'Completed'),
    ('3', 'Not Applicable'),
    ]
    status = models.CharField(max_length = 10, choices = STATUS_LIST, default = '0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.task)

    def get_status_colour(self):
        if self.status == '0':
            return 'warning'
        if self.status == '1':
            return 'info'
        if self.status == '2':
            return 'success'
        if self.status == '3':
            return 'secondary'

    def is_due(self):
        today = datetime.datetime.today()
        if today > self.end_date:
            return True
        else:
            return False
