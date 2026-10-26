import os
import sys
import time
import subprocess
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1280,1050")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--force-device-scale-factor=1.25")
    return webdriver.Chrome(options=chrome_options)

def wait_for_server(url, timeout=10):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url, timeout=1)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(0.3)
    return False

def run_part_a(driver):
    print("--- Capturing Part A Screenshots ---")
    port = 5050
    env = os.environ.copy()
    proc = subprocess.Popen(
        [sys.executable, "-c", f"""
import sys
sys.path.insert(0, r'{os.path.abspath("part_a")}')
from app import app
app.run(port={port}, debug=False)
"""],
        env=env
    )

    url = f"http://127.0.0.1:{port}/"
    try:
        assert wait_for_server(url), "Server failed to start"
        driver.get(url)
        time.sleep(1)
        # 1. Initial Home Page
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_a_1_initial_list.png"))
        print("Captured: part_a_1_initial_list.png")

        # 2. Fill form
        name_input = driver.find_element(By.NAME, "name")
        email_input = driver.find_element(By.NAME, "email")
        course_input = driver.find_element(By.NAME, "course")
        name_input.send_keys("Emily Davis")
        email_input.send_keys("emily.davis@example.com")
        course_input.send_keys("Artificial Intelligence")
        time.sleep(0.5)
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_a_2_add_student_form.png"))
        print("Captured: part_a_2_add_student_form.png")

        # 3. Submit form -> Student Added
        btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn.click()
        time.sleep(1)
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_a_3_student_added.png"))
        print("Captured: part_a_3_student_added.png")

        # 4. Delete a student (click first delete button)
        delete_btn = driver.find_element(By.CLASS_NAME, "del-btn")
        delete_btn.click()
        time.sleep(1)
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_a_4_student_deleted.png"))
        print("Captured: part_a_4_student_deleted.png")

    finally:
        proc.terminate()
        proc.wait()

def run_part_b(driver):
    print("--- Capturing Part B Screenshots ---")
    port = 5051
    env = os.environ.copy()
    proc = subprocess.Popen(
        [sys.executable, "-c", f"""
import sys
sys.path.insert(0, r'{os.path.abspath("part_b")}')
from app import app
app.run(port={port}, debug=False)
"""],
        env=env
    )

    url = f"http://127.0.0.1:{port}/"
    try:
        assert wait_for_server(url), "Server failed to start"
        driver.get(url)
        time.sleep(1)
        # 1. Initial Home Page
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_b_1_initial_list.png"))
        print("Captured: part_b_1_initial_list.png")

        # 2. Fill form
        roll_input = driver.find_element(By.NAME, "roll_no")
        name_input = driver.find_element(By.NAME, "name")
        dept_input = driver.find_element(By.NAME, "department")
        roll_input.send_keys("103")
        name_input.send_keys("Charlie Davis")
        dept_input.send_keys("Information Science")
        time.sleep(0.5)
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_b_2_registration_form.png"))
        print("Captured: part_b_2_registration_form.png")

        # 3. Submit form -> Student Registered
        btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn.click()
        time.sleep(1)
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_b_3_student_registered.png"))
        print("Captured: part_b_3_student_registered.png")

    finally:
        proc.terminate()
        proc.wait()

def run_part_c(driver):
    print("--- Capturing Part C Screenshots ---")
    port = 5052
    env = os.environ.copy()
    proc = subprocess.Popen(
        [sys.executable, "-c", f"""
import sys
sys.path.insert(0, r'{os.path.abspath("part_c")}')
from app import app
app.run(port={port}, debug=False)
"""],
        env=env
    )

    url = f"http://127.0.0.1:{port}/"
    try:
        assert wait_for_server(url), "Server failed to start"
        driver.get(url)
        time.sleep(1)
        # 1. Initial Home Page
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_c_1_course_registration_dashboard.png"))
        print("Captured: part_c_1_course_registration_dashboard.png")

        # 2. Fill registration form
        id_input = driver.find_element(By.NAME, "student_id")
        name_input = driver.find_element(By.NAME, "student_name")
        course_select = driver.find_element(By.NAME, "course_code")

        id_input.send_keys("STU003")
        name_input.send_keys("Ananya Sharma")
        from selenium.webdriver.support.ui import Select
        sel = Select(course_select)
        sel.select_by_value("CS103")
        time.sleep(0.5)
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_c_2_fill_course_form.png"))
        print("Captured: part_c_2_fill_course_form.png")

        # 3. Submit registration -> Enrolled
        btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn.click()
        time.sleep(1)
        driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "part_c_3_course_registered.png"))
        print("Captured: part_c_3_course_registered.png")

    finally:
        proc.terminate()
        proc.wait()

def main():
    driver = get_driver()
    try:
        run_part_a(driver)
        run_part_b(driver)
        run_part_c(driver)
        print("All screenshots successfully captured!")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
