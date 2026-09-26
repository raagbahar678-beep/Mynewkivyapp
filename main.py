from kivy.app import App
from kivy.uix.label import Label


class MyKivyApp(App):
    def build(self):
        return Label(
            text="Hello! My Kivy app is working.",
            font_size="24sp",
            halign="center",
            valign="middle",
        )


if __name__ == "__main__":
    MyKivyApp().run()
