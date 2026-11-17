
from abc import ABC, abstractmethod


# Базовый класс
class HospitalObject:
    def __init__(self, id, name, x, y):
        self._id = id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


# Интерфейс лечения
class Healer(ABC):
    @abstractmethod
    def treat(self, patient):
        pass


# Интерфейс перемещения
class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


# Класс пациента
class Patient(HospitalObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        self._hp = hp

    def is_alive(self):
        return self._hp > 0

    def get_hp(self):
        return self._hp

    def receive_damage(self, damage):
        self._hp = max(0, self._hp - damage)

    def receive_treatment(self, amount):
        self._hp = min(100, self._hp + amount)


# Класс врача
class Doctor(HospitalObject, Healer, Moveable):
    def treat(self, patient):
        if patient.is_alive():
            patient.receive_treatment(20)
            print(f"Врач {self._name} лечит {patient._name}")

    def move(self, x, y):
        self._x = x
        self._y = y
        print(f"Врач {self._name} переместился в ({x}, {y})")


# Базовый класс здания
class Building(HospitalObject):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y)
        self._built = built

    def is_built(self):
        return self._built


# Медицинский центр
class MedicalCenter(Building, Healer):
    def treat(self, patient):
        if patient.is_alive():
            patient.receive_treatment(10)
            print(f"Медицинский центр {self._name} оказывает помощь")


# Передвижная клиника
class MobileClinic(Building, Moveable):
    def move(self, x, y):
        self._x = x
        self._y = y
        print(f"Клиника {self._name} переместилась в ({x}, {y})")


# Общая функция для перемещения объектов
def move_object(obj, x, y):
    obj.move(x, y)


# Проверка работы программы
if __name__ == "__main__":

    patient = Patient(1, "Иван", 10, 20, 50)
    doctor = Doctor(2, "Александр", 5, 10)

    center = MedicalCenter(
        3, "Главный медицинский центр", 30, 40, True
    )

    clinic = MobileClinic(
        4, "Мобильная клиника", 50, 60, True
    )

    print("Пациент:", patient.get_name())
    print("Здоровье:", patient.get_hp())

    patient.receive_damage(10)
    print("После ухудшения состояния:", patient.get_hp())

    doctor.treat(patient)
    center.treat(patient)

    print("Здоровье после лечения:", patient.get_hp())

    move_object(doctor, 15, 25)
    move_object(clinic, 100, 100)

    print("Центр построен:", center.is_built())
