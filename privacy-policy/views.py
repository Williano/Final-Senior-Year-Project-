from django.shortcuts import render


def privacy(request):
    context = {}
    template = 'privacy-policy/privacy-policy.html'
    return render(request, template, context)
