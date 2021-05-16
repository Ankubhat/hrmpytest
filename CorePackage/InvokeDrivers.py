from selenium import webdriver

from CorePackage.Utilities.Utils import Utils

def StartChromeDriver():
    from CorePackage.WebTest import WebTest
    WebTest.Driver = webdriver.Chrome(
        executable_path=Utils.EnvVars.get("ChromeDriverPath"))
