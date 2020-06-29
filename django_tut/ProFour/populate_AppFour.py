import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProFour.settings')

import django
django.setup()


import random
from AppFour.models import UserInfo
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        userinfo = UserInfo.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')
