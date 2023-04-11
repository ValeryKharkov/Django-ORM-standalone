import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('-' * 10, 'Шаг 1', '-' * 10)
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

    print('-' * 10, 'Шаг 2', '-' * 10)
    passcards_list = Passcard.objects.all()
    print(passcards_list)

    print('-' * 10, 'Шаг 3', '-' * 10)
    viewe_passcard = passcards_list[0]
    print(f'owner_name: {viewe_passcard.owner_name}\n'
          f'passcode: {viewe_passcard.passcode}\n'
          f'created_at: {viewe_passcard.created_at}\n'
          f'is_active: {viewe_passcard.is_active}'
          )

    print('-' * 10, 'Шаг 4', '-' * 10)
    active_passcards = []
    for passcard in passcards_list:
        if passcard.is_active is True:
            active_passcards.append(passcard)

    print(f'Активных пропусков {len(active_passcards)}')


