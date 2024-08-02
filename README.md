# Python Keylogger

This project demonstrates a simple keylogger written in Python. The keylogger captures keystrokes and stores them in a text file. It is intended for educational purposes and to illustrate how keylogging works.

> **Warning:** Keyloggers can be used maliciously and have significant ethical and legal implications. Only use this tool in a controlled environment where you have explicit permission.

## Features

- **Capture Keystrokes**: Logs every key pressed on the keyboard.
- **Handle Special Keys**: Recognizes special keys like space and enter.
- **Store Keystrokes**: Saves the captured keystrokes to a text file (`keylog.txt`).

## How It Works

1. **Logging Keystrokes**: The script listens for keypress events and writes the captured keys to a log file.
2. **Special Key Handling**: It differentiates between normal keys and special keys (e.g., space, enter, escape).
3. **Stopping the Logger**: The keylogger can be stopped by pressing the `Esc` key.

## Prerequisites

Before running the keylogger, you need to install the `pynput` library. This library allows the program to monitor keyboard events.

Install the library using pip:

```bash
pip install pynput
