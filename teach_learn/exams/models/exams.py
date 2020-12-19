from django.db import models
from teach_learn.utils.models import BaseModel
from .categories import Category

class Exam(BaseModel):
    """Exam Model"""

    title = models.CharField(max_length=50)

    description = models.CharField(max_length=200)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.title
    

