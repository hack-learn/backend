from django.db import models
from teach_learn.utils.models import BaseModel


class Category(BaseModel):
    """Category Model"""

    title = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title
