from django.shortcuts import render


def refund(request):
    context = {}
    template = 'refund-policy/refund-policy.html'
    return render(request, template, context)
