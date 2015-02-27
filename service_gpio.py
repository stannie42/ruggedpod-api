
import RPi.GPIO as GPIO
from lxml import etree

AttentionLEDTable = {'1' : 7,
                     '2' : 12
                    }
PowerTable = { '1' : 7,
               '2' : 12
             }

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    # Set all led in Output
    for bladeId in AttentionLEDTable:
        GPIO.setup( AttentionLEDTable[ bladeId ], GPIO.OUT )
    for bladeId in PowerTable:
        GPIO.setup( PowerTable[ bladeId ], GPIO.OUT )


def SetBladeAttentionLEDOn( bladeId ):
    SetBladeAttentionLED(bladeId, True)

def SetBladeAttentionLEDOff( bladeId ):
    SetBladeAttentionLED(bladeId, False)

def SetBladeAttentionLED(bladeId, active):
    GPIO.output( AttentionLEDTable[ bladeId ], active)
    response = etree.Element('BladeResponse')
    etree.SubElement(response, 'CompletionCode').text = 'Success'
    etree.SubElement(response, 'statusDescription').text = ''
    etree.SubElement(response, 'apiVersion').text = '1'
    etree.SubElement(response, 'bladeNumber').text = bladeId
    return etree.tostring(response, pretty_print=True)

def SetAllBladesAttentionLEDOn():
    SetAllBladesAttentionLED(True)

def SetAllBladesAttentionLEDOff():
    SetAllBladesAttentionLED(False)

def SetAllBladesAttentionLED(active):
    response = etree.Element('AllBladesResponse')
    for bladeId in AttentionLEDTable:
        GPIO.output( AttentionLEDTable[ bladeId ], active)
        blade = etree.SubElement(response, 'BladeResponse')
        etree.SubElement(blade, 'CompletionCode').text = 'Success'
        etree.SubElement(blade, 'statusDescription').text = ''
        etree.SubElement(blade, 'apiVersion').text = '1'
        etree.SubElement(blade, 'bladeNumber').text = bladeId
    return etree.tostring(response, pretty_print=True)

def GetAllPowerState():
    response = etree.Element('GetAllPowerStateResponse')
    for bladeId in PowerTable:
        if GPIO.input( PowerTable[bladeId] ):
            PowerState = 'ON'
        else:
            PowerState = 'OFF'
        power = etree.SubElement(response, 'PowerStateResponse')
        blade = etree.SubElement(power, 'bladeResponse')
        etree.SubElement(blade, 'CompletionCode').text = 'Success'
        etree.SubElement(blade, 'statusDescription').text = ''
        etree.SubElement(blade, 'apiVersion').text = '1'
        etree.SubElement(blade, 'bladeNumber').text = bladeId
        etree.SubElement(power, 'powerState').text = PowerState
    return etree.tostring(response, pretty_print=True)

def GetPowerState(bladeId):
    print 'OK'
    response = etree.Element('PowerStateResponse')
    if GPIO.input( PowerTable[bladeId] ):
        PowerState = 'ON'
    else:
        PowerState = 'OFF'
    blade = etree.SubElement(response, 'bladeResponse')
    etree.SubElement(blade, 'CompletionCode').text = 'Success'
    etree.SubElement(blade, 'statusDescription').text = ''
    etree.SubElement(blade, 'apiVersion').text = '1'
    etree.SubElement(blade, 'bladeNumber').text = bladeId
    etree.SubElement(response, 'powerState').text = PowerState
    return etree.tostring(response, pretty_print=True)

def SetPowerOn(bladeId):
    SetPower(bladeId, Tuee)

def SetPowerOff(bladeId):
    SetPower(bladeId, False)

def SetPower(bladeId, active):
    GPIO.output( PowerTable[ bladeId ], active)
    response = etree.Element('BladeResponse')
    etree.SubElement(response, 'CompletionCode').text = 'Success'
    etree.SubElement(response, 'statusDescription').text = ''
    etree.SubElement(response, 'apiVersion').text = '1'
    etree.SubElement(response, 'bladeNumber').text = bladeId
    return etree.tostring(response, pretty_print=True)

def SetAllPowerOn():
    SetAllPower(True);

def SetAllPowerOff():
    SetAllPower(False);

def SetAllPower(active):
    response = etree.Element('AllBladesResponse')
    for bladeId in PowerTable:
        GPIO.output(PowerTable[ bladeId ], active)
        blade = etree.SubElement(response, 'BladeResponse')
        etree.SubElement(blade, 'CompletionCode').text = 'Success'
        etree.SubElement(blade, 'statusDescription').text = ''
        etree.SubElement(blade, 'apiVersion').text = '1'
        etree.SubElement(blade, 'bladeNumber').text = bladeId
    return etree.tostring(response, pretty_print=True)