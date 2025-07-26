import smtplib  # Import email sending module

# Get user inputs
email = input("SENDER EMAIL : ")  # Sender's email
Receiver_email = input("Receiver Email : ")  # Receiver's email

Subject = input("Subject : ")  # Email subject
message = input("Message: ")  # Email body message

# Combine subject and message
txt = f"Subject : {Subject}\n\n{message}"

# Connect to Gmail's SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)  # Server + port
#587	SMTP	Sending email (secure)	TLS (modern)
#Port 587 is the standard port used to send emails securely using SMTP with TLS encryption.
server.starttls()  # Start TLS encryption (secure connection)

# Login using sender's email and app password
server.login(email, "spxs goeq cseu exlr")  # Use app password, not normal password

# Send the email
server.sendmail(email, Receiver_email, txt)

# Print confirmation
print("Email Has been Sent to " + Receiver_email)
