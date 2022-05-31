from django.test import TestCase

from world_cup.models import Player, Team
from world_cup.process import PlayerProcess


class PlayerProcessTestCase(TestCase):
    def setUp(self) -> None:
        team_1 = Team(
            pk=1,
            name='Argentina',
            flag_image='fake_flag_image',
            shield_image='fake_shield_image',
            created_at='2022-05-30',
            updated_at='2022-05-30'
        )
        team_1.save()
        team_2 = Team(
            pk=2,
            name='España',
            flag_image='fake_flag_image',
            shield_image='fake_shield_image',
            created_at='2022-05-30',
            updated_at='2022-05-30'
        )
        team_2.save()

        Player(
            pk=1,
            name='Lionel',
            lastname='Messi',
            birth_date='1987-05-30',
            photo='fake_photo',
            position='Forward',
            player_number=10,
            is_first_team=True,
            team=team_1
        ).save()
        Player(
            pk=2,
            name='Rodrigo',
            lastname='de Paul',
            birth_date='1994-05-24',
            photo='fake_photo',
            position='Midfielder',
            player_number=5,
            is_first_team=False,
            team=team_1
        ).save()
        Player(
            pk=3,
            name='Sergio',
            lastname='Busquets',
            birth_date='1989-05-30',
            photo='fake_photo',
            position='Midfielder',
            player_number=5,
            is_first_team=True,
            team=team_2
        ).save()

    def test_create_player(self):
        data = dict(
            pk=4,
            name='Denis',
            lastname='Gonzalez',
            birth_date='1994-10-13',
            photo='fake_photo',
            position='Midfielder',
            player_number=5,
            is_first_team=True,
            team_id=2
        )

        player_result = PlayerProcess().create(data)

        self.assertIsNotNone(player_result.pk, 'Exists pk value')

    def test_get_players(self):
        expected_count_players = 3

        result = PlayerProcess().get_objects()

        self.assertEqual(
            len(result),
            expected_count_players,
            'length of data'
        )

    def test_get_player_by_id(self):
        player_id = 2
        expected_player_name = 'Rodrigo'

        player_result = PlayerProcess().get_by_id(player_id)

        self.assertEqual(
            player_result.name,
            expected_player_name,
            'Same player name'
        )

    def test_update_player(self):
        player_id = 2
        data = {
            'name': 'updated_name'
        }
        expected_name = 'updated_name'

        player_result = PlayerProcess().update(player_id, data)

        self.assertEqual(
            player_result.name,
            expected_name
        )

    def test_delete_player(self):
        player_id = 3
        expected_count_players = 2

        PlayerProcess().delete(player_id)
        count_player = Player.objects.all().count()

        self.assertEqual(
            count_player,
            expected_count_players,
            'Player count'
        )
