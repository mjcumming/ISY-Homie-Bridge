#! /usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_base import Node_Base
from homie.node.property.property_string import Property_String

from .base import Base


class ISY_Controller(Base, Device_Base):
    def __init__(self, isy_device=None, homie_settings=None, mqtt_settings=None):

        Base.__init__(self, isy_device)

        Device_Base.__init__(
            self, "isycontroller", "ISY Controller", homie_settings, mqtt_settings
        )

        node = Node_Base(self, "status", "Status", "status")
        self.add_node(node)

        self.heartbeat = Property_String(node, "heartbeat", "Heart Beat")
        node.add_property(self.heartbeat)

        self.state_busy = Property_String(node, "state", "State")
        node.add_property(self.state_busy)

        self.http_connected = Property_String(node, "http", "HTTP Status")
        node.add_property(self.http_connected)

        self.websocket_connected = Property_String(
            node, "websocket", "Websocket Status"
        )
        node.add_property(self.websocket_connected)

        self.add_communication_error_property()

        Device_Base.start(self)

    def property_change(self, property_, value):
        # print ('contoller',property_,value)
        if property_ == "heartbeat":
            self.heartbeat.value = value.strftime("%m/%d/%Y, %H:%M:%S")
        elif property_ == "state":
            self.state_busy.value = value
        elif property_ == "http":
            self.http_connected.value = value
        elif property_ == "websocket":
            self.websocket_connected.value = value

        if (
            self.http_connected.value != "connected"
            or self.websocket_connected.value != "connected"
        ):
            if self.state != "alert":
                self.state = "alert"
        else:
            if self.state != "ready":
                self.state = "ready"

        Base.property_change(self, property_, value)

