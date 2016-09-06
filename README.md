# py-temperature-reader

Python application to read DS18B20 1-wire temperature sensor and sends data to configured recorders. Read frequency can be configured in `config.json` by setting the property `read-interval` in seconds.

    {
        "read-interval": 30
    }

## Recorders

A recorder is where the data read from the sensor will be sent. Multiple recorders can be configured at the same time using config.json

Existing recorders are:

- Print
- File
- Http

Some recorders has a `format` configuration that can be used to format the output of the data. Fields that can be used in the string format are:

- **device_id**: the id of the sensor read
- **timestamp**: date and time of the read
- **celsius**: the value measured in Celsius
- **fahrenheit**: the value read in Fahrenheit

### Print recorder

Print the data received through the console using the string format configured in `format`.

    {
        "recorders": [
        {
            "type": "print",
            "config": {
                "format": "{device_id} C {celsius} / F {fahrenheit}"
            }
        }
    }

### File recorder

This recorder will create a file for each sensor read using the device id of the sensor as file name. The files will be stored in the path configured in `container` with the extension specified in `extension`. The data read from the sensor will be write using the string format in `format`.

    {
        {
            "type": "file",
            "config": {
                "format": "{timestamp},{celsius},C",
                "container": "/temperaturemonitor/",
                "extension": ".log"
            }
        }
    }