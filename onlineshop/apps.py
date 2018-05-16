from django.apps import AppConfig
from watson import search as watson


class OnlineshopConfig(AppConfig):
    name = 'onlineshop'

    def ready(self):
        onlineshop_model = self.get_model("Product")
        watson.register(onlineshop_model)

