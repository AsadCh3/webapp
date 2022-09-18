from django.db import models

# Create your models here.
class Test(models.Model):
	name = models.CharField(max_length=20),

	def __str__(self):
		return self.name

class Blog(models.Model):
	name = models.CharField(max_length=45)

	def __str__(self):
		return self.name 

class Elespectador(models.Model):
	title = models.CharField(max_length=1000)
	category = models.CharField(max_length=100)
	dateCreated = models.DateTimeField(auto_now_add=True, null=True)
	date = models.DateField(max_length=100, null=True)
	source = models.CharField(max_length=100)
	url = models.CharField(max_length=1000)

	def __str__(self):
		return self.title






















































# class ElespectadorPolitica(models.Model):
# 	title = models.CharField(max_length=1000)
# 	date = models.CharField(max_length=100)
# 	source = models.CharField(max_length=100)
# 	url = models.CharField(max_length=1000)

# 	def __str__(self):
# 		return self.title


# class ElespectadorOpinion(models.Model):
# 	title = models.CharField(max_length=1000)
# 	date = models.CharField(max_length=100)
# 	source = models.CharField(max_length=100)
# 	url = models.CharField(max_length=1000)

# 	def __str__(self):
# 		return self.title



# class ElespectadorJudicial(models.Model):
# 	title = models.CharField(max_length=1000)
# 	date = models.CharField(max_length=100)
# 	source = models.CharField(max_length=100)
# 	url = models.CharField(max_length=1000)

# 	def __str__(self):
# 		return self.title



# class ElespectadorEntretenimiento(models.Model):
# 	title = models.CharField(max_length=1000)
# 	date = models.CharField(max_length=100)
# 	source = models.CharField(max_length=100)
# 	url = models.CharField(max_length=1000)

# 	def __str__(self):
# 		return self.title




# class ElespectadorEntretenimiento(models.Model):
# 	title = models.CharField(max_length=1000)
# 	date = models.CharField(max_length=100)
# 	source = models.CharField(max_length=100)
# 	url = models.CharField(max_length=1000)

# 	def __str__(self):
# 		return self.title









