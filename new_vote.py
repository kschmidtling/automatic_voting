from selenium import webdriver
import os
import time
starttime = time.time()
gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver')) #Not sure if this even does anything

num = 1 #Track the amount of times we've voted per session
total_votes = 0 #Track total votes across all sessions
total_exceptions = 0 #Track the number of errors that we get

#driver = webdriver.Chrome(executable_path='C:\\Users\pvz6qwx\\Desktop\\chromedriver.exe')

browser = webdriver.Chrome() #Create the initial instance of our browser.
while num < 30:
	browser.get('https://www.vype.com/top-vype-san-antonio-running-back-recruit')
	#time.sleep(1)
	try:
		elementone = browser.find_element_by_id("PDI_answer48782186") # the id for the vote option (select it)
		elementone.click()
		#time.sleep(.5)
		elementtwo = browser.find_element_by_id("pd-vote-button10538324") # submit our vote with our vote option
		elementtwo.click()
		num += 1
		total_votes += 1
		time.sleep(1)
		print(f'Total Votes: {total_votes}')
	except:
		print('exception occured')
		total_exceptions += 1
		time.sleep(2)
		print(f'Total Exceptions: {total_exceptions}')
		pass
	if num == 22:					# reset the counter so that we dont get locked out
		browser.close()
		time.sleep(61) # pause to make the website forget us
		print(f'elapsed time: {time.time() - starttime}')
		browser = webdriver.Chrome() # re-initialize the browser for the next use
		num = 0 # reset the instance
		print(f'currently at {total_votes / (starttime - time.time())} votes per time')


# we have reached ip limit so close program
browser.close()
exit()

