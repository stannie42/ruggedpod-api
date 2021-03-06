from lxml import etree
import time
import mock

from common import importutils

GPIO = importutils.try_import('RPi.GPIO', default=mock.Mock(),
                              warn="WARNING: RPi.GPIO could not be imported,"
                              " you are in MOCK MODE!")

attention_led_dict = {'1' : 7,
                     '2' : 12
                    }
power_dict = { '1' : 7,
               '2' : 12
             }

reset_dict = { '1' : 7,
               '2' : 12
             }

onoff_dict = { '1' : 7,
               '2' : 12
             }
short_press = 0.2
long_press = 6

serial_select_dict = { '0' : 7,      # Least significan bit
                      '1' : 12      # Most significan bit
                    }


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    # Set all led in Output
    for blade_id in attention_led_dict:
        GPIO.setup(attention_led_dict[blade_id], GPIO.OUT)
    for blade_id in power_dict:
        GPIO.setup(power_dict[blade_id], GPIO.OUT)
    for blade_id in reset_dict:
        GPIO.setup(reset_dict[blade_id], GPIO.OUT)
        GPIO.output(reset_dict[blade_id], False)
    for blade_id in onoff_dict:
        GPIO.setup(onoff_dict[blade_id], GPIO.OUT)
        GPIO.output(onoff_dict[blade_id], False)

def _set_default_xml_attr(response):
    etree.SubElement(response, 'CompletionCode').text = 'Success'
    etree.SubElement(response, 'statusDescription').text = ''
    etree.SubElement(response, 'apiVersion').text = '1'

def set_blade_attention_led_on(blade_id):
    GPIO.output( attention_led_dict[blade_id], True)
    response = etree.Element('BladeResponse')
    _set_default_xml_attr(response)
    etree.SubElement(response, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_all_blades_attention_led_on():
    response = etree.Element('AllBladesResponse')
    for blade_id in attention_led_dict:
        GPIO.output(attention_led_dict[blade_id], True)
        blade = etree.SubElement(response, 'BladeResponse')
        _set_default_xml_attr(response)
        etree.SubElement(blade, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_blade_attention_led_off(blade_id):
    GPIO.output( attention_led_dict[blade_id], False)
    response = etree.Element('BladeResponse')
    _set_default_xml_attr(response)
    etree.SubElement(response, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_all_blades_attention_led_off():
    response = etree.Element('AllBladesResponse')
    for blade_id in attention_led_dict:
        GPIO.output(attention_led_dict[blade_id], False)
        blade = etree.SubElement(response, 'BladeResponse')
        _set_default_xml_attr(response)
        etree.SubElement(blade, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def get_all_power_state():
    response = etree.Element('GetAllPowerStateResponse')
    for blade_id in power_dict:
        if GPIO.input(power_dict[blade_id]):
            PowerState = 'ON'
        else:
            PowerState = 'OFF'
        power = etree.SubElement(response, 'PowerStateResponse')
        blade = etree.SubElement(power, 'bladeResponse')
        _set_default_xml_attr(response)
        etree.SubElement(blade, 'bladeNumber').text = blade_id
        etree.SubElement(power, 'powerState').text = PowerState
    return etree.tostring(response, pretty_print=True)

def get_power_state(blade_id):
    print 'OK'
    response = etree.Element('PowerStateResponse')
    if GPIO.input(power_dict[blade_id]):
        PowerState = 'ON'
    else:
        PowerState = 'OFF'
    blade = etree.SubElement(response, 'bladeResponse')
    _set_default_xml_attr(response)
    etree.SubElement(blade, 'bladeNumber').text = blade_id
    etree.SubElement(response, 'powerState').text = PowerState
    return etree.tostring(response, pretty_print=True)

def set_power_on(blade_id):
    GPIO.output( power_dict[blade_id], True)
    response = etree.Element('BladeResponse')
    _set_default_xml_attr(response)
    etree.SubElement(response, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_power_off(blade_id):
    GPIO.output(power_dict[blade_id], False)
    response = etree.Element('BladeResponse')
    _set_default_xml_attr(response)
    etree.SubElement(response, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_all_power_on():
    response = etree.Element('AllBladesResponse')
    for blade_id in power_dict:
        GPIO.output(power_dict[blade_id], True)
        blade = etree.SubElement(response, 'BladeResponse')
        _set_default_xml_attr(response)
        etree.SubElement(blade, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_all_power_off():
    response = etree.Element('AllBladesResponse')
    for blade_id in power_dict:
        GPIO.output( power_dict[blade_id], False)
        blade = etree.SubElement(response, 'BladeResponse')
        _set_default_xml_attr(response)
        etree.SubElement(blade, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_blade_short_onoff(blade_id):
    GPIO.output(onoff_dict[blade_id], True)
    time.sleep(short_press)
    GPIO.output(onoff_dict[blade_id], False)
    response = etree.Element('BladeResponse')
    _set_default_xml_attr(response)
    etree.SubElement(response, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_all_blades_short_onoff():
    for blade_id in onoff_dict:
        GPIO.output(onoff_dict[blade_id], True)
    time.sleep(short_press)
    response = etree.Element('AllBladesResponse')
    for blade_id in onoff_dict:
        GPIO.output(onoff_dict[blade_id], False)
        blade = etree.SubElement(response, 'BladeResponse')
        _set_default_xml_attr(response)
        etree.SubElement(blade, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def set_blade_long_onoff(blade_id):
    GPIO.output(onoff_dict[blade_id], True)
    time.sleep(long_press)
    GPIO.output(onoff_dict[blade_id], False)
    response = etree.Element('BladeResponse')
    _set_default_xml_attr(response)
    etree.SubElement(response, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)


def set_all_blades_long_onoff():
    for blade_id in onoff_dict:
        GPIO.output(onoff_dict[blade_id], True)
    time.sleep(long_press)
    response = etree.Element('AllBladesResponse')
    for blade_id in onoff_dict:
        GPIO.output(onoff_dict[blade_id], False)
        blade = etree.SubElement(response, 'BladeResponse')
        _set_default_xml_attr(response)
        etree.SubElement(blade, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)

def start_blade_serial_session(blade_id):
    for address_bit in serial_select_dict:
        status = False
        if (((int(blade_id) - 1) >> int(address_bit)) & 1):
            status = True
        GPIO.output(serial_select_dict[address_bit], status)
    response = etree.Element('BladeResponse')
    _set_default_xml_attr(response)
    etree.SubElement(response, 'bladeNumber').text = blade_id
    return etree.tostring(response, pretty_print=True)
