from django.db import models
from teach_learn.utils.models import BaseModel
from .questions import Question


class Answer(BaseModel):
    """Answer Model"""

    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    descrition = models.CharField(max_length=200)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.descrition
