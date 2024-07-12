import serial
import struct

# Initialize the serial connection
ser = serial.Serial('COM11', 115200)

while True:
    # Read the size of the incoming image
    size_data = ser.read(4)
    if len(size_data) < 4:
        continue  # If we didn't read enough bytes, skip this iteration
    size = struct.unpack('>I', size_data)[0]

    # Read the image data
    img_data = ser.read(size)
    if len(img_data) < size:
        continue  # If we didn't read enough bytes, skip this iteration

    # Save the image data to a file
    with open('received_image.jpg', 'wb') as f:
        f.write(img_data)

    print('Image received and saved')