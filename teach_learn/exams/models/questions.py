from django.db import models
from teach_learn.utils.models import BaseModel
from .tags import Tag
from .exams import Exam

class Question(BaseModel):
    """Exam Model"""

    title = models.CharField(max_length=50)

    description = models.CharField(max_length=200)

    component = models.CharField(max_length=200)

    difficulty = models.CharField(max_length=20)

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
