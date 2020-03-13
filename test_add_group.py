# -*- coding: utf-8 -*-

import pytest
from group import Group
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy())
    return fixture



def test_add_group(app):
  app.open_home_page()
  app.login(username="admin", password="secret")
  app.open_groups_page()
  app.create_group(Group(name="abc", header="abc", footer="abc"))
  app.return_to_group_page()
  app.logout()

def test_add_empty_group(app):
  app.open_home_page()
  app.login(username="admin", password="secret")
  app.open_groups_page()
  app.create_group(Group(name="", header="", footer=""))

  app.return_to_group_page()
  app.logout()

def test_add_contact(app):
  app.open_home_page()
  app.login(username="admin", password="secret")
  app.open_new_contact_page()
  app.add_new_contact(Contact(firstname="Bob", lastname="Marley"))
  app.return_to_homepage()
  app.logout()




def tearDown(app):
    app.destroy()


