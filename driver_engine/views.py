from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from driver_engine.forms import *
from driver_engine.models import *
from accounts_engine.decorators import is_user_allowed


@is_user_allowed
@login_required(login_url='/account/login')
def drivers(request):
    # show selected drivers
    driver_list = Driver.objects.filter(hiring_status = '2')
    return render(request, 'driver_engine/drivers.html', {
        'driver_list': driver_list,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def driver_details(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    try:
        driver.driver_recruitment = DriverRecruitment.objects.get(driver = driver)
    except:
        driver.driver_recruitment = None

    try:
        driver.behaviour_test = DriverBehaviourTest.objects.get(driver = driver)
    except:
        driver.behaviour_test = None



    return render(request, 'driver_engine/driver_details.html', {
        'driver': driver,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def add_driver_details(request):
    driver_form = DriverForm(initial = {'created_by': request.user})

    if request.method == 'POST':
        driver_form = DriverForm(request.POST, request.FILES)
        if driver_form.is_valid():
            driver_form = driver_form.save()
            messages.success(request, 'Driver added.')
            return redirect('drivers')
    return render(request, 'driver_engine/add_driver_details.html', {
        'driver_form': driver_form,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def edit_driver_details(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    edit_driver_form = DriverForm(instance = driver)

    if request.method == 'POST':
        edit_driver_form = DriverForm(request.POST, instance = driver)
        if edit_driver_form.is_valid():
            edit_driver_form = edit_driver_form.save()
            messages.warning(request, 'Driver updated.')
            return redirect('drivers')

    return render(request, 'driver_engine/edit_driver_details.html', {
        'edit_driver_form': edit_driver_form,
        'driver': driver,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def delete_driver(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    driver.delete()
    messages.error(request, 'Driver was deleted.')
    return redirect('drivers')


@is_user_allowed
@login_required(login_url='/account/login')
def add_driver_recruitment_details(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    driver_recruitment_form = DriverRecruitmentForm(initial = {'driver': driver, 'created_by': request.user})

    if request.method == 'POST':
        driver_recruitment_form = DriverRecruitmentForm(request.POST)
        if driver_recruitment_form.is_valid():
            driver_recruitment_form = driver_recruitment_form.save()
            messages.success(request, 'Driver recruitment details added.')
            return redirect('driver_details', driver_id)


    return render(request, 'driver_engine/add_driver_recruitment_details.html', {
        'driver_recruitment_form': driver_recruitment_form,
        'driver': driver,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def edit_driver_recruitment_details(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    driver_recruitment = DriverRecruitment.objects.get(driver = driver)
    edit_driver_recruitment_form = DriverRecruitmentForm(instance = driver_recruitment)

    if request.method == 'POST':
        edit_driver_recruitment_form = DriverRecruitmentForm(request.POST, instance = driver_recruitment)
        if edit_driver_recruitment_form.is_valid():
            edit_driver_recruitment_form = edit_driver_recruitment_form.save()
            messages.warning(request, 'Driver recruitment details updated.')
            return redirect('driver_details', driver_id)


    return render(request, 'driver_engine/edit_driver_recruitment_details.html', {
        'edit_driver_recruitment_form': edit_driver_recruitment_form,
        'driver': driver,
        'driver_recruitment': driver_recruitment,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def driver_hiring(request):
    driver_list = Driver.objects.filter(hiring_status__in = ['0', '1', '3'] )
    for each in driver_list:
        each.get_hiring_status()
    return render(request, 'driver_engine/driver_hiring.html', {
        'driver_list': driver_list,
    })



@is_user_allowed
@login_required(login_url='/account/login')
def add_driver_behaviour_details(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    add_driver_behaviour_test_form = DriverBehaviourTestForm(initial = {'driver': driver, 'created_by': request.user})
    
    if request.method == 'POST':
        add_driver_behaviour_test_form = DriverBehaviourTestForm(request.POST)
        if add_driver_behaviour_test_form.is_valid():
            add_driver_behaviour_test_form = add_driver_behaviour_test_form.save()
            messages.success(request, 'Driver behaviour details added.')
            return redirect('driver_details', driver_id)

    return render(request, 'driver_engine/add_driver_behaviour_details.html', {
        'add_driver_behaviour_test_form': add_driver_behaviour_test_form,
        'driver': driver,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def edit_driver_behaviour_details(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    driver_behaviour =  DriverBehaviourTest.objects.get(driver = driver)
    edit_driver_behaviour_test_form = DriverBehaviourTestForm(instance = driver_behaviour)

    if request.method == 'POST':
        edit_driver_behaviour_test_form = DriverBehaviourTestForm(request.POST, instance = driver_behaviour)
        if edit_driver_behaviour_test_form.is_valid():
            edit_driver_behaviour_test_form = edit_driver_behaviour_test_form.save()
            messages.warning(request, 'Driver behaviour details updated.')
            return redirect('driver_details', driver_id)


    return render(request, 'driver_engine/edit_driver_behaviour_details.html', {
        'edit_driver_behaviour_test_form': edit_driver_behaviour_test_form,
        'driver': driver,
        'driver_behaviour': driver_behaviour,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def add_driver_documents(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    driver_recruitment = DriverRecruitment.objects.get(driver = driver)
    driver_document_form = DriverDocumentForm(instance = driver)
    driver_recruitment_document_form = DriverRecruitmentDocumentForm(instance = driver_recruitment)

    if request.method == 'POST':
        driver_document_form = DriverDocumentForm(request.POST, request.FILES, instance = driver)
        driver_recruitment_document_form = DriverRecruitmentDocumentForm(request.POST, request.FILES, instance = driver_recruitment)
        
        if driver_document_form.is_valid():
            driver_document_form = driver_document_form.save()
            messages.success(request, 'Driver Document Added.')

        if driver_recruitment_document_form.is_valid():
            driver_recruitment_document_form = driver_recruitment_document_form.save()
            messages.success(request, 'Driver Recruitment Document Added.')
        return redirect('driver_details', driver_id)


    return render(request, 'driver_engine/add_driver_documents.html', {
        'driver_document_form': driver_document_form,
        'driver_recruitment_document_form': driver_recruitment_document_form,
        'driver': driver,
    })



@is_user_allowed
@login_required(login_url='/account/login')
def add_driver_past_verification(request, driver_id):
    return HttpResponse('asd')


@is_user_allowed
@login_required(login_url='/account/login')
def edit_driver_past_verification(request, driver_id):
    return HttpResponse('asd')


@is_user_allowed
@login_required(login_url='/account/login')
def change_driver_status(request, driver_id):
    driver = Driver.objects.get(id = driver_id)
    driver_status_form = DriverStatusForm(instance = driver)
    
    if request.method == 'POST':
        driver_status_form = DriverStatusForm(request.POST, instance = driver)
        if driver_status_form.is_valid():
            # driver status can only be set to active if driver's hiring status is selected
            hiring_status = request.POST['hiring_status']
            status = request.POST['status']
            if status == '1':
                if hiring_status == '2':
                    pass
                else:
                    messages.error(request, 'Change Hiring status of this Driver before activating this driver. Only selected drivers can be made as active')
                    return redirect('driver_details', driver_id)

            driver_status_form = driver_status_form.save()
            messages.success(request, 'Driver status updated.')
            return redirect('driver_details', driver_id)

    return render(request, 'driver_engine/change_driver_status.html', {
        'driver_status_form': driver_status_form,
        'driver': driver,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def driver_leaves(request):
    driver_leaves = DriverLeave.objects.all()
    return render(request, 'driver_engine/driver_leaves.html',{
        'driver_leaves': driver_leaves,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def add_driver_leave(request):
    driver_leave_form = DriverLeaveForm(initial = {'created_by': request.user})

    if request.method == 'POST':
        driver_leave_form = DriverLeaveForm(request.POST)

        if driver_leave_form.is_valid():
            driver_leave_form = driver_leave_form.save()
            messages.success(request, 'Driver leave added.')
            return redirect('driver_leaves')

    return render(request, 'driver_engine/add_driver_leave.html', {
        'driver_leave_form': driver_leave_form,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def edit_driver_leave(request, leave_id):
    leave = DriverLeave.objects.get(id = leave_id)
    driver_leave_form = DriverLeaveForm(instance = leave)
    
    if request.method == "POST":
        driver_leave_form = DriverLeaveForm(request.POST, instance = leave)
        if driver_leave_form.is_valid():
            driver_leave_form = driver_leave_form.save()
            messages.warning(request, 'Driver leave updated.')
            return redirect('driver_leaves')

    return render(request, 'driver_engine/add_driver_leave.html', {
        'driver_leave_form': driver_leave_form,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def delete_driver_leave(request, leave_id):
    leave = DriverLeave.objects.get(id = leave_id)
    leave.delete()
    messages.error(request, 'Driver leave deleted.')
    return redirect('driver_leaves')


@is_user_allowed
@login_required(login_url='/account/login')
def review_driver_leave(request, leave_id):
    leave = DriverLeave.objects.get(id = leave_id)

    return render(request, 'driver_engine/review_driver_leave.html', {
        'leave': leave,
    })


@is_user_allowed
@login_required(login_url='/account/login')
def approve_reject_driver_leave(request, leave_id):
    leave = DriverLeave.objects.get(id = leave_id)
    driver = Driver.objects.get(id = leave.driver.id)
    action = request.GET.get('action')
    # TODO : need to remove the driver from the vehicles before approving leave
    if action == 'approve':
        leave.status = '1'
        leave.save()
        driver.status = '0'
        driver.save()
        messages.success(request, 'Driver leave approved. This Driver is now inactive in system')
        return redirect('driver_leaves')
    
    if action == 'reject':
        leave.status = '2'
        leave.save()
        messages.error(request, 'Driver leave Rejected.')
        return redirect('driver_leaves')
