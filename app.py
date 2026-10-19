import os
import shutil
import threading
from datetime import datetime
from time import sleep
from flask import Flask, Response, render_template
from hardware import red_led, green_led
from camera import camera
from motor import motor
from config import PHOTOS_PER_ROTATION

app = Flask(__name__)
IMGS_DIR = "imgs"
os.makedirs(IMGS_DIR, exist_ok=True)

is_scanning = False
stop_requested = False
current_session_dir = None

def run_scan_sequence():
    global is_scanning, stop_requested, current_session_dir
    if is_scanning:
        return
    is_scanning = True
    stop_requested = False
    
    total_photos = PHOTOS_PER_ROTATION
    steps_per_photo = motor.steps_per_photo
    
    timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    current_session_dir = os.path.join(IMGS_DIR, f"scan_{timestamp_str}")
    os.makedirs(current_session_dir, exist_ok=True)
    
    for i in range(total_photos):
        if stop_requested:
            break
            
        green_led.on()
        sleep(0.5)
        green_led.off()
        sleep(0.5)
        
        if stop_requested:
            break
            
        filename = os.path.join(current_session_dir, f"photo_{i:03d}.jpg")
        camera.capture_to_file(filename)
        
        if stop_requested:
            break
            
        motor.rotate_steps(steps_per_photo, direction=True)
        sleep(0.5)
    
    green_led.off()
    
    if stop_requested and current_session_dir and os.path.exists(current_session_dir):
        shutil.rmtree(current_session_dir)
        
    is_scanning = False
    current_session_dir = None

def run_preview_scan_sequence():
    global is_scanning, stop_requested
    if is_scanning:
        return
    is_scanning = True
    stop_requested = False
    
    total_steps = motor.total_steps_per_rev
    
    red_led.on()
    motor.rotate_steps(total_steps, direction=True, delay=0.0004)
    red_led.off()
    
    is_scanning = False

def generate_frames():
    while True:
        try:
            frame = camera.get_stream_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            sleep(0.1)
        except Exception:
            sleep(0.5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/trigger')
def trigger():
    if not is_scanning:
        threading.Thread(target=run_scan_sequence).start()
        return "Scan triggered"
    return "Scan already running"

@app.route('/preview_scan')
def preview_scan():
    if not is_scanning:
        threading.Thread(target=run_preview_scan_sequence).start()
        return "Preview scan triggered"
    return "Scan already running"

@app.route('/stop')
def stop_scan():
    global stop_requested
    stop_requested = True
    return "Stop requested, cleaning up..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
