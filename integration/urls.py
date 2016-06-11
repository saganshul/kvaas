from django.conf.urls import url
from . import views
urlpatterns = [
		url(r'^generate_token/$', views.generate_firebase_token, name='generate_token'),
    ]
