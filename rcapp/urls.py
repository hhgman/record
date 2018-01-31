from django.conf.urls import url,include
from rcapp import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # url(r'^api-token-auth/', obtain_auth_token),
    url(r'^recordings/$',
        views.RecordingList.as_view(),
        name=views.RecordingList.name),
    url(r'^recordings/(?P<pk>[0-9]+)/$',
        views.RecordingDetail.as_view(),
        name=views.RecordingDetail.name),
    url(r'^userinfo/$',
        views.InformationList.as_view(),
        name=views.InformationList.name),
    url(r'^users/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
    url(r'^statics/$',
        views.Text.as_view(),
        name=views.Text.name),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
