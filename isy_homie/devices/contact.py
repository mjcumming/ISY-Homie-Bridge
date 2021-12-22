#! /usr/bin/env python

from homie.device_contact import Device_Contact
from .base import Base


class Contact(Base, Device_Contact):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Contact.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        self.add_communication_error_property()

        contact = self.isy_device.get_property("contact")
        if contact is not None:
            self.property_change("contact", contact)
       
    def get_homie_device_id(self):
        return "contact-" + Base.get_homie_device_id(self)

    def property_change(self, property_, value):
        if property_ == "contact":
            self.update_contact(value.upper())

        Base.property_change(self, property_, value)

