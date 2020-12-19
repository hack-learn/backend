from django.db import models
from teach_learn.utils.models import BaseModel
from .answers import Answer
from .tags import Tag

class Question(BaseModel):
    """Exam Model"""

    title = models.CharField(max_length=50)

    description = models.CharField(max_length=200)

    component = models.CharField(max_length=200)

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
