from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

# Now import other Kivy modules
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen

class MainApp(MDApp):
    def build(self):
        screen = MDScreen()
        btn = MDRaisedButton(
            text='Hello, World!',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        screen.add_widget(btn)
        return screen

if __name__ == '__main__':
    MainApp().run()
