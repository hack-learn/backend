from django.db import models
from teach_learn.utils.models import BaseModel
from .questions import Question

class Exam(BaseModel):
    """Exam Model"""

    title = models.CharField(max_length=50)

    description = models.CharField(max_length=200)

    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title
    

