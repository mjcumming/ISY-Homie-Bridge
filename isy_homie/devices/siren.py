#! /usr/bin/env python

from homie.device_switch import Device_Switch
from .base import Base

from homie.node.property.property_string import Property_String


class Siren(Base, Device_Switch):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Switch.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        node = self.get_node("switch")
        self.duration = Property_String(node, "duration", "Duration")
        node.add_property(self.duration)
        self.duration.value = 0

        self.add_communication_error_property()

        onoff = self.isy_device.get_property("onoff")
        if onoff is not None:
            self.property_change("onoff", onoff)

    def get_homie_device_id(self):
        return "siren-" + Base.get_homie_device_id(self)

    def property_change(self, property_, value):
        if property_ == "onoff":
            if value == "on":
                self.update_switch("ON")
            else:
                self.update_switch("OFF")

        elif property_ == "duration":
            self.duration.value = value

        Base.property_change(self, property_, value)

    def set_switch(self, onoff):
        if onoff == "ON":
            self.isy_device.turn_on()
        else:
            self.isy_device.turn_off()

