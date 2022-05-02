from driver import Driver
import pytest
import allure
import time
import sys
import os
import io

from pluggy import HookspecMarker
hookspec = HookspecMarker("pytest")
CT = time.time_ns()

def pytest_sessionfinish(session, exitstatus):
    Driver.driver.quit()
    if "--collect-only" not in sys.argv:
            os.popen("allure serve reports/allure")


def pytest_runtest_teardown(item):
    node = item.obj
    image_name = "./reports/images/" + str(CT) + ".png"
    image = Driver.driver.get_screenshot_as_file(image_name)

    allure.attach.file(
        image_name,
        name=node.__name__+"-step__screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
    # html_file = "./reports/html/" + str(CT) + ".html"
    # f = io.open(html_file, "w", encoding="utf-8")
    # html = Driver.driver.page_source()
    # f.write(html)
    # allure.attach.file(html, name="step__source_xml", attachment_type=allure.attachment_type.XML)


@hookspec(firstresult=True)
def pytest_runtest_makereport(item):
    node = item.obj
    print("\nNow testing: "+node.__name__)
    img = "./reports/images/" + str(CT) + ".png"
    Driver.driver.get_screenshot_as_file(img)
