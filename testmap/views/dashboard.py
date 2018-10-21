from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

# from testmap.models.userlocation import UserLocation

class DashboardView(View):

    dashboard_template = 'dashboard/index.html'

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

        long = float(body_json["long"])
        lat = float(body_json["lat"])
        user_location = UserLocation(id=1, name='triplesyntax', longitude=long, latitude=lat)

        user_location.save()
        return HttpResponse(status=200)

    @classmethod
    def get_coords(cls, request):
        cur_loc = UserLocation.objects.get(id=1)
        rsp = [{"long":cur_loc.longitude, "latitude":cur_loc.latitude}]

        return HttpResponse(status=200, content_type="application/json", content=json.dumps(rsp))
