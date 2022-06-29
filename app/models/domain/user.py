from app.models.common import DateTimeModelMixin, IDModelMixin, TimeTrackedModelMixin


class User(DateTimeModelMixin, IDModelMixin, TimeTrackedModelMixin):
    imageUrl: str
    analytics_id: str
