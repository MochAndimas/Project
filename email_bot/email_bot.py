"""email bot module"""

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = input("from? ")
email["to"] = input("to? ")
email["subject"] = input("message? ")

email.set_content(html.substitute(
    {"name": "dimas", "phone": "123456"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("account", "password")  # put your email an dpassword
    smtp.send_message(email)
    print("message sent!!")
