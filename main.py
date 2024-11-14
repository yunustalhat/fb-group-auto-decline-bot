from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to your Firefox profile here
# Replace with the correct path to your Firefox profile
# Example: profile_path = "/path/to/your/firefox/profile"
profile_path = "/home/yunustalha/.mozilla/firefox/fencdxqs.default-release"  # CHANGE THIS

firefox_profile = webdriver.FirefoxProfile(profile_path)

# Options for headless mode in Firefox
options = webdriver.FirefoxOptions()
options.profile = firefox_profile
options.add_argument('--headless')

# Launch Firefox browser with specified options
driver = webdriver.Firefox(options=options)

# Go to the Facebook group page
# Replace the URL with the URL of the Facebook group you want to target
# Example: driver.get("https://www.facebook.com/groups/your-group-id")
print("Navigating to the Facebook group page...")
driver.get("https://www.facebook.com/groups/1137538949694725/spam")  # CHANGE THIS
time.sleep(5)  # Short wait for the page to load

# Variables to track the number of rejections and errors
rejected_count = 0
consecutive_errors = 0  # Counter for consecutive errors
connection_error_count = 0  # Counter for internet connection errors

while True:
    try:
        # Find all the "Decline" buttons
        # If the button text changes, replace 'Decline' with the correct text
        reject_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[text()='Decline']"))  # CHANGE 'Decline' if needed
        )
        
        # If only one button is left and it is not active, skip the rejection process
        if len(reject_buttons) <= 1:
            print("No more posts to decline, checking again in 5 minutes...")
            time.sleep(300)  # Wait for 5 minutes
            driver.refresh()  # Refresh the page
            continue  # Check again
        
        # Click the "Decline" buttons
        for button in reject_buttons:
            try:
                # Click using JavaScript
                driver.execute_script("arguments[0].click();", button)
                rejected_count += 1
                print(f"Post #{rejected_count} rejected.")
                time.sleep(1)  # Short wait between rejections
                consecutive_errors = 0  # Reset consecutive error counter
                connection_error_count = 0  # Reset connection error counter
            except Exception as e:
                print(f"Rejection failed: {e}")
                continue

        # Scroll slightly to load more posts
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 500);")  # Scroll by a small amount

    except TimeoutError:
        # Internet connection issue
        print("Connection error. Trying again...")
        connection_error_count += 1
        if connection_error_count >= 3:
            print("Encountered 3 consecutive connection errors, stopping the program.")
            break
        time.sleep(10)  # Wait before trying again
        driver.refresh()  # Refresh the page and try again

    except Exception as e:
        consecutive_errors += 1  # Increment consecutive error counter
        if consecutive_errors >= 3:
            print("Encountered 3 consecutive errors, stopping the program.")
            break
        time.sleep(10)  # Wait before trying again
        driver.refresh()  # Refresh the page and try again

# Close the browser when done
driver.quit()
