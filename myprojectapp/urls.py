from django.conf.urls import url, include
from django.urls import path
from myprojectapp.views import index
from myprojectapp.views import mappage

app_name='myprojectapp'
urlpatterns=[
	path('',index,name='index'),
	path('map/',mappage,name='mappage1'),
]