from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from data.accounts import authenticate
from data.session import current_user
import data.session as session



class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        layout = BoxLayout(orientation="vertical", padding=40, spacing=20)
        
        logo = Image(source=r"C:\Users\HP\GodlivesEmpire\BankApp\assets/logo.png", size_hint=(1, None), height=200, allow_stretch=True, keep_ratio=False)
        layout.add_widget(logo)

        title = Label(text="GodlivesEmpire Bank", font_size=28, bold=True)
        layout.add_widget(title)

        self.username = TextInput(hint_text="Username", multiline=False, size_hint_y=None, height=50)
        self.pin = TextInput(hint_text="PIN", password=True, multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.username)
        layout.add_widget(self.pin)

       

        

        self.message = Label(text="", font_size=16, color=(1,0,0,1))
        layout.add_widget(self.message)

        login_btn = Button(text="Login", size_hint=(1, 0.15), background_color=(0.1, 0.5, 0.9, 1))
        login_btn.bind(on_press=self.login)
        layout.add_widget(login_btn)

        signup_btn = Button(
            text="Create Account",
            size_hint=(1, 0.15)
        )
        signup_btn.bind(on_press=self.go_signup)
        layout.add_widget(signup_btn)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username.text.strip()
        pin = self.pin.text.strip()

        if authenticate(username, pin):
            session.current_user = self.username.text
            self.manager.current = "dashboard"
            
        else:
            self.message.text = "Invalid login"

    def go_signup(self, instance):
        self.manager.current = "signup"
  
