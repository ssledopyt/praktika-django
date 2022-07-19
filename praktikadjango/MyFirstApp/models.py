from django.db import models
from django.db.models import Count


class PersonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def have_pets(self, flag):
        return self.get_queryset().filter(pets__isnull=flag)


class Person(models.Model):
    objects = PersonManager()
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


class PetManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def have_friends(self, flag):
        if flag:
            return self.get_queryset().annotate(pets_count=Count('owner__pets')).filter(pets_count__gte=2)
        else:
            return self.get_queryset().annotate(pets_count=Count('owner__pets')).filter(pets_count__lte=2)


class PetTypeManager(models.Manager):
    pass


class PetType(models.Model):
    objects = PetTypeManager()
    title = models.CharField(max_length=64, verbose_name='name', unique=True)

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.type

    class Meta:
        ordering = ['title']
        verbose_name = 'typepet'
        verbose_name_plural = 'typepet'


class Pet(models.Model):
    objects = PetManager()
    name = models.CharField(max_length=64, verbose_name='name')
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='xozain', related_name='pets')
    type = models.ForeignKey(PetType, on_delete=models.CASCADE, verbose_name='type', related_name='pets', blank=True)

    class Meta:
        ordering = ['owner']
        unique_together = ['name', 'owner']
        verbose_name = 'pet'
        verbose_name_plural = 'pets'

    def __str__(self):
        return self.name + " " + str(self.owner.id) + " " + self.owner.full_name()

    def __repr__(self):
        return self.name + " " + str(self.owner.id) + " " + self.owner.full_name()


class HomeManager(models.Manager):
    pass


class Home(models.Model):
    objects = HomeManager()
    address = models.CharField(max_length=64, verbose_name='address', unique=True)
    persons = models.ManyToManyField(Person, related_name='houses')
    pets = models.ManyToManyField(Pet, related_name='houses')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        result = super().save(force_insert, force_update, using, update_fields)
        pets = []
        for person in self.persons:
            for pet in person.pets:
                pets.append(pet)
        if self.pets in pets:
            return result
        else:
            self.delete()
            return

    def __str__(self):
        return self.address

    def __repr__(self):
        return self.address

    class Meta:
        ordering = ['address']
        verbose_name = 'house'
        verbose_name_plural = 'houses'
