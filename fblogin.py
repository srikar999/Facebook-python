from selenium import webdriver


usr= input("Username=")
passs=input("pass=")

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

usernamebox=driver.find_element_by_id("email")
usernamebox.send_keys(usr)

passwordbox=driver.find_element_by_id("pass")
passwordbox.send_keys(passs)

login_btn=driver.find_element_by_id("u_0_3")
login_btn.submit()