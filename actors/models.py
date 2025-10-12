from django.db import models


NATIONALITY_CHOICE = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
)


class Actor(models.Model):
    name = models.CharField()
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        choices=NATIONALITY_CHOICE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
