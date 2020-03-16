from django.db import models
from django.contrib.auth.models import User

# Criaçao do Banco de dados
class Roupas(models.Model):
    marca = models.CharField(max_length=100)
    descricao = models.TextField()
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='Roupas')
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'vestuario'