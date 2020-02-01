#!/usr/bin/env python

import time
import os
import sys

import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOG_FILE = os.path.expanduser("~") + "/isybridge.log"

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(FORMATTER)

file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight")
file_handler.setFormatter(FORMATTER)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logging.basicConfig(level=logging.INFO,handlers=[file_handler,console_handler])

from isy994.controller import Controller
import isy994
import homie
import isy_homie

from .devices.switch import Switch
from .devices.dimmer import Dimmer
from .devices.fan import Fan
from .devices.contact import Contact
from .devices.controller_action import Controller_Action
from .devices.scene import Scene
from .devices.variable import Variable
from .devices.program import Program
from .devices.thermostat import Thermostat
from .devices.isy_controller import ISY_Controller

HOMIE_SETTINGS = {
    "update_interval": 60,
    "implementation": "ISY Bridge Version {} Homie 4 Version {}".format(
        isy_homie.__version__, homie.__version__
    ),
    "fw_name": "ISY994V5",
    "fw_version": isy994.__version__,
}


class Bridge(object):

    controller = None

    homie_devices = {}  # indexed by item identifier

    def __init__(
        self,
        address=None,
        username=None,
        password=None,
        homie_settings=HOMIE_SETTINGS,
        mqtt_settings=None,
    ):
        logger.debug("ISY Homie MQTT {}".format(mqtt_settings))

        self.homie_settings = homie_settings
        self.mqtt_settings = mqtt_settings

        self.controller = Controller(
            address=address,
            port=None,
            username=username,
            password=password,
            use_https=False,
            event_handler=self._isy_event_handler,
        )

    def _isy_event_handler(self, container, item, event, *args):
        logger.info(
            "Event {} from {}: {} {}".format(
                event, container.container_type, item.name, *args
            )
        )

        if container.container_type == "Device":
            self._device_event_handler(item, event, args)
        elif container.container_type == "Scene":
            self._scene_event_handler(item, event, args)
        elif container.container_type == "Variable":
            self._variable_event_handler(item, event, args)
        elif container.container_type == "Program":
            self._program_event_handler(item, event, args)
        elif container.container_type == "Controller":
            self._controller_event_handler(item, event, args)

    def _device_event_handler(self, device, event, *args):
        logger.debug("Device event {}".format(device.name, event, args))
        if event == "add":
            if device.device_type == "switch":
                device = Switch(device, self.homie_settings, self.mqtt_settings)
            elif device.device_type == "dimmer":
                device = Dimmer(device, self.homie_settings, self.mqtt_settings)
            elif device.device_type == "fan":
                device = Fan(device, self.homie_settings, self.mqtt_settings)
            elif device.device_type == "contact":
                device = Contact(device, self.homie_settings, self.mqtt_settings)
            elif device.device_type == "thermostat":
                device = Thermostat(device, self.homie_settings, self.mqtt_settings)
            elif device.device_type == "controller":
                device = Controller_Action(
                    device, self.homie_settings, self.mqtt_settings
                )

            self.homie_devices[device.get_homie_device_id()] = device

    def _scene_event_handler(self, device, event, *args):
        logger.debug("Scene event {}".format(device.name, event))
        if event == "add":
            scene = Scene(device, self.homie_settings, self.mqtt_settings)
            self.homie_devices[scene.get_homie_device_id()] = scene

    def _variable_event_handler(self, device, event, *args):
        logger.debug("Variable event {}".format(device.name, event))
        if event == "add":
            variable = Variable(device, self.homie_settings, self.mqtt_settings)
            self.homie_devices[variable.get_homie_device_id()] = variable

    def _program_event_handler(self, device, event, *args):
        logger.debug("Program event {}".format(device.name, event))
        if event == "add":
            program = Program(device, self.homie_settings, self.mqtt_settings)
            self.homie_devices[program.get_homie_device_id()] = program

    def _controller_event_handler(self, device, event, *args):
        logger.debug("Controller event {}".format(device.name, event))
        # print ('container event',device.name,event)
        if event == "add":
            controller = ISY_Controller(device, self.homie_settings, self.mqtt_settings)
            self.homie_devices[controller.get_homie_device_id()] = controller

        # if event == 'property':
        #   if args [0] [0] == 'state' and args[0] [1] == 'lost'
        #      pass # could propagate this to all devices
        # print ('args',args [0] [0], args[0] [1] )

