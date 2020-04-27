#! /usr/bin/env python

from homie.device_lock import Device_Lock
from .base import Base


class Door_Lock(Base, Device_Lock):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Lock.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        lock = self.isy_device.get_property("lock")
        if lock is not None:
            self.property_change("lock", lock)

    def get_homie_device_id(self):
        return "lock-" + Base.get_homie_device_id(self)

    def lock(self):
        self.isy_device.lock()

    def unlock(self):
        self.isy_device.unlock()

    def property_change(self, property_, value):
        if property_ == "lock":
            self.update_lock(value.upper())

        Base.property_change(self, property_, value)

