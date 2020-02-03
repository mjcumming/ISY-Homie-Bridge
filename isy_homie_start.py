#!/usr/bin/env python

import time
import yaml 

from isy_homie.bridge import Bridge


with open("isy_homie.yml", 'r') as ymlfile:
    cfg = yaml.full_load(ymlfile)

bridge = None

try:
    bridge = Bridge (address=cfg['isy'] ['url'], username=cfg['isy'] ['username'],password=cfg['isy'] ['password'],mqtt_settings=cfg['mqtt'])

    while True:
        time.sleep(1)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")    

