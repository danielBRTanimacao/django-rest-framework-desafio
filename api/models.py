from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.  
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    register_number = models.BigIntegerField()
    school_serie = models.BigIntegerField()

    def __str__(self) -> str:
        return f'{self.name} registro {self.register_number}'



class StudentNote(models.Model):
    owner = models.OneToOneField(Student, on_delete=models.CASCADE)

    first_semester = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    second_semester = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    third_semester = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    four_semester = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    first_note = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    second_note = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    third_note = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    four_note = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    def __str__(self) -> str:
        return self.owner.name


@receiver(post_save, sender=Student)
def create_student_notes(sender, instance, created, **kwargs):
    if created:
        StudentNote.objects.create(owner=instance)