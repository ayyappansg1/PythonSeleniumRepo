import pytest
from selenium.webdriver.chrome.service import Service
#from seleniumwire import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="class", autouse=True, params=["chrome", "edge", "firefox"])
def setup(request):
    global driver
    # browser_name = request.config.getoption("--browser_name")
    browser_name = request.param
    remote_url = "http://localhost:4444/wd/hub"
    #remote_url="http://host.docker.internal:4444/wd/hub"
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # serviceObj = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=serviceObj)
        driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)
    elif browser_name == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        # serviceObj = Service(EdgeChromiumDriverManager().install())
        # driver = webdriver.Edge(service=serviceObj)
        driver = webdriver.Remote(command_executor=remote_url, options=edge_options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        # serviceObj = Service(GeckoDriverManager().install())
        # driver = webdriver.Firefox(service=serviceObj)
        driver = webdriver.Remote(command_executor=remote_url, options=firefox_options)
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
            # _capture_screenshot(filename)  # Pass item to capture screenshot
            if filename:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px" onclick="window.open(this.src)" align="right"/></div>' % filename
                extra.append(pytest_html.extras.html(html))
    report.extra = extra
