from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    
    # we need to import signals to make the signals work
    def ready(self):
        import account.signals
 