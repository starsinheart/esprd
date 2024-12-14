from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def post_data(request):
    logger.info(f"Received request: {request.method} {request.path}")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(f"Received data: {data}")
            return JsonResponse({'status': 'success', 'received_data': data})
        except json.JSONDecodeError:
            logger.error("Invalid JSON")
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        logger.error("Invalid request method")
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
        
def get_data(request):
    # Retrieve data to send back to the ESP8266
    response_data = {'command': 'turn_on_led'}
    return JsonResponse(response_data)