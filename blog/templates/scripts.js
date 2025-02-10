const API_URL = '/send_command/';
const SENSOR_DATA_URL = '/get_sensor_data/';

// Отправка команды на сервер
async function sendCommand(command, value) {
    console.log(`Sending command: ${command}, value: ${value}`);  // Логирование
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            'X-CSRFToken': csrfToken,
            body: JSON.stringify({ command, value })
        });
        const data = await response.json();
        document.getElementById('response').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Ошибка при отправке команды:', error);
    }
}

// Установка порога
function setThreshold(type) {
    const inputField = document.getElementById(type);
    const value = parseInt(inputField.value);
    if (!isNaN(value)) {
        sendCommand(type, value);
        inputField.value = '';
    }
}

// Получение и отображение данных с датчиков
async function fetchSensorData() {
    try {
        const response = await fetch(SENSOR_DATA_URL);
        const data = await response.json();
        if (data.status === 'success' && data.data.length > 0) {
            const latestData = data.data[0];
            animateValue('sensorValue1', latestData.sensor_value_1);
            animateValue('sensorValue2', latestData.sensor_value_2);
            animateValue('sensorValue3', latestData.sensor_value_3);
        }
    } catch (error) {
        console.error('Ошибка при получении данных:', error);
    }
}

// Анимация изменения значений
function animateValue(elementId, newValue) {
    const element = document.getElementById(elementId);
    let current = parseFloat(element.innerText) || 0;
    const delta = (newValue - current) / 10;

    const update = () => {
        current += delta;
        if (Math.abs(newValue - current) < Math.abs(delta)) {
            current = newValue;
        } else {
            requestAnimationFrame(update);
        }
        element.innerText = Math.round(current);
    };
    requestAnimationFrame(update);
}

// Инициализация графика
const ctx = document.getElementById('sensorChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [
            { label: 'Уровень воды', data: [], borderColor: 'rgb(75, 192, 192)', tension: 0.1 },
            { label: 'Влажность почвы', data: [], borderColor: 'rgb(255, 99, 132)', tension: 0.1 },
            { label: 'Освещенность', data: [], borderColor: 'rgb(54, 162, 235)', tension: 0.1 }
        ]
    },
    options: { responsive: true, scales: { y: { beginAtZero: true } } }
});

// Обновление графика
async function updateChart() {
    try {
        const response = await fetch(SENSOR_DATA_URL);
        const data = await response.json();
        if (data.status === 'success') {
            const sensorData = data.data.slice(0, 20);
            chart.data.labels = sensorData.map(d => new Date(d.timestamp).toLocaleTimeString());
            chart.data.datasets[0].data = sensorData.map(d => d.sensor_value_1);
            chart.data.datasets[1].data = sensorData.map(d => d.sensor_value_2);
            chart.data.datasets[2].data = sensorData.map(d => d.sensor_value_3);
            chart.update();
        }
    } catch (error) {
        console.error('Ошибка при обновлении графика:', error);
    }
}

// Запуск периодических задач
setInterval(fetchSensorData, 1000);
setInterval(updateChart, 5000);