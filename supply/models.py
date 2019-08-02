from django.db import models

# Create your models here.


class Distillate(models.Model):
    name = models.CharField(max_length=60, blank=True)  # distillate name
    quantity_volume = models.DecimalField(decimal_places=4, max_digits=20, blank=True, null=True)
    source_from = models.CharField(max_length=60, blank=True)
    strain_type = models.CharField(max_length=60, blank=True)
    date_received = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    purity_source = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    purity_third_party = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    purity_in_house_test = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
