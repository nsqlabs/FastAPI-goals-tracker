from typing import List
from unicodedata import category
from app.models.common import CommonOrganizationInfoModelMixin


class Goal(CommonOrganizationInfoModelMixin):
   category_id: str
   user_id: str
