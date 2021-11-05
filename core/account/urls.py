from django.urls import path
from account.views import UserRegistration

app_name = 'account'

urlpatterns = [
    path('api/registration', UserRegistration.as_view(), name='registration'),

]