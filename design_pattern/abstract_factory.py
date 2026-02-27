from abc import ABC, abstractmethod


class Message(ABC):
  @abstractmethod
  def set_content(self, to: str, body: str):
    pass

  @abstractmethod
  def format(self) -> str:
    pass

class Sender(ABC):
  @abstractmethod
  def send(self, message: Message):
    pass

class EmailMessage(Message):
  def set_content(self, to: str, body: str):
    self.to = to