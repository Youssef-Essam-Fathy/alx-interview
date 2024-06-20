#!/usr/bin/python3
import sys
import signal

# Dictionary to hold the count of status codes
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

# Variable to keep track of total file size
total_file_size = 0

# Variable to keep track of the number of lines processed
line_count = 0

def print_statistics():
    """Print the statistics of the log parsing."""
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_code_counts[status_code]))

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract the file size and status code from the line
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update the total file size
            total_file_size += file_size

            # Update the status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            # Increment the line count
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics()

        except (ValueError, IndexError):
            # Skip lines with improper format
            continue

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_statistics()
    sys.exit(0)

# Final print of statistics after all lines are processed
print_statistics()
