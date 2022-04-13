# Complete project details at https://RandomNerdTutorials.com

import dht
import ssd1306
from machine import Pin, SoftI2C
from time import sleep

sensor = dht.DHT22(Pin(23))
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

tempMIN = + 100
tempMAX = - 100

while True:
    
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        if temp > tempMAX:
            tempMAX = temp
        if temp < tempMIN:
            tempMIN = temp

        oled.fill(0)
        oled.text('TempC   : %3.1f C' % temp, 0, 0)
        oled.text('Feuchte : %3.1f %%' %hum, 0, 10)
        oled.text('TMin    : %3.1f C' %tempMIN, 0, 20)
        oled.text('TMax    : %3.1f C' %tempMAX, 0, 30)
        oled.show()

    except OSError as e:
        print('Failed to read sensor.')