#!/usr/bin/env python

import time
import yaml 

from isy_homie import ISY_Homie


with open("isy_homie.yml", 'r') as ymlfile:
    cfg = yaml.full_load(ymlfile)

try:
    bridge = ISY_Homie (address=cfg['isy'] ['url'], username=cfg['isy'] ['username'],password=cfg['isy'] ['password'],mqtt_settings=cfg['mqtt'])
    
    while True:
        time.sleep(10)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")     
