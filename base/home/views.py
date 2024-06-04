from django.http import JsonResponse
from django.shortcuts import redirect, render
from vege.models import *

def update_total(request):
    if request.is_ajax() and request.method == 'POST':
        receipe_id = request.POST.get('receipe_id')
        action = request.POST.get('action')
        receipe = Receipe.objects.get(id=receipe_id)
        total = request.session.get('total', 0.0)

        if action == 'add':
            total += receipe.receipe_price
        elif action == 'remove':
            total -= receipe.recipe_price

        request.session['total'] = total

        return JsonResponse({'total': total})


def home(request):
    queryset = Receipe.objects.all();
    total = request.session.get('total', 0.0)  
    context = {'receipes': queryset, 'total': total};
    return render(request, 'base.html', context);