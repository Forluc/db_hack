# db_hack

Скрипты позволяют изменять оценки, удалять и добавлять комментарии

## Окружение

### Требования к установке

Python3 должен быть уже установлен

### Функция fix_marks

В качестве аргумента передается объект ученика QuerySet

Функция изменяет оценки 2 и 3 на 5

### Функция remove_chastisements

В качестве аргумента передается объект ученика QuerySet

Функция удаляет записи с замечаниями от учителя ученику

### Функция create_commendation

В качестве аргумента передается ФИО ученика

Функция добавляет комментарий похвалы от учителя ученику

## Запуск файла

Запуск на Linux(Python 3) или Windows:

Скопировать нужный скрипт и вставить в shell или python console

## Цель проекта

Код был написан в образовательных целях
