from django.shortcuts import render


def contact(request):
    context = {}
    template = 'contact/contact.html'
    return render(request, template, context)
