from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='name')
    last_name = models.CharField(max_length=64, verbose_name='last_name')

    class Meta:
        ordering = ['first_name', 'last_name']
        unique_together = ['first_name', 'last_name']
        verbose_name = 'man'
        verbose_name_plural = 'people'

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()

    def __repr__(self):
        return self.full_name()



class Pet(models.Model):
    name = models.CharField(max_length=64, verbose_name='name')
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='xozain', related_name='pets')

    class Meta:
        ordering = ['owner']
        unique_together = ['name', 'owner']
        verbose_name = 'pet'
        verbose_name_plural = 'pets'


    def __str__(self):
        return self.name + " " + str(self.owner.id) + " " + self.owner.full_name()

    def __repr__(self):
        return self.name + " " + str(self.owner.id) + " " + self.owner.full_name()