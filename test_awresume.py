from selenium import webdriver
import unittest, time

class Awresume(unittest.TestCase):
    def setUp(self):

        # set pdf handling to auto download so Firefox doesn't hang on prompt
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
        
        self.driver = webdriver.Firefox(firefox_profile=fp)
        # poll DOM until pageload
        self.driver.implicitly_wait(15)
        self.base_url = "http://resume-aaronweitekamp.rhcloud.com/"
        self.verificationErrors = []

    def test_resume(self):
        """Test a few components of site:
        Assert title match, expand and collapse "Skills and Comp" section,
        download PDF. Sleep statements are not an elegant solution 
        but allow browser to catch up.
        """
        driver = self.driver
        driver.get(self.base_url)

        self.assertRegexpMatches(driver.title, r"^.*[aA]aron.[wW]eitekamp.*$")

        driver.find_element_by_id("skills").click()

        time.sleep(1)

        driver.find_element_by_id("skills").click()

        driver.find_element_by_id("resume-pdf").click()

        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
