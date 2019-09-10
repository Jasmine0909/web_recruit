import unittest
from selenium import webdriver


class SinaTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_username_password_null(self):
        self.assertEqual(self.driver.title, '新浪邮箱')
        name = self.driver.find_element_by_id('freename')
        psw = self.driver.find_element_by_id('freepassword')
        self.assertTrue(name.is_enabled())
        self.assertTrue(psw.is_enabled())
        # 自动登录按钮
        sel = self.driver.find_element_by_id('store1')
        self.assertFalse(sel.is_selected())


if __name__ == '__main__':
    unittest.main(verbosity=2)
