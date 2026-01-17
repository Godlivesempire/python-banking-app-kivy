import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.dashboard_screen import DashboardScreen
from screens.deposit_screen import DepositScreen
from screens.withdraw_screen import WithdrawScreen
from screens.transfer_screen import TransferScreen
from screens.signup_screen import SignupScreen

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class GodlivesEmpireBank(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignupScreen(name="signup"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(DepositScreen(name="deposit"))
        sm.add_widget(WithdrawScreen(name="withdraw"))
        sm.add_widget(TransferScreen(name="transfer"))
        

        
        return sm
    
if __name__ == "__main__":
    GodlivesEmpireBank().run()