import os
import keyboard

class Program:
    def __init__(self):
        self.setup_keyboard()

    def setup_keyboard(self):
        print("Naciśnij 'q', aby zakończyć program.")
        print("Naciśnij 'a', aby wykonać Akcję A.")
        print("Naciśnij 'b', aby wykonać Akcję B.")
        print("Naciśnij 'z+x', aby wykonać Akcję C.")
        print("Oczekiwanie na zdarzenia klawiatury...")

        keyboard.add_hotkey('z+x', lambda: self.perform_action_c())
        keyboard.on_press(self.on_key_event)

    def on_key_event(self, event):
        if event.name == 'q':
            print("Wykryto klawisz: 'q'. Program zakończy działanie.")
            return False
        elif event.name == 'a':
            print("Wykryto klawisz: 'a'. Akcja A wykonana.")
        elif event.name == 'b':
            print("Wykryto klawisz: 'b'. Akcja B wykonana.")
        return True

    def perform_action_c(self):
        print("Wykryto sekwencję klawiszy: 'z+x'. Akcja C wykonana.")

    def run(self):
        desktop_path = os.path.join(os.getenv('USERPROFILE'), 'Desktop')
        os.system(r'start cmd /K python "{}"'.format(os.path.join(desktop_path, 'main_program.py')))
        keyboard.wait('q')

if __name__ == "__main__":
    program = Program()
    program.run()
