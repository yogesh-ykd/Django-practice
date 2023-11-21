from django.shortcuts import render
from django.http import HttpResponse

def expense_form(request):
    user1 = 100
    user2 = 100

    if request.method == 'POST':
        expense = request.POST.get('expense')
        paid_by = request.POST.get('paid_by')

        if paid_by == 'deepesh':
            half = int(expense) // 2
            user1 += half
            user2 -= half
        elif paid_by == 'yogesh':
            half = int(expense) // 2
            user1 -= half
            user2 += half
        else:
            return HttpResponse('Invalid value for paid_by')

        return render(request, 'index.html', {'user1': user1, 'user2': user2, 'expense': expense})
    else:
        # For GET requests, just render the form
        return render(request, 'index.html', {'user1': user1, 'user2': user2})

