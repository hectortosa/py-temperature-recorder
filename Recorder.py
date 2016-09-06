import Measurement

class Recorder(object):
    def __init__(self, type):
        self.type = type

    def record(self, measure: Measurement):
        None