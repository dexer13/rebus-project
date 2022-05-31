from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from ....exceptions import NotFoundException
from ....process.team_process import BaseProcess


class ListCreateBaseAPIView(APIView):
    process: BaseProcess = None
    serializer: Serializer = None
    messages_response = {
        'get': None,
        'created': None,
    }

    def get(self, request):
        try:
            data = self.process().get_objects()
            data_serialized = [self.serializer(item).data for item in data]
            return Response({
                'data': data_serialized,
                'message': self.messages_response.get('get')
            })
        except Exception as e:
            # capture in log
            print(e)
            return Response(
                'Internal Server Error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            params = self.serializer(request.data).data
            data = self.process().create(params)
            data_serialized = self.serializer(data).data
            return Response({
                'data': data_serialized,
                'message': self.messages_response.get('created')
            })
        except Exception as e:
            # capture in log
            print(e)
            return Response(
                'Internal Server Error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetUpdateDeleteBaseAPIView(APIView):
    process: BaseProcess = None
    serializer: Serializer = None
    update_serializer: Serializer = None
    messages_response = {
        'get': None,
        'updated': None,
        'deleted': None,
    }

    def get(self, request, object_id):
        try:
            data = self.process().get_by_id(object_id)
            data_serialized = self.serializer(data).data
            return Response({
                'data': data_serialized,
                'message': self.messages_response.get('get')
            })
        except NotFoundException as e:
            return Response(
                str(e),
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            # capture in log
            print(e)
            return Response(
                'Internal Server Error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, object_id):
        try:
            data = self.update_serializer(request.data).data
            data = self.process().update(object_id, data)
            data_serialized = self.serializer(data).data

            return Response({
                'data': data_serialized,
                'message': self.messages_response.get('updated')
            })
        except NotFoundException as e:
            return Response(
                str(e),
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(e)
            return Response(
                'Internal Server Error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, object_id):
        try:
            data = self.process().delete(object_id)
            data_serializer = self.serializer(data).data
            return Response({
                'data': data_serializer,
                'message': self.messages_response.get('deleted')
            })
        except NotFoundException as e:
            return Response(
                str(e),
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            # capture in log
            print(e)
            return Response(
                'Internal Server Error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
