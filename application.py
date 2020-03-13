from selenium import webdriver


class Application:
      def __init__(self):
        self.wd = webdriver.Firefox(executable_path="/Users/olgakim/PycharmProjects/python_projects/geckodriver")
        self.wd.implicitly_wait(30)

      def open_home_page(self):
          wd = self.wd
          wd.get("http://127.0.0.1/addressbook/index.php")


      def add_new_contact(self, wd, contact):
          wd.find_element_by_name("firstname").click()
          wd.find_element_by_name("firstname").clear()
          wd.find_element_by_name("firstname").send_keys(contact.firstname)
          wd.find_element_by_name("lastname").click()
          wd.find_element_by_name("lastname").clear()
          wd.find_element_by_name("lastname").send_keys(contact.lastname)
          wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

      def return_to_homepage(self, wd):
          wd.find_element_by_link_text("home").click()

      def open_new_contact_page(self, wd):
          wd.find_element_by_link_text("add new").click()

      def logout(self, wd):
          wd.find_element_by_link_text("Logout").click()

      def return_to_group_page(self, wd):
          wd.find_element_by_link_text("group page").click()

      def create_group(self, wd, group):
          wd.find_element_by_xpath("(//input[@name='new'])[2]").click()
          # fill group form
          wd.find_element_by_name("group_name").click()
          wd.find_element_by_name("group_name").clear()
          wd.find_element_by_name("group_name").send_keys(group.name)
          wd.find_element_by_name("group_header").click()
          wd.find_element_by_name("group_header").clear()
          wd.find_element_by_name("group_header").send_keys(group.header)
          wd.find_element_by_name("group_footer").click()
          wd.find_element_by_name("group_footer").clear()
          wd.find_element_by_name("group_footer").send_keys(group.footer)
          # submit group creation
          wd.find_element_by_name("submit").click()

      def open_groups_page(self, wd):
          wd.find_element_by_link_text("groups").click()

      def login(self, wd, username, password):
          wd.find_element_by_name("user").clear()
          wd.find_element_by_name("user").send_keys(username)
          wd.find_element_by_name("pass").click()
          wd.find_element_by_name("pass").clear()
          wd.find_element_by_name("pass").send_keys(password)
          wd.find_element_by_xpath("//input[@value='Login']").click()



      def destroy(self):
         self.wd.quit()