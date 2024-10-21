from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    data = {

    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Form is not valid'

    form = ContactForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/contact.html', data)