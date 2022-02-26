import smtplib

message = f'Subject: {"Testing"}\n\n{"testing"}'

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("abc@gmail.com", "password")
server.sendmail("abc@gmail.com", "reciever@gmail.com ", message)
server.quit()
