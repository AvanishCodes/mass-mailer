
import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

smtp_server = "smtp.gmail.com"
port = 587  # For starttls


sender_email = input("Enter the email of the sender: ")
password = input("Enter the password: ")



context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    file = "emails.csv"
    with open(file, "r") as f:
        for line in f:
            # Get the email address from the line
            receiver_name, receiver_email, attachment = line.split(',')
            attachment = attachment.strip()
            receiver_email = receiver_email.strip()
            print(receiver_email)
            print(attachment)
            # Add the attachment to the message
            with open(attachment, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attachment}",
            )
            html_msg = f"""\
            <html>
            <body>
            <p>Hi {receiver_name}<br>
            <p> This is your certificate for GitHub Workshop.
            <br>
            """
            message = MIMEMultipart()
            message["Subject"] = "Certificate"
            message["From"] = sender_email
            message["To"] = receiver_email
            message.attach(MIMEText(html_msg, "html"))
            message.attach(part)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent to: ", receiver_email)
            print("Attachment: ", attachment)
            print("\n")
            continue
    print("Done")