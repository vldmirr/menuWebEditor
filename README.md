# menuWebEditor
Прорисовка меню осуществляется с помощью тега. Вставить новое меню можно непосредственно в html шаблон  
`{% draw_menu 'World Cuisines' %}`

## Установка и настройка:

### Настройка виртуальной среды и зависимостей:
```bash
python -m venv venv
source venv/Scripts/activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Создание миграции: 
```bash
python manage.py makemigrations menu_app
python manage.py migrate
```
### Загрузка тестовых данных для демонстрации:
```bash
python manage.py loaddata data/db.json
```

### Создание суперпользователя и запуск сервера: 
```bash
python manage.py createsuperuser
python manage.py runserver
```

## Ссылки для работы с приложением:
http://localhost:8000/admin - админ панель для взаимодействия с меню

http://localhost:8000 - заглавная страница
