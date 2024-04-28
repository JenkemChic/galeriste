from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.image import Image


class SharpCornerButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "Roboto"  # KivyMD uses Roboto by default
        self.font_size = 16
        self.bold = True
        self.color = (0, 0, 0, 1)  # Text color

        # Invisible rectangle for button area
        with self.canvas.before:
            Color(0, 0, 0, 0)  # Transparent color
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Custom drawing for the border
        with self.canvas.after:
            Color(0, 0, 0, 1)  # Set the border color to black
            self.border_top = Line(points=[], width=2)
            self.border_right = Line(points=[], width=2)
            self.border_bottom = Line(points=[], width=2)
            self.border_left = Line(points=[], width=2)

        # Update the border lines and rectangle on size and position changes
        self.bind(size=self.update_border, pos=self.update_border)

    def update_border(self, *args):
        # Update the points for each border line
        self.border_top.points = [
            self.x, self.top,  # Top-left corner
            self.right, self.top  # Top-right corner
        ]
        self.border_right.points = [
            self.right, self.top,  # Top-right corner
            self.right, self.y  # Bottom-right corner
        ]
        self.border_bottom.points = [
            self.right, self.y,  # Bottom-right corner
            self.x, self.y  # Bottom-left corner
        ]
        self.border_left.points = [
            self.x, self.y,  # Bottom-left corner
            self.x, self.top  # Top-left corner
        ]

        # Update the position and size of the invisible rectangle
        self.rect.pos = self.pos
        self.rect.size = self.size


class MainApp(MDApp):
    def build(self):
        screen = MDScreen()

        # Logo image
        logo = Image(
            source='logo.png',  # Update the path to your logo image
            size_hint=(None, None),
            size=(300, 300),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        screen.add_widget(logo)

        layout = MDBoxLayout(orientation='vertical', padding=65, spacing=15)

        # Button with sharp corners and thick border
        btn_artist = SharpCornerButton(
            text='ARTIST',  # Text in uppercase
            size_hint=(None, None),
            size=(200, 50),  # Adjust size as needed
            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # Adjust position to center
        )
        layout.add_widget(btn_artist)

        # Second button with sharp corners and thick border
        btn_patron = SharpCornerButton(
            text='PATRON',  # Text in uppercase
            size_hint=(None, None),
            size=(200, 50),  # Adjust size as needed
            pos_hint={'center_x': 0.5, 'center_y': 0.4}  # Adjust position to center below the first button
        )
        layout.add_widget(btn_patron)

        screen.add_widget(layout)
        return screen


if __name__ == '__main__':
    MainApp().run()
