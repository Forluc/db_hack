import random

from datacenter.models import Mark, Chastisement, Schoolkid, Commendation, Subject, Teacher


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid):
    year_of_study = schoolkid.year_of_study
    subject = Subject.objects.filter(title='Музыка', year_of_study=year_of_study)  # В title ввести название предмета
    teacher = Teacher.objects.all()
    teacher = random.choice(teacher[:])

    Commendation.objects.create(text='Молодец!', schoolkid=schoolkid, teacher=teacher, subject=subject,
                                created='2018-09-15')  # Введите дату в created для добавления похвалы


if __name__ == '__main__':
    name = 'Фролов Иван Григорьевич'
    schoolkid = Schoolkid.objects.filter(full_name__contains=name).first()

    fix_marks(schoolkid)  # Изменяем оценки 2 и 3 на 5
    remove_chastisements(schoolkid)  # Удаляем замечания от учителей
    create_commendation(schoolkid)  # Добавляем похвалу для ученика
