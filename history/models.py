from django.db import models
from bladder_cancer.models import BladderCancer


class History(models.Model):
  hisID = models.ManyToManyField(BladderCancer)
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
  progresiva = models.CharField(max_length=255)
  recidiva = models.CharField(max_length=255)
  exitus = models.CharField(max_length=255)
  nrecidivas = models.CharField(max_length=255)
  evoldesfavorable = models.CharField(max_length=255)
  created_at = models.DateField(default=timezone.now)