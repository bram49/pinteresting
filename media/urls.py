
from django.conf.urls import url
from . import views

app_name = 'media'

urlpatterns = [
    # /media/
    url(r'^$', views.login_user, name='index'),
    url(r'^index/', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /media/{picture_id)/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /media/picture/add/
    url(r'picture/add/$', views.PictureCreate.as_view(), name='picture_form'),

    # /media/picture/(picture_id)/
    url(r'picture/(?P<pk>[0-9]+)/$', views.PictureUpdate.as_view(), name='picture_update'),

    # /media/picture/(picture_id)/
    url(r'picture/(?P<pk>[0-9]+)/delete/$', views.PictureDelete.as_view(), name='picture_delete'),

]

