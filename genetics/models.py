from django.db import models

class Chromosome(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Genotype(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value


class Snp(models.Model):
    rsid = models.CharField(max_length=15)
    chromosome = models.ForeignKey(Chromosome,on_delete=models.CASCADE, blank=True)
#    genotype = models.ManyToManyField(Genotype)

    def __str__(self):
        return self.rsid

class UserGenome(models.Model):
    opensnpid = models.PositiveIntegerField(blank=True, null=True)
    snp = models.ManyToManyField(Snp, through='Allele', blank=True)
    genomefile = models.FileField(upload_to='uploads/', blank=True, null=True)

    def usergenotype(self, snip):
        try:
            return self.allele_set.get(snp=snip).genotype
        except:
            return 'n/a'

    def __str__(self):
        if self.opensnpid:
            suffix = ' oID ' + str(self.opensnpid)
        else:
            suffix =''
        return 'Genome for ' + self.geneuser.user.get_full_name() + suffix


class Allele(models.Model):
    genotype=models.OneToOneField(Genotype,on_delete=models.CASCADE)
    snp = models.ForeignKey(Snp, on_delete=models.CASCADE)
    usergenome = models.ForeignKey(UserGenome, on_delete=models.CASCADE)

    def __str__(self):
        return self.snp.rsid + '=' + self.genotype.value
