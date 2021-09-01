# 2021/08/26 Day 01 Project no - 01
import time
from selenium import webdriver


PATH = 'C:\\Users\\BAKUL\\PycharmProjects\\QUPS_Day01\\drivers\\chromedriver92.exe'  # use \\, otherwise path not work
driver = webdriver.Chrome(PATH)
driver.maximize_window()    # for maximize browser
driver.implicitly_wait(3)

link = 'http://evaly.com.bd'
driver.get(link)
print("\nOur tasting site name is -\n\t\t", driver.title)


# start 1at task - log in
driver.find_element_by_css_selector('button.absolute').click()  # remove add
driver.find_element_by_css_selector('button.flex span span.p-2').click()  # for login
driver.find_element_by_name('phone').send_keys('01558960437')
driver.find_element_by_name('password').send_keys('@01558960437')
driver.find_element_by_class_name('btn').click()
driver.find_element_by_css_selector('div.bg-white img.UserAvator___StyledImg-sc-1f5qhvl-1').click()
time.sleep(2)  # for wait 2 second
# end 1at task - log in

# start 2nd task - print Speaker brand items name
driver.refresh()
driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/button').click()  # cookies 'I understand' button
driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/div[1]/div/div[1]/div/ul/li[9]/a').click()  # Speaker button

# create an item list, print items name in terminal
brand_items = driver.find_elements_by_xpath('//div[@id="__next"]/div/div[3]/div/div[2]/div/div/div/a')
print("We found", len(brand_items), "Speaker Brands.")
for item in brand_items:
    print("\t", item.text)

# code for MI brand items
driver.find_element_by_xpath('//div[@id="__next"]/div/div[3]/div/div[2]/div/div/div/a').click()  # clck mi brand item
mi_brand_items = driver.find_elements_by_xpath('//div[@id="__next"]/div/div[3]/div/div[3]/a/div/div[3]/p')
price_list = []  # price list
print("We found", len(mi_brand_items), "MI Speaker Brands and items price are here:")
for item in mi_brand_items:
    print("\t", item.text)
    price_list.append(item.text)


price_list.sort()  # high print
print("The high price is:", price_list[0])
price_list.reverse()  # low print
print("The low price is:", price_list[0])
time.sleep(2)
# end 2nd task - print Speaker brand items name


# start 3rd task - check domain name in Career
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # for scroll down
driver.find_element_by_xpath('//div[@id="__next"]/div/div[6]/div/div/div[2]/ul/li[5]/a').click()  # click career button

domain_name = "career@evaly.com.bd"
print("We will check the domain (", domain_name, ") in our all Career items.")

# count_career_name - this variable is only for For Loop
count_career_name = driver.find_elements_by_xpath('//div[@id="__next"]/div/div[3]/div/div[2]/div/div/div/h3')
n = 1
for a in count_career_name:
    driver.find_element_by_xpath('//div[@id="__next"]/div/div[3]/div/div[2]/div/div[%s]/div/h3'%n).click()  # open career item
    career_name = driver.find_element_by_xpath('//div[@id="__next"]/div/div[3]/div/div[2]/div/div[%s]/div/h3'%n)  # career item name
    career_details = driver.find_element_by_xpath('//div[@id="__next"]/div/div[3]/div/div[2]/div/div[%s]/div[2]/p/a'%n)  # career item domain
    print("\t", career_name.text)  # print Career title
    if domain_name in career_details.text:  # checking domain
        print("\t\tSuccessfully, found", domain_name, "in", career_name.text)
    else:
        print("\t\tNot found")
    driver.find_element_by_xpath('//div[@id="__next"]/div/div[3]/div/div[2]/div/div[%s]/div/h3'%n).click()  # close career item
    n += 1

# end 3rd task - check domain name in Career


time.sleep(2)
driver.quit()
