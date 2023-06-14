from django.db.models import Count



from .models import *

menu = [
    {"title": "VirtAssis®", "url_name": "home"},
]

apps = [
    {"title": "Contacts", "url_name": "home"},
    {"title": "Notes", "url_name": "home"},
    {"title": "Files", "url_name": "add_contact"},
    {"title": "News", "url_name": "home"},
]


class DataMixin:
    paginate_by =8

    def get_user_context(self, **kwargs):
        context = kwargs

        user_apps = apps.copy()
        if not self.request.user.is_authenticated:
            user_apps.pop(0)
            user_apps.pop(0)
            user_apps.pop(0)

        context['apps'] = user_apps

        if 'app_selected' not in context:
            context['app_selected'] = 0

        context["menu"] = menu

        return context