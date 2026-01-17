from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from data.accounts import create_account
import data.session as session
from kivy.clock import Clock

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        self.username_input = TextInput(hint_text="Choose a username", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.username_input)

        self.pin_input = TextInput(hint_text="Choose a PIN", multiline=False, password=True, size_hint_y=None, height=50)
        layout.add_widget(self.pin_input)

        self.message = Label(text="", font_size=16)
        layout.add_widget(self.message)

        signup_btn = Button(text="Create Account")
        signup_btn.bind(on_press=self.signup)
        layout.add_widget(signup_btn)

        back_btn = Button(text="Back")
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def signup(self, instance):
       username = self.username_input.text.strip()
       pin = self.pin_input.text.strip()

       if not username or not pin:
           self.message.text = "All field are required"
           return
       
       if not pin.isdigit():
           self.message.text = "PIN must be numbers only"
           return
       
       success, account_number, created_pin = create_account(username, pin)
       self.message.text = f"Account created!\nAccount No: {account_number}"

       if not success:
           self.message.text = "Username already exists"
           return
       
       
       self.manager.text = (
           "Account Created Successfully\n\n"
           f"Account Number: {account_number}\n"
           f"PIN: {created_pin}\n\n"
           "Save these details. PIN will not be shown again."
       )

       session.current_user = username
       Clock.schedule_once(lambda dt: setattr(self.manager, "current", "dashboard"), 3)
    
           

    def go_back(self, instance):
        self.manager.current = "login"

