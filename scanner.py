import socket
import sys
from datetime import datetime

target = "127.0.0.1"
start_port = 1
end_port = 100

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")

        s.close()

except KeyboardInterrupt:
    print("\nScan stopped by user.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to the target.")
    sys.exit()

print("\nScanning complete.")
