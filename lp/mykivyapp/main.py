from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password1_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.password2_input = TextInput(hint_text='Repeat Password', multiline=False, password=True)
        self.register_button = Button(text='Register', on_press=self.register)
        self.layout.add_widget(Label(text='Register'))
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.password1_input)
        self.layout.add_widget(self.password2_input)
        self.layout.add_widget(self.register_button)
        self.add_widget(self.layout)

    def register(self, instance):
        # Replace this with your actual registration logic
        # For example, you can make a request to your Django API
        url = 'http://127.0.0.1:8000/api_register/'  # Adjust the URL accordingly
        data = {
            'username': self.username_input.text,
            'password1': self.password1_input.text,
            'password2': self.password2_input.text
        }
        headers = {'Content-type': 'application/x-www-form-urlencoded'}

        def on_success(req, result):
            # Handle the successful response
            print(result)
            # Optionally, you can switch to the login screen after registration
            self.manager.current = 'login'

        def on_failure(req, result):
            # Handle the failure response
            print(result)

        UrlRequest(url, on_success=on_success, on_failure=on_failure, req_headers=headers, req_body=data, method='POST')

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.login_button = Button(text='Login', on_press=self.login)
        self.layout.add_widget(Label(text='Login'))
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.login_button)
        self.add_widget(self.layout)

    def login(self, instance):
        # Replace this with your actual login logic
        # For example, you can make a request to your Django API
        url = 'http://127.0.0.1:8000/api_login/'  # Adjust the URL accordingly
        data = {
            'username': self.username_input.text,
            'password': self.password_input.text
        }
        headers = {'Content-type': 'application/x-www-form-urlencoded'}

        def on_success(req, result):
            # Handle the successful response
            print(result)
            self.manager.current = 'welcome'  # Switch to the WelcomeScreen

        def on_failure(req, result):
            # Handle the failure response
            print(result)

        UrlRequest(url, on_success=on_success, on_failure=on_failure, req_headers=headers, req_body=data, method='POST')

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='Welcome!'))
        self.add_widget(self.layout)

class MyKivyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.welcome_screen = WelcomeScreen(name='welcome')
        self.register_screen = RegisterScreen(name='register')
        self.screen_manager.add_widget(self.register_screen)
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.welcome_screen)
        return self.screen_manager

if __name__ == '__main__':
    MyKivyApp().run()
