#! /usr/bin/env python

from homie.device_notification import Device_Notification
from .base import Base


class Notification_Sensor(Base, Device_Notification):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Notification.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        notification = self.isy_device.get_property("notification")
        if notification is not None:
            self.property_change("notification", notification)

    def get_homie_device_id(self):
        return "notification-" + Base.get_homie_device_id(self)

    def property_change(self, property_, value):
        if property_ == "notification":
            self.update_notification(value.upper())

        Base.property_change(self, property_, value)
