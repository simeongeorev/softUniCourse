class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails_list = []

while (command := input()) != "Stop":
    command_list = command.split()
    email = Email(command_list[0], command_list[1], command_list[2])
    emails_list.append(email)

sent_emails_list = list(map(int, input().split(", ")))

for i in range(len(sent_emails_list)):
    emails_list[sent_emails_list[i]].send()

for mail in emails_list:
    print(mail.get_info())
