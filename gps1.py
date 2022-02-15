import serial
import pynmea2

serial_port = serial.Serial("/dev/serial0", 9600, timeout=0.5)

def parse_gps(gps_data):
    if gps_data.find("GGA") > 0:
        msg = pynmea2.parse(gps_data)
        #msg.lat
        #msg.lon
        #msg.lat_dir
        #msg.lon_dir
        

while True:
    sr = serial_port.readline()
    sr = sr.decode("utf8") 
    parse_gps(sr)
    