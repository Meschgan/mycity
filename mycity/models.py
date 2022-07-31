from django.db import models


class Citizen(models.Model):
    PRINCE = 'Pr'
    MERCHANT = 'Merch'
    SERF = 'Serf'
    CITIZEN_TYPES = (
        (PRINCE, 'Князь'),
        (MERCHANT, 'Купец'),
        (SERF, 'Холоп')
    )

    role = models.CharField(max_length=20, choices=CITIZEN_TYPES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    income = models.PositiveIntegerField()
    boss = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return "Житель: {} {} {}".format(self.first_name, self.last_name, self.role)

