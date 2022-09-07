from django.urls import path

from . import views

urlpatterns = [
    path('agencies/', views.index, name='index'),
    path('agencies/<int:agency_id>/', views.agency_details, name='detail')
]
