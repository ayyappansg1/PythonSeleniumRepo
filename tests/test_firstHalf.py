import time

import pyautogui
import pytest
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from POM.HomePage import HomePage
from seleniumwire import webdriver as wire_web_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup", "launchApplication")
class TestFirstHalf:

    @pytest.fixture(scope="function")
    def setup_logger_and_object_creation(self):
        logger = BaseClass.getLogger()
        homepage = HomePage(self.driver)
        pyautogui.FAILSAFE = False
        return logger, homepage

    #@pytest.mark.skip
    def test_Add_And_Delete_Element(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        logger.info("About to click the element")
        homepage.clickAddRemoveElementButton()
        homepage.clickAddElementButton()
        assert homepage.verifyDeleteElementPresentOrNot() == True
        homepage.clickDeleteElementButton()
        assert homepage.verifyDeleteElementPresentOrNot() == False

    #@pytest.mark.skip
    @pytest.mark.parametrize("username,password", [("admin", "admin")])
    def test_verify_basic_authentication_verify(self, username, password, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        logger.info("click Basic Auth Button")
        homepage.clickBasicAuthButton()
        logger.info("Basic Auth button clicked")
        logger.info(f"value 1 is :{username} and second value is :{password}")
        homepage.sendValuesToTheAuthenticationBoxUsingRobot(username, password)
        assert homepage.verifySuccessMessage() == True

    #@pytest.mark.skip
    def test_verify_broken_Images(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        logger.info("Click Broken Image button")
        urls = BaseClass.useDevToolstoGrabAPINetworks(logger, homepage.driver)
        logger.info(f"urls list is: {urls}")
        homepage.clickBrokenImageButton()
        count = homepage.fetchBrokenImageLinks(urls)
        logger.info(f" count is :{count}")
        assert count > 0

    def test_verify_challenging_dom(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        logger.info("Click Challenging Dom Button")
        homepage.clickChallengingDomButton()
        homepage.clickRandomButton()
        tableValues = homepage.fetchColumnValues()
        logger.info(f"map Value is:{tableValues}")
        assert len(tableValues) != 0

    def test_verify_check_boxes(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        homepage.clickCheckboxesButton()
        homepage.checkAllCheckboxOptions()
        status = homepage.verifyFirstAndSecondBox()
        assert status is True

    #@pytest.mark.skip
    def test_verify_context_menu(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        homepage.clickContextMenuButton()
        homepage.rightClickOnRectangleBox()
        logger.info("Before alert")
        handlingAlert = homepage.handlingAlert(homepage.driver)
        logger.info(f"Alert text is :{handlingAlert}")
        assert "You selected a context menu" in handlingAlert

    #@pytest.mark.skip
    def test_verify_disappearing_elements(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        homepage.clickDisappearingElementsButton()
        compareTheCountings = homepage.compareTheCountings()
        assert compareTheCountings != 0

    #@pytest.mark.skip
    def test_drag_and_drop(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        homepage.clickDragAndDropButton()
        homepage.performDragDropInPage()
        verifyVisibilityOfINterchangedBoxes = homepage.verifyVisibilityOfINterchangedBoxes()
        assert verifyVisibilityOfINterchangedBoxes == "B"

    #@pytest.mark.skip
    def test_verifyDropdown(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        homepage.clickDropDownButton()
        homepage.selectGivenOptionFromDropdown("Option 2")
        fetchSelectedOptionFromDropdown = homepage.fetchSelectedOptionFromDropdown()
        assert fetchSelectedOptionFromDropdown == "Option 2"

    #@pytest.mark.skip
    def test_verifyDynamicContent(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        logger.info("Before click dynamic content button")
        homepage.clickDynamicContentButton()
        dynamicContentsComparision = homepage.dynamicContentsComparision()
        assert dynamicContentsComparision is False
        logger.info("First comparision passed")
        dynamicContentsComparision2 = homepage.dynamicContentsComparision()
        assert dynamicContentsComparision2 is False
        logger.info("Second comparision passed")

    #@pytest.mark.skip
    def test_verifyDynamicControlsButton(self, setup_logger_and_object_creation):
        logger, homepage = setup_logger_and_object_creation
        logger.info("Before click dynamic controls button")
        homepage.clickDynamicControlsButton()
        homepage.performActionsOnCheckBox()
        assert homepage.verifyGoneText("It's gone!") == True
        homepage.performAddButtonAgain()
        assert homepage.verifyBackText("It's back!") == True
        assert homepage.verifyTextBoxDisabled() == False
        homepage.clickEnableButton(homepage.driver, "SAngar")
        assert homepage.verifyEnabledMessage("It's enabled!") == True
        homepage.clickDisableButton()
        assert homepage.verifyDisabledMessage("It's disabled!") == True

    #@pytest.mark.skip
    def test_verifyEntryAd(self, setup_logger_and_object_creation):
        logger, homePage = setup_logger_and_object_creation
        homePage.clickEntryAdButton()
        assert homePage.verifyModelTitle("THIS IS A MODAL WINDOW") == True
        assert homePage.clickCloseButtonAndVerifyPopupClosed() == True

    #@pytest.mark.skip
    def test_verifyExitIntent(self, setup_logger_and_object_creation):
        logger, homePage = setup_logger_and_object_creation
        homePage.clickExitIntentButton()
        homePage.movingCursorAwayFromPage()
        assert homePage.verifyModalWindowOpened("THIS IS A MODAL WINDOW") == True

    #@pytest.mark.skip
    def test_verifyFileDownload(self, setup_logger_and_object_creation):
        logger, homePage = setup_logger_and_object_creation
        homePage.clickFileDownloadButton()
        downloadRandomFile = homePage.downloadRandomFile()
        assert homePage.verifyDownloadedFile(downloadRandomFile) == True, "file is not present"

    #@pytest.mark.skip
    def test_verifyFileUpload(self, setup_logger_and_object_creation):
        logger, homePage = setup_logger_and_object_creation
        homePage.clickFileUploadButton()
        clickAndUploadFile = homePage.clickAndUploadFile()
        assert homePage.verifyFilesUpload("File Uploaded!") == True, "Success Message not matches"
        assert homePage.verifyFileName(clickAndUploadFile) == True, "Uploaded file name not matching"

    #@pytest.mark.skip
    def test_verifyFloatingMenu(self,setup_logger_and_object_creation):
        logger, homePage = setup_logger_and_object_creation
        homePage.clickFloatingMenuButton()
        homePage.clickHomeTab()
        assert homePage.verifyUrlForEachClickTab("home")==True, "Url not contain:" + "home"
        homePage.clickNewsTab()
        assert homePage.verifyUrlForEachClickTab("news")==True, "Url not contain:" + "news"
        homePage.clickcontactTab()
        assert homePage.verifyUrlForEachClickTab("contact")==True, "Url not contain:" + "contact"
        homePage.clickaboutTab()
        assert homePage.verifyUrlForEachClickTab("about")==True, "Url not contain:" + "about"


    #@pytest.mark.skip
    def test_verifyForgotPassword(self,setup_logger_and_object_creation):
        logger, homePage = setup_logger_and_object_creation
        homePage.clickForgotPasswordButton()
        homePage.enterPasswordAndClickRetrivePassword(homePage.driver)
        assert homePage.verifyRetrivePasswordMessage()==True, "Invalid message"

    def test_verifyFormAuthentication(self,setup_logger_and_object_creation):
        logger, homePage = setup_logger_and_object_creation
        homePage.clickFormAuthenticationButton()
        homePage.enterUsernameAndPasswordGrabbedFromwebPage()
        assert homePage.verifySuccessMessageAfterLogin("You logged into a secure area!")==True,"Invalid Login  message"

    def test_verifyFrames(self,setup_logger_and_object_creation):
        logger, homePage = setup_logger_and_object_creation
        homePage.clickFramesButton()
        homePage.clickNestedFrame()
        assert "MIDDLE" in homePage.getTextFromNestedFrameMiddle(), "Nested Frame Content mismatch"
        homePage.clickIFrame()
        assert "Your content goes" in homePage.getTextFromIFrame(), "Iframe Content mismatch"

    def test_intercept_response_edge_case_testing(self):
        options = Options()
        options.add_argument("--start-maximized")
        wire_driver = wire_web_driver.Chrome(options=options)
        wire_driver.get("https://rahulshettyacademy.com/client")
        wire_driver.implicitly_wait(30)
        wire_driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("ayyappangunasekaran5@gmail.com")
        wire_driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("9442768022")
        wire_driver.find_element(By.CSS_SELECTOR, "#login").click()
        wire_driver.find_element(By.XPATH, "//button[contains(@routerlink,'/dashboard/myorders')]").click()

        # WebDriverWait(wire_driver,30).until(EC.presence_of_element_located(By.XPATH,"//h1[text()='Your Orders']"))
        # wire_driver.find_elements(By.XPATH, "//button[text()='View']")[0].click()

        def intercept_request(request):
            if "get-orders-details?id=" in request.url:
                print(f"Url is :{request.url}")
                modified_url = request.url.replace("id=673ff6dfae2afd4c0bc8c956", "id=674007b5ae2afd4c0bc8d134")
                request.url = modified_url

        wire_driver.request_interceptor = intercept_request

        WebDriverWait(wire_driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[text()='View']"))
        )
        wire_driver.find_elements(By.XPATH, "//button[text()='View']")[0].click()
        web_element = WebDriverWait(wire_driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='You are not authorize to view this order']"))
        )
        assert " not authorize" in web_element.text
