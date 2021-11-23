from selenium import webdriver
driver = webdriver.Chrome(r'E:\software\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://www.51job.com')
# 输入条件
ele = driver.find_element_by_id('kwdselectid')
ele.send_keys('python')
# 选择城市
ele = driver.find_element_by_id('work_position_input')
ele.click()
# 选择深圳
eles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')
for ele in eles:
    ele.click()
driver.find_element_by_id('work_position_click_center_right_list_category_000000_040000').click()
# 点击确定
driver.find_element_by_id('work_position_click_bottom_save').click()
# 点击搜索
driver.find_element_by_css_selector('.ush  button').click()
# 搜索结果分析
jobs = driver.find_elements_by_css_selector('.j_joblist div[class=e]')
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFields = [field.text for field in fields]
    print(' | '.join(stringFields))