"""
此conftest.py文件用作确保直接在项目下执行pytest命令时能正常导入utils等模块。
也可以不使用该文件，但是在项目中执行时要使用python -m pytest来执行用例。
"""
import os
from datetime import datetime
from utils.notify import send_email

def pytest_configure(config):
    """更改生成报告的路径"""
    htmlpath = config.getoption('htmlpath')
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


