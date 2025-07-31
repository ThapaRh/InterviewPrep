'''
It is used when one object needs to modify many other objects(observers) of the state changes
Real life analogy:
You are subscribed to a yt channel 
When new video is uploaded, you and other subscribers(observers) get notified
'''

class Subscriber():
    def update(self):
        pass

class EmailSubscriber():
    def update(self,notification):
        print(f'Hello Email Subscriber, {notification}')

class SMSSubscriber():
    def update(self,notification):
        print(f'Hello SMS Subscriber{notification}')
        
class NotificationService():
    def __init__(self):
        self.subscribers = []
    
    def add_subscriber(self,subscriber):
        self.subscribers.append(subscriber)
    
    def unsubscribe(self,subscriber):
        self.subscribers.remove(subscriber)
        print(self.subscriber)
    
    def notify_all(self,message):
        for s in self.subscribers:
            s.update(message)

class Main:
    notification_service = NotificationService()
    email_subs = EmailSubscriber()
    sms_subs = SMSSubscriber()
    notification_service.add_subscriber(email_subs)
    notification_service.add_subscriber(sms_subs)
    notification_service.notify_all("Walk dont run, you dont have to follow what world says.")
    notification_service.unsubscribe(sms_subs)
            

