control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function () {
    if (lastValue != control.eventValue()) {
        lastValue = control.eventValue()
        vitesseM2 = 255
        vitesseM1 = 255
        led.stopAnimation()
        if (control.eventValue() == 1) {
            motor.MotorRun(motor.Motors.M1, motor.Dir.CCW, vitesseM1)
            motor.MotorRun(motor.Motors.M2, motor.Dir.CW, vitesseM2)
            basic.showString("A")
        } else if (control.eventValue() == 3) {
            motor.MotorRun(motor.Motors.M1, motor.Dir.CW, vitesseM1)
            motor.MotorRun(motor.Motors.M2, motor.Dir.CCW, vitesseM2)
            basic.showString("B")
        } else if (control.eventValue() == 5) {
            motor.MotorRun(motor.Motors.M1, motor.Dir.CCW, vitesseM1)
            motor.MotorRun(motor.Motors.M2, motor.Dir.CCW, vitesseM2)
            basic.showString("C")
        } else if (control.eventValue() == 7) {
            motor.MotorRun(motor.Motors.M1, motor.Dir.CW, vitesseM1)
            motor.MotorRun(motor.Motors.M2, motor.Dir.CW, vitesseM2)
            basic.showString("D")
        } else if (control.eventValue() == 9) {
            motor.motorStopAll()
            basic.showString("1")
        } else {
            basic.clearScreen()
        }
    }
})
let vitesseM2 = 0
let vitesseM1 = 0
let lastValue = 0
lastValue = 0
vitesseM1 = 0
vitesseM2 = 0
bluetooth.startLEDService()
