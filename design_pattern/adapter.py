"""
The Adapter Design Pattern is a structural design pattern that allows incompatible interfaces 
to work together by converting the interface of one class into another that the client expects.

You're integrating with a legacy system or a third-party library that doesn't match your current interface.
You want to reuse existing functionality without modifying its source code.
You need to bridge the gap between new and old code, or between systems built with different interface designs.
"""
from abc import ABC, abstractmethod
import time
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str):
        pass

    @abstractmethod
    def is_payment_successful(self) -> bool:
        pass

    @abstractmethod
    def get_transaction_id(self) -> str:
        pass

class InHousePaymentProcessor(PaymentProcessor):
    def __init__(self):
        self._transaction_id = None
        self._payment_successful = False
    
    def process_payment(self, amount, currency):
        print(f"InHouseProcessor: Processing {amount} {currency}")
        self._transaction_id = f"TXN_{int(time.time() * 1000)}"
        self._payment_successful = True
        print(f"InHouseProcessor: Success. Txn ID: {self._transaction_id}")
    
    def is_payment_successful(self):
        return self._payment_successful
    
    def get_transaction_id(self):
        return self._transaction_id
    
class CheckoutService:
    def __init__(self, payment_processor: PaymentProcessor):
        self._processor = payment_processor
    
    def checkout(self, amount: float, currency: str):
        print(f"Checkout: Processing order for ${amount} {currency}")
        self._processor.process_payment(amount, currency)
        if self._processor.is_payment_successful():
            print(f"Checkout: Order successful! Txn: {self._processor.get_transaction_id()}")
        else:
            print("Checkout: Order failed.")

class LegacyGateway:
    def __init__(self):
        self._transaction_reference = None
        self._payment_successful = False

    def execute_transaction(self, total_amount: float, currency: str):
        print(f"LegacyGateway: Executing {currency} {total_amount}")
        self._transaction_reference = time.time_ns()
        self._payment_successful = True
        print(f"LegacyGateway: Done. Ref: {self._transaction_reference}")

    def check_status(self, ref: int) -> bool:
        print(f"LegacyGateway: Checking status for ref: {ref}")
        return self._payment_successful

    def get_reference_number(self) -> int:
        return self._transaction_reference

class LegacyGatewayAdapter(PaymentProcessor):
    def __init__(self, legacy_gateway: LegacyGateway):
        self._legacy_gateway = legacy_gateway
        self.current_ref = None

    def process_payment(self, amount, currency):
        self._legacy_gateway.execute_transaction(amount, currency)
        self.current_ref = self._legacy_gateway.get_reference_number()

    def is_payment_successful(self):
        return self._legacy_gateway.check_status(self.current_ref)
    
    def get_transaction_id(self):
        return f"LEGACY_TXN_{self.current_ref}"

if __name__ == '__main__':
    processor = InHousePaymentProcessor()
    checkout = CheckoutService(processor)
    checkout.checkout(199.99, "USD")