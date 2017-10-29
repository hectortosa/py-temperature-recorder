from Measurement import Measurement
from Recorders import Recorder
import json
import paho.mqtt.client as mqtt

class MqttRecorder(Recorder):
    def __init__(self, config):
        Recorder.__init__(self, 'mqtt')
        self.format = config['format']
        
        self.host = config['host']
        self.port = config['port'] if 'port' in config else 1883
        self.topic = config['topic']
        self.client_id = config['client_id']
        self.username = config['username']
        self.password = config['password']
        self.timeout = config['timeout'] if 'timeout' in config else 30
        self.qos = config['qos'] if 'qos' in config else 1
        self.client = None

    def _open_client(self):
        self.client = mqtt.Client(self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.connect(self.host, self.port, self.timeout)
    
    def get_client(self):
        if self.client == None:
            self._open_client()
        return self.client
            
    def record(self, measure: Measurement):
        payload = self.format.format(
            device_id=measure.device_id,
            celsius=measure.get_celsius(),
            fahrenheit=measure.get_fahrenheit(),
            timestamp=measure.timestamp)
        
        client = self.get_client()
        client.publish(self.topic, payload, qos=self.qos, retain=False)
