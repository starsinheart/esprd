from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .models import SensorData
from django.shortcuts import render

logger = logging.getLogger(__name__)

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(f"Received data: {data}")

            # Сохранение команды в базе данных (опционально)
            if 'command' in data:
                # Здесь можно добавить логику для обработки команды
                logger.info(f"Received command: {data['command']}")

            return JsonResponse({'status': 'success', 'received_data': data})
        except json.JSONDecodeError:
            logger.error("Invalid JSON received")
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

def get_data(request):
    # Получение данных сенсоров из базы данных
    sensor_data = SensorData.objects.all().order_by('-timestamp')[:10]  # Последние 10 записей
    data = [{'sensor_value': d.sensor_value, 'timestamp': d.timestamp} for d in sensor_data]

    # Возвращение данных в формате JSON
    return JsonResponse({'status': 'success', 'data': data})

def interface(request):
    return render(request, 'interface.html')