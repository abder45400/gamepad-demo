def on_mes_dpad_controller_id_microbit_evt():
    global lastValue, vitesseM2, vitesseM1
    if lastValue != control.event_value():
        lastValue = control.event_value()
        vitesseM2 = 255
        vitesseM1 = 255
        led.stop_animation()
        if control.event_value() == 1:
            motor.motor_run(motor.Motors.M1, motor.Dir.CCW, vitesseM1)
            motor.motor_run(motor.Motors.M2, motor.Dir.CW, vitesseM2)
            basic.show_string("A")
        elif control.event_value() == 3:
            motor.motor_run(motor.Motors.M1, motor.Dir.CW, vitesseM1)
            motor.motor_run(motor.Motors.M2, motor.Dir.CCW, vitesseM2)
            basic.show_string("B")
        elif control.event_value() == 5:
            motor.motor_run(motor.Motors.M1, motor.Dir.CCW, vitesseM1)
            motor.motor_run(motor.Motors.M2, motor.Dir.CCW, vitesseM2)
            basic.show_string("C")
        elif control.event_value() == 7:
            motor.motor_run(motor.Motors.M1, motor.Dir.CW, vitesseM1)
            motor.motor_run(motor.Motors.M2, motor.Dir.CW, vitesseM2)
            basic.show_string("D")
        elif control.event_value() == 9:
            motor.motor_stop_all()
            basic.show_string("1")
        else:
            basic.clear_screen()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

vitesseM2 = 0
vitesseM1 = 0
lastValue = 0
lastValue = 0
vitesseM1 = 0
vitesseM2 = 0
bluetooth.start_led_service()
basic.show_string("GAMEPAD DEMO")