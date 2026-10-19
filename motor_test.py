import time
from gpiozero import DigitalOutputDevice
from config import TURNTABLE_STEP_PIN, TURNTABLE_DIR_PIN, TURNTABLE_EN_PIN

def test_motor():
    step_pin = DigitalOutputDevice(TURNTABLE_STEP_PIN, active_high=True, initial_value=False)
    dir_pin = DigitalOutputDevice(TURNTABLE_DIR_PIN, active_high=True, initial_value=False)
    en_pin = DigitalOutputDevice(TURNTABLE_EN_PIN, active_high=True, initial_value=False)
    
    # Enable driver (active low)
    en_pin.off()
    print("Motor enabled. Starting test steps...")

    try:
        for direction in [True, False]:
            dir_pin.value = 1 if direction else 0
            print(f"Moving direction: {'Forward' if direction else 'Backward'}")
            
            for _ in range(200):
                step_pin.on()
                time.sleep(0.005)
                step_pin.off()
                time.sleep(0.005)
                
            time.sleep(1)
    finally:
        en_pin.on()
        print("Test complete. Motor disabled.")

if __name__ == "__main__":
    test_motor()
