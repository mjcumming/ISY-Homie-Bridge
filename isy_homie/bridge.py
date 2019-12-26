#!/usr/bin/env python

import time

import logging
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

from isy994.controller import Controller 
 
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
    'update_interval' : 60, 
    'implementation' : 'ISY994', 
    'fw_name' : 'isy homie bridge',
    'fw_version' : 0, # isy994.__version__,
}

class Bridge (object):
    
    controller = None

    homie_devices = {} #indexed by container_type,device_address

    def __init__(self, address=None, username=None, password=None, homie_settings=HOMIE_SETTINGS, mqtt_settings=None):
        logger.debug('ISY Homie MQTT {}'.format (mqtt_settings))

        self.homie_settings = homie_settings
        self.mqtt_settings = mqtt_settings

        self.controller = Controller(address=address,port=None,username=username,password=password,use_https=False,event_handler=self._isy_event_handler)

    def _isy_event_handler(self,container,item,event,*args):
        logger.warn ('Event {} from {}: {} {}'.format(event,container.container_type,item.name,*args))

        if container.container_type == 'Device':
            self._device_event_handler (item,event,args)
            pass
        elif container.container_type == 'Scene':
            self._scene_event_handler (item,event,args)
            pass
        elif container.container_type == 'Variable':
            self._variable_event_handler (item,event,args)
            pass
        elif container.container_type == 'Program':
            self._program_event_handler (item,event,args)
            pass
        elif container.container_type == 'Controller':
            self._container_event_handler (item,event,args)
            #print (event,item,args)
            if event == 'property':
                pass
                #print ('args',args [0] [0], args[0] [1] )

        if event == 'add':
            pass
            #time.sleep(.5)

    def _device_event_handler(self,device,event,*args):
        #print ('device event',device.name,event,args)
        if event == 'add':
            if device.device_type == 'switch':
                switch = Switch (device,self.homie_settings,self.mqtt_settings)
            elif device.device_type == 'dimmer':
                switch = Dimmer (device,self.homie_settings,self.mqtt_settings)
            elif device.device_type == 'fan':
                fan = Fan (device,self.homie_settings,self.mqtt_settings)
            elif device.device_type == 'contact':
                contact = Contact (device,self.homie_settings,self.mqtt_settings)
            elif device.device_type == 'thermostat':
                thermostat = Thermostat (device,self.homie_settings,self.mqtt_settings)
            elif device.device_type == 'controller':
                controller = Controller_Action (device,self.homie_settings,self.mqtt_settings)

    def _scene_event_handler(self,device,event,*args):
        #print ('device event',device.name,event)
        if event == 'add':
            scene = Scene (device,self.homie_settings,self.mqtt_settings)

    def _variable_event_handler(self,device,event,*args):
        if event == 'add':
            variable = Variable (device,self.homie_settings,self.mqtt_settings)

    def _program_event_handler(self,device,event,*args):
        #print ('device event',device.name,event)
        if event == 'add':
            program = Program (device,self.homie_settings,self.mqtt_settings)

    def _container_event_handler(self,device,event,*args):
        #print ('container event',device.name,event)
        if event == 'add':
            controller = ISY_Controller (device,self.homie_settings,self.mqtt_settings)
