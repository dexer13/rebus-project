from ..models import Player
from .base_process import BaseProcess


class PlayerProcess(BaseProcess):
    def __init__(self):
        super(PlayerProcess, self).__init__(Player)

    def count(self) -> int:
        return Player.objects.count()

    def get_youngest_player(self) -> Player:
        return Player.objects.get_youngest()

    def get_oldest_player(self) -> Player:
        return Player.objects.get_oldest()

    def count_not_first_team(self) -> int:
        return Player.objects.count_not_first_team()

    def get_average_not_first_team_by_team(self) -> list:
        return Player.objects.calculate_average_not_first_team_by_team()

    def get_team_with_more_players(self) -> dict:
        return Player.objects.calculate_team_with_more_players()

    def get_average_age(self) -> float:
        return Player.objects.calculate_average_age()

    def get_average_count_players_by_team(self) -> float:
        return Player.objects.calcule_average_count_players_by_team()
