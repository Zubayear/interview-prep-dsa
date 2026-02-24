from abc import abstractmethod, ABC

"""
The Factory Pattern is a creational design pattern that provides an interface for creating objects without exposing the 
creation logic to the client. Instead of calling a constructor directly, you call a factory method/function.
"""


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(Animal):
    def speak(self) -> str:
        return "woof"


class Cat(Animal):
    def speak(self) -> str:
        return "meow"


class Duck(Animal):
    def speak(self) -> str:
        return "quack"


def animal_factory(animal_type: str) -> ValueError | Animal:
    animals = {
        "dog": Dog,
        "cat": Cat,
        "duck": Duck,
    }

    creator = animals.get(animal_type.lower())
    if not creator:
        return ValueError(f"Unknown animal type: {animal_type}")
    return creator()

#

class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending email with {message}")

class SmsNotification(Notification):
    def send(self, message: str):
        print(f"Sending sms with {message}")

class PushNotification(Notification):
    def send(self, message: str):
        print(f"Sending push notification with {message}")

class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass
    def send(self, message: str):
        notification = self.create_notification()
        notification.send(message)

class EmailNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SmsNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SmsNotification()

class PushNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return PushNotification()

if __name__ == '__main__':
    notificationCreator = EmailNotificationCreator()
    notificationCreator.send("Welcome")

    notificationCreator = SmsNotificationCreator()
    notificationCreator.send("Welcome")

    notificationCreator = PushNotificationCreator()
    notificationCreator.send("Welcome")