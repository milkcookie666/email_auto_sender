import smtplib

class email_distribution:
    def __init__(self, file_name, message):
        self.file_name = file_name
        self.message = message


    def get_user_list(self):
        self.file = open(self.file_name, 'r')
        return [line.rstrip('\n') for line in self.file]

    def input_message(self):
        return self.message

    def sender(self, email_login, email_password):
        for user in self.get_user_list():
            self.s = smtplib.SMTP('smtp.mail.ru', 587)
            self.s.starttls()
            self.s.login(email_login, email_password)
            self.s.sendmail(email_login, user, self.message)
            self.s.quit()

