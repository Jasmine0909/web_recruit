import os
import unittest
import time
import HTMLTestRunner


def sinaTest():
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__), 'Sina'),
        pattern='*.py',
        top_level_dir=None
    )
    return suite


def getTime():
    now_time = time.strftime('%y-%m-%d %H-%M-%S', time.localtime(time.time()))
    return now_time


def run():
    filename = os.path.join(os.path.dirname(__file__), 'repost', getTime()+'.html')
    f = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title='测试新浪邮箱网页',
        description='UI自动化报告详细信息'
    )
    runner.run(sinaTest())


if __name__ == '__main__':
    run()
