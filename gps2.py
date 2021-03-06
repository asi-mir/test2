from tkinter import *
#import serial
import pynmea2
import requests
import io
from PIL import Image, ImageTk
from threading import Timer

def read_gps_load_map():
    global label
    serial_port = serial.Serial("/dev/serial0", 9600, timeout=0.5)
    gps_data = serial_port.decode("utf8") 
    if gps_data.find("GGA") > 0:
        msg = pynmea2.parse(gps_data)
    
        #https://api.mapbox.com/styles/v1/{username}/{style_id}/static/{overlay}/{lon},{lat},{zoom},{bearing},{pitch}|{bbox}|{auto}/{width}x{height}{@2x}
        mapbox_url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/{},{},1,0,60/600x600?access_token=pk.eyJ1Ijoib2xkYm95MSIsImEiOiJja3l2dmttZTgwMmphMnNxdzdneWlrc2prIn0.Y0ikftYadGXpBD_ZhG70Zw".format(msg.lat,msg.lon)
        response = requests.get(mapbox_url)
        image_bytes = response.content
        #conver bytes to image
        data_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(data_stream)
        tk_image = ImageTk.PhotoImage(pil_image)
        #update label
        label.configure(image=tk_image)
        label.image = tk_image
        
    Timer(1.0, read_gps_load_map).start()


root = Tk()
url = "https://paroshat.com/wp-content/uploads/2022/01/The-Marvelous-Mrs.-Maisel-2-750x422.jpg"
#get cat image
response = requests.get(url)
image_bytes = response.content
data_stream = io.BytesIO(image_bytes)
pil_image = Image.open(data_stream)
tk_image = ImageTk.PhotoImage(pil_image)
label = Label(root, image=tk_image)
label.image = tk_image
label.pack(padx=5,pady=5)

read_gps_load_map()

root.mainloop()

