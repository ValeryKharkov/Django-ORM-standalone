import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

    passcards = Passcard.objects.all()
    print(passcards)

    one_passcard = passcards[0]
    print(f'owner_name: {one_passcard.owner_name}\n'
          f'passcode: {one_passcard.passcode}\n'
          f'created_at: {one_passcard.created_at}\n'
          f'is_active: {one_passcard.is_active}\n'
          )
