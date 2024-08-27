from django.db import models

# Create your models here.  
class Base(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.title


class Assessment(Base):
    course = models.OneToOneField(Course, related_name="assessment", on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    comments = models.TextField(blank=True)
    note = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self) -> str:
        return f'{self.name} avaliou o curso {self.course} com nota {self.note}' 

