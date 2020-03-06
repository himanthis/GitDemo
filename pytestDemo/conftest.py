import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data is been created")
    return ["Himanthi", "Siriwardane","Female"]


@pytest.fixture(params=[("Chrome","Himanthi", "Siriwardane","Female"),("Firefox", "Siriwardane"),("IE","Female")])
def crossBrowser(request):
    return request.param
