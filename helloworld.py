import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def send_email(subject, body, to_email):
    # Email configuration
    from_email = "aravindcuts@gmail.com"
    from_password = "ysfz phef wwps ahvl"
    
    # Set up the server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()
    server.login(from_email, from_password)
    
    # Create the email
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    # Send the email
    server.send_message(msg)
    server.quit()

def main():
    # Set Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Comment this line to run with GUI

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open a webpage
        driver.get("https://google.com")

        # Perform a basic action
        assert "Google" in driver.title

        # Close the browser
        driver.quit()

        # Send success email
        send_email(
            subject="Selenium Script Executed Successfully",
            body="The Selenium script has executed successfully.",
            to_email="aravindcuts@gmail.com"
        )

    except Exception as e:
        # If there is any error, print the error message
        print(f"An error occurred: {e}")

        # Optionally, send an email notification about the failure
        send_email(
            subject="Selenium Script Execution Failed",
            body=f"The Selenium script failed with the following error:\n\n{e}",
            to_email="aravindcuts@gmail.com"
        )

if __name__ == "__main__":
    main()
