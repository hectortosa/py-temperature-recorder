import datetime

class Measurement(object):
    def __init__(self, device_id, value):
        self.device_id = device_id
        self.value = value
        self.timestamp = datetime.datetime.utcnow

    def get_celsius(self):
        return self.value / 1000.0

    def get_fahrenheit(self):
        return ((self.value / 1000.0) * 9.0 / 5.0 ) + 32