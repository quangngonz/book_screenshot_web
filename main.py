from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os
from dotenv import load_dotenv
load_dotenv()

# Configure the browser options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode, without a GUI
options.add_argument("--start-maximized")  # Start browser maximized
options.add_argument("--force-device-scale-factor=2")  # Increase pixel density

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

def set_high_res():
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 3840,
        "height": 2160,
        "deviceScaleFactor": 3,  # Simulates a high DPI screen
        "mobile": True
    })
    driver.execute_cdp_cmd("Emulation.setTouchEmulationEnabled", {
        "enabled": False
    })
    print("High resolution set.")

def login_and_screenshot(url, username, password):
    driver.get(url)
    print(f"Opened the URL: {url}")

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

    # Wait for the page to load with a visible countdown timer
    for i in range(10, 0, -1):
        print(f"Waiting for the page to load: {i} seconds remaining", end="\r")
        time.sleep(1)
    print("Page loaded.                                                ")

def click_next_page():
    # Wait for the button to be present (if needed)
    time.sleep(2)  # Replace with WebDriverWait if page load times vary

    iframe = driver.find_element(By.ID, "mainFrame")
    driver.switch_to.frame(iframe)
    print("Switched to iframe.")

    # Click using data attribute (recommended)
    button = driver.find_element(By.CSS_SELECTOR, '[data-nav-name="go-right"]').click()
    time.sleep(5)  # Allow time for smooth scrolling

    print("Clicked Next Page button.")

    # Switch back to the main page after interacting
    driver.switch_to.default_content()
    print("Switched back to main content.")

def screenshot(screenshot_path):
    set_high_res()
    # refresh the page
    driver.refresh()
    time.sleep(5)  

    # Take a screenshot
    driver.save_screenshot(f'/screenshot/{screenshot_path}')
    print(f"Screenshot saved to {screenshot_path}")

    click_next_page()
    driver.save_screenshot("/screenshot/screenshot2.png")
    print("Screenshot saved to screenshot2.png")

    input("Press Enter to close the browser...")

# Example usage
login_and_screenshot(
    url="https://cgpbooks.co.uk/extras",
    username=os.getenv("EMAIL"),
    password=os.getenv("PASSWORD"),
)

screenshot("screenshot.png")
