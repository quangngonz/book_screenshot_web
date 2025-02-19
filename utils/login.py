from selenium.webdriver.common.by import By
from utils.pause import pause

def login(driver, url, username, password):
    driver.get(url)
    print(f"Opened the URL: {url}")
    try:
        driver.find_element(By.ID, 'p_lt_ctl04_CookieMessage_lnkClose').click()
    except:
        pass

    #Click on element with id=signin
    driver.find_element(By.ID, "signin").click()
    
    # Find and fill the username field with id p_lt_Body_lt_ctl01_Login_Login1_UserName
    driver.find_element(By.ID, "p_lt_Body_lt_ctl01_Login_Login1_UserName").send_keys(username)
    
    # Find and fill the password field
    driver.find_element(By.ID, "p_lt_Body_lt_ctl01_Login_Login1_Password").send_keys(password)
    
    # Submit the form by clicking the submit button
    driver.find_element(By.ID, "p_lt_Body_lt_ctl01_Login_Login1_LoginButton").click()

    # Select image with title
    driver.find_element(By.ID, "p_lt_Body_lt_ctl00_MyProductList_rptProducts_ctl01_ucProductSummary_btnProductLinkMain").click()

    pause(5, "Logged in successfully.")
