from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Initialize Chrome
driver = webdriver.Chrome()

try:
    print("Step 1: Opening website invu.ge...")
    driver.get("https://invu.ge/")
    
    # Wait instance
    wait = WebDriverWait(driver, 15)
    time.sleep(5)  # Wait longer for page to fully load
    print("✓ Website opened successfully")
    
    # 1. Click "შესვლა" (Sign in) button
    print("\nStep 2: Looking for 'შესვლა' (Sign in) button...")
    login_button = None
    
    # Try different ways to find the შესვლა button (primarily Georgian, with English fallback)
    login_locators = [
        (By.XPATH, '//button[text()="შესვლა"]'),
        (By.XPATH, '//button[contains(text(), "შესვლა")]'),
        (By.XPATH, '//a[text()="შესვლა"]'),
        (By.XPATH, '//a[contains(text(), "შესვლა")]'),
        (By.XPATH, '//button[text()="Sign in"]'),
        (By.XPATH, '//button[contains(text(), "Sign in")]'),
        (By.XPATH, '//button[text()="Login"]'),
        (By.XPATH, '//button[contains(text(), "Login")]'),
        (By.CSS_SELECTOR, 'button.mobile-auth-btn'),
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
    
    # Click the button immediately using JavaScript to avoid stale element issues
    print("Clicking 'შესვლა' button...")
    try:
        driver.execute_script("arguments[0].click();", login_button)
    except:
        # Fallback to regular click
        try:
            login_button.click()
        except:
            # If still fails, find it again and click
            login_button = driver.find_element(By.XPATH, '//a[text()="შესვლა"]')
            driver.execute_script("arguments[0].click();", login_button)
    
    time.sleep(3)
    print("✓ Clicked 'შესვლა' button successfully")

    # 2. Click "დარეგისტრირდით აქ" (Sign up here) button
    print("\nStep 3: Looking for 'დარეგისტრირდით აქ' (Sign up here) button...")
    sign_up_button = None
    
    # Wait a bit more for the login modal/page to fully load
    time.sleep(2)
    
    # Try different variations for the sign up button (Georgian and English)
    signup_locators = [
        (By.XPATH, '//button[text()="დარეგისტრირდით აქ"]'),  # Exact Georgian text
        (By.XPATH, '//button[contains(text(), "დარეგისტრირდით აქ")]'),
        (By.XPATH, '//button[contains(text(), "დარეგისტრირდით")]'),
        (By.XPATH, '//button[contains(., "აქ")]'),  # "here" in Georgian
        (By.XPATH, '//button[contains(text(), "რეგისტრაცია")]'),  # Registration
        (By.XPATH, '//a[contains(text(), "დარეგისტრირდით")]'),
        (By.XPATH, '//button[contains(text(), "Sign up here")]'),
        (By.XPATH, '//button[contains(text(), "sign up here")]'),
        (By.XPATH, '//a[contains(text(), "Sign up here")]'),
        (By.CSS_SELECTOR, 'a[href*="register"]'),
        (By.CSS_SELECTOR, 'a[href*="signup"]'),
    ]
    
    for locator_type, locator_value in signup_locators:
        try:
            sign_up_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            print(f"✓ Found 'Sign up' button: {locator_value}")
            break
        except:
            continue
    
    if sign_up_button is None:
        print("Could not find 'Sign up here' button. Checking page elements...")
        # Debug: Show all visible buttons and links after clicking login
        all_buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"\nVisible buttons after clicking შესვლა:")
        for btn in all_buttons:
            if btn.is_displayed():
                print(f"  - Text: '{btn.text}' Class: '{btn.get_attribute('class')}'")
        
        all_links = driver.find_elements(By.TAG_NAME, "a")
        print(f"\nVisible links after clicking შესვლა:")
        for link in all_links:
            if link.is_displayed() and link.text.strip():
                print(f"  - Text: '{link.text}' Href: '{link.get_attribute('href')}'")
        
        raise Exception("Could not find 'Sign up here' button. Check the output above for available elements.")
    
    sign_up_button.click()
    time.sleep(2)
    print("✓ Clicked 'Sign up here' button")
    
    # 3. Fill "First name"
    print("\nStep 4: Filling 'First name' field with 'mari'...")
    first_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'firstName')))
    first_name_input.send_keys("mari")
    print("✓ First name entered")
    
    # 4. Fill "Last name"
    print("\nStep 5: Filling 'Last name' field with 'kharabadze'...")
    last_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'lastName')))
    last_name_input.send_keys("kharabadze")
    print("✓ Last name entered")
    
    # 5. Fill "Email address"
    print("\nStep 6: Filling 'Email address' field with 'marimar@gmail.com'...")
    email_input = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
    email_input.send_keys("marimar@gmail.com")
    print("✓ Email entered")
    
    # 6. Fill "Password"
    print("\nStep 7: Filling 'Password' field...")
    password_input = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
    password_input.send_keys("marimari123")
    print("✓ Password entered")
    
    # 7. Fill "Confirm Password"
    print("\nStep 8: Filling 'Confirm Password' field...")
    confirm_password_input = wait.until(EC.visibility_of_element_located((By.ID, 'confirmPassword')))
    confirm_password_input.send_keys("marimari123")
    print("✓ Confirm password entered")
    
    # 8. Click "Create Account" button (English or Georgian)
    print("\nStep 9: Clicking 'Create Account' button...")
    create_account_button = None
    
    create_account_locators = [
        (By.XPATH, '//button[contains(text(), "Create Account")]'),
        (By.XPATH, '//button[contains(text(), "CREATE ACCOUNT")]'),
        (By.XPATH, '//button[contains(text(), "Create account")]'),
        (By.XPATH, '//button[@type="submit"]'),  # Submit button
        (By.XPATH, '//button[contains(text(), "აქაუნთის შექმნა")]'),  # Georgian
        (By.XPATH, '//button[contains(text(), "რეგისტრაცია")]'),  # Georgian
    ]
    
    for locator_type, locator_value in create_account_locators:
        try:
            create_account_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            print(f"✓ Found 'Create Account' button: {locator_value}")
            break
        except:
            continue
    
    if create_account_button is None:
        raise Exception("Could not find 'Create Account' button.")
    
    create_account_button.click()
    print("✓ Clicked 'Create Account' button")
    
    # Wait to see the result
    print("\nWaiting for registration to complete...")
    time.sleep(5)
    print("\n✓✓✓ Registration test completed successfully! ✓✓✓")

except Exception as e:
    print(f"\n❌ Error occurred: {str(e)}")
    print(f"Failed at current step. Check the browser window for details.")
    time.sleep(3)

finally:
    print("\nClosing browser...")
    driver.quit()
    print("Browser closed.")
