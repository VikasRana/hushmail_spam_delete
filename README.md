Here is the fast version of this script, which doesn't involve opening of indivial emails for deletion. This here checks all the spams and deletes them all together, thus also saving bandwidth along with time. Go here, https://github.com/VikasRana/hushmail_spam_delete_fast_version


# hushmail_spam_delete
A simple Python script that uses Selenium WEBDriver to delete the spams from Hushmail.com Inbox

You all know how Hushmail manages our spam reports against emails. We continously see spam mails getting landing in our inboxes. For this, I've designed this simple script so that I can go and make myself a cup of coffee while the script does it's job.

This script uses Selenium WEBDriver. And it can be installed easily, pip install selenium -U

You need to change certain field before you can run the script.

In line 11, usr = '' ; put your email id within quotes

In line 12, pss = '' ; put your password within quotes

In line 40, assert assert_string2.text == 'YOUR_USER_THAT_YOU_SEE_ON_THE_TOP_RIGHT_OF_THE_PAGE'; put your username in quotes that you see on the top right of the page in BOLD

In line 47, spam = ["", ""]; add spammers here within double quotes

To run the script: python hush_spam_delete.py
