class CashRegister:

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.transactions = []

    def __add__(self, amt):
        self.transactions.append(float(amt))
        self.balance = sum(self.transactions)
        return self

    def __str__(self):
        return f"Today's balance: $ {self.balance:.2f}"

    def __repr__(self):
        return f"{self.name}'s cash register with {len(self.transactions)} transactions"

    def __lt__(self, other):
        return self.balance < other


# Example of usage
if __name__ == '__main__':
    c1 = CashRegister(0.00, 'Chris')
    c1 + 2.00
    c1 + 3.00
    print(c1.transactions)  # Outputs: [2.0, 3.0]
    print(c1.name)  # Outputs: Chris
    print(c1)  # Outputs: Today's balance: $ 5.00
    print(c1 < 10.0)  # Outputs: True
    print(c1 < 1.0)  # Outputs: False
