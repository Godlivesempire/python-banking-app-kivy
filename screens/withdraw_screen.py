from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import  BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from data.accounts import withdraw
import data.session as session

class WithdrawScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        self.amount_input = TextInput(hint_text="Enter amount to withdraw", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.amount_input)

        self.message = Label(text="", font_size=16)
        layout.add_widget(self.message)

        withdraw_btn = Button(text="withdraw")
        withdraw_btn.bind(on_press=self.make_withdraw)
        layout.add_widget(withdraw_btn)

        back_btn = Button(text="Back")
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def make_withdraw(self, instance):
        if not self.amount_input.text.isdigit():
            self.message.text =  "Enter a valid amount"
            return
        
       
        amount = int(self.amount_input.text)

        success, msg = withdraw(session.current_user, amount)
        self.message.text = msg

        self.amount_input.text = "" 


    def go_back(self, instance):
        self.manager.current = "dashboard"