import emails

class Recipient:
    def __init__(self, id, email, day, IsCognit):
        self.id = id
        self.email = email
        self.day = day
        self.IsCognit = IsCognit

    def send_email(self):
        emails.send_email(self.email, self.day)
        self.day += 1

    def __str__(self):
        return f'{self.id}, {self.email}, {self.day}, {self.IsCognit}'

    def to_dict(self):
        return {
            'ID': self.id,
            'email': self.email,
            'day': self.day,
            'IsCognit': self.IsCognit
        }

# test = Recipient('P01', 'natalou55@gmail.com', 0, True)
# print(test)