#! /usr/bin/env python

from homie.device_integer import Device_Integer
from .base import Base


class Variable(Base, Device_Integer):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Integer.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        """
        value = self.isy_device.get_property('value')
        if value is not None:
            self.property_change('value',value)
        """

    def get_homie_device_id(self):
        return "variable-" + Base.get_homie_device_id(self).replace(":", "-")

    def property_change(self, property_, value):
        if property_ == "value":
            self.update_value(value)

        Base.property_change(self, property_, value)

    def set_value(self, value):
        self.isy_device.set_value(value)
