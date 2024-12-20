import time

import pyautogui
import pytest
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from POM.HomePage import HomePage
from POM.SecondPage import SecondPage
from seleniumwire import webdriver as wire_web_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup", "launchApplication")
class TestSecondHalf:

    @pytest.fixture(scope="function")
    def setup_logger_and_object_creation(self):
        logger = BaseClass.getLogger()
        homepage = HomePage(self.driver)
        secondpage = SecondPage(self.driver)
        pyautogui.FAILSAFE = False
        return logger, homepage, secondpage

    def test_verifyGeoLocation(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickGeoLocationButton()
        secondpage.clickWhereAmIButton()
        assert secondpage.verifyBothLongtitudeAndLatitude("12.906197", "80.225775") == True, "Both Values are mismatch"

    def test_verifyHorizontalSlider(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickHorizontalSliderButton()
        secondpage.performActionOnSlider()
        assert secondpage.verifySliderText(5) == True, "Sliding not happened"

    def test_verifyHover(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickHoversButton()
        asMap = [{"first": "user1"}, {"second": "user2"}, {"third": "user3"}]

        assert secondpage.mouseHoverToEachImage(homepage.driver, asMap) == True, "Profile not matches"

    def test_verifyInfiniteScroll(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickInfiniteScrollButton()
        secondpage.scrollFiveTimes(5)

    def test_verifyInputs(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickInputsButton()
        secondpage.enterNumberAndClickAdd(245445, homepage.driver)

    def test_verifyJQueryMenus(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickJQueryUIMenusButton()
        secondpage.mouseHoverToEnabled()
        assert secondpage.verifyAfterMouseHoverToEnabledTab("Downloads",
                                                            "Back to JQuery UI") == True, "Enabled Tab options mismatch"
        secondpage.clickOnJQueryBackUI()
        assert secondpage.verifyMenuHyperLink() == True, "Menu hyperLink is not visible"
        secondpage.clickMenuRedirectLink()
        secondpage.verifyRedirectionLink("menu")
        secondpage.mouseHoverToDownloadsPage()
        assert secondpage.verifyDownloadsTabOptions("PDF", "CSV","Excel") == True, "Downloads tab not having all these three options"
        secondpage.clicksOnPdfOption()
        assert secondpage.verifyDownloadedFile() == True, "PDF file is not downloaded"

    def test_verifyJavaScriptAlerts(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickJavaScriptAlertsButton()
        secondpage.clickJSAlertButton()
        assert secondpage.verifyJSAlertButton(
            "You successfully clicked an alert") == True, "JS Alert text is not matching"
        secondpage.clickJSAlertConfirmButton()
        assert secondpage.verifyJSAlertButton("You clicked: Ok") == True, "JS Alert Confirm text is not matching"
        secondpage.clickJSAlertConfirmWithCancelButton()
        assert secondpage.verifyJSAlertButton("You clicked: Cancel") == True, "JS Alert Confirm text is not matching"
        secondpage.clickJSAlertPromptButton("sangar")
        assert secondpage.verifyJSAlertButton("You entered: sangar") == True, "JS Alert Prompt text is not matching"

    def test_verifyJavaScriptOnloadEventError(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickJavaScriptOnloadEventErrorButton()
        assert secondpage.verifyUserLandingPageAfterClickJSOnloadError() == True, "User landed in unexpected page"
        assert secondpage.verifyJavascriptErrorOnPage(
            "JavaScript error in the onload event") == True, "Error mismatch or not found"

    def test_verifyKeyPresses(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickKeyPressesButton()
        asList = ["ENTER", "TAB", "SHIFT", "CONTROL", "SPACE"]
        secondpage.pressKeysBasedOnGiven(asList)
        asList1 = ["ENTER", "TAB", "SHIFT", "CONTROL", "SPACE"]
        assert secondpage.verifyKeysPressed(asList1) == True, "List Mismatches"

    def test_verifyLargeAndDeepDom(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickLargeAndDeepDOMButton()
        secondpage.fetchValueFromTable()
        assert secondpage.verifyingTheValueWithTableValue(6.22) == True, "Value matching with exact value"

    def test_verifyMultipleWindows(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickMultipleWindowsButton()
        secondpage.clickClickHereNewWindow()
        assert secondpage.switchToNewWindowAndGrabText("New Window") == True, "Value Mismatches in both"

    def test_verifyNestedFrames(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickNestedFramesButton()
        assert secondpage.fetchingBottomFrameTextAndVerify("BOTTOM", homepage.driver), "Bottom Frame has issue"
        assert secondpage.fetchingRightFrameTextAndVerify("RIGHT", homepage.driver), "Right frame has issue"

    def test_verifyNotificationMessage(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickNotificationMessageButton()
        secondpage.clickClickHereNotification()
        assert secondpage.verifyTheFirstNotificationMessage("Action successful",
                                                            "Action unsuccesful, please try again") == True, "First message not equal"
        secondpage.clickClickHereNotificationUntilNewMessageAppears()
        assert secondpage.verifyTheSecondNotification() == True, "second message not equal"

    def test_verifyRedirectLink(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickRedirectLinkButton()
        secondpage.clickClickHereRedirectLinkbutton()
        assert secondpage.verifyURLAfterRedirectClick("status_codes") == True, "landed in incorrect url"

    def test_verifySecureFileDownload(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickSecurefiledownloadButton()
        secondpage.enterCredentialsUsingRobot()
        downloadRandomFile = homepage.downloadRandomFile()
        assert secondpage.checkDownloadedFileInLocal(downloadRandomFile) == True, "file is not present"

    def test_verifyShadowDom(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickShadowDomButton()
        assert secondpage.gettingTextFromFirstParagraphShadowDom(
            "Let's have some different text!") == True, "first para has non matching text"
        assert secondpage.gettingTextFromSeconddParagraphShadowDom("Let's have some different text!",
                                                                   "In a list!") == True, "SecondPara not matching"

    def test_verifyShiftingContent(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickShiftingContentButton()
        asList = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
        assert secondpage.clickMenuElementAndVerifyTabs(asList) == True, "Menus are mismatch"
        assert secondpage.clickHomeElementAndRedirectToHomePage(homepage.driver) == True, "Not landed on home page"
        secondpage.clickAnImageButtonAndGetBeforeClickCssValue(secondpage.driver)
        assert secondpage.verifyImageMovedAfterReload() == False, "Image not moved to new location"
        secondpage.clickList()
        assert secondpage.compareContentsForEveryLoad(homepage.driver) == True, "Content not changing dynamically"

    def test_verifySlowResources(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickSlowResourcesButton(homepage.driver)
        assert secondpage.captureAndReturnUrls(503, secondpage.driver), "Status Code is not as expected"

    def test_verifySortableDataTables(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickSortableDataTablesButton()
        assert secondpage.verifyLastNameFirstTable() == True, "Mismatch after sorting"
        assert secondpage.verifyFirstNameFirstTable() == True, "Mismatch after sorting"
        assert secondpage.verifyEmailFirstTable() == True, "Mismatch after sorting"
        assert secondpage.verifyDueFirstTable() == True, "Mismatch after sorting"
        assert secondpage.verifyWebSiteFirstTable() == True, "Mismatch after sorting"
        assert secondpage.verifyLastNameSecondTable() == True, "Mismatch after sorting"
        assert secondpage.verifyFirstNameSecondTable() == True, "Mismatch after sorting"
        assert secondpage.verifyEmailSecondTable() == True, "Mismatch after sorting"
        assert secondpage.verifyDueSecondTable() == True, "Mismatch after sorting"
        assert secondpage.verifyWebSiteSecondTable() == True, "Mismatch after sorting"

    def test_verifyStatusCodes(self, setup_logger_and_object_creation):
        logger, homepage, secondpage = setup_logger_and_object_creation
        homepage.clickStatusCodesButton()
        assert secondpage.clickAndValidate200StatusCode(200, homepage.driver) == True, "Status Code is not as expected"
        assert secondpage.clickAndValidate301StatusCode(301, homepage.driver) == True, "Status Code is not as expected"
        assert secondpage.clickAndValidate404StatusCode(404, homepage.driver) == True, "Status Code is not as expected"
        assert secondpage.clickAndValidate500StatusCode(500, homepage.driver) == True, "Status Code is not as expected"
