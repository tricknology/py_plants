import RPi.GPIO as GPIO
import time

def main():
    set_gpio()

def set_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)

    for i in range(0, 2000):
        print
        "LED on"
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        print
        "LED off"
        GPIO.output(18, GPIO.LOW)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
