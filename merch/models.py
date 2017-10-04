from django.db import models


WEAR_TSHIRT = 1
WEAR_SWEATER = 2
WEAR_HAT = 3
WEAR_TYPES = (
    (WEAR_TSHIRT, 'T-Shirt'),
    (WEAR_SWEATER, 'Sweater'),
    (WEAR_HAT, 'Hat')
)


DESIGN_SLOGO = 1
DESIGN_BLOGO = 2
DESIGN_TYPES = (
    (DESIGN_SLOGO, 'Small Logo'),
    (DESIGN_BLOGO, 'Big Logo')
)


# Create your models here.
class Merch(models.Model):
    wear_type = models.IntegerField(choices=WEAR_TYPES, blank=False)
    description = models.TextField(max_length=250, blank=True)
    design = models.IntegerField(choices=DESIGN_TYPES, blank=False)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
