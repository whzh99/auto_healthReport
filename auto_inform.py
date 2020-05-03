from selenium import webdriver
from tkinter import messagebox
import time


def auto(stuID, name, personID):
    browser = webdriver.Chrome()
    browser.get("http://xgsys.swjtu.edu.cn/SPCP/Web/UserLogin.aspx")

    username_box = browser.find_element_by_id('StudentId')
    username_box.send_keys(stuID)

    name_box = browser.find_element_by_id('Name')
    name_box.send_keys(name)

    stucard_box = browser.find_element_by_id('StuCard')
    stucard_box.send_keys(personID)

    code_box = browser.find_element_by_id('codeInput')
    code_input = browser.find_element_by_xpath("//div[@id='code-box']").text
    code_box.send_keys(code_input)

    signin_link = browser.find_element_by_id('Button4')
    signin_link.click()

    check_box = browser.find_element_by_id('Checkbox1')
    check_box.click()

    save_button = browser.find_element_by_id('Save_Btn')
    save_button.click()

    info = browser.find_element_by_xpath(
        "//*[@id=\"layui-layer1\"]/div[2]").text
    messagebox.showinfo("提示", time.strftime("%Y/%m/%d") + info)

    ok_button = browser.find_element_by_xpath(
        "//*[@id=\"layui-layer1\"]/div[3]/a")
    ok_button.click()


def main():
    stuID = ''  # 学号
    name = ''  # 姓名
    personID = ''  # 身份证号后六位
    auto(stuID, name, personID)


if __name__ == '__main__':
    main()
