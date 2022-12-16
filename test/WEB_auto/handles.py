"""
多窗口操作
"""
# 1. 导入模块
from time import sleep
from selenium import webdriver # 2. 实例化浏览器对象
driver = webdriver.Chrome() # 3. 打开页面
driver.get('www.baidu.com')

# 需求：打开‘注册实例.html’页面，完成以下操作# 1). 点击‘注册A页面’链接driver.find_element_by_id('ZCA').click()

# 查看当前窗口的句柄值
# 说明: 在浏览器的一个生命周期内(开启到关闭),
# 任意一个窗口都有唯一的一个句柄值, 可以通过句柄值完成窗口切换操作
print('当前句柄值为:', driver.current_window_handle)

# 切换窗口操作
# 1> 获取所含有窗口句柄(包含新窗口) handles =  driver.window_handles # print(handles)
# print(type(handles))


# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()