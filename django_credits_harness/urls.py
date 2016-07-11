""" urls.py for django_credits_harness project.
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^credits/", include("django_credits.urls"))
]
