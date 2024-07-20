from django.shortcuts import render, redirect

from repairApp.forms import RepairForm
from repairApp.models import Repair


# Create your views here.
def repairs(request):
    if request.method == 'POST':
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user=request.user
            image=form.cleaned_data['image']
            repair.image=image
            repair.save()
            return redirect("repairs")
    repairs=Repair.objects.filter(user=request.user,car__type="Sedan").all()
    context={'repairs':repairs,'form':RepairForm()}
    return render(request,"repairs.html",context=context)