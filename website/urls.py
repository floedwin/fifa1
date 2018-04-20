from django.conf.urls import patterns, url
from website import views
urlpatterns =[
url(r'^$', views.index, name='index'),
url(r"^about/$", views.about, name='about'),
url(r"^calender/$", views.calender, name='calender'),
url(r"^gallery/$", views.gallery, name='gallery'),
url(r"^projects/$", views.projects, name='projects'),
url(r"^register/$", views.register, name='register'),
    # ADD NEW PATTERN!
url(r"^login/$", views.user_login, name='login'),
url(r"^restricted/", views.restricted, name='restricted'),
url(r"^logout/$", views.user_logout, name='logout'),
]