from django.db import models

# Create your models here.

class Details(models.Model):
    Name = models.CharField(max_length=60)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=10)
    Message = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.Name} {self.Date}"

class Email(models.Model):
    Email = models.EmailField()
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.Email} {self.Date}"
