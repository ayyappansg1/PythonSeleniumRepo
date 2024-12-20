import inspect
import time

import pytest
import random
import os
import pyperclip
from seleniumwire import webdriver as wire_webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common import NoAlertPresentException
import requests
from selenium.webdriver.chrome.webdriver import WebDriver
from seleniumwire import webdriver

import logging
import pyautogui


@pytest.mark.usefixtures("setup")
class BaseClass:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = None

    @staticmethod
    def getLogger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('log.log')
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        console_logger_handler = logging.StreamHandler()
        console_logger_formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        console_logger_handler.setFormatter(console_logger_formatter)
        logger.addHandler(console_logger_handler)
        logger.setLevel(logging.INFO)
        return logger

    def click_element(self, *locator):
        logger = BaseClass.getLogger()
        found_element = self.driver.find_element(*locator)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(found_element))
        self.driver.execute_script("arguments[0].scrollIntoView(true)", found_element)
        try:
            found_element.click()
            logger.info("Element clicked")
        except ElementClickInterceptedException as e:
            self.driver.execute_script("arguments[0].click();", found_element)
            logger.info(f"Clicked using JS-{str(e)}")
        except StaleElementReferenceException as m:
            found_element.click()
            logger.info(f"StaleElementException {str(m)}")

    def click_element_with_element(self, element):
        logger = BaseClass.getLogger()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)
        try:
            element.click()
            logger.info("Element clicked")
        except ElementClickInterceptedException as e:
            self.driver.execute_script("arguments[0].click();", element)
            logger.info(f"Clicked using JS-{str(e)}")
        except StaleElementReferenceException as m:
            element.click()
            logger.info(f"StaleElementException {str(m)}")

    def scrollToLast(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def verify_element(self, *element):
        logger = BaseClass.getLogger()
        try:
            found_element = self.driver.find_element(*element)
            status = found_element.is_displayed()
            logger.info("Element is displayed")
            return status
        except NoSuchElementException as e:
            statuss = False
            logger.info(f"NosuchElement occured-{str(e)}")
            return statuss
        except TimeoutException as n:
            status = False
            logger.info(f"Timeout Exception occured-{str(n)}")
            return status
        except Exception as o:
            status = False
            logger.info(f"Exception occured-{str(o)}")
            return status

    def verify_enabled_element(self, *element):
        logger = BaseClass.getLogger()
        found_element = self.driver.find_element(*element)
        try:
            if found_element is not None:
                status = found_element.is_enabled()
                logger.info("Element is displayed")
                return status
            else:
                status = False
                return status
        except NoSuchElementException as e:
            status = False
            logger.info(f"NosuchElement occured-{str(e)}")
            return status
        except TimeoutException as n:
            status = False
            logger.info(f"Timeout Exception occured-{str(n)}")
            return status
        except Exception as o:
            status = False
            logger.info(f"Exception occured-{str(o)}")
            return status

    def highlight_element(self, *element):
        found_element = self.driver.find_element(*element)
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located(found_element))

    def handling_alert(self, username, password, accept_or_dismiss):
        try:
            alert = self.driver.switch_to.alert
            if username is not None:
                alert.send_keys(username + Keys.TAB + password)
            if "accept" in accept_or_dismiss.lower():
                alert.accept()
            else:
                alert.dismiss()
        except NoAlertPresentException as e:
            print(f"No alert present: {e}")

    def passingValuesInWindowPopup(self, username, password):
        username = username.lower()
        password = password.lower()
        pyautogui.typewrite(username)
        pyautogui.press('tab')
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        time.sleep(3)

    def get_text_content(self, *element):
        found_element = self.driver.find_element(*element)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(found_element))
        return found_element.text

    def get_text_content_withElement(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(element))
        return element.text

    def fetchBrokenImageUsingNaturalWidth(self, *element):
        found_element = self.driver.find_element(*element)
        return found_element.get_attribute('src')

    def fetchOnlyImageUrls(self, urlList):
        newUrlList = []
        for s in urlList:
            if "jpg" in s:
                newUrlList.append(s)
        return newUrlList

    def returnBrokenImagesUrl(self, urlList):
        newUrlList = []
        for s in urlList:
            try:
                response = requests.get(s, timeout=10)
                if response.status_code != 200:
                    newUrlList.append(s)
            except requests.RequestException as e:
                newUrlList.append(s)

        return len(newUrlList)

    def getAllTextContents(self, *elements):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_all_elements_located(elements))
        logger = BaseClass.getLogger()
        text_contents = []
        all_elements = self.driver.find_elements(*elements)
        for s in range(len(all_elements)):
            text = all_elements[s].text
            logger.info(f"Text extracted from {text}")
            text_contents.append(text)
            time.sleep(1)
        return text_contents

    def combineTwoListAndReturnMap(self, first_list, second_list):
        if len(first_list) != len(second_list):
            raise ValueError("Both lists must be of the same length")

        result_map = {}
        for s in range(len(first_list)):
            result_map[first_list[s]] = second_list[s]
        return result_map

    def clickAllCheckboxes(self, *elements):
        all_elements = self.driver.find_elements(*elements)
        for s in all_elements:
            s.click()

    def rightClickOnElement(self, *element):
        element = self.driver.find_element(*element)
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    @staticmethod
    def handlingAlertWithGetText(driver, logger):
        logger.info("inside handling alertwith gettext method")
        try:
            logger.info("inside try block")
            # WebDriverWait(driver,30)
            #  .until(expected_conditions.alert_is_present())
            alert = driver.switch_to.alert
            content = alert.text
            alert.accept()
            logger.info(f"content is :{content}")
            logger.info("exiting try block")
            return content
        except UnexpectedAlertPresentException:
            logger.info("Inside except block:UnexpectedAlertPresentException")
            (WebDriverWait(driver, 30)
             .until(expected_conditions.alert_is_present()))
            alert = driver.switch_to.alert
            content = alert.text
            alert.accept()
            logger.info(f"Exiting except block with content:{content}")
            return content
        except NoAlertPresentException:
            print("No alert is present.")

    def refreshTheCurrentPage(self):
        self.driver.execute_script("history.go(0)")

    def refreshThePageWithPreviousElementsCount(self, *elements):
        global aftercount
        logger = BaseClass.getLogger()
        all_elements = self.driver.find_elements(*elements)
        count_before = len(all_elements)
        logger.info(f"count_before size is:{count_before}")
        while count_before == len(all_elements):
            self.driver.get(self.driver.current_url)
            try:
            # Wait for the page to load and the headers to be present again
                WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_all_elements_located(elements))
            except TimeoutException:
                logger.warning("Timeout while waiting for headers after page refresh.")
                return None
            all_elements = self.driver.find_elements(*elements)
            aftercount = len(all_elements)
            logger.info(f"After count size is:{aftercount}")
            # self.driver.execute_script("history.go(0)")
        # self.driver.execute_script("history.go(0)")
        # logger.info("before history refresh")
        # self.driver.get(self.driver.current_url)
        # WebDriverWait(self.driver,30).until(expected_conditions.)
        return count_before - aftercount

    def performDragAndDrop(self, fromElement, toElement):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(fromElement))
        source = self.driver.find_element(*fromElement)
        target = self.driver.find_element(*toElement)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def extractTextFromParticularElement(self, element):
        element = self.driver.find_element(*element)
        WebDriverWait(self.driver, 20).until(expected_conditions
                                             .visibility_of(element))
        return element.text

    def handlingDropdown(self, *element, option):
        element = self.driver.find_element(*element)
        select = Select(element)
        select.select_by_visible_text(option)

    def get_first_selected_option_from_dropdown(self, *element):
        element = self.driver.find_element(*element)
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of(element))
        select = Select(element)
        return select.first_selected_option.text

    def verifyCheckBoxChecked(self, *element):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(element))
        return self.driver.find_element(*element).is_selected()

    @staticmethod
    def sendValue(driver, *element, option):
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(element))
        driver.find_element(*element).send_keys(option)

    def sendValueWithTAB(self, *element, firstValue, secondValue):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(element))
        self.driver.find_element(*element).send_keys(firstValue)
        pyautogui.press("tab")
        pyautogui.typewrite(secondValue)

    def getBackToPreviousPage(self):
        self.driver.back()

    def mouseHoverAwayFromPage(self):
        pyautogui.moveTo(0, -10)

    def clickRandomElement(self, *allElements):
        all_elements = self.driver.find_elements(*allElements)
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_all_elements_located(allElements))
        element = random.choice(all_elements)
        text = element.text
        element.click()
        return text

    def verifyFileName(self, web_file_name):
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        file_exist = False
        for filename in os.listdir(download_path):
            if web_file_name.split('.')[0].split(' ')[0] in filename:
                file_exist = True
                break

        return file_exist

    def uploadFileUsingSendKeys(self, *element):
        upload_path = os.path.join(os.path.expanduser("~"), "Downloads")
        list_files = os.listdir(upload_path)
        if list_files:
            file_upload = os.path.join(upload_path, list_files[0])
            self.driver.find_element(*element).send_keys(file_upload)
            return list_files[0]
        else:
            raise FileNotFoundError("NO files found in the upload directory")

    def uploadFileUsingRobot(self):
        upload_path = os.path.join(os.path.expanduser("~"), "Downloads")
        files = os.listdir(upload_path)
        if files:
            upload_file = os.path.join(upload_path, files[0])
            pyperclip.copy(upload_file)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)  # Add a slight delay for pasting
            pyautogui.press("enter")
            return upload_file
        else:
            raise FileNotFoundError("No files found in the upload directory.")

    def verifyUrlContainsExpectedText(self, text):
        return text in self.driver.current_url

    def switchToFrame(self, *element):
        WebDriverWait(self.driver, 30).until(expected_conditions.frame_to_be_available_and_switch_to_it(element))

    def switchToParent(self):
        self.driver.switch_to.default_content()

    def slidingUsingMouseAction(self, element1, element2):
        first_element = self.driver.find_element(*element1)
        second_element = self.driver.find_element(*element2)
        ActionChains(self.driver).click_and_hold(first_element).move_to_element(second_element).release().perform()

    def mouseHover(self, *element):
        element = self.driver.find_element(*element)
        ActionChains(self.driver).move_to_element(element).perform()

    def mouseHoverWithElement(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def scrollNumberOfTimes(self, num):
        for i in range(num):
            self.driver.execute_script("window.scrollBy(0,1000)")
            time.sleep(3)

    def getCurrentPageUrl(self):
        return self.driver.current_url

    def sendValueWithArrow(self, *element):
        element = self.driver.find_element(*element)
        element.send_keys(Keys.ARROW_UP)

    def handlingAlertWithAllPossibleActions(self, acceptOrDismiss, enterText):
        alert = self.driver.switch_to.alert
        WebDriverWait(self.driver, 30).until(expected_conditions.alert_is_present())
        if enterText is None:
            if acceptOrDismiss == "accept":
                alert.accept()
            elif acceptOrDismiss == "dismiss":
                alert.dismiss()
            else:
                raise ValueError("Invalid option to handle alert")
        else:
            alert.send_keys(enterText)
            if acceptOrDismiss == "accept":
                alert.accept()
            else:
                alert.dismiss()

    def pressKeysAndReturnTextFromChangeOccured(self, keysToPress, *element):
        maps = {
            "TAB": Keys.TAB,
            "SPACE": Keys.SPACE,
            "CONTROL": Keys.CONTROL,
            "ENTER": Keys.ENTER,
            "SHIFT": Keys.SHIFT
        }
        empty_list = []
        action = ActionChains(self.driver)
        for key in keysToPress:
            if key in maps:
                action.send_keys(maps[key]).perform()
                time.sleep(2)
                element_final = self.driver.find_element(*element)
                text = element_final.text
                if ": " in text:
                    empty_list.append(text.split(": ")[1])
        return empty_list

    def getParentWindow(self):
        return self.driver.current_window_handle

    def switchToAnotherWindow(self, parentWindow):
        windows = self.driver.window_handles
        for win in windows:
            if win != parentWindow:
                self.driver.switch_to.window(win)
                break

    def switchToParentWindow(self, parentWindow):
        self.driver.switch_to.window(parentWindow)

    def getTextFromShadowDomAccessing(self):
        shadowHost = self.driver.find_elements(By.TAG_NAME, "my-paragraph")[0]
        self.logger.info(f"Shadow host located: {shadowHost}")
        # shadowRoot = self.driver.execute_script("return arguments[0].shadowRoot", shadowHost)
        # self.logger.info(f"Shadow root accessed: {shadowRoot}")
        paragraph = self.driver.execute_script("return arguments[0].querySelector('span[slot=\"my-text\"]')",
                                               shadowHost)
        self.logger.info(f"Paragraph element: {paragraph}")
        if paragraph is not None:
            shadowText = paragraph.text
            self.logger.info(f"Text inside shadow DOM paragraph: {shadowText}")
            return shadowText
        else:
            self.logger.error("No paragraph element found inside shadow DOM")
            raise Exception("No paragraph element found inside shadow DOM")

    def getTextFromShadowDomAccessingMultiple(self):
        shadowHost = self.driver.find_elements(By.TAG_NAME, "my-paragraph")[1]
        self.logger.info(f"Shadow host located: {shadowHost}")
        # shadowRoot = self.driver.execute_script("return arguments[0].shadowRoot", shadowHost)
        # self.logger.info(f"Shadow root accessed: {shadowRoot}")
        paragraph = self.driver.execute_script("return arguments[0].querySelectorAll('ul[slot=\"my-text\"] li')",
                                               shadowHost)
        self.logger.info(f"Paragraph element: {paragraph}")
        empty_list = [ele.text for ele in paragraph]
        return empty_list

    def getTextFromShadowDomAccessingWithoutJS(self, shadowHost, actualElement):
        shadow_roots = shadowHost.shadow_root
        return shadow_roots.find_element(actualElement).text

    def getTextFromShadowDomAccessingMultipleWithoutJS(self, shadowHost, actualElement):
        shadow_roots = shadowHost.shadow_root
        all_elements = shadow_roots.find_elements(actualElement)
        empty_list = [ele.text for ele in all_elements]
        print(f"Texts retrived : {empty_list}")
        return empty_list

    def compareTwoListAndCheckItContainsStringIn(self, firstList, secondList):
        status = False
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                if secondList[i] in firstList[i]:
                    status = True
                else:
                    status = False
        return status

    def getCssValueFromParticularElement(self, *element, cssValue):
        element_loc = self.driver.find_element(*element)
        return element_loc.value_of_css_property(cssValue)

    def goBack(self):
        self.driver.back()

    def directlylandOnParticularUrl(self, url):
        self.driver.get(url)

    def hitParticularAPIUsingInbuiltJava(self, url):
        response = requests.get(url)
        return response.status_code

    @staticmethod
    def useDevToolstoGrabAPINetworks(logger, driver):
        logger.info("inside API Networks")
        urls = []
        if isinstance(driver, wire_webdriver.Chrome):
            print(f"inside instance to check")
            driver.request_interceptor = lambda request: urls.append(request.url)
        logger.info("Outside Bro")
        logger.info(f"Url list :{urls}")
        return urls
