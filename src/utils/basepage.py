"""定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类"""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os.path
# from src.utils.logger import Logger
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from random import choice
from src.utils.log import Log
from src.utils.screenshot import ScreenShot


logger = Log()
# logger = Logger("BasePage").getlog()
png_path = ScreenShot()


class BasePage:


    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, selector):
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.add_log("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.add_log("NoSuchElementException: %s" % e)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == 'classname':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.add_log("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.add_log("NoSuchElementException: %s" % e)
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    # 输入
    def input(self, selector, text):
        el = self.find_element(selector)
        try:
            el.clear()
            el.send_keys(text)
            logger.add_log("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.add_log("Failed to type in input box with %s" % e)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.add_log("Sleep for %d seconds" % seconds)

    # 点击
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            # logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.add_log("Failed to click the element with %s" % e)

    # 清理
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
        except NameError as e:
            logger.add_log("Failed to click the element with %s" % e)

    # 切到iframe
    def switch_frame(self):
        iframe = self.find_element('classname=>embed-responsive-item')
        try:
            self.driver.switch_to_frame(iframe)
            # logger.info("The element \' %s \' was clicked." % iframe.text)
        except NameError as e:
            logger.add_log("Failed to click the element with %s" % e)

    # 处理标准下拉选择框,随机选择
    def select(self, id):
        select1 = self.find_element(id)
        try:
            options_list = select1.find_elements_by_tag_name('option')
            del options_list[0]
            s1 = choice(options_list)
            Select(select1).select_by_visible_text(s1.text)
            logger.add_log("随机选的是：%s" % s1.text)
        except NameError as e:
            logger.add_log("Failed to click the element with %s" % e)

    # 执行js
    def execute_js(self, js):
        self.driver.execute_script(js)

    # 模拟回车键
    def enter(self, selector):
        e1 = self.find_element(selector)
        e1.send_keys(Keys.ENTER)

    # 模拟鼠标左击
    def leftclick(self, element):
        # e1 = self.find_element(selector)
        ActionChains(self.driver).click(element).perform()

    # 截图，保存在根目录下的screenshots
    def take_screenshot(self, img_name):
        photo_path = png_path.return_photo_path(img_name)
        # print(photo_path)
        try:
            self.driver.get_screenshot_as_file(photo_path)
            logger.add_log("Had take screenshot and saved!")
        except Exception as e:
            logger.add_log("Failed to take screenshot!%s" % e)

    def take_page(self):
        self.driver.tilte

    def isElementExist(self, xpath):
        flag = True
        driver = self.driver
        try:
            driver.find_element_by_xpath(xpath)
            return flag
        except:
            flag = False
            return flag