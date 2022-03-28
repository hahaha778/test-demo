#爬取步骤
    #一，获取网页
    #二，提取信息
    #三，保存数据
    #四，自动化程序
import requests
import urllib.request

import scrapy

'''requests.post(url,data)'''
'''post数据来源{一,固定值      抓包比较不变值
              二,输入值       抓包比较根据自身变化值
              三,预设值-静态文件 需要提前从html中获取 
              四,
              五,
}'''
url='http://www.baidu.com'
'''proxies代理参数'''
'''协议http,https,socks'''
'''页面源代码查看字符命令charset'''
proxies={
    "http":"http://114.98.16.182:8085",
     "https":"https://58.56.149.198:53281"
        }
from fake_useragent import UserAgent
ua = UserAgent().random         #随机ua
#一，response=requests.get(url,proxies=proxies,verift=False,timeout=10)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
'''response.text=response.content.decode'''
#response.text是str response.content是bytes
'''timeout超时限制'''
'''verift 跳过CA证书'''
'''连续多次请求requests.session'''
# session=requests.session() 实例化请求
# response=session.get(url,headers=headers)
# response=session.post(url,headers=headers,data)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# response=urllib.request.urlopen(url)
# print(response.getheaders())
# ''''响应头信息----[('Bdpagetype', '1'), ('Bdqid', '0xc13a9ebd00006072'), ('Cache-Control', 'private'), ('Content-Type', 'text/html;charset=utf-8'), ('Date', 'Mon, 08 Nov 2021 08:54:18 GMT'), ('Expires', 'Mon, 08 Nov 2021 08:53:25 GMT'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('P3p', 'CP=" OTI DSP COR IVA OUR IND COM "'), ('Server', 'BWS/1.1'), ('Set-Cookie', 'BAIDUID=A669A82063D46BF3D15AC938565411CA:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'BIDUPSID=A669A82063D46BF3D15AC938565411CA; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'PSTM=1636361658; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'), ('Set-Cookie', 'BAIDUID=A669A82063D46BF3E7252EE08F601ED2:FG=1; max-age=31536000; expires=Tue, 08-Nov-22 08:54:18 GMT; domain=.baidu.com; path=/; version=1; comment=bd'), ('Set-Cookie', 'BDSVRTM=0; path=/'), ('Set-Cookie', 'BD_HOME=1; path=/'), ('Set-Cookie', 'H_PS_PSSID=34948_34443_34067_31254_35063_34505_34916_34579_34812_34815_26350_22160_35018; path=/; domain=.baidu.com'), ('Traceid', '1636361658028891188213923615732555341938'), ('Vary', 'Accept-Encoding'), ('Vary', 'Accept-Encoding'), ('X-Frame-Options', 'sameorigin'), ('X-Ua-Compatible', 'IE=Edge,chrome=1'), ('Connection', 'close'), ('Transfer-Encoding', 'chunked')]'''
#print(response.getheader('Server'))  ---------BWS/1.1
'''查看服务器是用什么搭建的'''

'''xml和html区别
    xml传输和储存数据
    html展示数据
    '''
#解析库
'''-----------------------------------------------------re模块-----------------------------------------------------------------------'''
# import re
# content="Yunnan Transportation Vocational and Technical College"
# result=re.match("\w{6}\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)",content)  跨行匹配参数 re.S    re.findall()   re.search()    re.sub()
# import re
# content="hg45dsf154sf54ds5f"
# data=re.sub('\d+','',content)
# print(data)
# print(len(content))
# print(result)
# print(result.group())
# print(result.span())







# jsonpath
# from jsonpath import jsonpath
# data={'value1':{'value2':{'value3':{'value4':{'value5':{'value6':{'value7':'python'}}}}}}}
# print(data['value1']['value2']['value3']['value4']['value5']['value6']['value7'])
# print(jsonpath(data,'$..value7')[0])


'''--------------------------------------------------------Xpath----------------------------------------------------------------------------'''
# nodename    选取此节点的所有子节点
# /           从当前节点选取直接子节点
# //          从当前节点选取子孙节点
# .           选取当前节点
# ..          选取当前节点的父节点
# @           选取属性
# from lxml import etree
# text = '''
# <div>
# <ul>
# <li class="item-O"><a href="link1.html">first item</a><li>
# <li class="item-1"><a href="link4.html">fourth item</a>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </ul>
# </div>
# '''
# html=etree.HTML(text)
# result=etree.tostring(html)    tostring补全html
#print(result.decode('utf-8'))
# data=etree.HTML(text)
# result=data.xpath('//li[@class="item-1"]/a/@href')   属性提取
# print(result)
# text = '''
# <div>
# <ul>
# <li class="li li-first" name="item"><a href="link1.html">first item</a><li>
# </ul>
# </div>
# '''
# data=etree.HTML(text)
# result=data.xpath('//li[contains(@class,"li") and @name="item"]//text()') 多属性匹配
'''-----------------------------------------------bs4--------------------------------------------------------------------------------'''
# from bs4 import BeautifulSoup
# html ='''
# <html><head><title>The Dormouse’s story</title></head>
# <body>
# <p class=”title”name=”dromouse”><b>The Dormouse’s story</b></p>
# <p class ＝"story" Once upon a time there were three little sisters; and their names were
# <a href="http"://example.com/elsie" class= "sister"  id ＝"link1"><!-- Elsie --> </a>,
# <a href="http"://example.com/lacie" class ＝"sister" id="link2">Lacie</a> and
# <a href=“ http ://example.com/tillie" class="sister" id="link3”>Tillie</a>;
# and they lived at the bottom of a well. </p>
# <p class="story")...</p>
# '''
# soup=BeautifulSoup(html,'lxml')   传入的HTML以lxml形势
# print(soup)
# print(soup.title.string)  获取title标签的字符
# print("p",soup.p)        获取p节点
# print("head",soup.head)
# print("body",soup.body)
#print(type(soup.body))      <class 'bs4.element.Tag'>

# from bs4 import BeautifulSoup
# html=''',.
# <div class=”panel”>
# <div class="panel-heading”>
# <h4>Hello</h4>
# </div>
# <div class=”panel-body”>
# <ul class=”list” id=”list-1">
# <li class=“ element”> Foo<lli>
# <li class=” element”>Bar</li>
# <li class="element”>]ay</li>
# </ul>
# <Ul class="list list-small" id=”list-2">
# <li class=”element”> Foo</li>
# <li class=”element”>Bar</li>
# </ul>
# </div>
# '''
# soup=BeautifulSoup(html,'lxml')
# print(soup.select('li'))                   CSS选择器


'''----------------------------------------------selenium web自动化测试工具------------------------------------------------------------------'''
# phantomJS无界面浏览器          url="http://phantomjs.org/download.html"
# 开发使用有头浏览器，部署使用无头浏览器
# 谷歌的driver下载 url="https://npm.taobao.org/mirrors/chromedriver"

import  time
from selenium import webdriver
url="http://www.baidu.com"
driver=webdriver.Chrome()
data=driver.get(url)
#time.sleep(4)                等待时间4秒
#print(driver.page_source)   显示源码
#print(driver.current_url)   显示对应的url
#print(driver.title)        显示对应的标题
time.sleep(4)
driver.get("https://www.taobao.com/")
# time.sleep(4)
# driver.back()             返回上一页
# time.sleep(4)
# driver.forward()          前进到上一页
driver.save_screenshot("taobao.png")      #保存图片
driver.close()              #关闭标签页
# driver.quit()            关闭浏览器
'''---------------------------------------元素定位--------------------------------------'''
from selenium import webdriver
from selenium.webdriver.common.by import By
# 定位方式	By
# id	                 By.ID
# name	                 By.NAME
# class_name	         By.CLASS_NAME
# tag_name	             By.TAG_NAME
# link_text	             By.LINK_TEXT       链接文本
# partial_link_text	     By.PARTIAL_LINK_TEXT      模糊定位链接文本
# css_selector	         By.CSS_SELECTOR
# xpath	                 By.XPATH
'''---------------------------------调用webdriver浏览器查看58同城租房页面------------------------------------'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
url='https://www.baidu.com'
driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,value='#kw').send_keys('58')    #send_keys不能有中文  注意提取速度
driver.find_element(By.ID,value="su").click()
time.sleep(5)                      #注意时间间隔
driver.find_element(By.XPATH,value='//*[@id="1"]/h3/a[1]').click()
print(driver.window_handles)                                    #看看有几个标签页
driver.switch_to.window(driver.window_handles[-1])      #窗口句柄
driver.find_element(By.XPATH,value='/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a').click()
time.sleep(5)
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
url='https://km.58.com/chuzu/?PGTID=0d100000-0021-d119-378b-1638c8f4c542&ClickID=6&utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT'
driver=webdriver.Chrome()
driver.get(url)
data_list = driver.find_element(By.XPATH,value='/html/body/div[6]/div[2]/ul/li[1]/div[2]/h2/a')
for data in data_list:
    print(data.text,data.get_attribute("href"))     #提取元素

'''---------------------------------------自动登录qq空间----------------------------------------'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
url='https://qzone.qq.com/'
driver=webdriver.Chrome()
driver.get(url)
delukuang=driver.find_element(By.XPATH,value='//*[@id="login_frame"]')       #定位到frame框
driver.switch_to.frame(delukuang)       #操作区定位到frame里面，可以进行后面操作
# js='scrollTo(0,500)'                    #设定浏览器向y轴拉动500像素
# driver.execute_script(js)                #拉动浏览器
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,value='#switcher_plogin').click()
driver.implicitly_wait(5)                     #隐式等待 有反应计时结束，无反应时间到结束,数值最大为28
driver.find_element(By.XPATH,value='//*[@id="u"]').send_keys("3182651401")                #提取xpath值注意单双引号
driver.find_element(By.XPATH,value='//*[@id="p"]').send_keys("20020128dyhwd@")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,value='//*[@id="login_button"]').click()
time.sleep(10)
driver.quit()
print(str(int(time.time()*1000)))       #时间戳

'''----------------------------进行拖曳操作--------------------'''
from selenium import webdriver
from selenium.webdriver import ActionChains       #拖曳操作需要用到的模块
from selenium.webdriver.common.by import By
browser=webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")
url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source=browser.find_element(By.CSS_SELECTOR,value='#draggable')
target=browser.find_element(By.CSS_SELECTOR,value='#droppable')
actions=ActionChains(browser)
actions.drag_and_drop(source,target)    #说明拖曳对象和目标
actions.perform()             #执行拖曳动作


'''----------------反屏蔽--------------'''
from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(executable_path=r"C:/Program Files/Google/Chrome/Application/chromedriver.exe",options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
   'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'   #将webdriver值设置成空
})
browser.get('https://antispider1.scrape.center/')

'-----pyppeteer使用---------------------------------------'
import asyncio
from pyppeteer import launch
async def main():
    browser = await launch()                             #启动浏览器
    page = await browser.newPage()                      #启动浏览器后新建选项卡
    await page.goto('https://www.baidu.com/')          #请求网页
    await page.screenshot({'path': 'baidu.png'})      #截图网页
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
async def main():
   browser = await launch()                  #创建浏览器
   page = await browser.newPage()            #创建选项卡
   await page.goto('https://spa2.scrape.center/')
   await page.waitForSelector('.item .name')         #加载页面
   doc = pq(await page.content())                    #调用content方法 可以获取页面源代码，js渲染后的结果
   names = [item.text() for item in doc('.item .name').items()]
   print('Names:', names)
   await browser.close()
asyncio.get_event_loop().run_until_complete(main())

'''-----pyppeteer反屏蔽-----'''
import asyncio
from pyppeteer import launch
async def main():
    browser = await launch(headless=False, args=['--disable-infobars'],devtools=True)     #开启无头模式，和禁用提示条(chrome自动测试),开启调试模式
    page = await browser.newPage()
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')    #反屏蔽设置
    await page.goto('https://antispider1.scrape.center/')
    await asyncio.sleep(10)
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())

import asyncio
from pyppeteer import launch
width,height=1200,768
async def main():
    browser = await launch(headless=False, userDataDir='./userdata', args=['--disable-infobars',f'--window-size={width},{height}'])#用户数据持久化,保存cookie,数据将存在userdata里,设置页面大小
    context=await browser.createIncogniteBrowserContext()      #无痕浏览设置
    page = await browser.newPage()
    await page.setViewport({'width':width,'height':height})      #执行页面大小
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(10)
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://dynamic1.scrape.cuiqingcai.com/')
    await page.goto('https://spa2.scrape.center/')
    # 后退
    await page.goBack()
    # 前进
    await page.goForward()
    # 刷新
    await page.reload()
    # 保存 PDF
    await page.pdf()
    # 截图
    await page.screenshot()
    # 设置页面 HTML
    await page.setContent('<h2>Hello World</h2>')
    # 设置 User-Agent
    await page.setUserAgent('Python')
    # 设置 Headers
    await page.setExtraHTTPHeaders(headers={})
    # 关闭
    await page.close()
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())

'''------------------------------------------多线程和多进程-----------------------------------------------------------------------'''
#多线程
from threading import Thread      #线程类
def hello():
    for i in range(10,1000,10):
        print("hello",i)

if __name__ == '__main__':
    t=Thread(target=hello)       #创建线程并安排任务
    t.start()         #多线程状态为可以开始工作状态，具体的执行时间由CPU决定
    for i in range(5,500,15):
        print("hi",i)


from threading import Thread  #线程类
class Thread1(Thread):
    def hello():
        for i in range(10,1000,10):
            print("hello",i)
    def start(self):
        st=Thread(target=Thread1.hello)
        st.start()
if __name__ == '__main__':
    t=Thread1()     #创建线程并安排任务
    t.start()         #多线程状态为可以开始工作状态，具体的执行时间由CPU决定
    for i in range(5, 500, 15):
        print("fun", i)
'''-------------------------------------多进程-----------------------------'''







'''------------------------------------------------------异步爬虫----------------------------------------------------------------'''
# event_loop:事件循环
# coroutine 协程
# task 任务
# future 代表将来执行或者没有执行的任务的结果 实际跟task没有区别
import asyncio
async def execute(x):
    print('number:',x)
coroutine=execute(1)
print('Coroutine:',coroutine)
print('After calling execute')
loop=asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print("after calling loop")
'''---------------------------------多任务协程---------------------------'''
import asyncio
import requests
async def request():
    url='https://www.baidu.com'
    status=requests.get(url)
    return status
tasks=[asyncio.ensure_future(request()) for _ in range(5)]    #相当于把任务传入赋值
print('tasks',tasks)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))            #执行任务，流程从新从上面执行下去
for task in tasks:
    print('task retult',task.result())
#输出结果
# tasks [<Task pending name='Task-1' coro=<request() running at C:\Users\LUCK\PycharmProjects\pythonProject\数据存储\线程和进程.py:4>>, <Task pending name='Task-2' coro=<request() running at C:\Users\LUCK\PycharmProjects\pythonProject\数据存储\线程和进程.py:4>>, <Task pending name='Task-3' coro=<request() running at C:\Users\LUCK\PycharmProjects\pythonProject\数据存储\线程和进程.py:4>>, <Task pending name='Task-4' coro=<request() running at C:\Users\LUCK\PycharmProjects\pythonProject\数据存储\线程和进程.py:4>>, <Task pending name='Task-5' coro=<request() running at C:\Users\LUCK\PycharmProjects\pythonProject\数据存储\线程和进程.py:4>>]
# task retult <Response [200]>
# task retult <Response [200]>
# task retult <Response [200]>
# task retult <Response [200]>
# task retult <Response [200]>

'''-----------------aiohttp异步请求的库------------------'''
import asyncio
import aiohttp
import time
start = time.time()
async def get(url):
    session = aiohttp.ClientSession()     #调用方法
    response = await session.get(url)
    await response.text()
    await session.close()
    return response
async def request():
    url = 'https://www.httpbin.org/delay/5'    #此页面会等待5秒
    print('Waiting for', url)
    response = await get(url)
    print('得到的回应', url, 'response', response)
tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('Cost time:', end - start)

#高并发
import time
import asyncio
import aiohttp
def test(number):
    start=time.time()
    async def get(url):
        session=aiohttp.ClientSession()
        response=await session.get(url)
        await response.text()
        await session.close()
        return response
    async def request():
        url='https://www.baidu.com/'
        await get(url)
    tasks=[asyncio.ensure_future(request()) for _ in range(number)]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end=time.time()
    print('number',number,'cost time',end-start)
for number in [1,3,5,10,15,30,50,75,100,200,500]:
    test(number)


import aiohttp
import asyncio
async def main():
   data = {'name': 'germey', 'age': 25}
   async with aiohttp.ClientSession() as session:
       async with session.post('https://httpbin.org/post', data=data) as response:
           print(await response.text())
if __name__ == '__main__':
   asyncio.get_event_loop().run_until_complete(main())


import aiohttp
import asyncio
async def main():
   timeout = aiohttp.ClientTimeout(total=5)   #5秒超时异常
   async with aiohttp.ClientSession(timeout=timeout) as session:
       async with session.get('https://httpbin.org/get') as response:
           print('status:', response.status)
if __name__ == '__main__':
   asyncio.get_event_loop().run_until_complete(main())


import asyncio
import aiohttp
CONCURRENCY = 10        #最大的并发量设置为5
URL = 'https://www.baidu.com'
semaphore = asyncio.Semaphore(CONCURRENCY)    #Semaphore信号量对象
session = None
async def scrape_api():
   async with semaphore:
       print('scraping', URL)
       async with session.get(URL) as response:
           await asyncio.sleep(5)                 #爬取速度
           return await response.text()
async def main():
   global session
   session = aiohttp.ClientSession()
   scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
   await asyncio.gather(*scrape_index_tasks)            #gather方法运行
if __name__ == '__main__':
   asyncio.get_event_loop().run_until_complete(main())


'''----------------------------------------------代理的使用-----------------------------------------------------------------------'''








'''-----------------------------------------------模拟登录-----------基于传统MVC-------------------------------------------------------------'''
import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL, data={
   'username': USERNAME,
   'password': PASSWORD
}, allow_redirects=False)   #requests 可以自动处理重定向，所以模拟登录的过程我们要加上 allow_redirects 参数并设置为 False，使其不自动处理重定向

cookies = response_login.cookies
print('Cookies', cookies)

response_index = requests.get(INDEX_URL, cookies=cookies)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)


import requests
from urllib.parse import urljoin
BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'
session = requests.Session()
response_login = session.post(LOGIN_URL, data={
   'username': USERNAME,
   'password': PASSWORD
})
cookies = session.cookies
print('Cookies', cookies)
response_index = session.get(INDEX_URL)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)

'''------用selenium-------'''
from urllib.parse import urljoin
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'
browser = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")
browser.get(BASE_URL)
browser.find_element(By,value='input[name="username"]').send_keys('admin')
browser.find_element(By,value='input[name="password"]').send_keys('admin')
browser.find_element(By,value='input[type="submit"]').click()
time.sleep(10)
# get cookies from selenium
cookies = browser.get_cookies()
print('Cookies', cookies)
browser.close()
# set cookies to requests
session = requests.Session()
for cookie in cookies:
   session.cookies.set(cookie['name'], cookie['value'])
response_index = session.get(INDEX_URL)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)


'''-------基于JWT   前后端分离-----------'''
import requests
from urllib.parse import urljoin
BASE_URL = 'https://login3.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/api/login')
INDEX_URL = urljoin(BASE_URL, '/api/book')
USERNAME = 'admin'
PASSWORD = 'admin'
response_login = requests.post(LOGIN_URL, json={
   'username': USERNAME,
   'password': PASSWORD
})
data = response_login.json()
print('Response JSON', data)
jwt = data.get('token')
print('JWT', jwt)
headers = {
   'Authorization': f'jwt {jwt}'
}
response_index = requests.get(INDEX_URL, params={
   'limit': 18,
   'offset': 0
}, headers=headers)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
print('Response Data', response_index.json())



'''------------------------------------------------------scrapy--------------------------------------------------------------------'''
'''灵活好用的scrapy
scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html'''
















