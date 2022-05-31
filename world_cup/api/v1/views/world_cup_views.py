from rest_framework.serializers import Serializer

from ....process import (
    TeamProcess,
    BaseProcess,
    PlayerProcess,
    StaffProcess
)
from ..serializers import (
    TeamSerializer,
    UpdateTeamSerializer,
    PlayerSerializer,
    UpdatePlayerSerializer,
    StaffSerializer,
    UpdateStaffSerializer
)
from .base_views import (
    ListCreateBaseAPIView,
    GetUpdateDeleteBaseAPIView
)


class TeamsAPIView(ListCreateBaseAPIView):
    process: BaseProcess = TeamProcess
    serializer: Serializer = TeamSerializer
    messages_response = {
        'get': 'List of teams',
        'created': 'Team created',
    }


class TeamAPIView(GetUpdateDeleteBaseAPIView):
    process: BaseProcess = TeamProcess
    serializer: Serializer = TeamSerializer
    update_serializer: Serializer = UpdateTeamSerializer
    messages_response = {
        'get': 'Team data',
        'updated': 'Team updated',
        'deleted': 'Team deleted',
    }


class PlayersAPIView(ListCreateBaseAPIView):
    process: BaseProcess = PlayerProcess
    serializer: Serializer = PlayerSerializer
    messages_response = {
        'get': 'List of players',
        'created': 'Player created',
    }


class PlayerAPIView(GetUpdateDeleteBaseAPIView):
    process: BaseProcess = PlayerProcess
    serializer: Serializer = PlayerSerializer
    update_serializer: Serializer = UpdatePlayerSerializer
    messages_response = {
        'get': 'Player data',
        'updated': 'Player updated',
        'deleted': 'Player deleted',
    }


class StaffManyAPIView(ListCreateBaseAPIView):
    process: BaseProcess = StaffProcess
    serializer: Serializer = StaffSerializer
    messages_response = {
        'get': 'List of staff',
        'created': 'Staff created',
    }


class StaffAPIView(GetUpdateDeleteBaseAPIView):
    process: BaseProcess = StaffProcess
    serializer: Serializer = StaffSerializer
    update_serializer: Serializer = UpdateStaffSerializer
    messages_response = {
        'get': 'Staff data',
        'updated': 'Staff updated',
        'deleted': 'Staff deleted',
    }
