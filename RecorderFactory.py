from Recorders import Recorder, PrintRecorder, FileRecorder
from MqttRecorder import MqttRecorder

def create_print_recorder(config):
    return PrintRecorder(config)

def create_file_recorder(config):
    return FileRecorder(config)

def create_mqtt_recorder(config):
    return MqttRecorder(config)

recorderInitializers = dict([
    ('mqtt', create_mqtt_recorder),
    ('print', create_print_recorder),
    ('file', create_file_recorder)])

def create_recorder(config):
    return recorderInitializers[config['type']](config['config'])
