from django.db import models

class Measure(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class nameOfItem(models.Model):
    nameof = models.CharField(max_length=50)
    typeof = models.ForeignKey(Measure, on_delete=models.CASCADE)
    limited = models.FloatField()

    def __str__(self):
        return str(self.nameof)

class Commodity(models.Model):
    name = models.ForeignKey(nameOfItem, on_delete=models.CASCADE)
    quantity = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)

    @property
    def procent(self):
        return str((self.quantity/self.name.limited)*100)

    def __str__(self):
        return str(self.name)

class OutWareHouse(models.Model):
    product = models.ForeignKey(nameOfItem, on_delete=models.PROTECT)
    quantity = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)

class Personal(models.Model):
    product = models.ForeignKey(nameOfItem, on_delete=models.PROTECT)
    quantity = models.FloatField() 
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

class Useless(models.Model):
    product = models.ForeignKey(nameOfItem, on_delete=models.PROTECT)
    quantity = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

class history(models.Model):
    product = models.ForeignKey(nameOfItem, on_delete=models.PROTECT)
    quantity = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

class history_added(models.Model):
    product = models.ForeignKey(nameOfItem, on_delete=models.PROTECT)
    quantity = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']