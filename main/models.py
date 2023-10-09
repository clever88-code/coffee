from django.db import models




class Record(models.Model):
    name = models.CharField(unique=True, max_length=150, verbose_name='Имя')
    email = models.CharField(unique=True, max_length=150, verbose_name='Email')
    number = models.CharField(unique=True, max_length=150, verbose_name='Номер')


    class Meta:
        managed = False
        verbose_name='Заказы'
        verbose_name_plural = 'Заказы'
    def __str__(self):
        return self.name

    






