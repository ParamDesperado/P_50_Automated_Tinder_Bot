# 🔥 Tinder Auto Swipe (Educational Demo)

**Author:** Param Sangani  

**Purpose:** Learning project demonstrating Selenium browser automation, element selection, and dynamic content handling.

> ⚠ **Disclaimer:** This script is for **educational use only** — do **not** use it to automate Tinder or any real production website.

---

## 🧠 Overview

This Python project demonstrates how to:

- ✅ Automate a complete **login-and-swipe workflow** using Selenium WebDriver.  
- ⏳ Handle **dynamic popups** using Explicit Waits (e.g., waiting for a "match" popup to appear and then disappear).  
- 🧍 Simulate **human-like behavior**, such as slow typing and realistic pauses between actions.  
- 🧩 Organize simple `By.ID` selectors for easy maintenance.  
- ⚙ Run out-of-the-box thanks to **Selenium Manager**, which automatically handles `chromedriver.exe`.

This script is designed to run against the included `mock_tinder.html` file — providing a **safe and reliable way** to practice automation without touching a real website.

---

## ⚙ How to Run This Demo

### 1️⃣ Download the Files

Clone this repository or download the two main files:

- `run_test.py` (the Python automation script)  
- `mock_tinder.html` (the mock Tinder website)

Place them both in the **same folder**.

---

### 2️⃣ Install Dependencies

- pip install selenium
  
### 3️⃣ Update the File Path
Open run_test.py and update the MOCK_TINDER_URL variable with the absolute path to your HTML file.
💻 Example (Windows)
- MOCK_TINDER_URL = "file:///C:/Users/Param/MyProjects/Tinder_Bot/mock_tinder.html"
🍎 Example (macOS/Linux)
- MOCK_TINDER_URL = "file:///Users/Param/MyProjects/Tinder_Bot/mock_tinder.html"

### 4️⃣ Run the Script
---
## 🧩 Configuration
- Setting	        Description
- SELECTORS	      Dictionary of all element IDs for easy editing
- TOTAL_SWIPES    Number of swipes to perform (default: 10)
- WAIT_TIMEOUT	  Maximum seconds to wait for an element
- MOCK_TINDER_URL	File path to your local mock Tinder HTML

- 💡 The “It’s a Match!” popup is triggered automatically on the 6th swipe (index 5).

---
## ⚠ Disclaimer

This project is intended only for educational and testing purposes.
Automating real platforms like Tinder, Bumble, or Hinge violates their Terms of Service.
This script should be used exclusively with the included mock_tinder.html file.

---
## ✨ Author

Param Sangani
💻 Automation Enthusiast | 🧠 Python Developer | ⚙ QA Learner
