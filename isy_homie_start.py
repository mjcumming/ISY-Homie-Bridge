#!/usr/bin/env python

import time
import yaml 

from isy_homie.bridge import Bridge

with open("/etc/isy_homie.yml", 'r') as ymlfile:
    cfg = yaml.full_load(ymlfile)

bridge = None

try:
    if 'logging' in cfg:
        logging = cfg ['logging']
    else:
        logging = None

    bridge = Bridge (address=cfg['isy'] ['url'], username=cfg['isy'] ['username'],password=cfg['isy'] ['password'],mqtt_settings=cfg['mqtt'],log_settings=logging)

    while True:
        time.sleep(1)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")    

