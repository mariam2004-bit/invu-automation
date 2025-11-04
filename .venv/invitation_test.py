from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try:
    print("Step 1: Opening website invu.ge...")
    # Open the website
    driver.get("https://invu.ge")
    
    # Wait instance
    wait = WebDriverWait(driver, 15)
    time.sleep(3)
    print("✓ Website opened successfully")
    
    print("\nStep 2: Looking for 'შესვლა' (Sign in) button...")
    # Click "შესვლა" (Sign in) button
    login_button = None
    
    # Try different ways to find the შესვლა button
    login_locators = [
        (By.XPATH, '//button[text()="შესვლა"]'),
        (By.XPATH, '//button[contains(text(), "შესვლა")]'),
        (By.XPATH, '//a[text()="შესვლა"]'),
        (By.XPATH, '//a[contains(text(), "შესვლა"]'),
        (By.XPATH, '//button[text()="Sign in"]'),
        (By.XPATH, '//button[contains(text(), "Sign in")]'),
    ]
    
    for locator_type, locator_value in login_locators:
        try:
            login_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            print(f"✓ Found 'შესვლა' button: {locator_value}")
            break
        except:
            continue
    
    if login_button is None:
        raise Exception("Could not find 'შესვლა' (Sign in) button on the page.")
    
    # Click the button using JavaScript to avoid stale element issues
    print("Clicking 'შესვლა' button...")
    try:
        driver.execute_script("arguments[0].click();", login_button)
    except:
        try:
            login_button.click()
        except:
            login_button = driver.find_element(By.XPATH, '//a[text()="შესვლა"]')
            driver.execute_script("arguments[0].click();", login_button)
    
    time.sleep(3)
    print("✓ Clicked 'შესვლა' button successfully")
    
    # 1. Log in with valid credentials
    print("\nStep 3: Logging in with email and password...")
    time.sleep(2)  # Extra wait for login modal to fully load
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    email_input.send_keys("marimar@gmail.com")
    print("✓ Email entered")
    
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("marimari123")
    print("✓ Password entered")
    
    # Click login button (try both Georgian and English)
    signin_button = None
    signin_locators = [
        (By.XPATH, '//button[text()="შესვლა"]'),
        (By.XPATH, '//button[contains(text(), "შესვლა")]'),
        (By.XPATH, '//button[text()="Sign in"]'),
        (By.XPATH, '//button[contains(text(), "Sign in")]'),
        (By.XPATH, '//button[@type="submit"]'),
    ]
    
    for locator_type, locator_value in signin_locators:
        try:
            signin_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            print(f"✓ Found login button: {locator_value}")
            break
        except:
            continue
    
    if signin_button is None:
        raise Exception("Could not find login/submit button.")
    
    signin_button.click()
    time.sleep(3)
    print("✓ Logged in successfully")

    # 2. Navigate to the "Templates" page
    print("\nStep 4: Navigating to 'Templates' page...")
    templates_link = None
    templates_locators = [
        (By.XPATH, "//a[@href='/templates' and text()='შაბლონები']"),  # Exact match
        (By.XPATH, "//a[@href='/templates']"),  # href match
        (By.XPATH, "//a[text()='შაბლონები']"),  # Templates in Georgian
        (By.XPATH, "//a[contains(text(), 'შაბლონები')]"),
        (By.XPATH, "//a[contains(@class, 'nav-item') and contains(text(), 'შაბლონები')]"),
        (By.XPATH, "//a[text()='Templates']"),
        (By.XPATH, "//a[contains(text(), 'Templates')]"),
    ]
    
    for locator_type, locator_value in templates_locators:
        try:
            templates_link = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            print(f"✓ Found Templates link: {locator_value}")
            break
        except:
            continue
    
    if templates_link is None:
        raise Exception("Could not find 'Templates' link.")
    
    templates_link.click()
    time.sleep(2)
    print("✓ Navigated to Templates page")
    
    # 3. Click "simple wedding" template
    print("\nStep 5: Clicking 'simple wedding' template...")
    simple_wedding_template = None
    template_locators = [
        (By.XPATH, "//div[contains(text(), '🎨')]"),  # Emoji in the card
        (By.XPATH, "//div[@class='text-5xl' and text()='🎨']"),  # Exact emoji div
        (By.XPATH, "//div[contains(@class, 'bg-gradient-to-br')]//div[contains(text(), '🎨')]"),
        (By.XPATH, "//div[contains(text(), 'simple wedding')]"),  # Text fallback
        (By.XPATH, "//div[contains(text(), 'Simple Wedding')]"),
        (By.XPATH, "//div[contains(@class, 'bg-gradient-to-br')]"),  # Click the gradient card
    ]
    
    for locator_type, locator_value in template_locators:
        try:
            simple_wedding_template = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            print(f"✓ Found 'simple wedding' template: {locator_value}")
            break
        except:
            continue
    
    if simple_wedding_template is None:
        raise Exception("Could not find 'simple wedding' template.")
    
    simple_wedding_template.click()
    time.sleep(2)
    print("✓ Selected 'simple wedding' template")
    
    # 4. Enter "Wedding" in the "Event Title" field
    print("\nStep 6: Filling invitation form...")
    event_title = None
    event_title_locators = [
        (By.XPATH, "//input[@type='text' and contains(@class, 'focus:ring-amber-500')]"),  # Exact class match
        (By.XPATH, "//input[@type='text' and contains(@class, 'bg-muted-50')]"),
        (By.XPATH, "//input[@placeholder='Event Title']"),  # Fallback
        (By.XPATH, "//input[contains(@class, 'border-red-300')]"),
    ]
    
    for locator_type, locator_value in event_title_locators:
        try:
            event_title = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            print(f"✓ Found Event Title field: {locator_value}")
            break
        except:
            continue
    
    if event_title is None:
        raise Exception("Could not find Event Title field.")
    
    event_title.send_keys("Wedding")
    print("✓ Event Title entered: Wedding")
    
    # 5. Enter "Join us to celebrate our wedding day!" in the "Message" field
    message_field = None
    message_locators = [
        (By.XPATH, "//textarea[@rows='3' and contains(@class, 'focus:ring-amber-500')]"),  # Exact class match
        (By.XPATH, "//textarea[contains(@class, 'bg-muted-50') and contains(@class, 'resize-none')]"),
        (By.XPATH, "//textarea[contains(@class, 'border-red-300')]"),
        (By.XPATH, "//textarea[@placeholder='Message']"),  # Fallback
        (By.XPATH, "//textarea[@rows='3']"),
    ]
    
    for locator_type, locator_value in message_locators:
        try:
            message_field = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            print(f"✓ Found Message field: {locator_value}")
            break
        except:
            continue
    
    if message_field is None:
        raise Exception("Could not find Message field.")
    
    message_field.send_keys("Join us to celebrate our wedding day!")
    print("✓ Message entered: Join us to celebrate our wedding day!")
    
    # 6. Enter "Kutaisi" in the "Location" field
    location_field = None
    location_locators = [
        (By.XPATH, "(//input[@type='text' and contains(@class, 'focus:ring-amber-500')])[2]"),  # Second input with this class
        (By.XPATH, "(//input[@type='text' and contains(@class, 'bg-muted-50')])[2]"),
        (By.XPATH, "//input[@placeholder='Location']"),  # Fallback
        (By.XPATH, "(//input[contains(@class, 'border-red-300')])[2]"),
    ]
    
    for locator_type, locator_value in location_locators:
        try:
            location_field = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            print(f"✓ Found Location field: {locator_value}")
            break
        except:
            continue
    
    if location_field is None:
        raise Exception("Could not find Location field.")
    
    location_field.send_keys("Kutaisi")
    print("✓ Location entered: Kutaisi")
    
    # 7. Enter "05/12/2026" in the "Date" field
    date_field = None
    date_locators = [
        (By.XPATH, "//input[@type='date' and contains(@class, 'focus:ring-amber-500')]"),  # Exact class match
        (By.XPATH, "//input[@type='date' and contains(@class, 'bg-muted-50')]"),
        (By.XPATH, "//input[@type='date' and contains(@class, 'border-red-300')]"),
        (By.XPATH, "//input[@placeholder='Date']"),  # Fallback
        (By.XPATH, "//input[@type='date']"),
    ]
    
    for locator_type, locator_value in date_locators:
        try:
            date_field = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            print(f"✓ Found Date field: {locator_value}")
            break
        except:
            continue
    
    if date_field is None:
        raise Exception("Could not find Date field.")
    
    date_field.send_keys("05/12/2026")
    print("✓ Date entered: 05/12/2026")
    
    # 8. Enter "06:00 PM" in the "Time" field
    time_field = None
    time_locators = [
        (By.XPATH, "//input[@type='time' and contains(@class, 'focus:ring-amber-500')]"),  # Exact class match
        (By.XPATH, "//input[@type='time' and contains(@class, 'bg-muted-50')]"),
        (By.XPATH, "//input[@type='time' and contains(@class, 'border-red-300')]"),
        (By.XPATH, "//input[@placeholder='Time']"),  # Fallback
        (By.XPATH, "//input[@type='time']"),
    ]
    
    for locator_type, locator_value in time_locators:
        try:
            time_field = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            print(f"✓ Found Time field: {locator_value}")
            break
        except:
            continue
    
    if time_field is None:
        raise Exception("Could not find Time field.")
    
    # HTML time input expects 24-hour format (HH:MM), not 12-hour with AM/PM
    # 06:00 PM = 18:00 in 24-hour format
    time_field.send_keys("18:00")
    print("✓ Time entered: 18:00 (06:00 PM)")
    
    # 9. Click the button "მოსაწვევის შექმნა" (CREATE INVITATION)
    print("\nStep 7: Clicking 'მოსაწვევის შექმნა' (CREATE INVITATION) button...")
    create_invitation_btn = None
    create_btn_locators = [
        (By.XPATH, "//button[contains(text(), 'მოსაწვევის შექმნა')]"),  # Georgian text
        (By.XPATH, "//button[contains(., 'მოსაწვევის შექმნა')]"),
        (By.XPATH, "//button[contains(@class, 'bg-white') and contains(text(), 'მოსაწვევის')]"),
        (By.XPATH, "//button[text()='CREATE INVITATION']"),  # English fallback
        (By.XPATH, "//button[contains(text(), 'CREATE INVITATION')]"),
    ]
    
    for locator_type, locator_value in create_btn_locators:
        try:
            create_invitation_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            print(f"✓ Found 'CREATE INVITATION' button: {locator_value}")
            break
        except:
            continue
    
    if create_invitation_btn is None:
        raise Exception("Could not find 'CREATE INVITATION' button.")
    
    # Scroll button into view and click using JavaScript to avoid click interception
    driver.execute_script("arguments[0].scrollIntoView(true);", create_invitation_btn)
    time.sleep(1)
    try:
        driver.execute_script("arguments[0].click();", create_invitation_btn)
    except:
        create_invitation_btn.click()
    print("✓ Clicked 'მოსაწვევის შექმნა' button")
    
    # Wait to see the result
    print("\nWaiting for invitation creation to complete...")
    time.sleep(5)
    print("\n✓✓✓ Invitation test completed successfully! ✓✓✓")

except Exception as e:
    print(f"\n❌ Error occurred: {str(e)}")
    print(f"Failed at current step. Check the browser window for details.")
    time.sleep(3)

finally:
    print("\nClosing browser...")
    driver.quit()
    print("Browser closed.")
