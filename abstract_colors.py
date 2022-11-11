import time
from random import seed
from random import randint

from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 650000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
#LED_STRIP      = ws.SK6812_STRIP_RGBW
LED_STRIP      = ws.SK6812W_STRIP
k = 0
A = [0]*256


""" Define functions which animate LEDs in various ways. """

def wipe_together(strip, pos, wait_ms=0):
	# Wipe color across display a pixel at a time.
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, wheel(pos))
	strip.show()
	time.sleep(wait_ms/1000.0)


def wipe_separately(strip, pos, arr):
	# Wipe color across display a pixel at a time.
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, wheel(pos+ arr[i]))
		arr[i] += randint(0, 1)
		if arr[i] >= 255:
			arr[i] -= 255
	strip.show()


def wheel(pos):
    # Generate rainbow colors across 0-255 positions.
    if pos > 255:
        pos -= 255
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	seed(1)
	for i in range(len(A):
		A[i] = randint(0, 255)

	print ('Press Ctrl-C to quit.')
	while True:
		# wipe_together(strip, k)
		wipe_separately(strip, k, A)
		k = k+1
		if k == 255:
			k = 0
		time.sleep(0.1)
