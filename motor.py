import time
from gpiozero import DigitalOutputDevice
from config import (
    TURNTABLE_STEP_PIN, TURNTABLE_DIR_PIN, TURNTABLE_EN_PIN,
    FULL_STEPS_PER_REV, MICROSTEPS, PHOTOS_PER_ROTATION
)

class MotorController:
    def __init__(self):
        self.step_pin = DigitalOutputDevice(TURNTABLE_STEP_PIN, active_high=True, initial_value=False)
        self.dir_pin = DigitalOutputDevice(TURNTABLE_DIR_PIN, active_high=True, initial_value=False)
        self.en_pin = DigitalOutputDevice(TURNTABLE_EN_PIN, active_high=True, initial_value=False)
        self.en_pin.off()

    @property
    def total_steps_per_rev(self):
        return FULL_STEPS_PER_REV * MICROSTEPS

    @property
    def steps_per_photo(self):
        return round(self.total_steps_per_rev / PHOTOS_PER_ROTATION)

    def rotate_steps(self, steps, direction=True, delay=0.001):
        self.dir_pin.value = 1 if direction else 0
        for _ in range(steps):
            self.step_pin.on()
            time.sleep(delay)
            self.step_pin.off()
            time.sleep(delay)

motor = MotorController()
