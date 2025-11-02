"""
✅ Works with the mock_tinder.html file you provided
✅ No ChromeDriver path needed — uses Selenium Manager automatically
✅ Simulates human-like typing, pauses, and match popup behavior
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------

MOCK_TINDER_URL = (
    "file:///C:/Users/param/Downloads/Param Python Projects/"
    "P_50_Automated_Tinder_Bot/mock_tinder.html"
)

WAIT_TIMEOUT = 10
TOTAL_SWIPES = 10

# Selectors to match mock_tinder.html
SELECTORS = {
    "cookies_accept": (By.ID, "accept-cookies"),
    "login_google": (By.ID, "login-google"),
    "google_email": (By.ID, "google-email"),
    "google_password": (By.ID, "google-password"),
    "google_submit": (By.ID, "google-submit"),
    "like_button": (By.ID, "like-btn"),
    "match_popup": (By.ID, "match-popup"),
}

# ---------------------------------------------------------------------
# BOT
# ---------------------------------------------------------------------
class MockTinderBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # ✅ Selenium Manager automatically handles ChromeDriver
        self.driver = webdriver.Chrome(options=options)
        # Default wait for most elements
        self.wait = WebDriverWait(self.driver, WAIT_TIMEOUT)
        # A shorter wait just for the popup to appear
        self.popup_wait = WebDriverWait(self.driver, 5)

    def type_like_human(self, element, text, delay=0.15):
        """Simulate human typing behavior."""
        for ch in text:
            element.send_keys(ch)
            sleep(delay)

    def click(self, selector):
        """Click an element safely with a small pause."""
        el = self.wait.until(EC.element_to_be_clickable(selector))
        el.click()
        sleep(2)  # consistent timing for realism

    def run(self):
        print("🚀 Opening Mock Tinder...")
        self.driver.get(MOCK_TINDER_URL)

        # Step 1: Accept cookies
        self.click(SELECTORS["cookies_accept"])

        # Step 2: Login with Google
        self.click(SELECTORS["login_google"])

        # Step 3: Type credentials slowly
        print("⌨️ Typing credentials...")
        email = self.wait.until(EC.presence_of_element_located(SELECTORS["google_email"]))
        password = self.wait.until(EC.presence_of_element_located(SELECTORS["google_password"]))

        self.type_like_human(email, "test@example.com")
        sleep(1)
        self.type_like_human(password, "password123")
        sleep(1)
        self.click(SELECTORS["google_submit"])
        print("✅ Logged in successfully!")

        # Step 4: Swiping loop with popup handling
        for i in range(TOTAL_SWIPES):
            if i == 5:
                print("💫 Expecting a match on this swipe...")

            # Wait for the like button to be clickable
            like_btn = self.wait.until(EC.element_to_be_clickable(SELECTORS["like_button"]))
            like_btn.click()

            # Handle the popup after 6th swipe (index 5)
            if i == 5:
                print("🎉 Match appeared! Waiting for popup to close...")
                # Wait for popup to be visible
                self.popup_wait.until(EC.visibility_of_element_located(SELECTORS["match_popup"]))
                print("... Popup is visible. Waiting for it to disappear...")
                # Wait for popup to be invisible (it hides after 3s)
                self.wait.until(EC.invisibility_of_element_located(SELECTORS["match_popup"]))
                print("✅ Popup closed. Continuing swipes...")
            else:
                # Regular pause for other swipes
                sleep(2.5)

            print(f"💖 Liked profile #{i + 1}")

        print("🏁 Finished all 10 swipes!")


# ---------------------------------------------------------------------
if __name__ == "__main__":
    bot = MockTinderBot()
    bot.run()

