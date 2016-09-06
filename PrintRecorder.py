import Recorder, Measurement

class PrintRecorder(Recorder):
    def __init__(self, config):
        Recorder.__init__(self, 'file')

        self.format = config.format

    def record(self, measure: Measurement):
        line = self.format.format(
            device_id=measure.device_id,
            celsius=measure.get_celsius(),
            fahrenheit=measure.get_fahrenheit(),
            timestamp=measure.timestamp)

        print(line, end='\n')