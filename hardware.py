from gpiozero import LED, Button
from config import LED_RED_PIN, LED_GREEN_PIN, BUTTON_PREVIEW_PIN, BUTTON_SCAN_PIN

red_led = LED(LED_RED_PIN)
green_led = LED(LED_GREEN_PIN)

preview_btn = Button(BUTTON_PREVIEW_PIN, pull_up=True, bounce_time=0.02)
scan_btn = Button(BUTTON_SCAN_PIN, pull_up=True, bounce_time=0.02)
