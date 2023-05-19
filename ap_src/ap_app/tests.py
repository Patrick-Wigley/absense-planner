import pytest
from django.test import LiveServerTestCase
from seleniumbase import BaseCase

#TODO: Add id's to web-page elements being used during testing, instead of using xPaths 
#NOTE: 
# - If executing in terminal with pytest, must run command inside "ap_src" directory - (where "pytest.ini" is located)
# - Example in terminal: C:\[BASE_DIR]\ap_src> pytest
# - Although using Coverage is recommended as will produces a report of lines covered in testing suite
# - Example in terminal using coverage: C:\[BASE_DIR]> pytest --cov=ap_app ap_src/ap_app
# main.yml does this automatically in CI pipeline. 

# LiveServerTestCase is used to run the django application on an alternative thread, while tests are being executed
# SB - Driver

# Consts 
DEMO = False
USERNAME = "RandomUsername"
PASSWORD = "R@nD0mP@ssW0rD"

class TestSuiteTemplate(LiveServerTestCase, BaseCase):
    """ Testing Suite Class - Implement any tests inside
    its own method - (Methods to be tests must start with "test_*") """
    
    # @pytest.fixture
    # def setup(self):
    #     self.demo_mode = DEMO
    #     self.headless = (DEMO is False)
    #     print(f"[Test] Mode = {'DEMO' if DEMO else 'Headless'}")

# Basic test examples
    @pytest.mark.order1
    def test_example_pass(self):
        self.demo_mode = DEMO

        # PASS expected
        self.open(self.live_server_url)
        self.assert_true("Home" in self.get_page_title(),
            msg="[ERROR]: Not on Home-Page - Title does not match")
        self.click("/html/body/nav/div[2]/div[2]/div/div/div/a[1]")
        self.send_keys("/html/body/container/div/div/form/div[1]/div/input", text=USERNAME)
        self.send_keys("/html/body/container/div/div/form/div[2]/div/input", text=PASSWORD)
        self.send_keys("/html/body/container/div/div/form/div[3]/div/input", text=PASSWORD)
        self.click("/html/body/container/div/div/form/button")

    @pytest.mark.order2
    def test_example2_pass(self):
        self.demo_mode = DEMO

        # PASS expected
        self.open(self.live_server_url)
        self.assert_element_present("/html/body/nav/div[2]/div[2]/div/div/div/a[1]")

    @pytest.mark.order3
    def test_example3_fail(self):
        self.demo_mode = DEMO

        # FAIL expected
        self.open(self.live_server_url)
        self.assert_true("This is Not In Title" in self.get_page_title(),
            msg="[ERROR]: Not on Home-Page - Title does not match")
        