import serial
import serial.tools.list_ports

class GPSDriver:
    def __init__(self, baudrate=9600):
        self.ser = None
        ports = list(serial.tools.list_ports.comports())
        
        # Try to find an active port
        for p in ports:
            try:
                self.ser = serial.Serial(p.device, baudrate, timeout=1)
                print(f"[🛰️ GPS] Found and Listening on {p.device}")
                break
            except:
                continue
        
        if not self.ser:
            print("[🛰️ GPS] No hardware detected. Using Stretford Defaults.")

    def get_location(self):
        if not self.ser:
            return {"lat": 53.448, "lon": -2.305}
        return {"lat": "Searching...", "lon": "Searching..."}
