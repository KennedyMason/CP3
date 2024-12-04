from kivy.app import App
from kivy.lang import Builder


class HelloWorldApp(App):

    def build(self):
        return Builder.load_file('main.kv')
    

HelloWorldApp().run()


#Labels make text appear on the screen.

#on_press tells the button what to do when pressed.

#hint_text create a prompt in a text input

#ids are used for something that doesn't have any other value

#FloatLayout: no default locations
#   Button:
#       text: text displayed on button
#       size_hint
#       pos_hint


#ScreenManager:
#   name: 'Home_screen'
