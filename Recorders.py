from Measurement import Measurement

class Recorder(object):
    def __init__(self, recorderType):
        self.recorderType = recorderType

    def record(self, measure: Measurement):
        None

class PrintRecorder(Recorder):
    def __init__(self, config):
        Recorder.__init__(self, 'file')

        self.format = config['format']

    def record(self, measure: Measurement):
        line = self.format.format(
            device_id=measure.device_id,
            celsius=measure.get_celsius(),
            fahrenheit=measure.get_fahrenheit(),
            timestamp=measure.timestamp)

        print(line, end='\n')

class FileRecorder(Recorder):
    def __init__(self, config):
        Recorder.__init__(self, 'file')

        self.format = config['format']
        self.container = config['container']
        self.extension = config['extension']

    def record(self, measure: Measurement):
        log_entry = self.format.format(
            device_id=measure.device_id,
            celsius=measure.get_celsius(),
            fahrenheit=measure.get_fahrenheit(),
            timestamp=measure.timestamp)

        file_path = self.container + measure.device_id.split('/')[-1] + self.extension

        f = open(file_path, 'w')
        f.writelines([log_entry])