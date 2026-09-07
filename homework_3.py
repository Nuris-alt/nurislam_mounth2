TRIP_COSTS = 20

class TransportCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0


    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def add_money(self, amount):
        self.__balance += amount

    def pay_for_trip(self, trip_costs):
        self.__balance -= trip_costs

card1 = TransportCard("Нургиза")
card2 = TransportCard("Алмаз")

print(card1.get_owner())
print(card2.get_owner())

card1 = TransportCard("Нургиза")
card2 = TransportCard("Алмаз")

card1.add_money(100)
card2.add_money(200)

print(card1.get_balance())
print(card2.get_balance())
try:
    card2.pay_for_trip(TRIP_COSTS)
except ValueError as error:
    print(error)

try:
    card1.add_money(-50)
except ValueError as error:
    print(error)
print(card1.get_balance())
print(card2.get_balance())









