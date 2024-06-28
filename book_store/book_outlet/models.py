from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)]
    )
    author = models.CharField(max_length=100, null=True)
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.rating}) {'Best Selling' if self.is_best_selling else 'Not Best Selling'}"
