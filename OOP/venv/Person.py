from inst import Instructor # skrift kun over til andre filer hvis det bliver store klasser


class Person:
    type = 'Mammel'
    # klasse variable

    def __init__(self, *args):  # args er en tuple
        print(args)
        if len(args) == 1:
            self.name = args[0]
        if len(args) == 2:
            self.name = args[0]
            self.last = args[1]
        else:
            raise Exception()

        def full_name(self):
            return self.name + '' + self.last

        # det hedder en init metode/ ikke helt en constructer, meeeen det er en constructer

        p1 = Person('claus', 'sofa')
        print(full_name(p1))


#class Instructor:
#   def __init__(self, name):
#      self.name = name


class Gender:
    def __init__(self, s):
        self.sex = s


class Student(Instructor, Gender): # nedarvning, du kan godt arve fra flere klasser
    def __init__(self, *args):
        # super().__init__(args[0]) # super tager objektet med over
        Instructor.__init__(self, args[0]) # self er objektet, hvis vi ikke skriver self, så følger objektet ikke med
        Gender.__init__(self, args[1])
        self.salary = args[2]


student = Student('Mads', "male", 12000)
print(student.name, student.salary, student.sex)
