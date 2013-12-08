import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write('\xFF')
print ser.read()