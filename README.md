# ISY-Homie

A bridge between the ISY994 controller and [Homie 4 MQTT convention](https://homieiot.github.io/).

Utilizes the [ISY944v5 package](https://pypi.org/project/ISY994v5/). Currently only supports Insteon devices, Insteon Scenes, ISY program, and ISY variables.

To start as a service on raspbian 

Create isy_homie.yml in /etc using the following settings:


```yaml
isy:
  url: xxx.xxx.xxx.xxx
  username: xxxxx
  password: xxxxx

mqtt:
  MQTT_BROKER: broker
  MQTT_PORT: 1883
  MQTT_USERNAME: null
  MQTT_PASSWORD: null
  MQTT_SHARE_CLIENT: true
  ```

  Create isy-homie.service in /etc/systemd/system

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



