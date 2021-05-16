from OrangeHRMDemoApp_Pages.LoginPage import LoginPage

def testLoginFunctionalityWithValidCredentials():

    loginpage=LoginPage("Chrome")
    loginpage.DoLogin("Admin","admin123")
    DashboardPageURL=loginpage.GetPageURL()
    assert DashboardPageURL=="https://opensource-demo.orangehrmlive.com/index.php/dashboard"
    loginpage.tearDown()