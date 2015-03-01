
import sys
from flask import Flask, request
from common import importutils
app = Flask(__name__)

if '-m' in sys.argv:
    import service_mock as service
else:
    importutils.exit_if_module_missing('RPi')
    import service_gpio as service


@app.route("/SetBladeAttentionLEDOn")
def SetBladeAttentionLEDOn():
    if 'bladeId' in request.args:
        return service.SetBladeAttentionLEDOn(request.args['bladeId'])
    else:
        return 'Set bladeId'

@app.route("/SetAllBladesAttentionLEDOn")
def SetAllBladesAttentionLEDOn():
    return service.SetAllBladesAttentionLEDOn()

@app.route("/SetBladeAttentionLEDOff")
def SetBladeAttentionLEDOff():
    if 'bladeId' in request.args:
        return service.SetBladeAttentionLEDOff(request.args['bladeId'])
    else:
        return 'Set bladeId'

@app.route("/SetAllBladesAttentionLEDOff")
def SetAllBladesAttentionLEDOff():
    return service.SetAllBladesAttentionLEDOff()

@app.route("/GetAllPowerState")
def GetAllPowerState():
    return service.GetAllPowerState()

@app.route("/GetPowerState")
def GetPowerState():
    if 'bladeId' in request.args:
        return service.GetPowerState(request.args['bladeId'])
    else:
        return 'Set bladeId'

@app.route("/SetPowerOn")
def SetPowerOn():
    if 'bladeId' in request.args:
        return service.SetPowerOn(request.args['bladeId'])
    else:
        return 'Set bladeId'

@app.route("/SetPowerOff")
def SetPowerOff():
    if 'bladeId' in request.args:
        return service.SetPowerOff(request.args['bladeId'])
    else:
        return 'Set bladeId'

@app.route("/SetAllPowerOn")
def SetAllPowerOn():
    return service.SetAllPowerOn()

@app.route("/SetAllPowerOff")
def SetAllPowerOff():
    return service.SetAllPowerOff()



if __name__ == "__main__":
    service.init()

    app.run(host= '0.0.0.0')
