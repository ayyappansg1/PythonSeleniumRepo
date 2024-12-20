import time

import faker
from faker import Faker
from selenium.webdriver.common.by import By
from tests.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        BaseClass.__init__(self, driver)
        self.logger=BaseClass.getLogger()

    addRemoveElement = (By.XPATH, "//a[contains(@href,'add')]")
    addElementButton = (By.XPATH, "//button[text()='Add Element']")
    deleteElementButton = (By.XPATH, "//button[text()='Delete']")
    basicAuthButton = (By.XPATH, "//a[text()='Basic Auth']")
    authSuccessMessage = (By.CSS_SELECTOR, "div p")
    brokenImageButton = (By.XPATH, "//a[text()='Broken Images']")
    challengingDomButton = (By.XPATH, "//a[text()='Challenging DOM']")
    randomButton = (By.XPATH, "//a[@class='button alert']")
    checkBoxButton = (By.XPATH, "//a[text()='Checkboxes']")
    ContextMenuButton = (By.XPATH, "//a[text()='Context Menu']")
    disappearingButton = (By.XPATH, "//a[text()='Disappearing Elements']")
    rectangleBox = (By.CSS_SELECTOR, "#hot-spot")
    checkBoxes = (By.CSS_SELECTOR, "#checkboxes input")
    pageHeaders = (By.XPATH, "//ul//li")
    seventhRow = (By.XPATH, "//tr[5]//td")
    rowHeader = (By.XPATH, "//thead//th")
    ABox = (By.CSS_SELECTOR, "#column-a")
    BBox = (By.CSS_SELECTOR, "#column-b")
    dragAndDropButton = (By.XPATH, "//a[text()='Drag and Drop']")
    dropDownButton = (By.XPATH, "//a[text()='Dropdown']")
    dropdownLocator = (By.ID, "dropdown")
    dynamicContentButton = (By.XPATH, "//a[text()='Dynamic Content']")
    dynamicContents = (By.XPATH, "//div[@id='content']//div[@class='large-10 columns']")
    dynamicControlButton = (By.XPATH, "//a[text()='Dynamic Controls']")
    dynamicLoadingButton = (By.XPATH, "//a[text()='Dynamic Loading']")
    inputCheckBox = (By.XPATH, "//input[@type='checkbox']")
    removeButton = (By.XPATH, "//button[text()='Remove']")
    goneText = (By.XPATH, "//button[text()='Add']//following::p")
    backText = (By.XPATH, "//button[text()='Remove']//following::p")
    addButton = (By.XPATH, "//button[text()='Add']")
    inputTextBox = (By.XPATH, "//input[@type='text']")
    enableButton = (By.XPATH, "//button[text()='Enable']")
    disableButton = (By.XPATH, "//button[text()='Disable']")
    disabledMessage = (By.XPATH, "//button[text()='Enable']//following::p")
    enabledMessage = (By.XPATH, "//button[text()='Disable']//following::p")
    example1 = (By.XPATH, "//a[contains(@href,'loading/1')]")
    example2 = (By.XPATH, "//a[contains(@href,'loading/2')]")
    startButton = (By.XPATH, "//button[text()='Start']")
    helloWorldMessage = (By.XPATH, "//div[@id='finish']/h4")
    entryAd = (By.XPATH, "//a[text()='Entry Ad']")
    exitIntent = (By.XPATH, "//a[text()='Exit Intent']")
    closebutton = (By.XPATH, "//div[@class='modal-footer']//p")
    modalTitle = (By.XPATH, "//div[@class='modal-title']")
    verificationPurpose = (By.CSS_SELECTOR, ".example h3")
    fileDownload = (By.XPATH, "//a[text()='File Download']")
    fileUpload = (By.XPATH, "//a[text()='File Upload']")
    floatingMenu = (By.XPATH, "//a[text()='Floating Menu']")
    forgotPassword = (By.XPATH, "//a[text()='Forgot Password']")
    formAuthentication = (By.XPATH, "//a[text()='Form Authentication']")
    frames = (By.XPATH, "//a[text()='Frames']")
    geoLocation = (By.XPATH, "//a[text()='Geolocation']")
    horizontalSlider = (By.XPATH, "//a[text()='Horizontal Slider']")
    hovers = (By.XPATH, "//a[text()='Hovers']")
    infiniteScroll = (By.XPATH, "//a[text()='Infinite Scroll']")
    inputs = (By.XPATH, "//a[text()='Inputs']")
    jqueryUIMenus = (By.XPATH, "//a[text()='JQuery UI Menus']")
    javaScriptAlerts = (By.XPATH, "//a[text()='JavaScript Alerts']")
    javaScriptOnloadEventError = (By.XPATH, "//a[text()='JavaScript onload event error']")
    keyPresses = (By.XPATH, "//a[text()='Key Presses']")
    largeAndDeepDom = (By.XPATH, "//a[text()='Large & Deep DOM']")
    multipleWindows = (By.XPATH, "//a[text()='Multiple Windows']")
    nestedFramees = (By.XPATH, "//a[text()='Nested Frames']")
    notificationMessages = (By.XPATH, "//a[text()='Notification Messages']")
    redirectLink = (By.XPATH, "//a[text()='Redirect Link']")
    secureFileDownload = (By.XPATH, "//a[text()='Secure File Download']")
    shadowDom = (By.XPATH, "//a[text()='Shadow DOM']")
    shiftingContent = (By.XPATH, "//a[text()='Shifting Content']")
    slowResources = (By.XPATH, "//a[text()='Slow Resources']")
    sortableDataTables = (By.XPATH, "//a[text()='Sortable Data Tables']")
    statusCodes = (By.XPATH, "//a[text()='Status Codes']")
    typos = (By.XPATH, "//a[text()='Typos']")
    WYSIWYGEditor = (By.XPATH, "//a[text()='WYSIWYG Editor']")
    chooseFileButton = (By.CSS_SELECTOR, "#file-upload")
    allFiles = (By.CSS_SELECTOR, ".example a")
    fileUploadedSuccessMessage = (By.XPATH, "//h3[text()='File Uploaded!']")
    uploadButton = (By.CSS_SELECTOR, "#file-submit")
    uploadedFileName = (By.CSS_SELECTOR, "#uploaded-files")
    homeTab = (By.XPATH, "//a[@href='#home']")
    newsTab = (By.XPATH, "//a[@href='#news']")
    contactTab = (By.XPATH, "//a[@href='#contact']")
    aboutTab = (By.XPATH, "//a[@href='#about']")
    forgotPasswordMessage = (By.CSS_SELECTOR, "body h1")
    emailTextBox = (By.CSS_SELECTOR, "#email")
    retrivePassword = (By.XPATH, "//i[text()='Retrieve password']")
    loginSuccessMessage = (By.XPATH, "//div[@class='flash success']")
    usernameBox = (By.CSS_SELECTOR, "#username")
    passwordBox = (By.CSS_SELECTOR, "#password")
    loginButton = (By.CSS_SELECTOR, ".radius")
    usernamePassword = (By.CSS_SELECTOR, ".subheader em")
    nestedFrame = (By.XPATH, "//a[text()='Nested Frames']")
    iFrame = (By.XPATH, "//a[text()='iFrame']")
    insideIFrame = (By.XPATH, "//iframe")
    frameContent = (By.CSS_SELECTOR, "#tinymce")
    mainFrame = (By.XPATH, "//frame[@src='/frame_top']")
    middleFrame = (By.XPATH, "//frame[@src='/frame_middle']")
    middleContent = (By.CSS_SELECTOR, "#content")

    def clickShiftingContentButton(self):
        self.logger.info("Trying to Click Shifting Content from the Home page")
        self.click_element(*HomePage.shiftingContent)

    def clickAddRemoveElementButton(self):
        self.click_element(*HomePage.addRemoveElement)

    def clickAddElementButton(self):
        self.click_element(*HomePage.addElementButton)

    def verifyDeleteElementPresentOrNot(self):
        return self.verify_element(*HomePage.deleteElementButton)

    def clickDeleteElementButton(self):
        self.click_element(*HomePage.deleteElementButton)

    def clickBasicAuthButton(self):
        self.click_element(*HomePage.basicAuthButton)

    def sendValuesToTheAuthenticationBoxUsingRobot(self, username, password):
        self.passingValuesInWindowPopup(username, password)

    def verifySuccessMessage(self):
        text = self.get_text_content(*HomePage.authSuccessMessage)
        self.logger.info(f"Success MEssage grabbed from Web{text}")
        return "Congratulations! You must" in text

    def clickBrokenImageButton(self):
        self.click_element(*HomePage.brokenImageButton)

    def fetchBrokenImageLinks(self, urlsList):
        fetchOnlyImageUrlss = self.fetchOnlyImageUrls(urlsList)
        return self.returnBrokenImagesUrl(fetchOnlyImageUrlss)

    def clickChallengingDomButton(self):
        self.click_element(*HomePage.challengingDomButton)

    def clickRandomButton(self):
        self.click_element(*HomePage.randomButton)

    def fetchColumnValues(self):
        seventhRowValues = self.getAllTextContents(*HomePage.seventhRow)
        rowHeaderValues = self.getAllTextContents(*HomePage.rowHeader)
        combinedMap = self.combineTwoListAndReturnMap(seventhRowValues, rowHeaderValues)
        return combinedMap

    def clickCheckboxesButton(self):
        self.click_element(*HomePage.checkBoxButton)

    def checkAllCheckboxOptions(self):
        self.clickAllCheckboxes(*HomePage.checkBoxes)

    def verifyFirstAndSecondBox(self):
        elements = self.driver.find_elements(*HomePage.checkBoxes)
        flag = False
        for ele in elements:
            if ele.is_selected():
                flag = True
        return flag

    def clickContextMenuButton(self):
        self.click_element(*HomePage.ContextMenuButton)

    def rightClickOnRectangleBox(self):
        self.rightClickOnElement(*HomePage.rectangleBox)

    def handlingAlert(self, driver):
        logger = BaseClass.getLogger()
        self.logger.info("inside homepage class")
        return BaseClass.handlingAlertWithGetText(driver, logger)

    def clickDisappearingElementsButton(self):
        self.click_element(*HomePage.disappearingButton)

    def compareTheCountings(self):
        return self.refreshThePageWithPreviousElementsCount(*HomePage.pageHeaders)

    def clickDragAndDropButton(self):
        self.click_element(*HomePage.dragAndDropButton)

    def performDragDropInPage(self):
        self.performDragAndDrop(HomePage.ABox, HomePage.BBox)

    def verifyVisibilityOfINterchangedBoxes(self):
        return self.extractTextFromParticularElement(HomePage.ABox)

    def clickDropDownButton(self):
        self.click_element(*HomePage.dropDownButton)

    def selectGivenOptionFromDropdown(self, option):
        self.handlingDropdown(*HomePage.dropdownLocator, option=option)

    def fetchSelectedOptionFromDropdown(self):
        return self.get_first_selected_option_from_dropdown(*HomePage.dropdownLocator)

    def clickDynamicContentButton(self):
        self.click_element(*HomePage.dynamicContentButton)

    def dynamicContentsComparision(self):
        allTextContents1 = self.getAllTextContents(*HomePage.dynamicContents)
        self.refreshTheCurrentPage()
        allTextContents2 = self.getAllTextContents(*HomePage.dynamicContents)
        return allTextContents1 == allTextContents2

    def clickDynamicControlsButton(self):
        self.click_element(*HomePage.dynamicControlButton)

    def performActionsOnCheckBox(self):
        self.click_element(*HomePage.inputCheckBox)
        assert self.verifyCheckBoxChecked(*HomePage.inputCheckBox) == True
        self.click_element(*HomePage.removeButton)

    def verifyGoneText(self, text):
        return self.get_text_content(*HomePage.goneText) == text

    def verifyBackText(self, text):
        return self.get_text_content(*HomePage.backText) == text

    def performAddButtonAgain(self):
        self.click_element(*HomePage.addButton)

    def verifyTextBoxDisabled(self):
        return self.verify_enabled_element(*HomePage.inputTextBox)

    def clickEnableButton(self, driver, option):
        self.click_element(*HomePage.enableButton)
        self.sendValue(driver, *HomePage.inputTextBox, option=option)

    def verifyEnabledMessage(self, text):
        return self.get_text_content(*HomePage.enabledMessage) == text

    def clickDisableButton(self):
        self.click_element(*HomePage.disableButton)

    def verifyDisabledMessage(self, text):
        return self.get_text_content(*HomePage.disabledMessage) == text

    def clickEntryAdButton(self):
        self.click_element(*HomePage.entryAd)

    def verifyModelTitle(self,text):
        return text in self.get_text_content(*HomePage.modalTitle)

    def clickCloseButtonAndVerifyPopupClosed(self):
        self.click_element(*HomePage.closebutton)
        return self.verify_element(*HomePage.verificationPurpose)

    def clickExitIntentButton(self):
        self.click_element(*HomePage.exitIntent)

    def movingCursorAwayFromPage(self):
        self.mouseHoverAwayFromPage()

    def verifyModalWindowOpened(self,text):
        return text in self.get_text_content(*HomePage.modalTitle)

    def clickFileDownloadButton(self):
        self.click_element(*HomePage.fileDownload)

    def downloadRandomFile(self):
        return self.clickRandomElement(*HomePage.allFiles)

    def verifyDownloadedFile(self,text):
        time.sleep(5)
        return self.verifyFileName(text)

    def clickFileUploadButton(self):
        self.click_element(*HomePage.fileUpload)

    def clickAndUploadFile(self):
        uploadFileUsingSendKeys = self.uploadFileUsingSendKeys(*HomePage.chooseFileButton)
        self.click_element(*HomePage.uploadButton)
        return uploadFileUsingSendKeys

    def verifyFilesUpload(self,text):
        return text in self.get_text_content(*HomePage.fileUploadedSuccessMessage)

    def verifyFileName(self,text):
        return text in self.get_text_content(*HomePage.uploadedFileName)

    def clickFloatingMenuButton(self):
        self.click_element(*HomePage.floatingMenu)

    def clickHomeTab(self):
        self.click_element(*HomePage.homeTab)

    def verifyUrlForEachClickTab(self,text):
        return self.verifyUrlContainsExpectedText(text)
    def clickNewsTab(self):
        self.click_element(*HomePage.newsTab)

    def clickcontactTab(self):
        self.click_element(*HomePage.contactTab)

    def clickaboutTab(self):
        self.click_element(*HomePage.aboutTab)

    def clickForgotPasswordButton(self):
        self.click_element(*HomePage.forgotPassword)
    def enterPasswordAndClickRetrivePassword(self,driver):
        self.sendValue(driver,*HomePage.emailTextBox,option=Faker().name()+"@yopmail.com")
        self.click_element(*HomePage.retrivePassword)

    def verifyRetrivePasswordMessage(self):
        return "Internal Server" in self.get_text_content(*HomePage.forgotPasswordMessage)

    def clickFormAuthenticationButton(self):
        self.click_element(*HomePage.formAuthentication)

    def enterUsernameAndPasswordGrabbedFromwebPage(self):
        allTextContents=self.getAllTextContents(*HomePage.usernamePassword)

        logger=BaseClass.getLogger()
        self.logger.info(f"all Contents grabbed from web:{allTextContents}")
        self.sendValueWithTAB(*HomePage.usernameBox,firstValue=allTextContents[0],secondValue=allTextContents[1])
        self.click_element(*HomePage.loginButton)

    def verifySuccessMessageAfterLogin(self,text):
        return text in self.get_text_content(*HomePage.loginSuccessMessage)

    def clickFramesButton(self):
        self.click_element(*HomePage.frames)

    def clickNestedFrame(self):
        self.click_element(*HomePage.nestedFrame)

    def getTextFromNestedFrameMiddle(self):
        self.switchToFrame(*HomePage.mainFrame)
        self.switchToFrame(*HomePage.middleFrame)
        textContent=self.get_text_content(*HomePage.middleContent)
        BaseClass.getLogger().info(f"Nested Frame content:{textContent}")
        self.switchToParent()
        return textContent

    def getTextFromIFrame(self):
        self.switchToFrame(*HomePage.insideIFrame)
        textContent=self.get_text_content(*HomePage.frameContent)
        BaseClass.getLogger().info(f"Another Frame content:{textContent}")
        self.switchToParent()
        return textContent

    def clickIFrame(self):
        self.getBackToPreviousPage()
        self.click_element(*HomePage.iFrame)

    def clickGeoLocationButton(self):
        self.logger.info("Trying to Click GeoLocation Button from the Home page")
        self.click_element(*HomePage.geoLocation)

    def clickHorizontalSliderButton(self):
        self.logger.info("Trying to Click Horizontal Slider Button from the Home page")
        self.click_element(*HomePage.horizontalSlider)
    def clickHoversButton(self):
        self.logger.info("Trying to Click Hovers Button from the Home page")
        self.click_element(*HomePage.hovers)

    def clickInfiniteScrollButton(self):
        self.logger.info("Trying to Click InfiniteScroll Button from the Home page")
        self.click_element(*HomePage.infiniteScroll)

    def clickInputsButton(self):
        self.logger.info("Trying to Click Inputs Button from the Home page")
        self.click_element(*HomePage.inputs)
    def clickJQueryUIMenusButton(self):
        self.logger.info("Trying to Click JQueryUIMenus Button from the Home page")
        self.click_element(*HomePage.jqueryUIMenus)
    def clickJavaScriptAlertsButton(self):
        self.logger.info("Trying to Click JavaScript Alerts Button from the Home page")
        self.click_element(*HomePage.javaScriptAlerts)

    def clickJavaScriptOnloadEventErrorButton(self):
        self.logger.info("Trying to Click JavaScript Alerts OnLoadEvent error from the Home page")
        self.click_element(*HomePage.javaScriptOnloadEventError)

    def clickKeyPressesButton(self):
        self.logger.info("Trying to Click KeyPresses from the Home page")
        self.click_element(*HomePage.keyPresses)

    def clickLargeAndDeepDOMButton(self):
        self.logger.info("Trying to Click Large and Deep from the Home page")
        self.click_element(*HomePage.largeAndDeepDom)

    def clickMultipleWindowsButton(self):
        self.logger.info("Trying to Click MultipleWindows from the Home page")
        self.click_element(*HomePage.multipleWindows)

    def clickNestedFramesButton(self):
        self.logger.info("Trying to Click NestedFrames from the Home page")
        self.click_element(*HomePage.nestedFramees)

    def clickNotificationMessageButton(self):
        self.logger.info("Trying to Click NotificationMessages from the Home page")
        self.click_element(*HomePage.notificationMessages)

    def clickRedirectLinkButton(self):
        self.logger.info("Trying to Click RedirectLink from the Home page")
        self.click_element(*HomePage.redirectLink)

    def clickSecurefiledownloadButton(self):
        self.logger.info("Trying to Click SecureFileDownload from the Home page")
        self.scrollToLast()
        self.click_element(*HomePage.secureFileDownload)

    def clickShadowDomButton(self):
        self.logger.info("Trying to Click ShaodwDom from the Home page")
        self.click_element(*HomePage.shadowDom)

    def clickShiftingContentButton(self):
        self.logger.info("Trying to Click Shifting Content from the Home page")
        self.click_element(*HomePage.shiftingContent)

    def clickSlowResourcesButton(self,driver):
        BaseClass.useDevToolstoGrabAPINetworks(self.logger,driver)
        self.logger.info("Trying to Click SlowResourcesfrom the Home page")
        self.click_element(*HomePage.slowResources)

    def clickSortableDataTablesButton(self):
        self.logger.info("Trying to Click SortableDataTables the Home page")
        self.click_element(*HomePage.sortableDataTables)

    def clickStatusCodesButton(self):
        self.logger.info("Trying to Click statusCodes the Home page")
        self.click_element(*HomePage.statusCodes)

    def clickTyposButton(self):
        logger.info("Trying to Click Typos the Home page")
        self.click_element(*HomePage.typos)

    def clickWYSIWYGEditorButton(self):
        logger.info("Trying to Click WYSIWYGEditor from the Home page")
        self.click_element(*HomePage.WYSIWYGEditor, driver)
