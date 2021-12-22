#! /usr/bin/env python


#!/usr/bin/env python

from homie.device_speed import Device_Speed

from .base import Base


class Fan(Base, Device_Speed):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Speed.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        self.add_communication_error_property()

        self.start()

    def get_homie_device_id(self):
        return "fan-" + Base.get_homie_device_id(self)

    def set_speed(self, speed):
        self.isy_device.set_speed(speed.lower())

    def property_change(self, property_, value):
        if property_ == "speed":
            self.speed_property.value = value.upper()

        Base.property_change(self, property_, value)

