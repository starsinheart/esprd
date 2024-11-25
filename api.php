<?php
header("Content-Type: application/json");

// Получение данных JSON из POST-запроса
$data = json_decode(file_get_contents("php://input"), true);

$response = [];

if (isset($data['connected'])) {
    // Обработка значения 'connected'
    // Например, вы можете сохранить состояние в файл или базу данных
    $response['status'] = 'success';
    $response['received'] = $data['connected'];
} else {
    $response['status'] = 'error';
    $response['message'] = 'Invalid request';
}

// Отправка ответа в формате JSON
echo json_encode($response);
?>