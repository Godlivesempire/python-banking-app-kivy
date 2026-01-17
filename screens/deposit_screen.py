from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from data.accounts import deposit
import data.session as session

class DepositScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        self.amount_input = TextInput(hint_text="Enter amount to deposit", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.amount_input)

        self.message = Label(text="", font_size=16)
        layout.add_widget(self.message)

        deposit_btn = Button(text="Deposit", size_hint=(1, 0.15))
        deposit_btn.bind(on_press=self.make_deposit)
        layout.add_widget(deposit_btn)

        back_btn = Button(text="Back", size_hint=(1, 0.15))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def make_deposit(self, instance):
        if not self.amount_input.text.isdigit():
            self.message.text = "Enter a valid amount"
            return
        amount = int(self.amount_input.text)
        deposit(session.current_user, amount)

        self.message.text = f"Deposit ${amount}"
        self.amount_input.text = ""


       

        
    def go_back(self, instance):
        self.manager.current ="dashboard"




