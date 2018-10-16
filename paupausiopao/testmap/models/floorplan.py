from django.db import models
from django import forms

class FloorPlan(models.Model):
	"""docstring for FloorPlan"""
	name = models.CharField(max_length=20)
	floor = models.PositiveSmallIntegerField()
	image = models.FileField(upload_to='floorplan/')

	# TODO: check if image can be changed

	def __str__(self):
		return self.name

# End FloorPlan

class FloorPlanForm(forms.ModelForm):
	"""docstring for FloorPlanForm"""
	class Meta:
		model = FloorPlan
		fields = ('name', 'floor','image',)

	