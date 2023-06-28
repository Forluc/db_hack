import random

from datacenter.models import Mark, Chastisement, Schoolkid, Commendation, Subject, Teacher


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=name)
    try:
        schoolkid = schoolkid[1]
        return False
    except:
        if schoolkid[0]:
            schoolkid = schoolkid[0]
            year_of_study = schoolkid.year_of_study
            subjects = Subject.objects.filter(year_of_study=year_of_study)
            teacher = Teacher.objects.all()
            teacher = random.choice(teacher[:])
            date = random.choice(['2018-09-15', '2018-09-20', '2018-09-21', '2018-09-22', '2018-09-23'])
            text = random.choice(['Молодец', 'Умничка', 'Молоток', 'Все сделал правильно', '5+'])

            for subject in subjects:
                Commendation.objects.create(text=text, schoolkid=schoolkid, teacher=teacher, subject=subject,
                                            created=date)
            return True
        else:
            return False


if __name__ == '__main__':
    if create_commendation('Фролов Иван Григорьевич'):
        print('Записи созданы')
    else:
        print('Введите корректное уникальное ФИО')
