import requests
response = requests.get("https://api.github.com")
print(response.json())

#      Описание:
# 1) Название библиотеки: requests
# 2) Для чего она используется: В этом случае код отправляет запрос
# на сервер https://api.github.com и возвращает его данные в json формате