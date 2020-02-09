#! /usr/bin/env python

import re


class Base(object):
    def __init__(self, isy_device=None):
        self.isy_device = isy_device
        self.isy_device.add_property_event_handler(self.property_change)

    def get_homie_device_id(self):
        # return re.sub(r'\W+', '', self.isy_device.name.lower())
        #return self.isy_device.get_identifier().replace(" ", "").lower()
        return self.isy_device.get_identifier().replace(" ", "").replace("_", "").lower()

    def property_change(self, property_, value):
        pass
        # print ('property change',self,property_,value)

