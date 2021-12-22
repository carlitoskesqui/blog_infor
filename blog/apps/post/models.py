from django.db import models


class Post(models.Model):
	titulo = models.CharField(max_length=250)
	cuerpo = models.CharField(max_length=250)
	fecha_creacion = models.TimeField(auto_now_add=True)
	autor= models.CharField(max_length=100)
	thumbnail = models.ImageField()

	class Meta:
		db_table="post"
