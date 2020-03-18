# -*- coding: utf-8 -*-

import pytest
from model.group import GroupHelper
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_group(app):
    app.login(username="admin", password="secret")
    app.group.create(GroupHelper(name="abc", header="abc", footer="abc"))
    app.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(GroupHelper(name="", header="", footer=""))
    app.session.logout()



