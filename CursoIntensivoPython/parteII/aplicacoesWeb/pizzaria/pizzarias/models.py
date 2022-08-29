from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Armazena os nomes das pizzas"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """retorna o nome da pizza"""
        return self.name

class Topping(models.Model):
    """Ingredientes do sabor da pizza"""
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name 