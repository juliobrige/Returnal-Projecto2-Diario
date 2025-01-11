from django.db import models

# Create your models here.
class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto')

    def __str__(self):
        return self.name  

class Diario(models.Model):
    titulo = models.CharField(max_length=100)
    tags = models.TextField()
    texto = models.TextField()
    pessoas = models.ManyToManyField(Pessoa, blank=True) 
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def get_tags(self):
        return self.tags.split(',') if self.tags else []

    def set_tags(self, list_tags, reset=False):
        if not reset: 
            existing_tags = set(self.get_tags()) 
            list_tags = existing_tags.union(set(list_tags))  # União das tags existentes com as novas
        self.tags = ','.join(list_tags)  # Atualiza o campo `tags` com a lista final
