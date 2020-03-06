#any pytest file should start with test_ or end with _test
#pytest method names should start with test
#any code should be wrapped in method only
#-k stands for method names execution
#-s logs in out put
#-v stands for more info metadata
#you can specific file with py.test <filename>
#you can mark(tag) test @pytest.mark.smoke and run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases -conftest file to generalized
# fixtures and make it available to all test cases
#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only , it will run once before class is initiates at th end


import pytest

@pytest.mark.smoke
def test_firstProgramme(setup):
    print("Hello")

@pytest.mark.xfail
def test_secondCreditCard():
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

