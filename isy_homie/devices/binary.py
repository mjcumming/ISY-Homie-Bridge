#! /usr/bin/env python

from homie.device_binary import Device_Binary
from .base import Base


class Binary(Base, Device_Binary):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Binary.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        binary = self.isy_device.get_property("binary")
        if binary is not None:
            self.property_change("binary", binary)

    def get_homie_device_id(self):
        return "binary-" + Base.get_homie_device_id(self)

    def property_change(self, property_, value):
        if property_ == "binary":
            self.update_binary(value.upper())

        Base.property_change(self, property_, value)

