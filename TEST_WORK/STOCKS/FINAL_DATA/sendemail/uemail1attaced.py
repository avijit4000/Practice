"""
######################################################################
Email With Attachments Python Script
Coded By "The Intrigued Engineer" over a coffee
Thanks For Watching!!!
######################################################################
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "avijit4000@gmail.com"
# email_list = ["avijit5557@gmail.com"]


# print(email_list)
with open("D:\Pyn\online learning\FINAL_DATA\sendemail\dsemail.txt","r") as emai:
    fi=emai.readlines()
email_list=[]
for i in fi:
    email_list.append(i.replace("\n",""))
    # print(i.replace("\n",""))
# print(fi)
print(email_list)


# Define the password (better to reference externally)
pswd = "lwrp hpjd arae czvv" # As shown in the video this password is now dead, left in as example only


# name the email subject
subject = "Application for Data Science Position - Avijit Biswas"



# Define the email function (dont call it email!)
def send_emails(email_list):

    for person in email_list:

        # Make the body of the email
        body = f"""
    Dear sir,
        
        My name is Avijit Biswas, and I am writing to express my interest in any potential Data Science positions within your organization. With over three years of hands-on experience in data science and management, I have successfully contributed to projects involving data analysis, machine learning, and natural language processing. I have attached my resume for your consideration.
        If there are any open positions or opportunities that match my skill set, I would greatly appreciate the opportunity to discuss. I am available for a conversation at your earliest convenience and can be reached at +91 7908023338 or avijit4000@gmail.com or WhatsApp +91 7908023338.
        Thank you for considering my application. I am eager to explore potential opportunities with your Company and believe that my background in data science could bring significant value to your team.
        
    With Best Regards
    Avijit Biswas
    +91 7908023338
    avijit4000@gmail.com
    https://www.linkedin.com/in/avijit-biswas4000/
        """

        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename = "Avijit_new68.pdf"

        # Open the file in python as a binary
        attachment= open(filename, 'rb')  # r for read and b for binary

        # Encode as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()


        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    TIE_server.quit()


# Run the function
send_emails(email_list)