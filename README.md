# ISY-Homie

A bridge between the ISY994 controller and [Homie 4 MQTT convention](https://homieiot.github.io/).

Utilizes the [ISY944v5 package](https://pypi.org/project/ISY994v5/). 

Currently supports 
    Insteon dimmers, switches, keypadlincs, fanlincs, templinc and contact devices
    ZWave locks and switches
    ISY Scenes
    ISY Programs
    ISY Variables


To install:
```
pip3 install ISY994-Homie4-Bridge --user 
```

To start as a service on raspbian:

Create isy_homie.yml in /home/pi using the following settings:


```yaml
isy:
  url: xxx.xxx.xxx.xxx
  username: admin
  password: admin

mqtt:
  MQTT_BROKER: localhost
  MQTT_PORT: 1883
  MQTT_USERNAME: null
  MQTT_PASSWORD: null
  MQTT_SHARE_CLIENT: true

logging:
  enable: true
  level: ERROR
```

Create `isy-homie.service` in `/etc/systemd/system`

```service
[Unit]
Description=ISY994 Homie
After=multi-user.target

[Service]
User=pi
Type=simple
WorkingDirectory=/home/pi
ExecStart=/usr/bin/python3 /home/pi/.local/bin/isy_homie_start.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

Then, start the service and enable launch on start up:
```sh
sudo service start isy-homie
sudo systemctl enable isy-homie
```
