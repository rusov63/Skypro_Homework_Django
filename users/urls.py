from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileView, generate_new_password, UserRegisterView, EmailConfirmationSentView, \
    UserConfirmEmailView, \
    EmailConfirmView, EmailConfirmationFailedView, UserForgotPasswordView, UserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'), # войти
    path('logout/', LogoutView.as_view(), name='logout'), # выйти
    path('register/', UserRegisterView.as_view(), name='register'), # регистрация
    path('profile/', ProfileView.as_view(), name='profile'), # профиль
    path('profile/genpassword/', generate_new_password, name='generate_new_password'), # сгенерировать пароль

    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'), #Письмо подтверждения отправлено
    path('confirm-email/<str:token>/', UserConfirmEmailView.as_view(), name='email_verified'), #работа с токеном
    path('email-confirmed/', EmailConfirmView.as_view(), name='email_verified'), #Электронная почта подтверждена
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'), #Ошибка подтверждения по электронной почте

    path('password_reset/', UserForgotPasswordView.as_view(), name='password_reset'),  # забыли пароль?
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
