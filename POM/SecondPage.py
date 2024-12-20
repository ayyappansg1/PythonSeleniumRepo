import time

import faker
from faker import Faker
from selenium.webdriver.common.by import By
from tests.BaseClass import BaseClass
from POM.HomePage import HomePage


class SecondPage(BaseClass):

    def __init__(self, driver):
        BaseClass.__init__(self, driver)
        self.pressed = None
        self.tableValue = None
        self.parentWindow = None
        self.firstFlash = None
        self.beforeClickCssValue = None
        self.logger = BaseClass.getLogger()

    whereAmIButton = (By.XPATH, "//button[text()='Where am I?']")
    lattitudeText = (By.CSS_SELECTOR, "#lat-value")
    longitudeText = (By.CSS_SELECTOR, "#long-value")
    slider = (By.XPATH, "//input[@type='range']")
    sliderText = (By.XPATH, "//span[@id='range']")
    images = (By.XPATH, "//div/img")
    imageText = (By.CSS_SELECTOR, ".figcaption h5")
    numberBox = (By.CSS_SELECTOR, ".example input")
    enabledTab = (By.XPATH, "//a[text()='Enabled']")
    enabledOptions = (By.XPATH, "//a[text()='Enabled']//following::ul[@aria-expanded='true']/child::li/a")
    downloadsTab = (By.XPATH, "//a[text()='Downloads']")
    menuHyperLink = (By.XPATH, "//a[text()='Menu']")
    backToJQueryUI = (By.XPATH, "//a[text()='Back to JQuery UI']")
    downloadsOptions = (By.XPATH, "//a[text()='Downloads']//following::ul//li/a")
    clickForJsAlertButton = (By.XPATH, "//button[text()='Click for JS Alert']")
    clickForJsAlertConfirmButton = (By.XPATH, "//button[text()='Click for JS Confirm']")
    clickForJsAlertPromptButton = (By.XPATH, "//button[text()='Click for JS Prompt']")
    resultText = (By.CSS_SELECTOR, "#result")
    jsErrorText = (By.XPATH, "//p")
    tableCellValue = (By.XPATH, "(//th/span[text()='21']//following::tr)[6]//td[22]")
    clickHereToOpenNewWindow = (By.XPATH, "//a[text()='Click Here']")
    newWindowText = (By.XPATH, "//h3")
    topFrame = (By.XPATH, "//frame[@src='/frame_top']")
    rightFrame = (By.XPATH, "//frame[@src='/frame_right']")
    rightFrameContent = (By.XPATH, "//body")
    bottomFrame = (By.XPATH, "//frame[@src='/frame_bottom']")
    bottomFrameContent = (By.XPATH, "//body")
    flashMessage = (By.CSS_SELECTOR, "#flash")
    clickHereNotificationLoad = (By.XPATH, "//a[text()='Click here']")
    redirectClick = (By.CSS_SELECTOR, "#redirect")
    shadowHost = (By.CSS_SELECTOR, "my-paragraph:first-of-type")
    shadowHostSecond = (By.CSS_SELECTOR, "my-paragraph:nth-of-type(2)")
    private = (By.XPATH, "//ul[@slot='my-text']/li")
    secondParaContents = (By.CSS_SELECTOR, "[slot='my-text'] li")
    firstParagraph = (By.CSS_SELECTOR, "[slot='my-text']")
    menuElement = (By.XPATH, "//a[text()='Example 1: Menu Element']")
    anImageElement = (By.XPATH, "//a[text()='Example 2: An image']")
    listElement = (By.XPATH, "//a[text()='Example 3: List']")
    clickHereToReloadForImage = (By.XPATH, "//code[text()='?mode=random']//following-sibling::a[text()='click here']")
    tabNames = (By.XPATH, "//ul/li/a")
    imgLocation = (By.CSS_SELECTOR, "img.shift")
    centreContents = (By.XPATH, "//div[@id='content']//child::div[contains(@class,'large-centered')]")
    example1LastNames = (By.XPATH, "//table[@id='table1']/tbody//td[1]")
    example1FirstNames = (By.XPATH, "//table[@id='table1']/tbody//td[2]")
    example1Email = (By.XPATH, "//table[@id='table1']/tbody//td[3]")
    example1Due = (By.XPATH, "//table[@id='table1']/tbody//td[4]")
    example1WebSite = (By.XPATH, "//table[@id='table1']/tbody//td[5]")
    example2LastNames = (By.XPATH, "//table[@id='table2']/tbody//td[1]")
    example2FirstNames = (By.XPATH, "//table[@id='table2']/tbody//td[2]")
    example2Email = (By.XPATH, "//table[@id='table2']/tbody//td[3]")
    example2Due = (By.XPATH, "//table[@id='table2']/tbody//td[4]")
    example2WebSite = (By.XPATH, "//table[@id='table2']/tbody//td[5]")
    lastNameHeaderExample1 = (By.XPATH, "//table[@id='table1']//span[text()='Last Name']")
    firstNameHeaderExample1 = (By.XPATH, "//table[@id='table1']//span[text()='First Name']")
    emailHeaderExample1 = (By.XPATH, "//table[@id='table1']//span[text()='Email']")
    dueHeaderExample1 = (By.XPATH, "//table[@id='table1']//span[text()='Due']")
    websiteHeaderExample1 = (By.XPATH, "//table[@id='table1']//span[text()='Web Site']")
    lastNameHeaderExample2 = (By.XPATH, "//table[@id='table2']//span[text()='Last Name']")
    firstNameHeaderExample2 = (By.XPATH, "//table[@id='table2']//span[text()='First Name']")
    emailHeaderExample2 = (By.XPATH, "//table[@id='table2']//span[text()='Email']")
    dueHeaderExample2 = (By.XPATH, "//table[@id='table2']//span[text()='Due']")
    websiteHeaderExample2 = (By.XPATH, "//table[@id='table2']//span[text()='Web Site']")
    TwoHundredHyperLink = (By.XPATH, "//a[text()='200']")
    ThreeZeroOneHyperLink = (By.XPATH, "//a[text()='301']")
    FourZeroFourHyperLink = (By.XPATH, "//a[text()='404']")
    FiveZeroZeroHyperLink = (By.XPATH, "//a[text()='500']")
    clickHereRedirectLink = (By.XPATH, "//a[@href='redirect']")

    def verifyAfterMouseHoverToEnabledTab(self, first, second):
        status = False
        allTextContents = self.getAllTextContents(*SecondPage.enabledOptions)
        for text in allTextContents:
            if str(first) in text:
                status = True
            elif str(second) in text:
                status = True
            else:
                status = False
        return status

    def clickOnJQueryBackUI(self):
        self.click_element(*SecondPage.backToJQueryUI)

    def verifyMenuHyperLink(self):
        return self.verify_element(*SecondPage.menuHyperLink)

    def clickMenuRedirectLink(self):
        self.click_element(*SecondPage.menuHyperLink)

    def verifyRedirectionLink(self, url):
        return url in self.getCurrentPageUrl()

    def mouseHoverToDownloadsPage(self):
        self.mouseHover(*SecondPage.enabledTab)
        time.sleep(2)
        self.mouseHover(*SecondPage.downloadsTab)

    def verifyDownloadsTabOptions(self, first, second, third):
        textFromFeatureFile = [first, second, third]
        allTextContents = self.getAllTextContents(*SecondPage.downloadsOptions)
        self.logger.info(f"allTextContents from Downloads Menu is:{allTextContents}")
        return allTextContents == textFromFeatureFile

    def clicksOnPdfOption(self):
        self.click_element(*SecondPage.downloadsOptions)

    def verifyDownloadedFile(self):
        return self.verifyFileName("menu")

    def clickJSAlertButton(self):
        self.click_element(*SecondPage.clickForJsAlertButton)
        self.handlingAlertWithAllPossibleActions("accept", None)

    def clickJSAlertConfirmButton(self):
        self.click_element(*SecondPage.clickForJsAlertConfirmButton)
        self.handlingAlertWithAllPossibleActions("accept", None)

    def clickJSAlertConfirmWithCancelButton(self):
        self.click_element(*SecondPage.clickForJsAlertConfirmButton)
        self.handlingAlertWithAllPossibleActions("dismiss", None)

    def clickJSAlertPromptButton(self, text):
        self.click_element(*SecondPage.clickForJsAlertPromptButton)
        self.handlingAlertWithAllPossibleActions("accept", text)

    def verifyJSAlertButton(self, text):
        actualtext = self.get_text_content(*SecondPage.resultText)
        self.logger.info(f"Actual text from web is :{actualtext}")
        return text in actualtext

    def verifyUserLandingPageAfterClickJSOnloadError(self):
        return self.verifyUrlContainsExpectedText("javascript_error")

    def verifyJavascriptErrorOnPage(self, text):
        return text in self.get_text_content(*SecondPage.jsErrorText)

    def pressKeysBasedOnGiven(self, list):
        self.logger.info("Before key press")
        self.pressed = self.pressKeysAndReturnTextFromChangeOccured(list, *SecondPage.resultText)

    def verifyKeysPressed(self, list):
        return list ==  self.pressed

    def fetchValueFromTable(self):
        self.tableValue = self.get_text_content(*SecondPage.tableCellValue)
        self.logger.info(f"actual table value is :{self.tableValue}")

    def verifyingTheValueWithTableValue(self, value):
        self.logger.info(f"actual table value is :{self.tableValue}")
        return str(value) == self.tableValue

    def clickClickHereNewWindow(self):
        self.parentWindow = self.getParentWindow()
        self.click_element(*SecondPage.clickHereToOpenNewWindow)

    def switchToNewWindowAndGrabText(self, text):
        self.switchToAnotherWindow(self.parentWindow)
        textContent = self.get_text_content(*SecondPage.newWindowText)
        self.logger.info("ACtual Text from web:" + textContent)
        self.logger.info("ACtual Text from feature file:" + text)
        equals = textContent == text
        self.switchToParentWindow(self.parentWindow)
        return equals

    def fetchingRightFrameTextAndVerify(self, right, driver):
        self.switchToFrame(*SecondPage.topFrame)
        self.switchToFrame(*SecondPage.rightFrame)
        textContent = self.get_text_content(*SecondPage.rightFrameContent)
        self.logger.info("right Frame content" + textContent)
        self.switchToParent()
        return right in textContent

    def fetchingBottomFrameTextAndVerify(self, bottom, driver):
        self.switchToFrame(*SecondPage.bottomFrame)
        textContent = self.get_text_content(*SecondPage.bottomFrameContent)
        self.switchToParent()
        self.logger.info("Bottom Frame content" + textContent)
        return bottom in textContent

    def clickClickHereNotification(self):
        self.click_element(*SecondPage.clickHereNotificationLoad)

    def verifyTheFirstNotificationMessage(self, flashMessageExp, alternate):
        self.firstFlash = self.get_text_content(*SecondPage.flashMessage)
        self.logger.info(f"First flash message {self.firstFlash}")
        status = False
        if flashMessageExp in self.firstFlash or alternate in self.firstFlash: status = True
        return status

    def clickClickHereNotificationUntilNewMessageAppears(self):
        textContent = self.get_text_content(*SecondPage.flashMessage)
        while textContent == self.firstFlash:
            self.click_element(*SecondPage.clickHereNotificationLoad)
            textContent = self.get_text_content(*SecondPage.flashMessage)

    def verifyTheSecondNotification(self):
        textContent = self.get_text_content(*SecondPage.flashMessage)
        self.logger.info("Second flash message" + textContent)
        if self.firstFlash not in textContent:
            return True
        else:
            return False

    def clickRedirectLink(self):
        self.click_element(*SecondPage.redirectClick)

    def enterCredentialsUsingRobot(self):
        self.passingValuesInWindowPopup("admin", "admin")

    def checkDownloadedFileInLocal(self, fileName):
        time.sleep(5)
        return self.verifyFileName(fileName)

    def gettingTextFromFirstParagraphShadowDom(self, text):
        return text in self.getTextFromShadowDomAccessing()

    def gettingTextFromSeconddParagraphShadowDom(self, first, second):
        asList = [first, second]
        textFromShadowDomAccessingMultiple = self.getTextFromShadowDomAccessingMultiple()
        return self.compareTwoListAndCheckItContainsStringIn(asList, textFromShadowDomAccessingMultiple)

    def clickMenuElementAndVerifyTabs(self, listsself):
        self.click_element(*SecondPage.menuElement)
        allTextContents = self.getAllTextContents(*SecondPage.tabNames)
        return listsself == allTextContents

    def clickHomeElementAndRedirectToHomePage(self, driver):
        self.click_element_with_element(driver.find_elements(*SecondPage.tabNames)[0])
        return self.getCurrentPageUrl() == "https://the-internet.herokuapp.com/"

    def clickAnImageButtonAndGetBeforeClickCssValue(self, driver):
        HomePage(driver).clickShiftingContentButton()
        self.click_element(*SecondPage.anImageElement)
        self.beforeClickCssValue = self.getCssValueFromParticularElement(*SecondPage.imgLocation, cssValue="left")
        self.logger.info(f"Before clicking the reload pixel is:{self.beforeClickCssValue}")
        self.click_element(*SecondPage.clickHereToReloadForImage)

    def verifyImageMovedAfterReload(self):
        text = self.getCssValueFromParticularElement(*SecondPage.imgLocation, cssValue="left")
        self.logger.info("After reload css value  is :" + text)
        while self.beforeClickCssValue == text:
            self.click_element(*SecondPage.clickHereToReloadForImage)
            text = self.getCssValueFromParticularElement(*SecondPage.imgLocation, cssValue="left")
            self.logger.info("After every click :" + text)
        return self.beforeClickCssValue == text

    def clickList(self):
        self.directlylandOnParticularUrl("https://the-internet.herokuapp.com/shifting_content")
        self.click_element(*SecondPage.listElement)

    def compareContentsForEveryLoad(self,driver):
        textContent = self.get_text_content(*SecondPage.centreContents).split("\n")
        listed = []
        for i in textContent:
            listed.append(i)
        BaseClass.getLogger().info(f"Listed Before Load{listed}")
        self.refreshTheCurrentPage()
        AfterRefreshlist = []
        textContentAfterRefresh = self.get_text_content(*SecondPage.centreContents).split("\n")
        for i in textContentAfterRefresh:
            AfterRefreshlist.append(i)
        BaseClass.getLogger().info(f"Listed Before Load:{AfterRefreshlist}")
        return set(listed) == set(AfterRefreshlist)

    def captureAndReturnUrls(self, statusCode, driver):
        useDevToolstoGrabAPINetworks = BaseClass.useDevToolstoGrabAPINetworks(self.logger, driver)
        self.logger.info(f"all api's {useDevToolstoGrabAPINetworks}")
        filteredApi = None
        for i in useDevToolstoGrabAPINetworks:
            if "slow_external" in i:
                filteredApi = i
        self.logger.info(f"Filtered API is {filteredApi}")
        return self.hitParticularAPIUsingInbuiltJava(filteredApi) == statusCode

    def verifyLastNameFirstTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example1LastNames)
        programmatically_sorted = sorted(beforeSorting)
        self.logger.info(f"Before sorting Lastname column:{programmatically_sorted}")
        self.click_element(*SecondPage.lastNameHeaderExample1)
        afterSorting = self.getAllTextContents(*SecondPage.example1LastNames)
        self.logger.info(f"After sorting fromActual web Lastname column:{afterSorting}")
        return programmatically_sorted == afterSorting

    def verifyFirstNameFirstTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example1FirstNames)
        programmatically_sorted = sorted(beforeSorting)
        self.logger.info(f"Before sorting treeset firstname column:{programmatically_sorted = }")
        self.click_element(*SecondPage.firstNameHeaderExample1)
        afterSorting = self.getAllTextContents(*SecondPage.example1FirstNames)
        self.logger.info(f"After sorting fromActual web firstname column {afterSorting}")
        return programmatically_sorted == afterSorting

    def verifyEmailFirstTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example1Email)
        programmatically_sorted = sorted(beforeSorting)
        self.logger.info(f"Before sorting Email column:{programmatically_sorted}")
        self.click_element(*SecondPage.emailHeaderExample1)
        afterSorting = self.getAllTextContents(*SecondPage.example1Email)
        self.logger.info(f"After sorting fromActual web Email column{afterSorting}")
        return programmatically_sorted == afterSorting

    def verifyDueFirstTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example1Due)
        convertedToInt = []
        for i in beforeSorting:
            convertedToInt.append(float(i.replace("$", "")))
        programmatically_sorted = sorted(convertedToInt)
        self.logger.info(f"Before sorting Due column:{programmatically_sorted}")
        self.click_element(*SecondPage.dueHeaderExample1)
        afterSorting = self.getAllTextContents(*SecondPage.example1Due)
        convertedToIntAfterSorting = []
        for i in afterSorting:
            convertedToIntAfterSorting.append(float(i.replace("$", "")))
        self.logger.info(f"After sorting fromActual Due column{afterSorting}")
        return programmatically_sorted == convertedToIntAfterSorting

    def verifyWebSiteFirstTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example1WebSite)
        programmatically_sorted = sorted(beforeSorting)
        self.logger.info(f"Before sorting website column:{programmatically_sorted}")
        self.click_element(*SecondPage.websiteHeaderExample1)
        afterSorting = self.getAllTextContents(*SecondPage.example1WebSite)
        self.logger.info(f"After sorting fromActual website column{afterSorting}")
        return programmatically_sorted == afterSorting

    def verifyLastNameSecondTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example2LastNames)
        programmatically_sorted = sorted(beforeSorting)
        self.logger.info(f"Before sorting Lastname column:{programmatically_sorted}")
        self.click_element(*SecondPage.lastNameHeaderExample2)
        afterSorting = self.getAllTextContents(*SecondPage.example2LastNames)
        self.logger.info(f"After sorting fromActual web Lastname column:{afterSorting}")
        return programmatically_sorted == afterSorting

    def verifyFirstNameSecondTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example2FirstNames)
        programmatically_sorted = sorted(beforeSorting)
        self.logger.info(f"Before sorting treeset firstname column:{programmatically_sorted}")
        self.click_element(*SecondPage.firstNameHeaderExample2)
        afterSorting = self.getAllTextContents(*SecondPage.example2FirstNames)
        self.logger.info(f"After sorting fromActual web firstname column {afterSorting}")
        return programmatically_sorted == afterSorting

    def verifyEmailSecondTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example2Email)
        programmatically_sorted = sorted(beforeSorting)
        self.logger.info(f"Before sorting Email column:{programmatically_sorted}")
        self.click_element(*SecondPage.emailHeaderExample2)
        afterSorting = self.getAllTextContents(*SecondPage.example2Email)
        self.logger.info(f"After sorting fromActual web Email column{afterSorting}")
        return programmatically_sorted == afterSorting

    def verifyDueSecondTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example2Due)
        convertedToInt = []
        for i in beforeSorting:
            convertedToInt.append(float(i.replace("$", "")))
        programmatically_sorted = sorted(convertedToInt)
        self.logger.info(f"Before sorting Due column:{programmatically_sorted}")
        self.click_element(*SecondPage.dueHeaderExample2)
        afterSorting = self.getAllTextContents(*SecondPage.example2Due)
        convertedToIntAfterSorting = []
        for i in afterSorting:
            convertedToIntAfterSorting.append(float(i.replace("$", "")))
        self.logger.info(f"After sorting fromActual Due column{afterSorting}")
        return programmatically_sorted == convertedToIntAfterSorting

    def verifyWebSiteSecondTable(self):
        beforeSorting = self.getAllTextContents(*SecondPage.example2WebSite)
        programmatically_sorted = sorted(beforeSorting)
        self.logger.info(f"Before sorting website column:{programmatically_sorted}")
        self.click_element(*SecondPage.websiteHeaderExample2)
        afterSorting = self.getAllTextContents(*SecondPage.example2WebSite)
        self.logger.info(f"After sorting fromActual website column{afterSorting}")
        return programmatically_sorted == afterSorting

    def clickAndValidate200StatusCode(self, statusCode, driver):
        useDevToolstoGrabAPINetworks = BaseClass.useDevToolstoGrabAPINetworks(self.logger, driver)
        self.click_element(*SecondPage.TwoHundredHyperLink)
        fullUrl = [link for link in useDevToolstoGrabAPINetworks if "com/status_codes/200" in link]
        self.logger.info("200 url is :" + fullUrl[0])
        return self.hitParticularAPIUsingInbuiltJava(fullUrl[0]) == statusCode

    def clickAndValidate301StatusCode(self, statusCode, driver):
        self.directlylandOnParticularUrl("https://the-internet.herokuapp.com/status_codes")
        useDevToolstoGrabAPINetworks = BaseClass.useDevToolstoGrabAPINetworks(self.logger, driver)
        self.click_element(*SecondPage.ThreeZeroOneHyperLink)
        fullUrl = [link for link in useDevToolstoGrabAPINetworks if "com/status_codes/301" in link]
        self.logger.info("301 url is :" + fullUrl[0])
        return self.hitParticularAPIUsingInbuiltJava(fullUrl[0]) == statusCode

    def clickAndValidate404StatusCode(self, statusCode, driver):
        self.directlylandOnParticularUrl("https://the-internet.herokuapp.com/status_codes")
        useDevToolstoGrabAPINetworks = BaseClass.useDevToolstoGrabAPINetworks(self.logger, driver)
        self.click_element(*SecondPage.FourZeroFourHyperLink)
        fullUrl = [link for link in useDevToolstoGrabAPINetworks if "com/status_codes/404" in link]
        self.logger.info("404 url is :" + fullUrl[0])
        return self.hitParticularAPIUsingInbuiltJava(fullUrl[0]) == statusCode

    def clickAndValidate500StatusCode(self, statusCode, driver):
        self.directlylandOnParticularUrl("https://the-internet.herokuapp.com/status_codes")
        useDevToolstoGrabAPINetworks = BaseClass.useDevToolstoGrabAPINetworks(self.logger, driver)
        self.click_element(*SecondPage.FiveZeroZeroHyperLink)
        fullUrl = [link for link in useDevToolstoGrabAPINetworks if "com/status_codes/500" in link]
        self.logger.info("500 url is :" + fullUrl[0])
        return self.hitParticularAPIUsingInbuiltJava(fullUrl[0]) == statusCode

    def clickClickHereRedirectLinkbutton(self):
        self.click_element(*SecondPage.clickHereRedirectLink)

    def verifyURLAfterRedirectClick(self, text):
        return self.verifyUrlContainsExpectedText(text)

    def clickWhereAmIButton(self):
        self.click_element(*SecondPage.whereAmIButton)

    def verifyBothLongtitudeAndLatitude(self, first, second):
        latidudeActual = self.get_text_content(*SecondPage.lattitudeText)
        longititudeActual = self.get_text_content(*SecondPage.longitudeText)
        self.logger.info("Longitude values is :" + str(longititudeActual))
        status = longititudeActual is not None and latidudeActual is not None
        return status

    def performActionOnSlider(self):
        self.logger.info("Performing slider functions")
        self.slidingUsingMouseAction(SecondPage.slider, SecondPage.sliderText)

    def verifySliderText(self, number):
        slider_text = self.get_text_content(*SecondPage.sliderText)
        self.logger.info(f"Extracted text from slider_text:{slider_text}")
        return slider_text == str(number)

    def mouseHoverToEachImage(self, driver, wholelist):
        status = False
        dum_list = []
        for i in range(len(driver.find_elements(*SecondPage.images))):
            self.mouseHoverWithElement(driver.find_elements(*SecondPage.images)[i])
            dum_list.append(self.get_text_content_withElement(driver.find_elements(*SecondPage.imageText)[i]))
        self.logger.info(f"list of  for hover text:{dum_list}")
        self.logger.info(f"WholeList size is:{len(wholelist)}")

        for key, value in wholelist[0].items():
            self.logger.info(f"ActualMap is :{key}:{value}")

        for i in range(len(dum_list)):
            profile = dum_list[i]
            self.logger.info(f"Profile name:{profile}")
            for mp in range(len(wholelist)):
                for key, value in wholelist[i].items():
                    if value in profile:
                        status = True
                        break
                    else:
                        status = False
        return status

    def scrollFiveTimes(self, num):
        self.scrollNumberOfTimes(num)

    def enterNumberAndClickAdd(self, num, driver):
        BaseClass.sendValue(driver, *SecondPage.numberBox, option=int(num))
        self.sendValueWithArrow(*SecondPage.numberBox)

    def mouseHoverToEnabled(self):
        self.mouseHover(*SecondPage.enabledTab)
