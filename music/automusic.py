import json
import time
import keyboard
import pydirectinput


class MusicHandler:
    exitProgram = False
    pauseProgram = False
    data = None

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_json_file(file_path)

        notes = self.data[0]['songNotes']
        bpm = self.data[0]['bpm']
        self.start_key, self.stop_key = self.get_hotkeys()

        keyboard.add_hotkey(self.stop_key, lambda: self.pause())
        while not self.exitProgram:
            keyboard.wait(self.start_key)
            time.sleep(2)
            self.pauseProgram = False
            self.simulate_keyboard_presses(notes, bpm)
    

    def get_hotkeys(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
            return config["music"]["start_key"], config["music"]["stop_key"]

    def read_json_file(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    
    def quit(self):
        self.exitProgram=True
    
    def pause(self):
        self.pauseProgram = True
    
    def simulate_keyboard_presses(self, notes, bpm):

        # Define a simple mapping of numbers to keyboard keys.
        with open('config.json', 'r') as file:
            config = json.load(file)
        key_mapping = config["music"]["key_mapping"]

        # Calculate interval in seconds between beats
        beat_interval = 60 / bpm  # Seconds per beat

        # Keep track of the last played time to manage relative delays
        last_time_ms = 0

        for note in notes:
            if self.pauseProgram: break
            current_time_ms = note['time']
            # Calculate the delay needed from the last note to this one
            if last_time_ms != 0:
                time_delay = (current_time_ms - last_time_ms) / 1000.0
            else:
                time_delay = current_time_ms / 1000.0

            # Wait for the next note to be simulated
            time.sleep(time_delay * beat_interval)

            # Simulate the key press
            key_to_press = key_mapping.get(note['key'][4:])
            pydirectinput.PAUSE=0.000001
            if key_to_press:
                pydirectinput.press(key_to_press)
                print(f"Pressed {key_to_press} for note {note['key']} at time {current_time_ms}")

            # Update the last_time_ms to the current note's time
            last_time_ms = current_time_ms

def mstart(file):
    ms = MusicHandler(file)