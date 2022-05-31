from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response


class HealthAPIView(APIView):
    @swagger_auto_schema(tag='Health')
    def get(self, request):
        return Response({
            'message': 'OK'
        })
