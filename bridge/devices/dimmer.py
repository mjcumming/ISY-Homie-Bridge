#! /usr/bin/env python

from homie.device_dimmer import Device_Dimmer
from .base import Base

class Dimmer(Base,Device_Dimmer):

    def __init__(self, isy_device=None,homie_settings=None, mqtt_settings=None):

        Base.__init__ (self,isy_device)

        Device_Dimmer.__init__ (self,self.get_homie_device_id(), isy_device.name, homie_settings, mqtt_settings)

        level = self.isy_device.get_property('level')
        if level is not None:
            self.property_change('level',level)


    def property_change(self,property_,value):
        if property_ == 'level':
            self.update_dimmer(value)

        Base.property_change (self,property_,value)

    def set_dimmer(self,level):
        self.isy_device.set_level (level)
