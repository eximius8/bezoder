from django.db import models

class Chromosome(models.Model):
    name = models.CharField(max_length=2)

class Genotype(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return value


class Snp(models.Model):
    rsid = models.CharField(max_length=15)
    chromosome = models.ForeignKey(Chromosome,on_delete=models.CASCADE)
    genotype = models.ManyToManyField(Genotype)

    def __str__(self):
        return rsid

class UserGenome(models.Model):
    opensnpid = models.PositiveIntegerField(blank=True)

    snp = models.ManyToManyField(Snp, through='UserGenotype')



class UserGenotype(models.Model):
    genotype=models.OneToOneField(Genotype,on_delete=models.CASCADE)
    snp = models.ForeignKey(Snp, on_delete=models.CASCADE)
    usergenome = models.ForeignKey(UserGenome, on_delete=models.CASCADE)
