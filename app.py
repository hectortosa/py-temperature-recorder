import os
import glob
import time
import Measurement, RecorderFactory
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
devices_folder = glob.glob(base_dir + '28*')
measure_file = '/w1_slave'

read_interval
recorders = []

def read_config():
    config = {}

    with open('config.json') as json_data:
        config = json.load(json_data)

    read_interval = config['read-interval']

    for recorder_config in config.recorders:
        recorders.append(RecorderFactory.create_recorder(recorder_config))
 
def read_temp():
    measures = []

    for folder in devices_folder:
        f = open(folder + measure_file, 'r')
        lines = f.readlines()
        value = read_value(lines)
        f.close()
        measures.append(Measurement(folder, value))

    return measures
 
def read_value(lines):
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        return float(temp_string)
	
while True:
    measures = read_temp()

    if measures.count > 0:
        for recorder in recorders:
            for measure in measures:
                recorder.record(measure)

	time.sleep(read_interval)