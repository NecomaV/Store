import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AUOOir3F1mGhB-v6M9rnS_eWqWSmNqcxiUTGBj7l-vx_D97P8oDvvsxnEqVHDixbRGzflLBSCX81VdYr"
        self.client_secret = "EOl0xPaHnHjEApew5vqAiL9SEv7RNp9XbTNZuByo6Zw76nmqNS_lywvrfwvi7XjUtPL8fr1mDQ8f2KT6"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)