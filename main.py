from classes import Project
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

countries = ("Czechia", "Slovakia")

class MainScreen(Screen):
    pass

class ProjectScreen(Screen):
    alt_checkbox = ObjectProperty()
    alt_slider = ObjectProperty()
    country_spinner = ObjectProperty()

    def load_countries(self):
        self.country_spinner.values = countries
        self.alt_slider.disabled = True

    def activate_alt_slider(self):
        if self.alt_checkbox.active is True:
            self.alt_slider.disabled = False
        else:
            self.alt_slider.disabled = True

    def printtxt(self, text):
        projects = Project(text)
        print projects.name
        if self.alt_checkbox.active is True:
            self.alt_checkbox.active = False
            print self.alt_slider.value

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        # country_spinner.values("Czechia", "Slovakia")
        return presentation

ConfiguratorApp = MainApp()
ConfiguratorApp.run()
