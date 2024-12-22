from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SensorData, Command
from django.shortcuts import render

@csrf_exempt
def send_command(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            command = data.get('command')
            value = data.get('value')
            cmd = Command(command=command, value=value)
            cmd.save()
            return JsonResponse({'status': 'success', 'received_data': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

def get_commands(request):
    commands = Command.objects.filter(completed=False).order_by('timestamp')
    commands_data = [{'command': cmd.command, 'value': cmd.value} for cmd in commands]
    return JsonResponse({'status': 'success', 'commands': commands_data})

@csrf_exempt
def post_sensor_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sensor_value = data.get('sensor_value')
            sensor_data = SensorData(sensor_value=sensor_value)
            sensor_data.save()
            return JsonResponse({'status': 'success', 'received_data': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

def get_sensor_data(request):
    sensor_data = SensorData.objects.all().order_by('-timestamp')[:10]
    data = [{
        'sensor_value_1': d.sensor_value_1,
        'sensor_value_2': d.sensor_value_2,
        'sensor_value_3': d.sensor_value_3,
        'timestamp': d.timestamp.isoformat()
    } for d in sensor_data]
    return JsonResponse({'status': 'success', 'data': data})
    
def interface(request):
    return render(request, 'interface.html')