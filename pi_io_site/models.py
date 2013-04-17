from django.db import models

class IOTypes(object):
	boolean = 'B'
	interger = 'I'

class RaspberryPi(models.Model):
	name = models.CharField(max_length = 200)
	# in this code it will look like aa:bb:cc:DD:ee:ff
	mac_address = models.CharField(max_length = 17, promary_key = True)
	current_ip = models.IPAddressField()
	online = models.BooleanField(default = False)

	def __unicode__(self):
		return self.name


class RaspberryPiInterface(models.Model):

	IO_TYPE = (
		('B', 'Boolean'),
		('I', 'Interger'),
	)

	name = models.CharField(max_length = 200)
	description = models.TextField(blank = True, default = '')
	# to determine the appropriate displays
	io_type = models.CharField(choices = IO_TYPE, max_length = 1)
	# stored as a list of choices in json
	possible_choices = models.TextField(default = '[]')

	rpi = models.ForeignKey(RaspberryPi)

	def __unicode__(self):
		return self.name

	class meta:
		unique_together = (("name", "rpi"),)
		abstract = True


class RPIReadInterface(RaspberryPiInterface):
	pass

class RPIWriteInterface(RaspberryPiInterface):
	pass

class Display(models.Model):
	channel_port = models.IntergerFIeld()
	rpi = models.ForeignKey(RaspberryPi)
	equation = models.CharField(max_length = 100, blank = True)

	label = models.CharField(max_length = 200, blank = True)

	def __unicode__(self):
		return '%s - %d' % (self.__class__.__name__, self.channel_port)

	class Meta:
		abstract = True

class WriteDisplay(Display):
	interface = models.ForeignKey(RPIWriteInterface)

class ReadDisplay(Display):
	interface = models.ForeignKey(RPIReadInterface)


class NumericDisplay(ReadDisplay):
	io_type = (IOTypes.boolean, IOTypes.interger)

class ProgressBarDisplay(ReadDisplay):
	io_type = (IOTypes.interger,)

class GraphDisplay(ReadDisplay):
	io_type = (IOTypes.interger,)

class ButtonDisplay(WriteDisplay):
	io_type = (IOTypes.boolean,)


"""
Connect signals to ws_comm handler for interface change updates
"""
from django.db.models.signals import post_save, post_delete
from ws_comm.client import config_changed_signal
post_save.connect(config_changed_signal, dispatch_uid = "uid_post_save_config")
post_delete.connect(config_changed_signal, dispatch_uid = "uid_post_del_config")