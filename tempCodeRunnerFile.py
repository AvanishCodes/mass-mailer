reate_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    file = "emails.csv"
    with open(file, "r") as f:
        for line in f:
            # Get the email address from the line
            receiver_email = line.strip(',')[0]
            # Get the attachment from the line
            attachment = line.strip(',')[1]
            pri