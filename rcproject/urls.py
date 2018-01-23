from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views  # 이 줄 추가
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from rcapp import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('rcapp.urls')),
    #url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^uploads/',include('uploads.urls'), name='uploads'),
    url(r'^join/$', views.UserCreate.as_view(),name='account-create'),
    url(r'^api-token-auth/', obtain_auth_token),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
