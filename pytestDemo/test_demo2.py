#any pytest file should start with test_ or end with _test
#pytest method names should start with test
#any code should be wrapped in method only
import pytest


@pytest.mark.smoke
@pytest.mark.skip

def test_firstProgramme():
    msg= "Hello"  #operations
    assert msg=="Hi", "Test Failed because string do not match"


def test_secondCreditCard():
    a=4
    b=6
    assert a+2==6, "Addition do not match"

