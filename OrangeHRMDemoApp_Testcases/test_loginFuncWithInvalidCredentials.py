import time
import pytest

from OrangeHRMDemoApp_Testcases.BaseTestCase import BaseTestCase

@pytest.mark.usefixtures("CreateLoginPageObj")
class TestLoginFunctionalityWithInvalidCredentials(BaseTestCase):
    loginpage=None
    def testLoginWithInvalidCredentials(self,LoginDataProvider):
        logger = self.getLogger()
        logger.info("Login with UserName: " + LoginDataProvider["UserName"]+" and Password: "+ LoginDataProvider["Password"])
        TestLoginFunctionalityWithInvalidCredentials.loginpage.T.CreateObjectRepositoy("LoginPage")
        TestLoginFunctionalityWithInvalidCredentials.loginpage.DoLogin(LoginDataProvider["UserName"],LoginDataProvider["Password"])
        time.sleep(3)
        ActualErrorMessage=TestLoginFunctionalityWithInvalidCredentials.loginpage.GetLoginErrorMessage()
        if(not ActualErrorMessage):
            logger.info("Login Successfully")
        else:
            logger.info(ActualErrorMessage + " error message displayed on Login Page")
        assert ActualErrorMessage==LoginDataProvider["Error"], "Wrong Error message displayed on Login Page"
