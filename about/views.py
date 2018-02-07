from django.shortcuts import render


def about(request):
    context = {}
    template = 'about/about.html'
    return render(request, template, context)
