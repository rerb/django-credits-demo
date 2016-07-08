from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import Contribution, Credit


class CreditsDemoView(TemplateView):

    template_name = "credits_demo_view.html"


def CreditsJSONView(request):

    data = []

    for credit in Credit.objects.all():
        data.append(
            {"headline": credit.headline,
             "entranceAnimation": credit.entrance_animation,
             "exitAnimation": credit.exit_animation,
             "contributions": [
                 {"contributor": str(contribution.contributor),
                  "entranceAnimation": contribution.entrance_animation,
                  "exitAnimation": contribution.exit_animation}
                 for contribution in Contribution.objects.filter(
                         credit=credit)]})

    return JsonResponse(data, safe=False)
