import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

kivy.require("2.1.0")

Builder.load_file('janela.kv')


class AnchorLayoutA(Widget):
    pass


class JanelaApp(App):

    def build(self):
        Window.size = (350, 580)

        SL = StackLayout(orientation='tb-lr')

        ALT = AnchorLayout()

        btn1 = Button(text="2019",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('2019 selecionado'))
        btn2 = Button(text="2020",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('2020 selecionado'))
        btn3 = Button(text="2021",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('2021 selecionado'))
        btn4 = Button(text="2022",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('2022 selecionado'))
        btn5 = Button(text="B5",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('None'))
        btn6 = Button(text="B6",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('None'))
        btn7 = Button(text="B7",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('None'))
        btn8 = Button(text="B8",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('None'))
        btn9 = Button(text="B9",
                      font_size=20,
                      size_hint=(.2, .1),
                      on_press=lambda x: print('None'))
        btn10 = Button(text="B10",
                       font_size=20,
                       size_hint=(.2, .1),
                       on_press=lambda x: print('None'))

        SL.add_widget(btn1)
        SL.add_widget(btn2)
        SL.add_widget(btn3)
        SL.add_widget(btn4)
        SL.add_widget(btn5)
        SL.add_widget(btn6)
        SL.add_widget(btn7)
        SL.add_widget(btn8)
        SL.add_widget(btn9)
        SL.add_widget(btn10)
        SL.add_widget(ALT)

        return SL


if __name__ == '__main__':
    JanelaApp().run()
