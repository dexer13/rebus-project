from django.db.models import Model

from ..exceptions import NotFoundException


class BaseProcess:
    model: Model = None

    def __init__(self, model: Model):
        self.model = model

    def get_objects(
            self,
            filters: dict = dict()
    ) -> list:
        values = self.model.objects.filter(**filters).all()
        return values

    def get_by_id(
            self,
            object_id: int
    ) -> Model:
        data = self.model.objects.filter(pk=object_id).first()
        if not data:
            raise NotFoundException('Data not found')
        return data

    def create(
            self,
            data: dict
    ) -> Model:
        value = self.model(**data)
        value.save()
        return value

    def update(
            self,
            object_id: int,
            data: dict
    ) -> Model:
        value = self.model.objects.filter(pk=object_id).first()
        if not value:
            raise NotFoundException('Data not found')
        self.model.objects.filter(pk=object_id).update(**data)
        return self.model.objects.filter(pk=object_id).first()

    def delete(
            self,
            object_id: int
    ) -> Model:
        value = self.model.objects.filter(pk=object_id).first()
        if not value:
            raise NotFoundException('Data not found')
        value.delete()
        return value
