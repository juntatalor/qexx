import re

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm

from common.validators import PhoneValidator

allowed_username = re.compile(r"^[a-zA-Z0-9_]+$")


class MyAuthenticationForm(AuthenticationForm):
    """
    Changes authentication method from username to email
    """

    username = None

    username_email = forms.CharField(
        label="Email \ login",
        widget=forms.TextInput(),
        required=True)

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        username_email = self.cleaned_data.get('username_email')
        password = self.cleaned_data.get('password')

        if username_email and password:
            if username_email.find('@') > 0:
                self.user_cache = authenticate(email=username_email, password=password)
            else:
                self.user_cache = authenticate(username=username_email, password=password)

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': 'email'},
                )
            else:
                self.confirm_login_allowed(self.user_cache)


class SignupForm(forms.Form):

    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(),
        required=True)

    username = forms.CharField(
        label="Имя пользователя",
        max_length=30,
        widget=forms.TextInput(),
        required=False)

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(render_value=False),
        required=False)

    def clean_username(self):
        if len(self.cleaned_data["username"]):
            # Соответствие юзернейма шаблону
            if not allowed_username.search(self.cleaned_data["username"]):
                raise forms.ValidationError("В имени пользователя допустимо использовать латинские символы, цифры и _")
            # Уникальность юзернейма
            user = get_user_model()
            if user.objects.filter(username__iexact=self.cleaned_data["username"]).exists():
                raise forms.ValidationError("Ой! Это имя пользователя уже используется. Попробуйте ввести другое.")
        return self.cleaned_data["username"]

    def clean_email(self):
        # Уникальный емейл
        user = get_user_model()
        if user.objects.filter(email__iexact=self.cleaned_data["email"]).exists():
            raise forms.ValidationError("Этот email уже используется")
        return self.cleaned_data["email"]

    def clean_password(self):
        # Слишком короткие пароли
        password_len = len(self.cleaned_data["password"])
        if 0 < password_len <= 4:
            raise forms.ValidationError("Длина пароля должна быть не менее 5 символов")
        return self.cleaned_data["password"]


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone'] = forms.CharField(label='Телефон',
                                               required=False,
                                               validators=[PhoneValidator(self.data.get('country', None))])

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'middle_name', 'country', 'address', 'phone']