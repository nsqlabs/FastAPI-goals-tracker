from app.models.common import CommonOrganizationInfoModelMixin


class Task(CommonOrganizationInfoModelMixin):
   milestone_id: str
   user_id: str
