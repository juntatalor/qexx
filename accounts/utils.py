__author__ = 'Сергей'
from random import choice, sample
from django.contrib.auth import get_user_model, login, authenticate
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

from accounts. models import UsernameAddition


def register_user(request, email, username=None, password=None):
    user_model = get_user_model()
    if not password:
        password = user_model.objects.make_random_password(8)

    if not username:
        # Делаем юзернейм из емейла и сразу делаем уникальным
        username = unique_username(email.split("@")[0], 0)[0]

    # Создаем пользователя...
    new_user = user_model.objects.create_user(username, email, password)

    # ...и сразу логинимся им в систему
    login(request, authenticate(email=email, password=password))

    return new_user, password


def update_userinfo():
    pass


def send_registration_email(user, password):
    send_mail('Спасибо за регистрацию!',
            get_template('accounts/email/registration.html').render(
                Context({
                    'username': user.username,
                    'password': password,
                    'email_token': user.email_token
                })
            ),
            'head@ardushop.com',
            [user.email,],
            fail_silently=True
        )


'''
Принимает имя пользователя
Вторым параметром принимает число
В первом случае возвращает список, содержащий не более <count> гарантированно уникальных юзернеймов
Если count==0, возвращает список из одного гарантированно уникального юзернейма
'''


def unique_username(form_username, count):
    user_model = get_user_model()
    unique_user_names = []
    if count == 0:
        if not user_model.objects.filter(username__iexact=form_username).exists():
            unique_user_names.append(form_username)
            return unique_user_names
        # Рандомизируем логин
        postfix = get_random_string()[0:2]
        return unique_username(form_username + postfix, 0)
    else:
        # Формируем список уникальных имен
        for addition in UsernameAddition.objects.all():
            if addition.position == UsernameAddition.LEFT:
                unique_user_names.append(addition.name + '_' + form_username)
            elif addition.position == UsernameAddition.RIGHT:
                unique_user_names.append(form_username + '_' + addition.name)
            else:
                if choice([UsernameAddition.LEFT, UsernameAddition.RIGHT]) == UsernameAddition.LEFT:
                    unique_user_names.append(addition.name + '_' + form_username)
                else:
                    unique_user_names.append(form_username + '_' + addition.name)

        # Если база добавок не заоплнена
        if len(unique_user_names) == 0:
            # Возвращаем полностью случайное имя на основе имеющегося
            return unique_username(form_username, 0)

        # Удаляем из списка уникальных имена, которые уже есть в базе
        # ToDo: возможно, множественный __iexact работает быстрее. __iin не реализован
        for existing_name in user_model.objects.filter(username__iregex=r'^(' + '|'.join(unique_user_names) + ')$'):
            unique_user_names.remove(existing_name.username)

        # Возвращаем count или сколько получилось случайных уникальных имен
        return sample(unique_user_names, min(len(unique_user_names), count))


