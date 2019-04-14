from django.apps import AppConfig


class SignInConfig(AppConfig):
    name = 'sign_in'

    def ready(self):
        import sign_in.signals
