from abc import ABC, abstractmethod


class NotificationSender(ABC):
    def __init__(self):
        self.is_under_maintenance = False

    @property
    @abstractmethod
    def sender_type(self):
        pass

    def send(self, message: str):
        if self.is_under_maintenance:
            print("This service is currently under maintenance.")
        else:
            print(f"Sending {self.sender_type} with message: {message}")


class EmailSender(NotificationSender):
    def __init__(self):
        super().__init__()

    @property
    def sender_type(self):
        return "email"


class SMSSender(NotificationSender):
    def __init__(self):
        super().__init__()

    @property
    def sender_type(self):
        return "SMS"

class PushSender(NotificationSender):
    def __init__(self):
        super().__init__()

    @property
    def sender_type(self):
        return "Push"


class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message: str):
        self.sender.send(message)


email_sender = EmailSender()
sms_sender = SMSSender()
push_sender = PushSender()

push_sender.is_under_maintenance = True
"""
The status change represents manual toggling done by an admin or a developer when they know a system component 
is under maintenance.
In more complex systems, this would be automated or pulled from an external source.
"""
email_service = NotificationService(email_sender)
sms_service = NotificationService(sms_sender)
push_service = NotificationService(push_sender)

email_service.notify('Hello via email!')
sms_service.notify('Hello via SMS!')
push_service.notify('Hello via Push!')

# try:
#     email_service = NotificationService("email")
#     email_service.notify("Hello via email!")
#
#     sms_service = NotificationService("sms")
#     sms_service.notify("Hello via SMS!")
#
#     push_service = NotificationService("push")
#     push_service.notify("Hello via Push!")
#
# except UnderMaintenanceException as ex:
#     print(ex)
