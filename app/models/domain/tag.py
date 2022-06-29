from app.models.common import IDModelMixin


class Tag(IDModelMixin):
    name: str
    user_id: str
