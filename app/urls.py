from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'profile/edit$', views.edit_profile, name='edit'),
    url(r'update$',views.updates, name='updates'),
    url(r'updates/new$', views.new_update, name='new_update')
    ,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)