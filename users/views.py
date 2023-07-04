#from django.contrib.auth.forms import UserCreationForm
import random

from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from users.models import User
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, CreateView, TemplateView
from django.conf import settings

from users.forms import UserRegisterForm, UserProfileForm
#from django.views.generic import CreateView, UpdateView



class UserRegisterView(CreateView):
    """Класс региcтрации пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались. Проверьте почту для активации!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.token = default_token_generator.make_token(user)
        activation_url = reverse_lazy(
            'users:confirm_email', kwargs={'token': user.token}
        )
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения регистрации перейдите по ссылке: http://localhost:8000/{activation_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        user.save()
        return redirect('users:email_confirmation_sent')


class UserConfirmEmailView(View):
    def get(self, request, token):
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            return redirect('users:email_confirmation_failed')

        user.is_active = True
        user.token = None
        user.save()
        return redirect('users:login')

class EmailConfirmationSentView(TemplateView):
    """Письмо подтверждения отправлено"""
    template_name = 'users/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


class EmailConfirmView(TemplateView):
    """Электронная почта подтверждена"""
    template_name = 'users/email_verified.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес активирован'
        return context

class EmailConfirmationFailedView(TemplateView):
    """Ошибка подтверждения по электронной почте"""
    template_name = 'users/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес не активирован'
        return context




class ProfileView(UpdateView):
    """Профиль зарегистрированного пользователя"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/users_form.html'

    def get_object(self, queryset=None):
        """метод который забирает - pk, его не надо указывать в урлах"""
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Страница пользователя: {self.object.email}'
        return context


def generate_new_password(request):
    """Сброс пароля зарегистрированного пользователя в профиле"""
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:index'))


def password_reset_form(request):
    """Восстановление пароля в форме входа (забыли пароль)"""
    # new_password = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    # send_mail(
    #     subject='Вы сменили пароль',
    #     message=f'Ваш новый пароль: {new_password}',
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[request.user.email]
    # )
    # if request.method == "POST":
    #     email = request.POST.get('email')
    #     generate_new_password(email)
    request.user.save()
    return render(request, ('catalog:index'))



    # def form_valid(self, form):
    #     """Отправка письма при регистрации нового пользователя"""
    #     new_user = form.save()
    #     send_mail(
    #         subject='Поздравляем с регистрацией!!!',
    #         message='Учебный проект по фреймворку Django от SkyPro. Ваша почта настроена - smtp yahoo',
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[new_user.email]
    #     )
    #     return super().form_valid(form)






