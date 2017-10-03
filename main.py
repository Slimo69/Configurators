from classes import Project
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import sqlite3

countries = ("Czechia", "Slovakia")
projects = []

class MainScreen(Screen):
    pass

class ProjectScreen(Screen):
    alt_checkbox = ObjectProperty()
    alt_slider = ObjectProperty()
    country_spinner = ObjectProperty()
    project_name = ObjectProperty()
    project_currency = ObjectProperty()

    def load_countries(self):
        self.country_spinner.values = countries
        self.alt_slider.disabled = True

    def activate_alt_slider(self):
        if self.alt_checkbox.active is True:
            self.alt_slider.disabled = False
        else:
            self.alt_slider.disabled = True

    def create_project(self):
        if self.alt_checkbox.active is True:
            projects.append(Project(1,self.project_name.text,self.country_spinner.text, self.alt_slider.value,self.project_currency.text))
        else:
            projects.append(Project(1, self.project_name.text, self.country_spinner.text, 1000, self.project_currency.text))
        print (projects[-1])

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

ConfiguratorApp = MainApp()
ConfiguratorApp.run()
