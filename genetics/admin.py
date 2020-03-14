from django.contrib import admin
from genetics.models import Genotype, Snp, Chromosome, UserGenome, Allele


admin.site.register(Genotype)
admin.site.register(Chromosome)
admin.site.register(Snp)
admin.site.register(UserGenome)
admin.site.register(Allele)
