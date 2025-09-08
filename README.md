

- Uses *Page Object Model (POM)* for clean structure.
- Automates login page of https://the-internet.herokuapp.com.
- Includes *valid login* and *invalid login* tests.
- Can be extended to more pages & test cases.

---

 Tech Stack
- Python 3.x
- Selenium
- Pytest

---
 Project Structure

selenium-testing-project/ │── src/ │   ├── pages/ │   │   ├── base_page.py │   │   └── login_page.py │   └── tests/ │       └── test_login.py │── requirements.txt │── README.md

---

 Run
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/selenium-testing-project.git
   cd selenium-testing-project

2. Install dependencies:

pip install -r requirements.txt


3. Run tests:

pytest -v




---


---

Would you like me to also add a *.github/workflows/test.yml (CI/CD with GitHub Actions)* so your Selenium tests run automatically when you push code? 🚀
