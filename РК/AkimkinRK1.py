# используется для сортировки
from operator import itemgetter

class Teacher():
    def __init__(self, id, name, lastname, midname, selary, course_id):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.midname = midname
        self.selary = selary
        self.course_id = course_id

class Course():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TC():
    def __init__(self, teach_id, cour_id):
        self.teach_id = teach_id
        self.cour_id = cour_id

courses = [
    Course(1, 'РИП'),
    Course(2, 'БКИТ'),
    Course(3, 'Вычислительные средства АСОиУ'),
    Course(4, 'Схемотехника дискретных устройств'),
]

teachers = [  
    Teacher(1, 'Юрий', 'Гапанюк', 'Евгеньевич', 80000, 1),
    Teacher(2, 'Юрий', 'Гапанюк',  'Евгеньевич',80000, 2),
    Teacher(3, 'Сергей', 'Спиридонов', 'Борисович', 100000, 3),
    Teacher(4, 'Сергей', 'Спиридонов', 'Борисович', 100000, 4),
    Teacher(5, 'Андрей', 'Аксенов', 'Николаевич', 75000, 3),
    Teacher(6, 'Андрей', 'Аксенов', 'Николаевич', 75000, 4),
]

teach_cour = [
    TC(1,1),
    TC(1,2),
    TC(3,3),
    TC(3,4),
]

def main():
	
    print()
    print('Акимкин М. Г., ИУ5ц-72Б, РИП, РК1')
    print()
	
    # Соединение данных один-ко-многим 
    one_to_many = [(e.name, e.lastname, d.name) 
        for d in courses 
        for e in teachers 
        if e.course_id == d.id]

    print()
    print('Задание Б1')
    print(sorted(one_to_many, key=itemgetter(0)))
    
    # Соединение данных один-ко-многим 
    one_to_many_2 = set()

    for i in courses:
        arr = ['', 0]
        for j in teachers:
            if j.course_id == i.id:
                if arr[0] == '':
                    arr[0] = i.name
                    arr[1] += 1
                else:
                    arr[1] += 1
                    continue
        one_to_many_2.add((arr[0], arr[1]))

    print()
    print('Задание Б2')
    print(sorted(one_to_many_2, key=itemgetter(1)))

    many_to_many = {}

    for i in teach_cour:
        length = len(teachers[i.cour_id-1].lastname)
        #print(teachers[i.cour_id-1].lastname[length-1])
        if courses[i.cour_id-1].name in many_to_many.keys():
            if teachers[i.cour_id-1].lastname[length-1] == 'в' and teachers[i.cour_id-1].lastname[length-2] == 'о':
                many_to_many[courses[i.cour_id-1].name].add((teachers[i.cour_id-1].name, teachers[i.cour_id-1].lastname, teachers[i.cour_id-1].midname))
        else:
            if teachers[i.cour_id-1].lastname[length-1] == 'в' and teachers[i.cour_id-1].lastname[length-2] == 'о':
                many_to_many[courses[i.cour_id-1].name] = set()
                many_to_many[courses[i.cour_id-1].name].add((teachers[i.cour_id-1].name, teachers[i.cour_id-1].lastname, teachers[i.cour_id-1].midname))
            
    print()
    print('Задание Б3')
    print(many_to_many)
    
    
if __name__ == '__main__':
    main()