import os
from datetime import datetime
from utils.notify import send_email

def pytest_configure(config):
    """更改生成报告的路径"""
    htmlpath = str(config.getoption('htmlpath'))
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    config.option.htmlpath = os.path.join(config.rootdir, 'reports', htmlpath.format(now))


def pytest_addoption(parser):
    parser.addoption("--send-email", action="store_true", help="发送邮件")
    parser.addini('toaddrs', help='收件人')
    parser.addini('fromaddr', help='发件人')
    parser.addini('body', help='邮件正文内容')


def pytest_terminal_summary(config):
    report_path = config.getoption('htmlpath')
    fromaddr = config.getini('fromaddr')
    toaddrs = config.getini('toaddrs')
    body = config.getini('body')
    send_email().sendeml(fromaddr, toaddrs,body,report_path)


