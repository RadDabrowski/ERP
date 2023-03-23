from django.db import models


class ModelTemp(models.Model):
    number = models.IntegerField(verbose_name='numer')
    name = models.CharField(max_length=255, verbose_name='nazwa')

    class Meta:
        abstract = True


class Segment(ModelTemp):

    def __str__(self):
        return self.name


class Category(ModelTemp):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, verbose_name='segment')

    def __str__(self):
        return self.name


class SubCategory(ModelTemp):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='kategoria')

    def __str__(self):
        return self.name
