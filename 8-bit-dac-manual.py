import RPi.GPIO as GPIO
inport time

leds = [24,22,23,27,17,25,5,16]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

dynamic_range = 3.3

def voltage_to_number (voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print ("Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В")
        print ("Устанавливаем 0.0 В")
        return 0

    return int (voltage / dynamic_range * 255)

def number_to_dac (number):
    a = [int(i) for i in bin(number)[2:].zfill(8)]
    print (a)
    for i in range (len (a)):
        GPIO.OUTPUT (dac_bits [i], a[i])



try:
    while True:
        try:
            voltage = float (input ("Введите напряжение в вольтах:"))
            number = voltage_to_number (voltage)
            number_to_dac (number)

        except ValueError:
                print ("Вы ввели не число. Еще раз\n")
finally:
    GPIO.output (dac_bits, 0)
    GPIO.cleanup()

