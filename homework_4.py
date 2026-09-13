class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            contact = Contact(name, phone_number)
            cls.all_contacts.append(contact)
        else:
            raise ValueError("Номер телефона должен содержать ровно 10 цифр")

ContactList.add_contact("Алина", "5551234567")

ContactList.add_contact("Бек", "12345")

print(ContactList.all_contacts)







