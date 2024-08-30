from django.urls import path
from .views import *

urlpatterns = [
    
    path('login/', admin_login, name='admin_login'),
    path('logout/', logout, name='logout'),
    
    path('dashboard/', dashboard_view, name='dashboard'),
    
    # job openings module
    path('add_job_openings/', add_job_openings_view, name='add_job_openings'),
    path('manage_job_openings/', manage_job_openings_view, name='manage_job_openings'),
    path('delete_job_openings/<int:id>/', delete_job_openings_view, name='delete_job_openings'),
    path('update_job_openings/<int:id>/', update_job_openings_view, name='update_job_openings'),
    path('delete_all_job_openings/', delete_all_job_openings_view, name='delete_all_job_openings'),
    
    path('update_job_opening_status/', update_job_opening_status, name='update_job_opening_status'),
    
    # # API for login and logout
    path('api/login/', user_login, name='login'),
    path('api/logout/', user_logout, name='api-logout'),
    
    # search course details
    path('search_job_openings/', SearchJobOpeningsResultsView.as_view(), name='search_job_openings'),
    
    # API for course module
    path('api/job_openings/', JobOpeningsListCreateView.as_view(), name='job_openings_list_create'),
    path('api/job_openings/<int:pk>/', JobOpeningsDetailView.as_view(), name='job_openings_detail'),
    path('api/update_job_openings/<int:pk>/', JobOpeningsUpdateView.as_view(), name='job_openings_update'),
    path('api/delete_job_openings/<int:pk>/', JobOpeningsDeleteView.as_view(), name='job_openings_delete'),
]