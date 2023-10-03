class MessageManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MessageManager, cls).__new__(cls)
            cls._instance.messages = []
        return cls._instance

    def addMessage(self, message):
        self.messages.append(message)

    def getMessages(self):
        return self.messages
