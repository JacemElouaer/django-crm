from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Lead
from .forms import *


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/home_page.html", context)


def lead_detail(request, id):
    print(id)
    try:
        lead = Lead.objects.get(id=id)
    except Lead.DoesNotExist:
        lead = None
    print(id)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        # ModelForms are great in stocking his request form
        # Then  Validate it
        if form.is_valid():
            form.save()
            print("the lead has been created")
            return redirect('/lead')

    context = {
        'form': form
    }
    return render(request, "leads/lead_create.html", context)


def lead_update(request, id):
    lead = Lead.objects.get(id=id)
    form = LeadForm(instance=lead)
    # instance is basically the lead instance that we need to update
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/lead')

    context = {
        'form': form,
        'lead': lead
    }
    return render(request, "leads/lead_update.html", context)


def lead_delete(request, id):
    lead = Lead.objects.get(id=id)
    lead.delete()
    return redirect('/lead')
