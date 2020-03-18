

class Contact:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname



    def open_new_contact_page(self, wd):
          wd.find_element_by_link_text("add new").click()

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