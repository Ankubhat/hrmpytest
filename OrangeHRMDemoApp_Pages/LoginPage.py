from CorePackage.Utilities.Utils import Utils
from OrangeHRMDemoApp_Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, BrowserName):
        super().__init__()
        Utils.InitialiseEnvVars()
        self.T.StartTest(BrowserName)
        self.T.CreateObjectRepositoy("LoginPage")

    def DoLogin(self, UserName, Passowrd):
        self.T.EnterText(self.T.ObjectRepo["UserNameField"], UserName)
        self.T.EnterText(self.T.ObjectRepo["PasswordField"], Passowrd)
        self.T.ClickElement(self.T.ObjectRepo["SignInBtn"])

    def GetLoginErrorMessage(self):
        errorMessage = self.T.FindAndReturnElement("BY_ID", "spanMessage")
        return self.T.GetElementText(errorMessage)

    def tearDown(self):
        self.T.tearDown()