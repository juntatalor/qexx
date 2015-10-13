from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class MyModelBackend(ModelBackend):
    """
    Changes authentication method
    """

    def authenticate(self, username=None, email=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            if email:
                user = user_model.objects.get(email=email)
            else:
                user = user_model.objects.get(username=username)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            user_model().set_password(password)