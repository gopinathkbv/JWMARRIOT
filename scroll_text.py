from kivy.app import App
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation


kv = """
<ScrollingText>:
    do_scroll:True,False
    Label: 
        text: 'FRENCH WINE BAR AT UNO'
        size_hint_x: None
        width: self.texture_size[0]


BoxLayout:
    orientation: 'vertical'
    Label: 
        text: 'JFW_MARRIOT_BANGLORE'
        bold:True
        size_hint_y: None
        height: 24
    ScrollingText:
"""


class ScrollingText(ScrollView):
    def on_kv_post(self, base_widget):
        scroll = Animation(scroll_x=1, duration=6) + Animation(scroll_x=0, duration=6)
        scroll.repeat = True
        scroll.start(self)



class ScrollingTextApp(App):
    def build(self):
        return Builder.load_string(kv)


ScrollingTextApp().run()
