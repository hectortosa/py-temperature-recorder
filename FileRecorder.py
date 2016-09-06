import Recorder, Measurement

class FileRecorder(Recorder):
    def __init__(self, config):
        Recorder.__init__(self, 'file')

        self.format = config.format
        self.container = config.container
        self.extension = config.extension

    def record(self, measure: Measurement):
        log_entry = self.format.format(
            device_id=measure.device_id,
            celsius=measure.get_celsius(),
            fahrenheit=measure.get_fahrenheit(),
            timestamp=measure.timestamp)
        file_path = self.container + measure.device_id + '/' + self.extension

        f = open(file_path, 'w')
        f.writelines([log_entry])