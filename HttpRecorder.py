from Measurement import Measurement
from Recorders import Recorder
import json
import urllib.request
import sys

def dict_format(template, measure: Measurement):
    d = {}
    # iterate over items in the dict
    for key, item in template.items():
        # if the item is a string, apply format
        if type(item) == str:
            formatted_value = item.format(
                device_id=measure.device_id,
                celsius=measure.get_celsius(),
                fahrenheit=measure.get_fahrenheit(),
                timestamp=measure.timestamp)
            d[key] = formatted_value
    return d


class HttpRecorder(Recorder):
    def __init__(self, config):
        Recorder.__init__(self, 'http')
        print("http recorder init")
        self.template = config['json_template']
        self.method = config['method']
        self.url = config['endpoint']
        self.headers = config['headers']
        self.headers['content-type'] = 'application/json'

    def record(self, measure: Measurement):
        # First, generate payload
        payload = dict_format(self.template, measure)
        j = json.dumps(payload).encode('utf8')

        # Construct url
        url = self.url.format(device_id = measure.device_id)

        # submit
        req = urllib.request.Request(url, data=j, headers=self.headers)
        response = urllib.request.urlopen(req)
        sys.stderr.write(response.read().decode('utf8'))
