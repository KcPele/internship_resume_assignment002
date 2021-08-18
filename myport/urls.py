from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
   path('', views.index, name="index"),
   path('email-contact/', views.email_contact, name='email_contact'),
   path('email-subscribe', views.email_subscribe, name='email_subscribe'),
]

urlpatterns += staticfiles_urlpatterns
