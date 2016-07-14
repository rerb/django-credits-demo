""" urls.py for django_credits_demo project.
"""
from django.conf.urls import url
from django.contrib import admin

from .views import DemoView


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^demo/", DemoView.as_view(), name="demo_view")
]
