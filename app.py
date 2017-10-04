import os
import glob
import json
import time
from Measurement import Measurement
import RecorderFactory

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

BASE_DIR = '/sys/bus/w1/devices/'
DEVICES_FOLDER = glob.glob(BASE_DIR + '28*')
MEASURE_FILE = '/w1_slave'

READ_INTERVAL = 30
RECORDERS = []

def read_config():
    config = {}

    with open('config.json') as json_data:
        config = json.load(json_data)

    READ_INTERVAL = config['read-interval']

    for recorder_config in config['recorders']:
        RECORDERS.append(RecorderFactory.create_recorder(recorder_config))


def read_temp():
    measures = []

    for folder in DEVICES_FOLDER:
        device_file = open(folder + MEASURE_FILE, 'r')
        lines = device_file.readlines()
        device_file.close()

        value = read_value(lines)

        if value is not None:
            measures.append(Measurement(folder.split('/')[-1], value))

    return measures


def read_value(lines):
    if (len(lines) > 0) and (lines[0].strip()[-3:] == 'YES'):
        temp_position = lines[1].find('t=')
        if temp_position != -1:
            temp_string = lines[1][temp_position + 2:]
            return float(temp_string)
        else:
            return None
    else:
        return None

def start_reading():
    while True:
        measures = read_temp()

        if len(measures) > 0:
            for recorder in RECORDERS:
                for measure in measures:
                    recorder.record(measure)

        time.sleep(READ_INTERVAL)

read_config()
start_reading()

