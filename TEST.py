"COMMENT ONE SECTION OF CODE BEFORE OR AFTER LINE 40 TO USE DESIRED SCENARIO"
# MATLAB PYTHON  DATA COMMUNICATION
# USING SERVER
import socket
import time  # Import time module to record timestamps

# Define server details
HOST = '127.0.0.1'  # Localhost (same machine)
PORT = 65432        # Port to match MATLAB's server port

# Create a socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the MATLAB server
    
    test_string = "Hello from Python!"  # Test string to send

    # Record the start time
    start_time = time.time()

    # Send the string
    s.sendall(test_string.encode('utf-8'))
    print(f"Sent: {test_string}")

    # Wait for response from MATLAB
    data = s.recv(1024)

    # Record the end time
    end_time = time.time()

    print(f"Received: {data.decode('utf-8')}")

    # Calculate and display the delay
    delay_time = end_time - start_time
    print(f"Delay Time: {delay_time:.6f} seconds")
"""



"""
# USING SERIAL PORT
import serial
import time

# Configure serial port
ser = serial.Serial('COM2', 9600, timeout=1)  # Replace 'COM3' with your serial port
time.sleep(2)  # Allow time for the serial port to initialize

# Define the test message
test_message = "Hello from Python!"

# Record the start time
start_time = time.time()

# Send the test message
ser.write(test_message.encode('utf-8'))
print(f"Sent: {test_message}")

# Wait for the response from MATLAB
response = ser.readline().decode('utf-8').strip()
print(f"Received: {response}")

# Record the end time
end_time = time.time()

# Calculate and display the communication time
communication_time = end_time - start_time
print(f"Communication Time: {communication_time:.6f} seconds")

ser.close()
"""

"""
import serial
import time

# Configure serial port
ser = serial.Serial('COM1', 115200, timeout=1)  # Replace 'COM3' with your serial port
time.sleep(2)  # Allow the serial port to initialize

# Define the MATLAB command to send
command = "spy"

# Record the start time
start_time = time.time()

# Send the command to MATLAB
ser.write(command.encode('utf-8'))
print(f"Sent command: {command}")

# Wait for MATLAB to respond
response = ser.readline().decode('utf-8').strip()

# Record the end time
end_time = time.time()

# Calculate and display the communication time
communication_time = end_time - start_time
print(f"Received response: {response}")
print(f"Total time (Python to MATLAB execution and back): {communication_time:.6f} seconds")

ser.close()



