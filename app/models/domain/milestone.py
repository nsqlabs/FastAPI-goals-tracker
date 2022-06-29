from app.models.common import CommonOrganizationInfoModelMixin


class Milestone(CommonOrganizationInfoModelMixin):
   project_id: str
   user_id: str
