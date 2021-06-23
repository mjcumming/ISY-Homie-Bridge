# ISY-Homie

A bridge between the ISY994 controller and [Homie 4 MQTT convention](https://homieiot.github.io/).

Utilizes the [ISY944v5 package](https://pypi.org/project/ISY994v5/). 

Currently supports 
    Insteon dimmers, switches, keypadlincs, fanlincs, templinc and contact devices
    ZWave locks and switches
    ISY Scenes
    ISY Programs
    ISY Variables

# To start as a service on Raspbian: 

Use pip3 to install, not pip
   
Create isy_homie.yml in /etc 
  sudo nano /etc/isy_homie.yml

Copy the following into that file, change the defaults and save

```yaml
isy:
  url: xxx.xxx.xxx.xxx
  username: admin
  password: admin

mqtt:
  MQTT_BROKER: broker
  MQTT_PORT: 1883
  MQTT_USERNAME: null
  MQTT_PASSWORD: null
  MQTT_SHARE_CLIENT: true
  ```

Create isy-homie.service in /etc/systemd/system
  sudo nano /etc/systemd/system/isy-homie.service

Copy the following into that file, change the User from pi if needed, and save


  ```service
[Unit]
Description=ISY995 Homie
After=multi-user.target

[Service]
User=pi
Type=simple
ExecStart=/usr/bin/python3 /usr/local/bin/isy_homie_start.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

Copy the file isy_home_start.py from the github repository to /usr/local/bin

sudo systemctl start isy-homie

