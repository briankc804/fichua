from django.apps import AppConfig


class MyfichuaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myfichua'
    
    
    # def ready(self):
    #     import myfichua.signals