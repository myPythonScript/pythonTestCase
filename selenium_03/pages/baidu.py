class BaiduPage(object):
    """百度首页页面对象,负责该页面所有元素的定位及操作"""
    # 1. 传入driver
    def __init__(self, driver):  # baidu = BaiduPage(driver)
        self.driver = driver  # 将传入的参数绑定到对象 baidu.driver

    # 2. 列出所有使用的元素定位器
    search_ipt_loc = ('id', 'kw')  # 搜索框  元素定位器: 由定位方式+定位表达式唯一识别一个元素
    search_btn_loc = ('id', 'su')  # 搜索按钮

    # 定位方式支持 'id', 'name', 'class name', 'tag name', 'link text', 'partial link test', 'xpath' 'css selector'
    # 通用的定位方式


    # 3. 针对每个元素的每项操作封装一个函数
    def input_keyword(self, text):
        print("搜索框输入关键字")
        # 类属性会自动绑定对象
        # print(self.search_ipt_loc)
        # search_ipt = self.driver.find_element(*('id', 'kw'))  # ('id', 'kw'), 元组
        # search_ipt = self.driver.find_element('id', 'kw')

        search_ipt = self.driver.find_element(*self.search_ipt_loc)  # ('id', 'kw'), 元组类型
        search_ipt.clear()
        search_ipt.send_keys(text)

    def click_search_btn(self):
        print("点击搜索按钮")
        self.driver.find_element(*self.search_btn_loc).click()

    # 4. 可选：也可以封装组合流程
    def search(self, text):
        self.input_keyword(text)
        self.click_search_btn()
