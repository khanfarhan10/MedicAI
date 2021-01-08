# python QRGenerate.py
# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
import os
  
# TODO implement QR reader

def create_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
    return dir
def GetQRCodeImage(LongString,QRSaveDirectory,QROutputPath):
    # Generate QR code 
    url = pyqrcode.create(LongString) 
    # Create and save the png file naming "myqr.png" 
    create_dir(QRSaveDirectory)
    url.png(os.path.join(QRSaveDirectory,QROutputPath), scale = 6)

if __name__=='__main__':
    # String which represents the QR code 
    s = "www.geeksforgeeks.org"
    QRSaveDirectory='QROutputs'
    QROutputPath='QRCode101.png'
    GetQRCodeImage(s,QRSaveDirectory,QROutputPath)
    
    
    
"""
print(os.getcwd())
"""
"""

# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming "myqr.svg" 
# url.svg("myqr.svg", scale = 8) 

def create_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
    # print("Created Directory : ", dir)
    return dir
  
# Create and save the png file naming "myqr.png" 
QRSaveDirectory='QROutputs'
url.png(os.path.join(QRSaveDirectory,'QRCode101.png'), scale = 6) 
"""
