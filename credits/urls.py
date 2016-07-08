""" urls.py for django-credits app.
"""
from django.conf.urls import url

from credits.views import CreditsJSONView, CreditsDemoView


urlpatterns = [
    url(r"^demo/", CreditsDemoView.as_view(), name="credits_demo_view"),
    url(r"^json/", CreditsJSONView, name="credits_json_view")
]
