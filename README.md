# Python Network Scanner

A beginner-friendly Python project that performs a basic TCP connect scan on a target host and reports open ports within a selected range.

## Purpose
This project was built to understand how socket-based network communication works in Python and how open ports can be detected using TCP connection attempts.

## Features
- Scans a selected range of ports.
- Uses Python's `socket` module.
- Detects whether a TCP connection succeeds.
- Uses timeout handling for faster scanning.
- Handles user interruption gracefully.

## How It Works
The script creates a TCP socket for each port in the chosen range and uses `connect_ex()` to attempt a connection to the target host.
- A return value of `0` usually means the port is open.
- A non-zero result usually means the port is closed or filtered.

## Example Use
This project is intended for local-lab testing, such as scanning `127.0.0.1` or systems where I have permission to test.

## Ethical Use
This project is for educational purposes and authorized testing only. It should not be used on public or third-party systems without permission.

## Limitations
- Performs a basic TCP connect scan only.
- Does not perform service detection.
- Does not distinguish perfectly between closed and filtered ports.
- Scan speed depends on timeout settings and network conditions.

## Concepts Practiced
- Python socket programming
- TCP connection attempts
- Port scanning basics
- Timeout handling
- Exception handling
- Local network testing

## Future Improvements
- User input for target IP and port range
- Banner grabbing
- Better result formatting
- Multi-threaded scanning
- Exporting scan results

## Author
Jay Prakash
GitHub: jayprakash-tech
