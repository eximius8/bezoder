from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MyDNAUpdateForm
from django.contrib import messages
from .models import UserGenome
from person.models import GeneVisitor

@login_required
def mydna(request):
    if request.method == 'POST':
        GeneVisitor.objects.get_or_create(user=request.user)
        uploadgenome = MyDNAUpdateForm(request.POST, instance=request.user.genevisitor.genome)
        if uploadgenome.is_valid():
            #useGenome=UserGenome(geneuser=request.user.genevisitor, opensnpid=uploadgenome.cleaned_data['opensnpid'],genomefile=uploadgenome.cleaned_data['genomefile'])
            #useGenome.save()
            uploadgenome.save()
            messages.success(request, f'Updloaded Successfully')
            return redirect('genetics:mydna')
    else:
        uploadgenome = MyDNAUpdateForm()
    pageArray = {'form': uploadgenome}
    return render(request, 'genetics/mydna.html',pageArray)
