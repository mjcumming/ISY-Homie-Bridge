#! /usr/bin/env python

from homie.device_barrier import Device_Barrier
from .base import Base


class Barrier(Base, Device_Barrier):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Barrier.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        barrier = self.isy_device.get_property("barrier")
        if barrier is not None:
            self.property_change("barrier", barrier)

    def get_homie_device_id(self):
        return "barrier-" + Base.get_homie_device_id(self)

    def property_change(self, property_, value):
        if property_ == "barrier":
            self.update_barrier(value.upper())

        Base.property_change(self, property_, value)

