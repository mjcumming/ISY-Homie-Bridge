
import time

from bridge import Bridge


MQTT_SETTINGS = {
    'MQTT_BROKER' : 'OpenHAB',
    'MQTT_PORT' : 1883,
    'MQTT_USERNAME' : None,
    'MQTT_PASSWORD' : None,
    'MQTT_KEEPALIVE' : 60,
    'MQTT_CLIENT_ID' : None,
}

HOMIE_SETTINGS = {
    'version' : '3.0.1',
    'topic' : 'homie', 
    'fw_name' : 'isy994',
    'fw_version' : '0.0.1', 
    'update_interval' : 60, 
    'implementation' : 'HomieV3', 
}

 
url = '192.168.1.213'

if __name__ == "__main__":

    try:
        c = Bridge (url,username='admin',password='admin',homie_settings = HOMIE_SETTINGS,mqtt_settings=MQTT_SETTINGS)
        time.sleep(2)  
        #device = c.device_container.get('14 A9 92 2')
        #device = c.device_container.get('42 C8 99 1')
        #print ('got device',device)

        #scene = c.scene_Container.get_scene('25770')
        #print ('got scene',scene)

        #program = c.program_Container.get_program ('0022')

        while True:
            time.sleep(2)
            #device.set_level (0)
            #device.set_speed ('low')
            #device.set_speed ('medium')
            #device.set_speed ('high')
            #scene.turn_on()
            #program.run()
            time.sleep(2)
            #device.set_speed ('off')
            #scene.turn_off()
            #device.set_level (100)
            #program.run_else()

    except KeyboardInterrupt:
        print("KeyboardInterrupt has been caught.")

