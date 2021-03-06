import sqlite3 as lite

import pycountry
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

try:
    conn = lite.connect('confirgurators.sqlite')
    cur = conn.cursor()
except:
    print ("DB connection failed")

countries = []

for i in range(0,len(pycountry.countries)):
    ctry = list(pycountry.countries)[i]
    countries.append(ctry.name)

class MainScreen(Screen):
    scope_button = ObjectProperty(None)
    mv_swg_button = ObjectProperty(None)


class ProjectScreen(Screen):
    project_id = ObjectProperty()
    alt_checkbox = ObjectProperty()
    alt_slider = ObjectProperty()
    country_spinner = ObjectProperty()
    project_name = ObjectProperty()
    project_currency = ObjectProperty()

    def last_id(self):
        l_id = cur.execute('SELECT max(id) FROM projects')
        l_id = l_id.fetchone()[0] +1
        self.project_id.text = str(l_id)

    def load_countries(self):
        self.country_spinner.values = countries
        self.alt_slider.disabled = True

    def activate_alt_slider(self):
        if self.alt_checkbox.active is True:
            self.alt_slider.disabled = False
        else:
            self.alt_slider.disabled = True

    def create_project(self, root_manager):
        if str(self.country_spinner.text) == "Country":
            popup = Popup(title='Warning', content=Label(text='Please select a country!'))
            popup.open()
        else:
            if self.alt_checkbox.active is True:
                cur.execute("INSERT INTO projects (project_name, country, altitude, currency) VALUES (?, ?, ?, ?)",
                            (self.project_name.text, self.country_spinner.text, self.alt_slider.value,
                            self.project_currency.text))
                conn.commit()
                root_manager.main_scrn.scope_button.disabled = False
            else:
                cur.execute("INSERT INTO projects (project_name, country, altitude, currency) VALUES (?, ?, ?, ?)",
                            (self.project_name.text, self.country_spinner.text, 1000,self.project_currency.text))
                conn.commit()
                root_manager.main_scrn.scope_button.disabled = False

class ScopeScreen(Screen):
    mv_switchgear_cb = ObjectProperty(None)
    def create_products(self,root_manager):
        root_manager.main_scrn.mv_swg_button.disabled = False

class SwitchgearScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    main_scrn = ObjectProperty(None)

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

ConfiguratorApp = MainApp()
ConfiguratorApp.run()
conn.close()