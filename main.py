import os

import django

from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit

if __name__ == '__main__':

    # Программируем здесь
    print('-' * 10, 'Шаг 1', '-' * 10)
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

    print('-' * 10, 'Шаг 2', '-' * 10)
    passcards_list = Passcard.objects.all()
    print(passcards_list)

    print('-' * 10, 'Шаг 3', '-' * 10)
    viewe_passcard = Passcard.objects.all()[0]
    print(f'owner_name: {viewe_passcard.owner_name}\n'
          f'passcode: {viewe_passcard.passcode}\n'
          f'created_at: {viewe_passcard.created_at}\n'
          f'is_active: {viewe_passcard.is_active}'
          )

    print('-' * 10, 'Шаг 4', '-' * 10)
    active_passcards = []
    for passcard in Passcard.objects.all():
        if passcard.is_active is True:
            active_passcards.append(passcard)

    print(f'Всего пропусков {len(Passcard.objects.all())}')
    print(f'Активных пропусков {len(active_passcards)}')

    print('-' * 10, 'Шаг 5', '-' * 10)
    active_passcards = Passcard.objects.filter(is_active=True)
    print(f'Всего пропусков {len(Passcard.objects.all())}')
    print(f'Активных пропусков {len(active_passcards)}')

    print('-' * 10, 'Шаг 8', '-' * 10)
    visits_list = Visit.objects.all()
    print(visits_list)

    print('-' * 10, 'Шаг 9', '-' * 10)
    not_leaved_visit = Visit.objects.filter(leaved_at=None)
    print(not_leaved_visit)
    """
    print('-' * 10, 'Шаг 10', '-' * 10)  # Как я понял условия задачи, вариант №1

    for employee in active_passcards:  # Выявление каждого сотрудника с активной пасскартой
        timer = datetime.timedelta()  # Определение таймера, начало отсчета
        visit_employee = Visit.objects.filter(passcard=employee)  # Фильтрация всех визитов по ФИО сотрудника

        for visit in visit_employee:  # Выявление каждого визита сотрудника
            if visit.leaved_at is not None:  # Убрать из расчета визиты тех сотрудников, которые ещё находятся в хранилище
                delta = visit.leaved_at - visit.entered_at  # Определение время нахождения сотрудника за один визит
                timer += delta  # Суммирование время нахождения сотрудника в хранилище

            print(f'{employee} находился в хранилище\n'
                  f'с:  {moscow_time(visit.entered_at)}\n'
                  f'по: {moscow_time(visit.leaved_at)}\n'
                  f'Таймер визита: {delta}\n')

        print(f'{employee} суммарно был в хранилище {timer}\n')

    """
    print('-' * 10, 'Шаг 10', '-' * 10)  # Как я понял условия задачи, вариант №2
    for visit in not_leaved_visit:  # Определение визита сотрудника, при котором сотрудник находится в хранилище
        now = timezone.now()
        mos_time = timezone.localtime(visit.entered_at)
        delta = now - mos_time
        print(delta)

        print(f'{visit.passcard} зашёл в хранилище (по московскому времени): {mos_time}\n'
              f'Находится в хранилище: {delta}')

    print('-' * 10, 'Шаг 11', '-' * 10)
    for visit in not_leaved_visit:  # Определение визита сотрудника, при котором сотрудник находится в хранилище
        print(visit.passcard)

