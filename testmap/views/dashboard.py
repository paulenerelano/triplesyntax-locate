from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json



class DashboardView(View):

    def get(self, request, *args, **kwargs):
        return render(request, self.dashboard_template)

    @classmethod
    @csrf_exempt
    def push_coords(cls, request):
        try:
            body_unicode = request.body.decode('utf-8')
            print(body_unicode)
            body_json = json.loads(body_unicode)
        except Exception as err:
            print(type(err))
            print(err.args)
            return HttpResponse(status=500)

        print(body_json)

        return HttpResponse(status=200)
