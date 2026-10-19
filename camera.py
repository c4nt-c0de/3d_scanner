import io
import os
from picamera2 import Picamera2

class CameraManager:
    def __init__(self):
        self.picam2 = Picamera2()
        self.stream_config = self.picam2.create_video_configuration(main={"size": (640, 480), "format": "RGB888"})
        self.picam2.configure(self.stream_config)
        self.picam2.start()
        
        self.picam2.set_controls({
            "AfMode": 0,
            "LensPosition": 10.0,
            "ExposureTime": 100000,
            "AnalogueGain": 1.0
        })

    def get_stream_frame(self):
        stream = io.BytesIO()
        self.picam2.capture_file(stream, format='jpeg')
        return stream.getvalue()

    def capture_to_file(self, filepath):
        self.picam2.stop()
        still_config = self.picam2.create_still_configuration(main={"size": (4608, 2592)})
        self.picam2.configure(still_config)
        self.picam2.start()
        
        self.picam2.set_controls({
            "AfMode": 0,
            "LensPosition": 10.0,
            "ExposureTime": 100000,
            "AnalogueGain": 1.0
        })
        
        self.picam2.capture_file(filepath)
        
        self.picam2.stop()
        self.picam2.configure(self.stream_config)
        self.picam2.start()
        
        self.picam2.set_controls({
            "AfMode": 0,
            "LensPosition": 10.0,
            "ExposureTime": 100000,
            "AnalogueGain": 1.0
        })

camera = CameraManager()
