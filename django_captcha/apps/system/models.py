from django.db import models

CATEGORIAS = (
    ('politica', ('Politica')),
    ('musica', ('Musica')),
    ('tecnologia', ('Tecnologia')),
    ('deportes', ('Deporte')),
)

class Pregunta(models.Model):
	titulo = models.CharField(max_length=50)
	contenido = models.TextField()
	categoria = models.CharField(max_length=50,choices=CATEGORIAS)

	def __unicode__(self):
		return "%s" % self.titulo

	def __str__(self):
		return "%s" % self.titulo

