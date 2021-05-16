from CorePackage.WebTest import WebTest

class BasePage:

    def __init__(self):
        self.T=WebTest()

    def GetPageURL(self):
        return self.T.GetCurrentURL()