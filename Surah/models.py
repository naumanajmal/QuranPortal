from django.db import models

# Create your models here.

class Surah(models.Model):
    number = models.IntegerField(null=True, blank=True)
    arabic = models.TextField(null=True, blank=True)
    urdu = models.TextField(null=True, blank=True)
    english = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Surah {self.urdu}"

class Ayat(models.Model):
    number = models.IntegerField(null=True, blank=True)
    surah = models.ForeignKey(
        Surah, on_delete=models.CASCADE)
    urdu = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Ayat {self.number} of Surah {self.surah.urdu}"

class Word(models.Model):
    number = models.IntegerField(null=True, blank=True)
    ayat = models.ForeignKey(
        Ayat, on_delete=models.CASCADE)
    arabic = models.TextField(null=True, blank=True)
    urdu = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Word {self.number} of Ayat {self.ayat.urdu}"

