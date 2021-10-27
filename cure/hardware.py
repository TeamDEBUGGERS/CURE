# Team DEBUGGERS 2021, Project CURE

# Hardware Module

# Latest update : 2021.10.18
# Developer : LEE Seok Ho

import board
import busio as io
import adafruit_mlx90614
import os
import RPi.GPIO as GPIO
import time
from rpi_ws281x import *

def temp(): #체온 측정 후 값 반환
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)
    temp = round(float("{:.2f}".format(mlx.object_temperature)), 1)

    if float(temp) >= 37.5 and float(temp) < 38.5: #미열
        led('red')
        sound('warning')
        sanitizer()
        return str(temp) + '°C 미열' 
    elif float(temp) >= 38.5: #고열
        led('red')
        sound('warning')
        sanitizer()
        return str(temp) + '°C 고열'   
    else: #정상체온
        led('green')
        sound('ding')
        sanitizer()
        return str(temp) + '°C 정상'

def colorWipe(strip, color, a, wait_ms=50): #인디케이터 LED 설정
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/a)
    
def led(color): #인디케이터 LED 출력
    strip = Adafruit_NeoPixel(8, 18, 800000, 10, False, 255, 0)
    strip.begin()
    if color == 'green':
        colorWipe(strip, Color(0, 255, 0), 1000)
        colorWipe(strip, Color(0, 0, 0), 1000)
    elif color == 'blue':
        colorWipe(strip, Color(0, 0, 255), 1000)
        colorWipe(strip, Color(0, 0, 0), 1000)
    elif color == 'red':
        for i in range(1,3):
            colorWipe(strip, Color(255, 0, 0), 3000)
            colorWipe(strip, Color(0, 0, 0), 3000)

def sound(name): #효과음 재생
    os.system('cvlc ./sound/' + name + '.mp3 --play-and-exit')
    
def sanitizer(): #손소독제 분사
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.LOW)
    time.sleep(1)
    GPIO.output(23, GPIO.HIGH)
