from rest_framework.urlpatterns import format_suffix_patterns
from django.urls.conf import path
from .views import greeting

urlpatterns = [
    path(r'', greeting)
]

urlpatterns = format_suffix_patterns(urlpatterns)
