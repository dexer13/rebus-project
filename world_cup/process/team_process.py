from ..models import Team
from .base_process import BaseProcess


class TeamProcess(BaseProcess):
    def __init__(self):
        super(TeamProcess, self).__init__(Team)

    def count(self) -> int:
        return Team.objects.count()
