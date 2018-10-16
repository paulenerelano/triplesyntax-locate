from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import json


from bnes.models.floorplan import FloorPlanForm
from bnes.models.floorplan import FloorPlan


class DashboardView(View):
	
	add_map_template = 'dashboard/add_map.html'
	dashboard_template = 'dashboard/index.html'
	MEDIA = 'bnes/media/'

	def get(self, request, *args, **kwargs):

		floor_id = kwargs.get('floor_id')
		print(kwargs)

		print(floor_id)

		if floor_id is None:
			form = FloorPlanForm
			return render(request, self.add_map_template, {'form':form})
		# End if

		floor_plan = FloorPlan.objects.get(id=floor_id)

		return render(request, self.dashboard_template, {'floor_plan':floor_plan})
		
	@classmethod
	def testjsonresponse(self, request):
		testjsonarr = [{"lala":"la123"}, {"lala":"12323", "qwert":"bert"}]

		return HttpResponse(status=200, content_type="application/json", content=json.dumps(testjsonarr))


	def post(self, request, *args, **kwargs):
		form = FloorPlanForm(request.POST, request.FILES)
		if form.is_valid():
			floor_plan = form.save(commit=False)
			floor_plan.save()
			self.__handle_file_upload(request.FILES['image'], str(floor_plan.image))

		return redirect(reverse('dashboard')+str(floor_plan.id))


	def __handle_file_upload(self, file, path):
		with open(self.MEDIA+path, 'wb+') as destination:
			for chunk in file.chunks():
				destination.write(chunk)
