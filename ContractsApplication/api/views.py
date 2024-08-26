from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ContractForm as ContractForm
from .models import Contracts_completed
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string

def contract_form(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save()
            # Redirect to view contract page after saving
            return redirect('view_contract', contract_id=contract.id)
    else:
        form = ContractForm()

    return render(request, 'contract_form.html', {'form': form})

def view_contract(request, contract_id):
    contract = get_object_or_404(Contracts_completed, id=contract_id)
    return render(request, 'view_contract.html', {'contract': contract})

def edit_contract(request, contract_id):
    contract = get_object_or_404(Contracts_completed, id=contract_id)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('view_contract', contract_id=contract.id)
    else:
        form = ContractForm(instance=contract)

    return render(request, 'edit_contract.html', {'form': form, 'contract': contract})

def download_contract(request, contract_id):
    contract = get_object_or_404(Contracts_completed, id=contract_id)
    # Generate PDF
    html_string = render_to_string('contract_template.html', {'contract': contract})
    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html_string.encode('utf-8')), dest=result)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="contract_{contract.id}.pdf"'
        return response
    else:
        return HttpResponse("Error generating PDF")

def show_view(request, contract_id):
    contract = get_object_or_404(Contracts_completed, id=contract_id)
    return render(request, 'contract_template.html', {'contract': contract})

def contact_view(request):
    return render(request, 'contact.html')

def internship_agreement(request):
    return render(request, 'connect.html')