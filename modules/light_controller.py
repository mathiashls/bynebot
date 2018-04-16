# Simple python module to ease the PLC management
from pymodbus.client.sync import ModbusTcpClient


class LightController(object):

    def __init__(self, host):
        self.client = ModbusTcpClient(host)

    def turn(self, id, option):
        if isinstance(option, bool):
            if isinstance(id, list):
                for item in id:
                    self.client.write_coil(item, option)
                return
            else:
                self.client.write_coil(id, option)
                return
        raise Exception
