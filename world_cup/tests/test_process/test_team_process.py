from django.test import TestCase

from ...models import Team
from ...process import TeamProcess


class TeamProcessTestCase(TestCase):
    def setUp(self) -> None:
        team_1 = Team(
            pk=1,
            name='Argentina',
            flag_image='fake_flag_image',
            shield_image='fake_shield_image'
        )
        team_1.save()
        team_2 = Team(
            pk=2,
            name='España',
            flag_image='fake_flag_image',
            shield_image='fake_shield_image'
        )
        team_2.save()

    def test_create_team(self):
        data = dict(
            pk=3,
            name='Mexico',
            flag_image='fake_flag_image',
            shield_image='fake_shield_image',
        )

        result_team = TeamProcess().create(data)

        self.assertIsNotNone(
            result_team.pk,
            'Should existed a pk in result data'
        )

    def test_get_teams(self):
        expected_count_teams = 2

        result = TeamProcess().get_objects()

        self.assertEqual(
            len(result),
            expected_count_teams,
            'Should count of teams in result data equal to 2'
        )

    def test_get_team_by_id(self):
        team_id = 2
        expected_name = 'España'

        result = TeamProcess().get_by_id(team_id)

        self.assertEqual(
            result.name,
            expected_name,
            'Should be team name equal to España'
        )

    def test_update_team(self):
        team_id = 2
        data = {
            "name": "updated_name"
        }
        expected_team_name = "updated_name"

        result = TeamProcess().update(team_id, data)

        self.assertEqual(
            result.name,
            expected_team_name,
            'Team name in result data should be "updated_name"'
        )

    def test_delete_team(self):
        team_id = 2
        expected_count_teams = 1

        TeamProcess().delete(team_id)
        teams_count = Team.objects.count()

        self.assertEqual(
            teams_count,
            expected_count_teams,
            'Count teams should be equal to 1'
        )
