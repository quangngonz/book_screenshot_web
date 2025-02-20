from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import os, filecmp
from utils.pause import pause
from utils.login import login
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
        "deviceScaleFactor": 2, 
        "mobile": False
    })
    print("High resolution set.")

login(driver, os.getenv("URL"), os.getenv("EMAIL"), os.getenv("PASSWORD"))

def take_screenshot(screenshot_path, index):
    # Click on the "Zoom In" button
    zoom_in_button = driver.find_element(By.CSS_SELECTOR, "button:nth-of-type(4) path")
    ActionChains(driver).move_to_element(zoom_in_button).click().perform()
    pause(1, "zoom in button")  # Wait for the action to complete

    #Double-click on the "minus" span (zoom out) 4 times
    minus_span = driver.find_element(By.CSS_SELECTOR, "span.minus")
    for i in range(3):
        ActionChains(driver).move_to_element(minus_span).click().perform()
        # pause(1, "minus span")  # Wait for the action to complete

    #Remove the "Zoom Panel" element
    #Hide the "Zoom Panel" element by setting display: none
    script_hide = """
    var element = document.querySelector('.zoom-panel');
    if (element) {
        element.style.display = 'none';
    }
    """
    driver.execute_script(script_hide)
    # pause(1, "hide panel")  # Pause for 5 seconds to observe the change

    # Step 2: Take a screenshot of the page
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved as {screenshot_path}")

    # Step 3: Restore the "Zoom Panel" element by setting display back to normal
    script_restore = """
    var element = document.querySelector('.zoom-panel');
    if (element) {
        element.style.display = '';
    }
    """
    driver.execute_script(script_restore)
    # pause(1, "show panel")  # Pause for 5 seconds to observe the change

    if index == 0:
        next_page_button = driver.find_element(By.CSS_SELECTOR, "div.nav-arrows path")
        ActionChains(driver).move_to_element(next_page_button).click().perform()
    else:
        next_page_button = driver.find_element(By.CSS_SELECTOR, "button.nav-right-arrow path")
        ActionChains(driver).move_to_element(next_page_button).click().perform()
    pause(1, 'next page')  # Wait for the action to complete

# refresh the page
driver.refresh()
pause(5, 'refresh page')  


iframe = driver.find_element(By.ID, "mainFrame")
driver.switch_to.frame(iframe)
print("Switched to iframe.")

set_high_res()

index = 0 

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Clear contents of the screenshots folder

for file in os.listdir("screenshots"):
    os.remove(f"screenshots/{file}")

while True:
    take_screenshot(f"screenshot_{index}.png", index)

    # Compare both files to check if they are the same
    # If they are the same, break the loop
    if index > 0:
        previous_file = f"screenshots/screenshot_{index - 1}.png"
        current_file = f"screenshot_{index}.png"
        if filecmp.cmp(previous_file, current_file, shallow=False):
            print("The screenshots are the same.")
            break

    if index == 300:
        break

    os.rename(f"screenshot_{index}.png", f"screenshots/screenshot_{index}.png")

    index += 1

input("Press Enter to close the browser...")
