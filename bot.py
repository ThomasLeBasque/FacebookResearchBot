#!/usr/bin/env python2.7
from selenium import webdriver
import selenium
from PIL import Image
from unidecode import unidecode
import urllib
import time
import sys

####################	DEFINITION DES FONCTIONS	#######################

#Login into facebook
def fb_login():
	print ("\nWriting email...")
	user=browser.find_element_by_name("email")
	user.send_keys("#PUT YOUR EMAIL ADRESS HERE#")
	#...
	print ("Writing password...")
	pwd=browser.find_element_by_name("pass")
	pwd.send_keys("#PUT YOUR EMAIL ADRESS HERE#")
	#...
	print ("Clicking LogIn button...")
	login=browser.find_element_by_xpath("//input[@value='Connexion']")
	login.click()
	time.sleep(3)
	#...
	connection_test(browser)
	
#get an element to see if the connection is done
def connection_test(browser):
	try:
		home = browser.find_element_by_class_name("_2md")
	except:
		print("Facebook connection error")
		time.sleep(5)
		exit()


#Search for someone with two different mehods
#	1_ write the nale directly on the URL
#	2_ use the search section in facebook
def search_name (browser, name_index, firstname, lastname):
	print ("\nSearching for your name...")

	#First research method
	if name_index == -1:
		print ("First method : getting directly the URL...")
		browser.get("https://facebook.com/" + ".".join((firstname, lastname)))
		time.sleep(1)
		#...

	#Second research method
	else:
		print ("Second method : using searching section into Facebook...")
		browser.get("https://www.facebook.com/search/people/?q=" + firstname + "%20" + lastname)
		time.sleep(1)
		#...

		print ("Getting result list... clicking on the number : " + str(name_index))
		user = browser.find_elements_by_class_name("_32mo")[name_index]
		browser.get(user.get_attribute("href"))
		time.sleep(2)
		#...

#Download the prifile picture of the founded person
#if nothing found, it cetrainely is because the person doesn't exist
def download_profile_img(browser):
	print ("\nGetting profile picture...\n")
	try :
		img = browser.find_element_by_class_name("profilePic")
		src = img.get_attribute("src")
		urllib.urlretrieve(src, "./output/capture.png")
		Image.open("./output/capture.png").show()
	except :
		print ("Image download problem !!!")
		
#Ask if it's the right person or not
#	if yes, stop into this person profile
#	if not, continue searching
def is_it_you_question():
	while 1:
		in_put = raw_input("\nIs it you ? (yes or no)\t")
		if in_put == "yes":
			return 1
		elif in_put == "no":
			return 0
		else:
			continue

#Getting person informations
def get_person_infos(browser, name):
	print ("\nGetting your infos...")
	about = browser.find_element_by_xpath("//a[@data-tab-key='about']")
	about.click()
	time.sleep(1)
	#...

	text = name
	text += '\n'
	try:
		get_list1 = browser.find_elements_by_class_name("_5yql")
		for element in get_list1:
			print (element.text)
			text += element.text
			text += '\n'
	except:
		print ("No information found on you 1 ")

	try:
		get_list2 = browser.find_elements_by_class_name("_1pi3")
		for e in get_list2:
			print (e.text)
			text += e.text
			text += '\n'
	except:
		print ("No information found on you 2 ")

	#Gestion des sons impronnoncables par la voix de sophia
	text.replace(".", "!")
	text.replace("ESIEA", "euhessieuhah")

	with open("./output/output.txt", "wb") as file:
		file.write(unidecode(text))


####################	MAIN	#######################

print ("\r\nSTARTING...\r\n")
start_time=time.time()

#GETTING PEOPLE NAME IN CONSOLE
firstname = raw_input("Give me your first name:\t")
lastname = raw_input("Give me your last name:\t\t")
name = " ".join((firstname, lastname))
print ("Your name is " + name)


print ("\r\nOpenning WebPage...")
fp = webdriver.FirefoxProfile("./profile")
browser = webdriver.Firefox(firefox_profile=fp)
print ("Oppening facebook.com")
browser.get("https://facebook.com")

#Fonction to login on Facebook
print ("\nConnecting to Facebook")
fb_login()
print ("Facebook connection done...")
time.sleep(3)
#...

#Fonction to find someone
is_it_you = 0
name_index = -1

while is_it_you == 0:
	search_name(browser, name_index, firstname, lastname)
	download_profile_img(browser)
	is_it_you = is_it_you_question()
	name_index += 1

get_person_infos(browser, name)

browser.close()
print ("---%s seconds ---" % (time.time() - start_time))
