# Simple python module to ease the PLC management
from pymodbus.client.sync import ModbusTcpClient


class LightController(object):

    def __init__(self, host):
        self.client = ModbusTcpClient(host)

    def turn(self, id, option):
        if isinstance(option, bool):
            self.client.write_coil(id, option)
            return
        raise Exception

    def turn_range_on(self, min, max):
        for id in range(min, max+1):
            self.client.write_coil(id, False)

    def turn_range_off(self, min, max):
        for id in range(min, max+1):
            self.client.write_coil(id, True)
