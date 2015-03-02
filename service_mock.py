import mock
from lxml import etree

import service_gpio

AttentionLEDTable={'1' : 1,
                   '2' : 2,
                   '3' : 3,
                   '4' : 4
                  }

PowerTable={'1' : 5,
            '2' : 6,
            '3' : 7,
            '4' : 8
           }


PowerState = { '1' : 'ON',
               '2' : 'OFF',
               '3' : 'OFF',
               '4' : 'ON'
             }


def init():
    print "Mock Ready"

@mock.patch('service_gpio.GPIO.output')
def SetBladeAttentionLEDOn(bladeId, mock_gpio_output):
    return service_gpio.SetBladeAttentionLEDOn(bladeId)

@mock.patch('service_gpio.GPIO.output')
def SetAllBladesAttentionLEDOn(mock_gpio_output):
    return service_gpio.SetAllBladesAttentionLEDOn()

@mock.patch('service_gpio.GPIO.output')
def SetBladeAttentionLEDOff(bladeId, mock_gpio_output):
    return service_gpio.SetBladeAttentionLEDOff(bladeId)

@mock.patch('service_gpio.GPIO.output')
def SetAllBladesAttentionLEDOff(mock_gpio_output):
    return service_gpio.SetAllBladesAttentionLEDOff()

@mock.patch('service_gpio.GetAllPowerState._GetPowerState')
def GetAllPowerState(mock_get_powerstate):
    mock_get_powerstate.side_effect = PowerState.values()
    return service_gpio.GetAllPowerState()
