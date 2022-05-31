from django.test import TestCase

from ...process import (
    TeamProcess,
    PlayerProcess,
    StaffProcess
)


class ResumeDataTestCase(TestCase):
    fixtures = [
        'world_cup/fixtures/test/teams.json',
        'world_cup/fixtures/test/players.json',
        'world_cup/fixtures/test/staff.json',
    ]

    def test_count_teams(self):
        expected_teams = 3

        count = TeamProcess().count()

        self.assertEqual(
            count,
            expected_teams,
            'Count teams should be 3'
        )

    def test_count_players(self):
        expected_count_players = 10

        count = PlayerProcess().count()

        self.assertEqual(
            count,
            expected_count_players,
            'Count players should be 9'
        )

    def test_get_youngest_player(self):
        expected_id = 7

        player = PlayerProcess().get_youngest_player()

        self.assertEqual(
            player.pk,
            expected_id,
            'pk of the youngest player should be 7 (Vinicius)'
        )

    def test_get_oldest_player(self):
        expected_id = 4

        player = PlayerProcess().get_oldest_player()

        self.assertEqual(
            player.pk,
            expected_id,
            'pk of the oldest player should be 4 (Messi)'
        )

    def test_count_not_first_team(self):
        expected_count = 3

        count = PlayerProcess().count_not_first_team()

        self.assertEqual(
            count,
            expected_count,
            'Count of players that are not in first team should be 3'
        )

    def test_get_average_not_first_team_by_team(self):
        expected_value = {
            'team__name': 'Brasil',
            'average_not_first_team': 0.3333333333333333
        }
        
        result = PlayerProcess().get_average_not_first_team_by_team()

        self.assertIn(
            expected_value,
            result,
            'average tha player aren not in first team of brasil should be 0.3333333333333333'
        )

    def test_get_team_with_more_players(self):
        expected_result = {
            "team__name": "Argentina",
            "count_players": 4
        }
        
        result = PlayerProcess().get_team_with_more_players()

        self.assertEqual(
            result,
            expected_result,
            'count players to argentina should be 4'
        )

    def test_get_average_age(self):
        expected_average_age = 28

        result = PlayerProcess().get_average_age()

        self.assertEqual(
            int(result),
            expected_average_age,
            'Average age should be around 27 years old'
        )

    def test_get_average_count_players_by_team(self):
        expected_value = 3.33

        result = PlayerProcess().get_average_count_players_by_team()

        self.assertEqual(
            float("{:.2f}".format(result)),
            expected_value,
            'average should be around 3.33'
        )
    
    def test_get_oldest_coach(self):
        expected_id = 5
        
        result = StaffProcess().get_oldest_coach()

        self.assertEqual(
            result.pk,
            expected_id,
            'pk expected should be 5 (Adenor (Tite))'
        )
