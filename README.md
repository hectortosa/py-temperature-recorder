# py-temperature-reader

Python application to read DS18B20 1-wire temperature sensor and sends data to configured recorders. Read frequency can be configured in `config.json` by setting the property `read-interval` in seconds.

```json
{
    "read-interval": 30
}
```

## Recorders

A recorder is where the data read from the sensor will be sent. Multiple recorders can be configured at the same time using config.json.

Existing recorders are:

- Print
- File
- Http

A Measurement object will be passed to each configured recorder each time the sensor is read. This object has following structure:

```json
{
    "device_id": "28ABCDEF123456",
    "value": 130.123,
    "timestamp": "2017-10-06T07:49:51Z"
}
```

Recorders has some configuration fields that accepts dynamic values from Measurement. To use a dynamic valye it must be referenced using braces (i.e. `{device_id}`). Fields that can be used as dynamic values are:

- **device_id**: the id of the sensor read
- **timestamp**: date and time of the read
- **celsius**: the value measured in Celsius
- **fahrenheit**: the value read in Fahrenheit

### Print recorder

Print the data received through the console using the string format configured in `format`. `format`configuration accepts dynamic values.

Example configuration:

```json
{
    "recorders": [{
        "type": "print",
        "config": {
            "format": "{device_id} C {celsius} / F {fahrenheit}"
        }
    }]
}
```

### File recorder

This recorder will create a file for each sensor read using the device id of the sensor as file name. The files will be stored in the path configured in `container` with the extension specified in `extension`. The data read from the sensor will be write using the string format in `format`. `format`configuration accepts dynamic values.

Example configuration:

```json
{
    "recorders": [{
        "type": "file",
        "config": {
            "format": "{timestamp},{celsius},C",
            "container": "/temperature/",
            "extension": ".log"
        }
    }]
}
```

### HTTP Recorder

This recorder will send measured data as JSON object in the body to the configured `endpoint` using HTTP POST. The `endpoint` can contain dynamic values.

Optionally `headers` can be configured to be sent in the request.

> `Content-Type` header should not be provided and if so will not be used since it is fixed to `application/json`.

Example configuration:

```json
{
    "recorders": [{
        "type": "http",
        "config": {
            "endpoint": "https://host/api/temperature/{device_id}",
            "headers": [
                { "Authorization": "Bearer ABCDE12345" }
            ]
        }
    }]
}
```