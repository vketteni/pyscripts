from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (make sure to choose the one that matches your browser)
driver = webdriver.Chrome()

# Open the target webpage
driver.get("URL_OF_THE_PAGE")

# Wait for the calendar to load
wait = WebDriverWait(driver, 10)
calendar_loaded = wait.until(EC.presence_of_element_located((By.ID, "ID_OF_CALENDAR_ELEMENT")))

# Find all available slots
available_slots = driver.find_elements_by_css_selector(".class_of_available_slots")

# Check if there are any available slots
if available_slots:
    for slot in available_slots:
        # Extract the date and time from the slot element
        date_time = slot.get_attribute("data-date-time-attribute")
        print(f"Available slot found: {date_time}")
else:
    print("No available slots found.")

# Close the browser
driver.quit()
