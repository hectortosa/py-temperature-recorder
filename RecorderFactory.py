from Recorders import Recorder, PrintRecorder, FileRecorder

def create_print_recorder(config):
    return PrintRecorder(config)

def create_file_recorder(config):
    return FileRecorder(config)

recorderInitializers = dict([
    ('print', create_print_recorder),
    ('file', create_file_recorder)])

def create_recorder(config):
    return recorderInitializers[config['type']](config['config'])