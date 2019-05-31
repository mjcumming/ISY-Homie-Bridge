#! /usr/bin/env python

from homie.device_switch import Device_Switch
from .base import Base

class Scene(Base,Device_Switch):

    def __init__(self, isy_device=None,homie_settings=None, mqtt_settings=None):

        Base.__init__ (self,isy_device)

        Device_Switch.__init__ (self,self.get_homie_device_id(), isy_device.name, homie_settings, mqtt_settings)

        onoff = self.isy_device.get_property('onoff')
        if onoff is not None:
            self.property_change('onoff',onoff)


    def property_change(self,property_,value):
        if property_ == 'onoff':
            if value == 'on':
                self.update_switch('ON')
            else:
                self.update_switch('OFF')

        Base.property_change (self,property_,value)

    def set_switch(self,onoff):
        if onoff == 'ON':
            self.isy_device.turn_on ()
        else:
            self.isy_device.turn_off ()

