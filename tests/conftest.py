import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service


#driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )

@pytest.fixture(scope="class")
def launch_browser_app(request):
    browser_name = request.config.getoption("browser_name")
    #chrome_options = webdriver.ChromeOptions()
    if browser_name == "chrome":
        #options = Options()
        #options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        service_obj = Service("/Users/supraja.kollapudi/OneDrive - Signant Health/Back Up/Python/Selenium Webdriver with Python - Raghul Setty/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "edge":
        service_obj = Service("/Users/supraja.kollapudi/OneDrive - Signant Health/Back Up/Python/Selenium Webdriver with Python - Raghul Setty/msedgedriver")
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    print("I am teardown")

"""
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
"""




