from django.shortcuts import render
from django.http import HttpResponse

def calculate_square(request):
    try:
        if request.method == 'POST':
            number = int(request.POST.get('number'))
            result = number ** 2
            return HttpResponse(f"The square of {number} is {result}.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

    return render(request, 'index.html')


