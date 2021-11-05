from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls', namespace='quiz')),
    path('account/', include('account.urls', namespace='account')),
    path('get_auth_token', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
