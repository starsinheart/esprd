from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .models import SensorData

logger = logging.getLogger(__name__)

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(f"Received data: {data}")

            if 'sensor_value' not in data:
                logger.warning("Missing sensor_value in request")
                return JsonResponse({'status': 'error', 'message': 'Missing sensor_value'}, status=400)

            # Сохранение данных в базе данных
            SensorData.objects.create(sensor_value=data['sensor_value'])

            return JsonResponse({'status': 'success', 'received_data': data})
        except json.JSONDecodeError:
            logger.error("Invalid JSON received")
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        
def get_data(request):
    # Retrieve data to send back to the ESP8266
    response_data = {'command': 'turn_on_led'}
    return JsonResponse(response_data)