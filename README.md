# Auto-Typer


This Python script automates the typing of content from a text file, simulating user input to bypass copy-pasting restrictions. It's particularly useful in environments where users are not allowed to copy-paste text, such as online exams, form filling, or restricted platforms.

## Features
- Reads text from a specified file.
- Simulates typing with customizable speed and delay.
- Capable of handling large blocks of text with minimal delay.
- Simple and easy-to-use automation tool.

## Use Case
The script is designed to address situations where copy-pasting is not allowed, but typing manually would be time-consuming. This can be applied to:
- **Examination platforms** where students or users are restricted from pasting copied content.
- **Form filling automation** for repetitive tasks.
- **Typing challenges** or competitions where every keystroke matters.
  
## How It Works
The script utilizes the `pyautogui` library to simulate keystrokes. The speed and delay between characters can be adjusted to mimic real human typing, making it nearly indistinguishable from actual manual input.

## Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/RituRajKumarWork/Auto-Typer
    ```
   
2. **Install required dependencies**:
    ```bash
    pip install pyautogui
    ```

3. **Run the script**:
    Update the `copy.txt` file with the content you want to type and then run:
    ```bash
    python main.py
    ```

## Configuration
You can adjust the typing speed and the delay before typing starts by modifying the following parameters in the script:

- `start_delay`: Delay (in 3 seconds) before typing begins.
- `typing_speed`: Interval (in 0 seconds) between each keystroke. Set it to `0` for instant typing.

```python
type_text(content, start_delay=3, typing_speed=0.0001) 
