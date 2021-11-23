from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

from pathlib import Path

kv = """
BoxLayout:
    Label:
        id: label
        text: 'Connect USB Device'
"""


class USBDriveTestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_file_read = False

    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        self.detect_usb()
        Clock.schedule_interval(self.detect_usb, 4) # check for the usb drive every 4 seconds

    def detect_usb(self, *args):
        # for p in Path('/Volumes').iterdir():  # you will need to change the path to match the raspberry pi
        drive_names = [p.name for p in Path('/Volumes').iterdir()]
        if 'RANDOMFILES' in drive_names:  # the name of the USB stick is RANDOMFILES, change to match your usb drive name
            print('drive detected')
            if not self.text_file_read:  # to prevent repeatidly reading the file
                with open('/Volumes/RANDOMFILES/text/note.txt') as f:
                    self.root.ids.label.text = f.read()
                    print('File Read')
                    self.text_file_read = True
        else:
            self.root.ids.label.text = 'Connect USB Device'
            self.text_file_read = False
            print('Drive missing')

USBDriveTestApp().run()
