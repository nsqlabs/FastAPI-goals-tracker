from app.models.common import CommonOrganizationInfoModelMixin


class Project(CommonOrganizationInfoModelMixin):
   goal_id: str
   user_id: str
