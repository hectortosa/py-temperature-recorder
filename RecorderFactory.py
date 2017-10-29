from Recorders import Recorder, PrintRecorder, FileRecorder
from HttpRecorder import HttpRecorder

def create_print_recorder(config):
    return PrintRecorder(config)

def create_file_recorder(config):
    return FileRecorder(config)

def create_http_recorder(config):
    return HttpRecorder(config)

recorderInitializers = dict([
    ('http', create_http_recorder),
    ('print', create_print_recorder),
    ('file', create_file_recorder)])

def create_recorder(config):
    return recorderInitializers[config['type']](config['config'])
