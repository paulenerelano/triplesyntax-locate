from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import json



class DashboardView(View):

	add_map_template = 'dashboard/add_map.html'
	dashboard_template = 'dashboard/index.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.dashboard_template)
