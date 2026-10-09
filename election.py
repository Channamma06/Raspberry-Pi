from machine import Pin
import time
import random
password=1234
buzzer = Pin(15, Pin.OUT)

button1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(1, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(2, Pin.IN, Pin.PULL_DOWN)
button4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
button5 = Pin(4,Pin.IN,Pin.PULL_DOWN)
led = Pin(5, Pin.OUT)

I2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000)

# Scan for I2C device
i2c_add = i2c.scan()
lcd = I2cLcd(i2c, i2c_add[0], 2, 16)
lcd.backlight_on()
lcd.clear()


INC = 0
BJP = 0
JDS = 0
OTH = 0

def led_operation():
    led.value(1)
    time.sleep(0.3)
    led.value(0)

def buzzer_operation():
    buzzer.value(1)
    time.sleep(0.3)
    buzzer.value(0)

while True:
    if button1.value() == 1:
        INC += 1
        led_operation()
        buzzer_operation()
        time.sleep(0.5) 
        print("Done")
    elif button2.value() == 1:
        BJP += 1
        led_operation()
        buzzer_operation()
        time.sleep(0.5)
        print("Done")

    elif button3.value() == 1:
        OTH += 1
        led_operation()
        buzzer_operation()
        time.sleep(0.5)
        print("Done")
    elif button4.value()==1:
        JDS+=1
        led_operation()
        buzzer_operation()
        time.sleep(0.5)
        print("Done")
    elif button5.value() == 1:
        passwrd=int(input("Enter the PassWord:"))
        if passwrd==password:
            print("----- Voting Result Window -----")
            print("INC Votes:", INC)
            print("BJP Votes:", BJP)
            print("OTH Votes:", OTH)
            print("JDS Votes:", JDS)
            time.sleep(0.3)
            if INC > BJP and INC > OTH and INC>JDS:
                print("INC Wins")
                break
            elif BJP > INC and BJP > OTH and BJP>JDS:
                print("BJP Wins")
                break
            elif OTH > INC and OTH > BJP and OTH>JDS:
                print("OTH Wins")
                break
            elif JDS>INC and JDS>BJP and JDS>OTH:
                print("JDS Wins")
                break 
        else:
               print("Tie / Results Awaited")
            
while True:
        lcd.clear()

        lcd.move_to(0, 0)
        lcd.putstr("INC WINS")

        time.sleep(1)
        lcd.move_to(0, 0)
        lcd.putstr("BJP WINS")

        time.sleep(1)
        lcd.move_to(0, 0)
        lcd.putstr("OTH WINS")

        time.sleep(1)
        lcd.move_to(0, 0)
        lcd.putstr("JDS WINS")

        time.sleep(1)
                                                              