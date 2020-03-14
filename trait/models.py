from django.db import models
from genetics.models import Snp, Genotype
# doesn't work due to circular import
#from person.models import Creator


class AbstractTrait(models.Model):
    name = models.CharField(max_length=300)
    shortDescr = models.TextField(blank=True)
    creator = models.ForeignKey('person.Creator', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        abstract = True



class OneSNPTrait(AbstractTrait):
    snp = models.ForeignKey(Snp, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return "One SNP Trait: " + self.name

    def result(self, genotype):
        return self.onesnpresult_set.get(genotype=genotype)



class OneSnpResult(models.Model):
    onesnptrait = models.ForeignKey(OneSNPTrait, on_delete=models.CASCADE)
    result = models.TextField(blank=True)
    genotype = models.ManyToManyField(Genotype)

    def __str__(self):
        return 'result for ' + self.onesnptrait.name
