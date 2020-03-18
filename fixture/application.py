from selenium import webdriver
from fixture.session import SessionHelper



class Application:

      def __init__(self):
        self.wd = webdriver.Firefox(executable_path="/Users/olgakim/PycharmProjects/python_projects/geckodriver")
        self.wd.implicitly_wait(30)
        self.session = SessionHelper

      def open_home_page(self):
          wd = self.wd
          wd.get("http://127.0.0.1/addressbook/index.php")

      def destroy(self):
         self.wd.quit()