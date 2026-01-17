import os
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from data.accounts import get_balance
import data.session as session


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dashboard_img_path = os.path.join(BASE_DIR, "assets", "dashboard.png")
        

        print("DASHBOARD IMAGE PATH:", dashboard_img_path)
        print("FILE EXISTS:", os.path.exists(dashboard_img_path))

        image = Image(
            source=dashboard_img_path,
            size_hint=(1, 0.3),
            
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(image)

        self.welcome = Label(text="", font_size=24)
        self.balance = Label(text="", font_size=20)

        layout.add_widget(self.welcome)
        layout.add_widget(self.balance)

        deposit_btn = Button(text="Deposit", size_hint=(1, 0.15))
        withdraw_btn = Button(text="Withdraw", size_hint=(1, 0.15))
        transfer_btn = Button(text="Transfer", size_hint=(1, 0.15))
        logout_btn = Button(text="Logout", size_hint=(1, 0.15))

        deposit_btn.bind(on_press=self.go_deposit)
        withdraw_btn.bind(on_press=self.go_withdraw)
        transfer_btn.bind(on_press=self.go_transfer)
        logout_btn.bind(on_press=self.logout)


        layout.add_widget(deposit_btn)
        layout.add_widget(withdraw_btn)
        layout.add_widget(transfer_btn)
        layout.add_widget(logout_btn)

        self.add_widget(layout)

    def on_enter(self):
        self.welcome.text = f"Welcome, {session.current_user}"
        
        self.balance.text = f"Account Balance: ${get_balance (session.current_user)}" 


    def go_deposit(self, instance):
        self.manager.current = "deposit"

    def go_withdraw(self, instance):
        self.manager.current = "withdraw"

    def go_transfer(self, instance):
        self.manager.current = "transfer"

    def logout(self, instance):
        session.current_user = None
        self.manager.current = "login"

    

       
       
    