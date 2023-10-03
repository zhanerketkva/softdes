class MessageSendingStrategy:
    def send(self, message):
        pass


class EmailSendingStrategy(MessageSendingStrategy):
    def send(self, message):
        print(f"Sending email: {message}")


class SMSSendingStrategy(MessageSendingStrategy):
    def send(self, message):
        print(f"Sending SMS: {message}")
