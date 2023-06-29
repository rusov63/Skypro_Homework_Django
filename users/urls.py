from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileView, UserRegisterView, EmailConfirmationSentView, UserConfirmEmailView, \
    EmailConfirmView, EmailConfirmationFailedView, generate_new_password, backup_pass


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'), # войти
    path('logout/', LogoutView.as_view(), name='logout'), # выйти
    path('register/', UserRegisterView.as_view(), name='register'), # регистрация
    path('profile/', ProfileView.as_view(), name='profile'), # профиль
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmView.as_view(), name='email_verified'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('generate_new_password/', generate_new_password, name='generate_new_password'), # сгенерировать пароль
    path('backup_pass/', backup_pass, name='backup_pass'), # забытый пароль
]
