#! /usr/bin/env python

from homie.device_thermostat import Device_Thermostat
from .base import Base

props = [
    'temperature',
    'humidity',
    'heatsetpoint',
    'coolsetpoint',
    'systemmode',
]

class Thermostat(Base,Device_Thermostat):

    def __init__(self, isy_device=None,homie_settings=None, mqtt_settings=None):

        Base.__init__ (self,isy_device)
        print (isy_device.properties)
        Device_Thermostat.__init__ (self,self.get_homie_device_id(), isy_device.name, homie_settings, mqtt_settings)

        for isy_prop in props:
            iprop_value = self.isy_device.get_property(isy_prop)
            if iprop_value is not None:
                self.property_change(isy_prop,iprop_value)

    def get_homie_device_id (self):
        return 'thermostat-' + Base.get_homie_device_id(self)

    def property_change(self,property_,value):
        if property_ == 'temperature':
            self.update_current_temperature(value)
        elif property_ == 'humidity':
            self.update_current_humidity(value)
        elif property_ == 'heatsetpoint':
            self.update_heat_setpoint(value)
        elif property_ == 'coolsetpoint':
            self.update_cool_setpoint(value)
        elif property_ == 'systemmode':
            self.update_system_mode(value)

        Base.property_change (self,property_,value)

    def set_heat_setpoint(self,value):
        self.isy_device.set_heatsetpoint(value)

    def set_cool_setpoint(self,value):
        self.isy_device.set_coolsetpoint(value)
        
    def set_system_mode(self,value):
        self.isy_device.setmode(value)
        
    def set_fan_mode(self,value):
        pass
        
    def set_hold_mode(self,value):
        pass
