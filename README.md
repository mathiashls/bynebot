# BYNE.bot

_Beep beep._

This is an [Errbot](http://errbot.io/en/latest/index.html#) plugin created to make it easy for [BYNE](http://www.simb.com.br/)'s crew to handle it's office infrasctruture.

## Bot commands

* turn [on|off] **place**: activate the relay associated with **place**. The **place** parameter can be "all".

    `turn on kitchen` - Turns the kitchen light on.

    `turn off all` - Turns all lights off.

* configure **configuration**: make possible to configure the **places**, as well as the host used to control the relays.

    `configure {'kitchen': 3}` - Set the coil id for kitchen as 3.

    `configure {'kitchen': 3, 'plc_host': '192.168.1.2'}` - Set the coil id for kitchen and the relay host.
