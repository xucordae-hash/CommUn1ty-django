from django.shortcuts import render, redirect
from .models import FaultReport

def home(request):
    faults = FaultReport.objects.order_by('-submitted_at')[:10]
    return render(request, 'home.html', {'faults': faults})

def report_fault(request):
    if request.method == 'POST':
        FaultReport.objects.create(
            fault_type=request.POST['fault_type'],
            description=request.POST.get('description', ''),
            location=request.POST.get('location', 'Auto-detected'),
        )
        return redirect('home')
    return render(request, 'report_fault.html')
