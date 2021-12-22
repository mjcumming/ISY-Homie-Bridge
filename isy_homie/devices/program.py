#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_base import Node_Base

from homie.node.property.property_string import Property_String
from homie.node.property.property_enum import Property_Enum

from .base import Base


class Program(Base, Device_Base):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Base.__init__(
            self,
            self.get_homie_device_id(),
            isy_device.name,
            homie_settings,
            mqtt_settings,
        )

        node = Node_Base(self, "program", "Program", "program")
        self.add_node(node)

        self.status = Property_String(node, "status", "Status")
        node.add_property(self.status)

        self.run = Property_Enum(
            node,
            id="run",
            name="Run Program",
            data_format="RUNIF,RUNTHEN,RUNELSE,STOP",
            set_value=self.set_run_program,
        )
        node.add_property(self.run)

        self.add_communication_error_property()

        self.start()

    def get_homie_device_id(self):
        return "program-" + Base.get_homie_device_id(self)

    def set_run_program(self, value):
        if value == "RUNIF":
            self.isy_device.run()
        elif value == "RUNTHEN":
            self.isy_device.run_then()
        elif value == "RUNELSE":
            self.isy_device.run_else()
        elif value == "STOP":
            self.isy_device.stop()

    def property_change(self, property_, value):
        if property_ == "state":
            self.status.value = value

        Base.property_change(self, property_, value)

