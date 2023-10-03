from message_manager import MessageManager
from message_strategy import EmailSendingStrategy, SMSSendingStrategy

message_manager = MessageManager()

email_strategy = EmailSendingStrategy()
sms_strategy = SMSSendingStrategy()

message_manager.sending_strategy = email_strategy

message_manager.addMessage("Hello, this is an email message.")
message_manager.sending_strategy.send("Hello, this is an email message.")

message_manager.sending_strategy = sms_strategy

message_manager.addMessage("Hello, this is an SMS message.")
message_manager.sending_strategy.send("Hello, this is an SMS message.")


