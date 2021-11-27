from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class AQIPrediction(models.Model):
	Average_Temperature=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	Maximum_Temperature=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	Minimum_Temperature=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	Atmospheric_Pressure=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1050)])
	Average_Humidity=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	Average_Visibility=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	Average_Wind_Speed=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	Maximum_Wind_Speed=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])