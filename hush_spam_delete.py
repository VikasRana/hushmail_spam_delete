# Automatically deletes Hushmail's Spam emails from the Inbox

import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
usr = ''
pss = ''


driver = webdriver.Chrome("C:/Users/home/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)
driver.get("https://www.hushmail.com/")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='navbar']/ul[2]/li[4]/a").click();
time.sleep(5)
assert_string = driver.find_element_by_xpath("//*[@id='username-container']/div[2]/em");
assert assert_string.text == 'jane@hushmail.com';
time.sleep(1)


driver.find_element_by_xpath("//*[@id='hush_username']").click();
driver.find_element_by_xpath("//*[@id='hush_username']").send_keys(usr);
time.sleep(0.2)


driver.find_element_by_xpath("//*[@id='hush_passphrase']").click();
driver.find_element_by_xpath("//*[@id='hush_passphrase']").send_keys(pss);
time.sleep(0.2)


driver.find_element_by_xpath("//*[@id='submit-container']/input").click();
time.sleep(10)


assert_string2 = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[1]/span[1]/span");
assert assert_string2.text == 'YOUR_USER_THAT_YOU_SEE_ON_THE_TOP_RIGHT_OF_THE_PAGE';
time.sleep(15)


# the_entries_need_to_match_exactly_how_they_look
# if_we_want_to_mark_this_sender_as_spam_https://i.imgur.com/b0Nht13.png_we_will_put_BookMyShow_and_not_bookmyshow_or_something_else
# so_the_field_is_case_sensitive_and_the_whitespaces_are_to_be_kept_in_mind
spam = ["aaaaa", "bbbbb"]; # customize_this_field_according_to_your_need


print("Press Ctrl+C to interrupt\n")


def try_spam():
	for i in spam[0:]:
	    try:
	    	driver.find_element_by_link_text(i).click();
	    	print("Detected spam by:", i)
	    	time.sleep(5)
	    	print("Deleting...")
	    	driver.find_element_by_xpath("//*[@id='message']/div[1]/div/div[5]/input[1]").click();
	    	time.sleep(0.1)
	    	driver.find_element_by_xpath("/html/body/div/div[3]/div[11]/div/div[3]/div[3]/form/div[2]/input").click();
	    	time.sleep(1)
	    	driver.get("https://secure.hushmail.com/1.1.5/preview/hushmail/bassiq@hushmail.com/folder/Inbox");
	    	time.sleep(10)
	    except NoSuchElementException as e:
	    	continue
	    try_spam()
try_spam()


print("All work done\n")
time.sleep(2)


def usr_inp():
	usr_inpt = input("Would you want me to delete the spam(s) from trash? Type only yes or no: ")
	if usr_inpt == 'yes':
	    print("Deleting spam(s) permanently from your trash. WIN users --> Ctrl+C to interrupt if gave a yes command by mistake.")
	    time.sleep(10)
	    driver.get("https://secure.hushmail.com/preview/hushmail/#folder/Trash")
	    time.sleep(10)
	    driver.find_element_by_xpath("//*[@id='element_message-list-toolbar']/div/div[6]/input").click();
	    time.sleep(1)
	    driver.find_element_by_xpath("//*[@id='element_delete-message-dialog-template']/div/div[3]/div[3]/form/div[2]/input").click();
	    time.sleep(3)
	    driver.get("https://secure.hushmail.com/1.1.5/preview/hushmail/bassiq@hushmail.com/folder/Inbox");
	elif usr_inpt == 'no':
		print("Thank you for using my service.")
	else:
		print("Type only yes or no.\n")
		usr_inp()
		time.sleep(5)
usr_inp()
