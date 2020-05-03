# auto_healthReport
 可以自动填写西南交通大学的每日健康等级
 如果非Windows系统则可以手动运行程序来进行填写。
 
## 前期准备
- 安装selenium模块
- 安装tkinter模块
- 安装浏览器对应的webdriver驱动并放置到正确位置
- 需要anaconda（非必须，为了配合Windows系统内的自动定时运行）

## 代码实现
# 参看我的auto_inform.py
'''
def main():
    stuID = ''  # 学号
    name = ''  # 姓名
    personID = ''  # 身份证号后六位
    auto(stuID, name, personID)
'''
 在对应的引号位置内填入有关信息
 
## 自动化处理（可选）
- 新建bat脚本 以任意名字命名 e.g.'''auto.bat'''
```python
call 你的anaconda访问路径\Anaconda3\Scripts\activate.bat 你的anaconda访问路径\Anaconda3
cd /d 你的python文件访问路径（若在C盘则不需要前面的/d）
python 你的python文件名.py
```
- 在开始中搜索'任务计划程序'
- 右击任务计划程序库，选择'创建任务'
- 填入名称
- 选择新建触发器
- 按需选择触发器的时间设置
- 来到'操作'选项卡
- 选择新建并浏览脚本 选择对应刚刚的bat文件
- 在条件选项卡的电源内可以选择是否唤醒计算机

## 参考文档（内有截图形式）
https://s3.us-west-2.amazonaws.com/temporary.notion-static.com/Export-0c12bbdc-9de9-45df-9e21-1eedb973a079/.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200503%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200503T155205Z&X-Amz-Expires=604800&X-Amz-Signature=673aa199729f9438572261593811ddbd27ff233abec2c100dbce0035eba32424&X-Amz-SignedHeaders=host
