import pyautogui
import time

# Function to read from a text file
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Function to simulate typing with a 3-second delay before starting and near-instant typing speed
def type_text(content, start_delay=3, typing_speed=0.0001):
    time.sleep(start_delay)  # 3-second delay before starting to type
    pyautogui.write(content, interval=typing_speed)  # Typing speed with a tiny interval to avoid system overload

# Main logic
#######################
file_path = 'copy.txt'  # Update this to your text file location
#######################
content = read_file(file_path)
type_text(content, start_delay=3, typing_speed=0.0001)  # Start delay of 3 seconds, near-instant typing
