from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):    
    pass

class Phone(Field):
    # Клас для зберігання номера телефону. Має валідацію формату (10 цифр). Необов'язкове поле з телефоном та таких один запис Record може містити декілька.    
    def __init__(self, value):
        if len(value) == 10 and (int(value) > 0):
            super().__init__(value)
        else:
            raise ValueError


class Record:
    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []        
          
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]
        
    def edit_phone(self, old_phone: str, new_phone: str):
        if old_phone in [p.value for p in self.phones]:
            for phone in self.phones:           
                if phone.value == old_phone:
                    self.phones.remove(phone)
                    self.phones.append(Phone(new_phone))
        else:
            raise ValueError            
        
    def find_phone(self, phone):
        for p in self.phones:            
            if p.value == phone:
                return p        
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        
    def add_record(self, record: Record):
        # метод add_record додає запис до self.data
        self.data[record.name.value] = record
    
    def find(self, name):
        # метод find знаходить запис за ім'ям
        return self.data.get(name)
    
    def delete(self, name):
        # метод delete видаляє запис за ім'ям
        self.data.pop(name, None)
    
    
