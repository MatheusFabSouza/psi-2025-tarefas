from django.db import models

class Post(models.Model):
    titulo    = models.CharField("titulo", max_length=200)
    texto     = models.TextField("texto")
    data_pub  = models.DateField("data")
    imagem_url = models.URLField("imagem")

    def __str__(self):
        return self.titulo
