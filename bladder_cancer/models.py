from django.db import models

class BladderCancer(models.Model):
  dni = models.CharField(max_length=80, unique=True)
  edad = models.IntegerField()
  sexo = models.CharField(max_length=10)
  fechacir = models.DateField()
  obesidad = models.CharField(max_length=255)
  hta = models.CharField(max_length=255)
  dm = models.CharField(max_length=255)
  tabaco = models.CharField(max_length=255)
  hereda = models.CharField(max_length=255)
  expoprofesional = models.CharField(max_length=255)
  clinica = models.CharField(max_length=255)
  citologias = models.CharField(max_length=255)
  numtumores = models.IntegerField()
  tamtumoral = models.CharField(max_length=255)
  aspectotumoral = models.CharField(max_length=255)
  estadotumoralclinico = models.CharField(max_length=255)
  acarsinoinsitu = models.CharField(max_length=255)
  gradotumoral = models.CharField(max_length=255)
  permiacionvascular = models.CharField(max_length=255)
  carcinomaUrotelial = models.CharField(max_length=255)
  fhistoatipicas = models.CharField(max_length=255)
  primario = models.CharField(max_length=255)
  recidivante = models.CharField(max_length=255)
  instalacionprevia = models.CharField(max_length=255)
  tac = models.CharField(max_length=255)
  rtu = models.CharField(max_length=255)
  progresiva = models.CharField(max_length=255, blank=True)
  recidiva = models.CharField(max_length=255, blank=True)
  exitus = models.CharField(max_length=255, blank=True)
  nrecidivas = models.CharField(max_length=255, blank=True)
  evoldesfavorable = models.CharField(max_length=255, blank=True)
  is_active = models.BooleanField(default=True)

