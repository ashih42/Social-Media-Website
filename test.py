class Ass:

    @classmethod
    def new(cls, **kwargs):
        a = cls()
        for key, value in kwargs.items():
            setattr(a, key, value)
        return a

a = Ass.new(name='joe', age=8)
print(a)
print(a.name)
print(a.age)