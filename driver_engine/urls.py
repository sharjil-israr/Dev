from django.urls import path, include
from . import views

urlpatterns = [
    path('drivers/', views.drivers, name='drivers'),
    path('driver-details/<int:driver_id>/', views.driver_details, name='driver_details'),
    path('add-driver-details/', views.add_driver_details, name='add_driver_details'),
    path('edit-driver-details/<int:driver_id>/', views.edit_driver_details, name='edit_driver_details'),
    path('delete-driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
    path('add-driver-recruitment-details/<int:driver_id>/', views.add_driver_recruitment_details, name='add_driver_recruitment_details'),
    path('edit-driver-recruitment-details/<int:driver_id>/', views.edit_driver_recruitment_details, name='edit_driver_recruitment_details'),

    path('driver-hiring/', views.driver_hiring, name='driver_hiring'),
    path('add-driver-behaviour-test/<int:driver_id>/', views.add_driver_behaviour_details, name='add_driver_behaviour_details'),
    path('edit-driver-behaviour-test/<int:driver_id>/', views.edit_driver_behaviour_details, name='edit_driver_behaviour_details'),

    path('add-driver-documents/<int:driver_id>/', views.add_driver_documents, name='add_driver_documents'),
    path('change-driver-status/<int:driver_id>/', views.change_driver_status, name='change_driver_status'),

    path('driver-leaves/', views.driver_leaves, name='driver_leaves'),
    path('add-driver-leave/', views.add_driver_leave, name='add_driver_leave'),
    path('edit-driver-leave/<int:leave_id>/', views.edit_driver_leave, name='edit_driver_leave'),
    path('delete-driver-leave/<int:leave_id>/', views.delete_driver_leave, name='delete_driver_leave'),
    path('review-driver-leave/<int:leave_id>/', views.review_driver_leave, name='review_driver_leave'),
    path('approve-reject-driver-leave/<int:leave_id>/', views.approve_reject_driver_leave, name='approve_reject_driver_leave'),
    
]
