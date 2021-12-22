#! /usr/bin/env python

from homie.device_dimmer import Device_Dimmer
from .base import Base

from homie.node.property.property_string import Property_String


class Dimmer(Base, Device_Dimmer):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Dimmer.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        node = self.get_node("dimmer")
        self.paddle = Property_String(node, "paddleaction", "Paddle Action")
        node.add_property(self.paddle)

        self.add_communication_error_property()
        
        level = self.isy_device.get_property("level")
        if level is not None:
            self.property_change("level", level)

        self.state = self.isy_device.get_property("status")

    def get_homie_device_id(self):
        return "dimmer-" + Base.get_homie_device_id(self)

    def property_change(self, property_, value):
        if property_ == "level":
            self.update_dimmer(value)
        elif property_ == "paddle_action":
            self.paddle.value = value

        Base.property_change(self, property_, value)

    def set_dimmer(self, level):
        self.isy_device.set_level(level)
