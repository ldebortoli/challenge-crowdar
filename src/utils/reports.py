import os, re
from datetime import datetime


def delete_files_in_dir(browser, dir_path, extention):
    for file in os.listdir(dir_path):
        if file.endswith(extention) and (browser in file):
            os.remove(os.path.join(dir_path, file))


def report_fail_test(report, item, html_plugin):
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            save_screenshot(item, report, html_plugin)


def save_screenshot(item, report, html_plugin):
    curr_time = re.sub(r"\.|\s|:|-", '_', str(datetime.now()))
    directory = os.path.dirname("reports")
    feature_request = item.funcargs["request"]
    browser = feature_request.getfixturevalue("driver_args")["browser"]

    filename = report.nodeid.replace("::", "_")
    filename = re.sub(r"\A.*\.py_", '', filename)
    filename = f"screenshots/{browser}_{filename}_{curr_time}.png"
    full_path = f"reports/{filename}"

    driver = feature_request.getfixturevalue("driver")
    driver.save_screenshot(full_path)

    append_img_html = (f"<div><img src=\"{filename}\" alt=\"screenshot\" "
                       "style=\"width:300px;height=200px\" "
                       "onclick=\"window.open(this.src)\" align=\"right\"/></div>")
    extra = getattr(report, "extra", [])
    extra.append(html_plugin.extras.html(append_img_html))
    report.extra = extra
