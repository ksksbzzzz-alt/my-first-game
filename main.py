from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        self.display = TextInput(
            text="",
            readonly=True,
            font_size=40,
            halign="right",
            multiline=False,
            background_color=(0.1,0.1,0.1,1),
            foreground_color=(1,1,1,1)
        )

        layout.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=8)

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "C","0",".","+",
            "="
        ]

        for t in buttons:
            btn = Button(
                text=t,
                font_size=30,
                background_normal=""
            )

            if t == "C":
                btn.background_color = (1,0.2,0.2,1)
            elif t == "=":
                btn.background_color = (0.2,0.8,0.2,1)
            elif t in ["+","-","*","/"]:
                btn.background_color = (1,0.6,0,1)
            else:
                btn.background_color = (0.2,0.5,1,1)

            btn.bind(on_press=self.press)
            grid.add_widget(btn)

        layout.add_widget(grid)
        return layout

    def press(self, instance):
        t = instance.text

        if t == "C":
            self.display.text = ""

        elif t == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"

        else:
            self.display.text += t

Calculator().run()