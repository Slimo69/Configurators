from classes import Project
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    pass

class ProjectScreen(Screen):
    def printtxt(self, text):
        projects = Project(text)
        print projects.name

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

ConfiguratorApp = MainApp()
ConfiguratorApp.run()
