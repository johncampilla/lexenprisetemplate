from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('client', views.client_list, name='client_list'),
    path('folders', views.folder_list, name='folder_list'),
    path('matters', views.matter_list, name='matter_list'),
    path('activity', views.activity_list, name='activity_list'),
    path('duedate', views.duedate_list, name='duedate_list'),
    path('AR', views.AR_list, name='AR_list'),
    path('doclist', views.document_list, name='document_list'),

]

