#! /usr/bin/env python

from homie.device_contact import Device_Thermostat
from .base import Base

class Thermostat(Base,Device_Thermostat):

    def __init__(self, isy_device=None,homie_settings=None, mqtt_settings=None):

        Base.__init__ (self,isy_device)
        
        Device_Thermostat.__init__ (self,self.get_homie_device_id(), isy_device.name, homie_settings, mqtt_settings)

        contact = self.isy_device.get_property('contact')
        if contact is not None:
            self.property_change('contact',contact)

    def get_homie_device_id (self):
        return 'thermostat-' + Base.get_homie_device_id(self)

    def property_change(self,property_,value):
        if property_ == 'level':
            self.update_dimmer(value)
        elif property_ == 'paddle_action':
            self.paddle.value = value

        Base.property_change (self,property_,value)
        
    def property_change(self,property_,value):
        if property_ == 'contact':
            self.update_contact (value.upper())

        Base.property_change (self,property_,value)

