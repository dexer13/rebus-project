from django.test import TestCase

from ...models import (
    Team,
    Staff
)
from ...process import StaffProcess


class StaffProcessTestCase(TestCase):
    def setUp(self) -> None:
        team_1 = Team(
            pk=1,
            name='Inglaterra',
            flag_image='fake_flag_image',
            shield_image='fake_shield_image',
            created_at='2022-05-30',
            updated_at='2022-05-30'
        )
        team_1.save()
        team_2 = Team(
            pk=2,
            name='Argentina',
            flag_image='fake_flag_image',
            shield_image='fake_shield_image',
            created_at='2022-05-30',
            updated_at='2022-05-30'
        )
        team_2.save()

        Staff(
            pk=101,
            name='Gareth',
            lastname='Southgate',
            birth_date='1970-09-03',
            nationality='Inglaterra',
            rol='Coach',
            team=team_1
        ).save()
        Staff(
            pk=102,
            name='Chris',
            lastname='Powell',
            birth_date='1969-09-08',
            nationality='Inglaterra',
            rol='Assistant',
            team=team_1
        ).save()
        Staff(
            pk=103,
            name='Lionel',
            lastname='Scaloni',
            birth_date='1978-05-16',
            nationality='Argentina',
            rol='Coach',
            team=team_2
        ).save()

    def test_create_staff(self):
        data = dict(
            name='Fake_name',
            lastname='Fake_last_name',
            birth_date='1999-09-09',
            nationality='Colombia',
            rol='Physical Trainer',
            team_id=1
        )

        result_staff = StaffProcess().create(data)

        self.assertIsNotNone(
            result_staff.pk,
            'Should have a pk in result data'
        )

    def test_get_staff_many(self):
        expected_count = 3

        result = StaffProcess().get_objects()

        self.assertEqual(
            len(result),
            expected_count,
            'Count of staff in result should be 3'
        )
    
    def test_get_staff_by_id(self):
        staff_id = 102
        expected_staff_name = 'Chris'
        
        result_staff = StaffProcess().get_by_id(staff_id)
        
        self.assertEqual(
            result_staff.name,
            expected_staff_name,
            'Name staff should be equal to Chris'
        )
    
    def test_update_staff(self):
        staff_id = 102
        data = {
            'name': 'name_updated'
        }
        expected_staff_name = 'name_updated'
        
        result_staff = StaffProcess().update(staff_id, data)
        
        self.assertEqual(
            result_staff.name,
            expected_staff_name,
            'Name in result should be "name_updated"'
        )

    def test_delete_staff(self):
        staff_id = 102
        expected_count = 2

        StaffProcess().delete(staff_id)
        count_staff = Staff.objects.count()

        self.assertEqual(
            count_staff,
            expected_count,
            'Count staff should be 2'
        )
        