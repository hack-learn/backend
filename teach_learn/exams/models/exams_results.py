from django.db import models
from teach_learn.utils.models import BaseModel
from teach_learn.users.models.users import User
from .exams import Exam


class Exam_Result(BaseModel):
    """Exam Model"""

    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)

    exam = models.ForeignKey(
        Exam, null=False, blank=False, on_delete=models.CASCADE)

    score = models.IntegerField(null=False)

    def __str__(self):
        return self.score
