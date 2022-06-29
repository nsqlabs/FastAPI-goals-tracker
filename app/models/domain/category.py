from app.models.common import IDModelMixin, TimeTrackedModelMixin


class Category(IDModelMixin, TimeTrackedModelMixin):
    name: str
    userId: str
    description: str
