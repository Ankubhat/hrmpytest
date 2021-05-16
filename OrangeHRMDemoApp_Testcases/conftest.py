import pytest

from CorePackage.Utilities.Utils import Utils
from OrangeHRMDemoApp_Pages.LoginPage import LoginPage

#Fixture
@pytest.fixture(params=Utils.ReadLoginTestData())
def LoginDataProvider(request):
    return request.param

@pytest.fixture(scope="class")
def CreateLoginPageObj(request):
    loginpage=LoginPage("Chrome")
    request.cls.loginpage=loginpage

