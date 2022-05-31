from ..models import Staff
from .base_process import BaseProcess


class StaffProcess(BaseProcess):
    def __init__(self):
        super(StaffProcess, self).__init__(Staff)

    def get_oldest_coach(self) -> Staff:
        return Staff.objects.get_oldest_coach()
