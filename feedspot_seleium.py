from selenium import webdriver
import time
import csv

# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome()
# Go to the page that we want to scrape
driver.get("https://blog.feedspot.com/usa_news_websites/")

#close the pop up 
time.sleep(2)
close_button = driver.find_element_by_xpath('//*[@id="wp_subscribe_popup"]/button')
close_button.click()
time.sleep(2)


csvfile = open('feedspot_data.csv', 'w', encoding='utf-8')
writer = csv.DictWriter(csvfile,fieldnames=['title','info', 'frequency number', 'frequency period', 'facebook fans', 'twitter followers'])
writer.writeheader()

infos = driver.find_elements_by_xpath('//p[@class="trow trow-wrap"]')
titles = driver.find_elements_by_xpath('//h3/a')

for i,info in enumerate(infos):
	# print('\n\n info list: \n{}\n\n'.format(info.text))
	# print('\n\n info len: \n{}\n\n'.format(len(info.text.split('\n'))))
	
	#split info

	# rawfrequency = info.text[info.text.find('\nFrequency ')+11:info.text.find('\nWebsite')-1] #careful with variable name
	rawfrequency = info.text[info.text.find('\nFrequency ')+11:info.text.find('.',info.text.find('Frequency ')+11)]
	freqnumber = rawfrequency.split()[1]
	freqperiod = rawfrequency.split()[-1]

	facebookrawnum = info.text[info.text.find('\nFacebook fans ')+14:info.text.find('. Twitter followers')-1]
	facebooknum = facebookrawnum.replace(',', '')

	twitterrawnum = info.text[info.text.find('Twitter followers ')+18:info.text.find('.',info.text.find('Twitter followers ')+18)]
	twitternum = twitterrawnum.replace(',', '')


	writer.writerow({
						'title':titles[i].text,
						'info':info.text,
						'frequency number':freqnumber,
						'frequency period':freqperiod,
						'facebook fans':facebooknum,
						'twitter followers':twitternum


						#'about':info.text.split('\n')[0],
						# 'frequency':info[1],
						# 'website': info[2],
						# 'popularity': info[3]
					})


		# for title in titles:
		# 	print(title.text)

	# 	print(infos[0].text.split('\n'))
	# 	print(infos[1])

	# 	for info in infos:
	# 		print(info.text)



csvfile.close()
driver.close()

