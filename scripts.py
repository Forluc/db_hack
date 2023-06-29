import random

from datacenter.models import Mark, Chastisement, Schoolkid, Commendation, Subject, Teacher, Lesson


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject_name):
    year_of_study = schoolkid.year_of_study
    subject = Subject.objects.filter(title=subject_name, year_of_study=year_of_study)
    subject = random.choice(subject[:])
    teacher = Teacher.objects.all()
    teacher = random.choice(teacher[:])
    lesson = Lesson.objects.filter(year_of_study=year_of_study, subject=subject)
    lesson_date = random.choice(lesson[:]).date

    Commendation.objects.create(text='Молодец!', schoolkid=schoolkid, teacher=teacher, subject=subject,
                                created=lesson_date)


if __name__ == '__main__':
    name = 'Фролов Иван Григорьевич'
    subject_name = 'Музыка'
    schoolkid = Schoolkid.objects.filter(full_name__contains=name).first()

    fix_marks(schoolkid)  # Изменяем оценки 2 и 3 на 5
    remove_chastisements(schoolkid)  # Удаляем замечания от учителей
    create_commendation(schoolkid, subject_name)  # Добавляем похвалу для ученика
