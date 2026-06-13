import socket
import sys
from datetime import datetime

# Define the target (127.0.0.1 scans your own computer safely)
target = "127.0.0.1" 

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # FIXED: Added range(1, 101) to scan ports 1 through 100
    for port in range(1, 101):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Fast response timing
        
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
