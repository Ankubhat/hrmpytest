import csv

from selenium.webdriver.common.by import By

from CorePackage.Switcher import BrowserDriverSwitcher
from CorePackage.Utilities.Utils import Utils

class WebTest:
    Driver=None
    def __init__(self):
        self.ObjectRepo={}

    def StartTest(self,BrowserName):
        self.__OpenBrowser(BrowserName)
        self.OpenURL()

    def __OpenBrowser(self,BrowserName):
        Func=BrowserDriverSwitcher.get(BrowserName)
        Func()
    def OpenURL(self):
        WebTest.Driver.get(Utils.EnvVars.get("ApplicationURL"))

    def CreateObjectRepositoy(self,FileName):
        FilePath= Utils.EnvVars.get("ObjectRepositoryPath")+"\\"+FileName+".csv"
        with open(FilePath) as ObjectRepo:
            csv_reader = csv.reader(ObjectRepo, delimiter=',')
            for row in csv_reader:
                El=self.FindAndReturnElement(row[1],row[2])
                self.ObjectRepo[row[0]]=El

    def FindAndReturnElement(self, Stratergy, Locator):
        IdentificationData= self.CreateStratergyLocatorTuple(Stratergy, Locator)
        RequiredElement= WebTest.Driver.find_element(*IdentificationData)
        return RequiredElement

    def CreateStratergyLocatorTuple(self, StratergyToken, Locator):
        StratergyLocatorTuple= {
            "BY_ID": (By.ID, Locator),
            "BY_CLASS": (By.CLASS_NAME, Locator),
            "BY_NAME": (By.NAME, Locator),
            "BY_CSS": (By.CSS_SELECTOR, Locator),
            "BY_XPATH": (By.XPATH, Locator),
            "BY_LINKTEXT": (By.LINK_TEXT, Locator)


        }
        return StratergyLocatorTuple.get(StratergyToken)

    def EnterText(self,El,TextTobeEntered):
        El.clear()
        El.send_keys(TextTobeEntered)

    def ClickElement(self,El):
        El.click()
    def GetCurrentURL(self):
        return self.Driver.current_url

    def GetElementText(self, element):
        return element.text

    def tearDown(self):
        self.Driver.close()