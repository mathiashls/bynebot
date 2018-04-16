from bynebot_vocabulary import BYNEBOT_INVALID_INPUT
from modules.light_controller import LightController

from errbot import BotPlugin, botcmd, ValidationException
from random import choice
from itertools import chain


class ByneBot(BotPlugin):

    CONFIG_TEMPLATE = {
        "all": [0, 3, 4, 5, 6, 7],
        "staff_back": 0,
        "staff_mid": 3,
        "staff_front": 4,
        "tv": 5,
        "kitchen": 7,
        "entrance": 6,
        "plc_host": "172.16.16.180"
    }

    def get_configuration_template(self):
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            self['config'] = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            self['config'] = CONFIG_TEMPLATE

        self['light_controller'] = LightController(self['config']['plc_host'])
        super(ByneBot, self).configure(self['config'])

    @botcmd(split_args_with=None)
    def turn_on(self, msg, arg):
        """
            Turn the lights on.

            Syntax: turn on [place]
        """
        if self.argument_is_valid(arg):
            if self['light_controller']:
                self['light_controller'].turn(self['config'][arg], True)
            else:
                yield("You may configure your light controller first!")
        else:
            yield choice(BYNEBOT_INVALID_INPUT)

    @botcmd(split_args_with=None)
    def turn_off(self, msg, arg):
        """
            Turn the lights off.

            Syntax: turn off [place]
        """
        if self.argument_is_valid(arg):
            if self['light_controller']:
                self['light_controller'].turn(self['config'][arg], False)
            else:
                yield("You may configure your light controller first!")
        else:
            yield choice(BYNEBOT_INVALID_INPUT)

    def argument_is_valid(self, arg):
        if not arg or len(arg) > 1:
            return False
        elif arg not in self['config'].keys():
            return False
        return True
