class Pycon:
    
    pycon_id = 0
    total_age = 0

    def __init__(self, name, age) -> None:
        Pycon.pycon_id += 1
        self.id = Pycon.pycon_id
        self.name = name
        self.age = age

        Pycon.total_age += age

    def __str__(self) -> str:
        return f'Id: {self.id} || Tên: {self.name} || Tuổi: {self.age}'

    def nhap():
        pycon_name = input()
        pycon_age = int(input())
        
        return Pycon(pycon_name, pycon_age)

    @classmethod
    def averAge(cls):
        if cls.pycon_id == 0:
            return 0
        return cls.total_age / cls.pycon_id

n = int(input())
for _ in range(n):
    pycon = Pycon.nhap()
    print(pycon)

average_age = Pycon.averAge()
print(f'Trung bình tuổi: {Pycon.averAge()}')