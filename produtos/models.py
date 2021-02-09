from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=50, blank=False, null=False)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao
