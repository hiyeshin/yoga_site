from pi_io_site.models import *
from django.contrib import admin
from django.forms import ModelForm, ChoiceField
from django.forms.models import BaseInlineFormSet
import json


class DisplayForm(ModelForm):
	# overriden to dynamically filter list, otherwise it is a intergerfield
	channel_port = ChoiceField(label = 'channel/port')


class DisplayFormSet(BaseInlineFormSet):
	# different from input and output
	# it filters based on IO type

	def add_fields(self, form, index):
		super(DisplayFormSet, self).add_fields(form, index)

		# read interface only
		if issubclass(self.model, ReadDisplay):
			if hasattr(form.insta ce, 'interface') and form.instance.interface is not None:
				interfaces = [form.instance.interface]
			else:
				interfaces = RPIReadInterface.objects.filter(rpi = self.instance)

		elif issubclass(self.model, WriteDisplay):
			if hasattr(form.instance, 'interface') and form.instance.interface is not None:
				interfaces = [form.instance.interface]
			else:
				interfaces = RPIWriteInterface.objects.filter(rpi=self.instance)

		choices = []
		for interface in interfaces:
			if interface.io_type not in self.model.io_type:
				continue # skip
			try:
				_choices = json.loads(interface.possible_choices)
			except:
				continue

			for item in _choices: # with selected only
				choices.append((item['s'], interface.__unicode__() + ' ' + item['d']))
		form.fields['channel_port'].choice = choices

		# filter queryset
		form.fields['interface'].queryset = form.fields['interface'].queryset.filter(io_type__in = self.model.io_type)
		form.fields['interface'].queryset = form.fields['interface'].queryset.filter(rpi = self.instance)


class DisplayInline(admin.TabularInline):
	extra = 0
	formset = DisplayFormSet
	form = DisplayForm


class MyAdminForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(MyAdminForm, self).__init__(*args, **kwargs)

	class Meta:
		model = RaspberryPi


"""
Add new displays here below
Input / Output and return / input type are determined by the model definition
"""

class NumericDisplayInLine(DisplayInline):
	model = NumericDisplayInLine

class ProgressBarDisplayInLine(DisplayInline):
	model = ProgressBarDisplay

class GraphDisplayInLine(DisplayInline):
	model = GraphDisplay

class ButtonDisplayInline(DisplayInline):
	model = ButtonDisplay

class RaspberryPiAdmin(admin.ModelAdmin):
		readonly_field = ('mac_adddress', 'current_ip', 'online')
		fields = ('name', 'mac_adddress', 'current_ip', 'online')
		form = MyAdminForm
		inlines = [NumericDisplayInLine, ProgressBarDisplayInLine, GraphDisplayInLine, ButtonDisplayInline]

admin.site.register(RaspberryPi, RaspberryPiAdmin)
