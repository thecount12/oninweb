from django.db import models

# Create your models here.


class Distillate(models.Model):
    name = models.CharField(max_length=60, blank=True)  # distillate name
    quantity_volume = models.DecimalField(decimal_places=4, max_digits=20, blank=True, null=True)
    source_from = models.CharField(max_length=60, blank=True)
    date_received = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    purity_source = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    purity_third_party = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    purity_in_house_test = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    unknown = models.TextField(blank=True, null=True, help_text="unknown elements in distillate")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Cartridge(models.Model):
    name = models.CharField(max_length=60, blank=True)  # brand
    cartridge_model = models.CharField(max_length=60, blank=True)
    cartridge_type = models.CharField(max_length=60, blank=True)  # .3mg .5 and 1
    sourced_from = models.CharField(max_length=60, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, help_text="cartridge review")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Batch(models.Model):
    batch_name = models.CharField(max_length=60, blank=True)  # magic batch
    distillate = models.ForeignKey(Distillate, related_name="dist_name", null=True, on_delete=models.DO_NOTHING)
    terpene_type = models.CharField(max_length=60, blank=True)
    thc = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    cbd = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    cartridge_type = models.ForeignKey(Cartridge, related_name="ct_name", null=True, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    delivery_for = models.CharField(max_length=60, blank=True)
    sold = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.batch_name

    def __str__(self):
        return self.batch_name


class Battery(models.Model):
    battery_name = models.CharField(max_length=60, blank=True)
    battery_model = models.CharField(max_length=60, blank=True)
    battery_type = models.CharField(max_length=60, blank=True)
    mah = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    sourced_from = models.CharField(max_length=60, blank=True)
    notes = models.TextField(blank=True, null=True, help_text="battery review")

    def __unicode__(self):
        return self.battery_name

    def __str__(self):
        return self.battery_name

