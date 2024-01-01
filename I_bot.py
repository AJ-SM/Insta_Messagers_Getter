import urllib3 
from xml.dom.minidom import Element
import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
driver = webdriver.Firefox()


Name = str(input("Please Enter YOur Insta Id : "))
Password= str(input("Please Enter YOur Insta Id : "))



print('')
print('')
print('')
print('')
print('Slepping 2 min ')
sleep(120)


Meassger = []



print("  ")

print("  ")
print("  ")
print("  ")

print('Initiating_Instagram_...')
driver.get("https://www.instagram.com/")
print("  ")
print("  ")
print("  ")
print("  ")


sleep(15)
driver.find_element("css selector",'div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)').send_keys(Name)
sleep(4)
driver.find_element("css selector","div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys(Password)
sleep(4)
print('Logged_In_Sucessfull_as' + '' + Name)
print("  ")
print("  ")
print("  ")
print("  ")

driver.find_element("xpath","/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
print('Grabbing_up_Messages......')
print("  ")
print("  ")
print("  ")

sleep(15)
driver.get("https://www.instagram.com/direct/inbox/")
sleep(15)

driver.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
sleep(15)
final = driver.page_source
done =  BeautifulSoup(   final.encode("utf-8")  ,  features="html5lib") 

name1 = done.find_all('div',{"class":"_aacl _aaco _aacu _aacx _aada"})


for itemos in name1:
    people = itemos.get_text()
    Meassger.append(people)

print("_______________________")
print("  ")
print("  ")
print("  ")


dope = []
for item in Meassger:
    if item not in dope:
        dope.append(item)

print ("Messangers") 
print("  ")
print("  ")
print("  ")
print("  ")

for i in dope:

    print("---" + " " + i)

sleep(10)
driver.close()
driver.get("https://www.instagram.com/#")