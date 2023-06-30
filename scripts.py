import random

from datacenter.models import Mark, Chastisement, Schoolkid, Commendation, Subject, Teacher, Lesson

COMMENDATION = ['Молодец', 'Умница', 'Хвалю', '5+', 'Отлично, так держать']


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject_name):
    global COMMENDATION
    year_of_study = schoolkid.year_of_study
    subject = Subject.objects.filter(title=subject_name, year_of_study=year_of_study).first()
    lesson = Lesson.objects.filter(year_of_study=year_of_study, subject=subject, group_letter='А').first()
    lesson_date = lesson.date
    teacher = lesson.teacher

    Commendation.objects.create(text=random.choice(COMMENDATION), schoolkid=schoolkid, teacher=teacher, subject=subject,
                                created=lesson_date)


if __name__ == '__main__':
    name = 'Фролов Иван Григорьевич'  # Введите ФИО ученика
    subject_name = 'Музыка'  # Введите предмет для похвалы
    schoolkid = Schoolkid.objects.filter(full_name__contains=name).first()

    fix_marks(schoolkid)  # Изменяем оценки 2 и 3 на 5
    remove_chastisements(schoolkid)  # Удаляем замечания от учителей
    create_commendation(schoolkid, subject_name)  # Добавляем похвалу для ученика
