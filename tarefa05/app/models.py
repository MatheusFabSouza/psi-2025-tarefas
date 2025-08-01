from django.db import models

class Post(models.Model):
    titulo    = models.CharField(max_length=200)
    texto     = models.TextField()
    data_pub  = models.DateField()
    imagem_url = models.URLField()

    def __str__(self):
        return self.titulo

class Blog(models.Model):
    titulo = models.CharField(max_length=99)
    criador = models.CharField(max_length=99)
    email = models.EmailField(max_length=99)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.titulo