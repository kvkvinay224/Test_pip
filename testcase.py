from object_repo.loginpage import Login_page
import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("set_up_browser")
class Test_Login:


    def setup_class(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.dr = Login_page(self.driver)
        
    @pytest.mark.smoke
    def test_valid_logins(self):
        self.dr.user_id(xpath="//input[@name='username']", value="Admin")
        logger.info("enter userid success")
        self.dr.password(xpath="//input[@name='password']", value="admin123")
        logger.info("enter pass success")
        self.dr.click_login(xpath="//button[@type='submit']")
        logger.info("click operation Login button success")

        
    @pytest.mark.regression
    def test_valid_login(self):
        self.dr.user_id(xpath="//input[@name='username']", value="Admin")
        self.dr.password(xpath="//input[@name='password']", value="admin123")
        self.dr.click_login(xpath="//button[@type='submit']")

        
    

    def teardown_class(self):
        self.driver.quit()

