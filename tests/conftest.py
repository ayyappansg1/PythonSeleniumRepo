import pytest
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class", autouse=True, params=["chrome", "edge", "firefox"])
def setup(request):
    global driver
    #browser_name = request.config.getoption("--browser_name")
    browser_name = request.param
    if browser_name == "chrome":
        serviceObj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=serviceObj)
    elif browser_name == "edge":
        serviceObj = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=serviceObj)
    elif browser_name == "firefox":
        serviceObj = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=serviceObj)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def launchApplication():
    driver.get("https://the-internet.herokuapp.com/")


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the pytest plugin to take and embed screenshot in HTML report
    :param item:
    :return:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            filename = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(filename)  # Pass item to capture screenshot
            if filename:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px" onclick="window.open(this.src)" align="right"/></div>' % filename
                extra.append(pytest_html.extras.html(html))
    report.extra = extra
