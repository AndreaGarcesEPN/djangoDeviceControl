import logging
from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
    TUYA_LOGGER,
)

ACCESS_ID = "3ujca7y7apppqpcjjmdt"
ACCESS_KEY = "e719ad0396c74b64bad8510c8baa491c"
API_ENDPOINT = "https://openapi.tuyaus.com"

# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init openapi and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

DEVICE_ID = "vdevo170000581142241"

#response = openapi.get("/v1.0/iot-03/devices/{}".format(DEVICE_ID)) #info devices
#response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))

#resquest= openapi.get("/v1.0/token")

commands = {"commands":[{"code":"switch_1","value":False}]}
request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)
#print(request)
