import socket
import sys
from datetime import datetime

# Define the target (scanme.nmap.org scans your own computer safely)
target = "scanme.nmap.org" 

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # Scan standard networking and server ports (1 to 1024)
    for port in range(1, 1025):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3) # 300 milliseconds timeout for fast scanning
        
        # connect_ex returns 0 if the connection was successful (port is open)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to the server.")
    sys.exit()
print("Scanning complete!)
