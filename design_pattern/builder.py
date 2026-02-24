"""
The Builder Design Pattern is a creational pattern that lets you construct complex objects step-by-step,
separating the construction logic from the final representation.

An object has many optional fields, and most callers only need a subset.
You want to avoid telescoping constructors or long parameter lists.
The object must be assembled through multiple steps, possibly in a specific order.
"""

class Email:
    # to = builder._to
    def __init__(self, builder):
        self.to = builder._to
        self.subject = builder._subject
        self.cc = list(builder._cc)
        self.bcc = list(builder._bcc)
        self.body = builder._body
        self.priority = builder._priority
        self.attachment = list(builder._attachment)

    def __str__(self):
        return f"Email - to {self.to}, with subject {self.subject}, cc = {self.cc}, bcc = {self.bcc}, body = {self.body}, priority = {self.priority}, attachments = {self.attachment}"


    class Builder:
        # _to = to
        def __init__(self, to, subject):
            self._to = to
            self._subject = subject
            self._cc = []
            self._bcc = []
            self._body = None
            self._priority = "normal"
            self._attachment = []

        def cc(self, cc):
            self._cc = cc
            return self

        def bcc(self, bcc):
            self._bcc = bcc
            return self

        def body(self, body):
            self._body = body
            return self

        def priority(self, priority):
            self._priority = priority
            return self

        def attachment(self, attachment):
            self._attachment = attachment
            return self

        def build(self):
            return Email(self) #

if __name__ == "__main__":
    email1 = Email.Builder("alice@example.com", "Meeting Tomorrow") \
        .body("Let's meet at 10am in conference room B.") \
        .build()

    email2 = Email.Builder("bob@example.com", "Project Update") \
        .cc("carol@example.com") \
        .cc("dave@example.com") \
        .bcc("manager@example.com") \
        .body("Attached is the Q4 report.") \
        .priority("high") \
        .attachment("q4-report.pdf") \
        .attachment("summary.xlsx") \
        .build()

    print(email1)
    print()
    print(email2)

