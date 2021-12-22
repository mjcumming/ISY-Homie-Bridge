#! /usr/bin/env python

from homie.node.property.property_integer import Property_Integer
from homie.node.property.property_boolean import Property_Boolean
from homie.node.node_base import Node_Base

class Base(object):
    def __init__(self, isy_device=None):
        self.isy_device = isy_device
        self.isy_device.add_property_event_handler(self.property_change)
        self.comm_err_count= None

    def add_communication_error_property(self):
        comms_node = Node_Base(self, id="communications", name="Communication", type_="status")
        self.add_node(comms_node)

        self.comm_ok_state = Property_Boolean(comms_node, "commsok", "Communication Ok",settable=False,value=True)
        self.comm_err_count = Property_Integer(comms_node, "commerrors", "Communication Errors",settable=False,value=0)
        self.comm_state_err_count = Property_Integer(comms_node, "commstateerrors", "Communication State Errors",settable=False,value=0)
        self.comm_requests = Property_Integer(comms_node, "commrequests", "Communication Requests",settable=False,value=0)
        comms_node.add_property(self.comm_ok_state)        
        comms_node.add_property(self.comm_err_count)        
        comms_node.add_property(self.comm_state_err_count)        
        comms_node.add_property(self.comm_requests)        

        self.publish_nodes(self.retained, self.qos)

    def get_homie_device_id(self):
        # return re.sub(r'\W+', '', self.isy_device.name.lower())
        #return self.isy_device.get_identifier().replace(" ", "").lower()
        return self.isy_device.get_identifier().replace(" ", "").replace("_", "").lower()

    def property_change(self, property_, value):
        if property_ == "status":
            self.state = value # homie and isy994 use same values
        elif property_ == "communication_error_count":
            self.comm_err_count.value = value   
        elif property_ == "communication_ok":
            self.comm_ok_state.value=value
        elif property_ == "communication_error_state_count":
            self.comm_state_err_count.value=value
        elif property_ == "communication_requests":
            self.comm_requests.value=value
   