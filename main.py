from faker import Faker
import phonenumbers 


from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

number = "+49 176 1234 5678"
carrier._is_mobile(number_type(phonenumbers.parse(number))) 

fake = Faker('pl_PL')



#fake.profile()
fakek_profil = fake.profile()
f_name = str.split(fakek_profil["name"])[0]
f_surname = str.split(fakek_profil["name"])[1]
f_phone = fake.phone_number()
f_email = str.split(fakek_profil["mail"])[0]
f_job = str.split(fakek_profil["job"])
f_company = fake.bs()
f_businesphone = fake.phone_number()


class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
    def contact(self):
        print(f'Wybieram numer {self.phone} i dzwonie do {self.name} {self.surname}')
    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email}'
    def label_length(self):
        a = len(self.name)
        b = len(self.surname)
        c = a + b 
        print(f'Długość imienia i nazwiska to {c}')


class BusinessContact(BaseContact):
    def __init__(self, name, surname, phone, email, job, company, businesphone):
        super().__init__(name, surname, phone, email)
        self.job = job
        self.company = company
        self.businesphone = businesphone

    def contact(self):
        print(f'Wybieram numer {self.businesphone} i dzwonie do {self.name} {self.surname}')

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email} {self.job} {self.company} {self.businesphone}'

#Losowa wizytówka

types = True
amount = 29999999
def create_contacts (types, amount):
    for i in range(amount):
        fakek_profil = fake.profile()
        fk_name = str.split(fakek_profil["name"])[0]
        fk_surname = str.split(fakek_profil["name"])[1]
        fk_phone = fake.phone_number()
        fk_email = str.split(fakek_profil["mail"])[0]
        fk_job = str.split(fakek_profil["job"])
        fk_company = fake.bs()
        fk_businesphone = fake.phone_number()
        if types == True:
            private = BaseContact(name = fk_name, surname = fk_surname, phone = fk_phone, email = fk_email)
            private.contact()
        else:
            business = BusinessContact(name = fk_name, surname = fk_surname, phone = fk_phone, email = fk_email, job = fk_job, company = fk_company, businesphone = fk_businesphone)
            business.contact()
            


create_contacts(True,amount)

print("################")      
kolega = BaseContact(name = f_name, surname = f_surname, phone = f_phone, email = f_email)
kolega.contact()
#print(kolega)
kolega.label_length()

print("################")
wspolpracownik = BusinessContact(name = f_name, surname = f_surname, phone = f_phone, email = f_email, job = f_job, company = f_company, businesphone = f_businesphone)
wspolpracownik.contact()
#print(wspolpracownik)




