from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from data.accounts import transfer
import data.session as session
from kivy.clock import Clock

class TransferScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        self.account_input = TextInput(hint_text="Enter recipient account", multiline=False, size_hint=(1, 0.1))
        layout.add_widget(self.account_input)

        self.amount_input = TextInput(hint_text="Enter amount to transfer", multiline=False, size_hint=(1, 0.1))
        layout.add_widget(self.amount_input)

        self.message = Label(text="", font_size=16)
        layout.add_widget(self.message)

        transfer_btn = Button(text="Transfer", size_hint=(1, 0.15))
        transfer_btn.bind(on_press=self.make_transfer)
        layout.add_widget(transfer_btn)

        back_btn = Button(text="Back", size_hint=(1, 0.15))
        back_btn.bind(on_press=self.go_dashboad)
        layout.add_widget(back_btn)

        self.add_widget(layout)
        
    def make_transfer(self, instance):
        receiver = self.account_input.text.strip()
        amount_text = self.amount_input.text.strip()

        if not receiver or not amount_text.isdigit():
            self.message.text = "Enter valid recipient and amount"
            return
        
        amount = int(amount_text)

        success, msg = transfer(
            session.current_user,
            receiver,
            amount
        )

        self.message.text = msg

        if success:
            self.account_input.text = ""
            self.amount_input.text = ""
           



    def go_dashboad(self, dt):
        self.manager.current = "dashboard"

    