from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

def api_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Обработка данных
        print(data)  # Выводим данные в консоль для проверки
        return JsonResponse({'status': 'success', 'data': data})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def interface(request):
    return render(request, 'blog/interface.html', {})

@csrf_exempt
def api_view(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        # Process the data as needed
        return JsonResponse({'status': 'success', 'received_data': data})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})