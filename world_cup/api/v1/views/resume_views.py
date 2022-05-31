from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ....process import (
    PlayerProcess,
    TeamProcess,
    StaffProcess
)

from ..serializers import (
    PlayerSerializer,
    StaffSerializer
)


class ResumeAPIView(APIView):
    def get(self, request):
        try:
            count_teams = TeamProcess().count()
            count_players = PlayerProcess().count()

            youngest_player = PlayerProcess().get_youngest_player()
            youngest_player = PlayerSerializer(youngest_player).data if youngest_player else None

            oldest_player = PlayerProcess().get_oldest_player()
            oldest_player = PlayerSerializer(oldest_player).data if oldest_player else None

            count_not_first_team = PlayerProcess().count_not_first_team()

            average_not_first_team = PlayerProcess().get_average_not_first_team_by_team()

            team_whit_more_player = PlayerProcess().get_team_with_more_players()

            average_players_age = PlayerProcess().get_average_age()

            average_count_players_by_team = PlayerProcess().get_average_count_players_by_team()

            oldest_coach = StaffProcess().get_oldest_coach()
            oldest_coach = StaffSerializer(oldest_coach).data if oldest_coach else None

            data = {
                'count_teams': count_teams,
                'count_players': count_players,
                'youngest_player': youngest_player,
                'oldest_player': oldest_player,
                'count_not_first_team': count_not_first_team,
                'average_not_first_team': average_not_first_team,
                'team_whit_more_player': team_whit_more_player,
                'average_players_age': average_players_age,
                'average_count_players_by_team': average_count_players_by_team,
                'oldest_coach': oldest_coach
            }
            return Response(data)
        except Exception as e:
            # capture in log
            print(e)
            return Response(
                'Internal Server Error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
