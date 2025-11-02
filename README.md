🔥 Tinder Auto Swipe (Educational Demo)

Author: Param Sangani

Purpose: Learning project demonstrating Selenium browser automation, element selection, and dynamic content handling.

⚠ This script is for educational use only — do not use it to automate Tinder or any real production website.

🧠 Overview

This Python project demonstrates how to:

Automate a complete login-and-swipe workflow using Selenium WebDriver.

Handle dynamic popups using Explicit Waits (e.g., waiting for a "match" popup to appear and then disappear).

Simulate human-like behavior, such as slow typing and realistic pauses between actions.

Organize simple (By.ID) selectors for easy maintenance.

Run out-of-the-box thanks to Selenium Manager, which automatically handles chromedriver.exe.

This script is designed to run against the included mock_tinder.html file, providing a safe and reliable way to practice automation.

⚙ How to Run This Demo

1. Download the Files

Clone this repository or download the two main files:

run_test.py (the Python script)

mock_tinder.html (the mock website)

Place them both in the same folder.

2. Install Dependencies

You only need selenium. From your terminal, run:

pip install selenium


3. Update the File Path

This is the most important step. Open run_test.py and update the MOCK_TINDER_URL variable to the absolute file path of where you saved mock_tinder.html on your computer.

Example for Windows:

MOCK_TINDER_URL = "file:///C:/Users/Param/MyProjects/Tinder_Bot/mock_tinder.html"


Example for macOS/Linux:

MOCK_TINDER_URL = "file:///Users/Param/MyProjects/Tinder_Bot/mock_tinder.html"


4. Run the Script

From your terminal, navigate to the folder and run the script:

python run_test.py


Watch the Chrome browser open and automate the entire flow!

🧩 Configuration

Selectors: All element IDs are defined in the SELECTORS dictionary at the top of run_test.py.

Behavior: You can change TOTAL_SWIPES to run more or fewer swipes. The "match" logic is hardcoded in the run() method to trigger on the 6th swipe (index 5).

⚠ Disclaimer

This project is intended for educational and testing purposes only.

Automating interactions with real online platforms such as Tinder violates their Terms of Service.

This script is designed only for the included mock_tinder.html file.

✨ Author

Param Sangani

💻 Automation Enthusiast | 🧠 Python Developer | ⚙ QA Learner
