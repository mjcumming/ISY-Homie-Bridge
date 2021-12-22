#! /usr/bin/env python

from homie.device_thermostat import Device_Thermostat
from .base import Base

THERMOSTAT_SETTINGS = {
    "current_temperature": 70,
    "current_humidity": 30,
    "cool_setpoint": 70,
    "max_cool_setpoint": 90,
    "min_cool_setpoint": 60,
    "heat_setpoint": 70,
    "max_heat_setpoint": 90,
    "min_heat_setpoint": 60,
    "fan_mode": "On",
    "fan_modes": ["On", "Auto"],
    "system_mode": "Off",
    "system_modes": ["Off", "Heat", "Cool", "Auto"],
    "system_status": ["Idle", "Heating", "Cooling"],
    "units": "F",
}

props = [
    "temperature",
    "humidity",
    "heatsetpoint",
    "coolsetpoint",
    "systemmode",
    "systemstatus",
    "fanmode",
]


class Thermostat(Base, Device_Thermostat):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Thermostat.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        for isy_prop in props:
            iprop_value = self.isy_device.get_property(isy_prop)
            if iprop_value is not None:
                self.property_change(isy_prop, iprop_value)

        self.add_communication_error_property()

    def get_homie_device_id(self):
        return "thermostat-" + Base.get_homie_device_id(self)

    def property_change(self, property_, value):
        if property_ == "temperature":
            self.update_current_temperature(value)
        elif property_ == "humidity":
            self.update_current_humidity(value)
        elif property_ == "heatsetpoint":
            self.update_heat_setpoint(value)
        elif property_ == "coolsetpoint":
            self.update_cool_setpoint(value)
        elif property_ == "systemmode":
            self.update_system_mode(value)
        elif property_ == "systemstatus":
            self.update_system_status(value)
        elif property_ == "fanmode":
            self.update_fan_mode(value)

        Base.property_change(self, property_, value)

    def set_heat_setpoint(self, value):
        self.isy_device.set_heatsetpoint(value)

    def set_cool_setpoint(self, value):
        self.isy_device.set_coolsetpoint(value)

    def set_system_mode(self, value):
        self.isy_device.setmode(value)

    def set_system_status(self, value):
        self.isy_device.setstatus(value)

    def set_fan_mode(self, value):
        pass

    def set_hold_mode(self, value):
        pass
