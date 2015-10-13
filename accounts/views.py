from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from accounts.forms import SignupForm, ProfileForm
from accounts.utils import register_user, unique_username, send_registration_email

# Create your views here.


@login_required
@require_http_methods(['GET', 'POST'])
def profile(request):
    """
    Отображение / обновление профиля пользователя
    :param request:
    :return:
    """

    if request.method == 'GET':
        form = ProfileForm(instance=request.user)
        return render(request, 'accounts/profile.html', {'form': form})

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        success = False
        if form.is_valid():
            form.save()
            success = True
        return render(request, 'accounts/profile.html', {'form': form,
                                                         'success': success})


@require_http_methods(['GET', 'POST'])
def signup(request):
    """
    Отображение формы регистрации пользователя / регистрация пользователя
    :param request:
    :return:
    """

    # Для авторизованных пользователей регистрация недоступна
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('products:index'))

    signup_form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if not signup_form.is_valid():
            if signup_form.username_not_unique:
                return render(request, 'accounts/signup.html', {'form': signup_form,
                                                                'usernames': unique_username(request.POST['username'],
                                                                                             5)})
            return render(request, 'accounts/signup.html', {'form': signup_form})
        # Регистрируем пользователя
        user, password = register_user(request,
                                       signup_form.cleaned_data['email'],
                                       signup_form.cleaned_data['username'],
                                       signup_form.cleaned_data['password'])
        send_registration_email(user, password)
        return HttpResponseRedirect(reverse('accounts:profile'))

    if request.method == 'GET':
        return render(request, 'accounts/signup.html', {'form': signup_form})
