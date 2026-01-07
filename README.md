[![Automated Tests](https://github.com/limin77/QA-Automation-Portfolio/actions/workflows/main.yml/badge.svg)](https://github.com/limin77/QA-Automation-Portfolio/actions/workflows/main.yml)

# QA Automation Portfolio 🚀

## Overview
This repository contains a robust Test Automation Framework built using **Python** and **Selenium WebDriver**. It demonstrates modern automation practices including the **Page Object Model**, **REST API Validation**, and **Data-Driven Testing**.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Web Automation:** Selenium WebDriver (Chrome)
* **API Testing:** Requests Library
* **Test Runner:** Pytest
* **Reporting:** Pytest-HTML
* **CI/CD:** GitHub Actions (Automated Cloud Testing)

## 📂 Project Structure
* `tests/test_login.py`: **Smart UI Automation** using Explicit Waits (`WebDriverWait`) and ID locators.
* `tests/test_api.py`: Backend validation for REST API endpoints (GET/POST/DELETE).
* `tests/test_login_negative.py`: Security validation for "Locked Out" user scenarios.
* `.github/workflows/`: Configuration for automated testing in the cloud.

## 🚀 Key Features
* **Smart Waits:** Eliminates flaky tests by replacing `time.sleep` with dynamic Explicit Waits.
* **Cross-Browser Ready:** Structured to support multiple browser drivers.
* **CI/CD Ready:** Integrated with GitHub Actions to run tests on every code push.

## 💻 How to Run Locally
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt