from django.db import models

class Regiao(models.Model):
    nome_regiao = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.nome_regiao)

    class  Meta:  #new
        verbose_name_plural  =  "Regioes"

class Lider(models.Model):
    nome_lider = models.CharField(max_length=200)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    foto = models.URLField()
    def __str__(self):
        return '{} | {}'.format(self.nome_lider, self.regiao)


class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=200)
    lider = models.ForeignKey(Lider, on_delete=models.CASCADE)
    numero_de_participantes = models.IntegerField(default=0)
    link = models.URLField(null=True, blank=True)
    ativo = models.Boole

    def __str__(self):
        return '{} | {} | {}'.format(self.nome_grupo, self.lider.nome_lider, self.numero_de_participantes)
