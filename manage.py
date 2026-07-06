# Сохраните как manage.py и запускайте: python manage.py runserver
import os, sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.db import models
from django.core.management import execute_from_command_line

# --- Конфигурация Django ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
settings.configure(
    DEBUG=True,
    SECRET_KEY='dev-key-only',
    ROOT_URLCONF=__name__,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
    ],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    }],
)

# --- Модель ---
class UserName(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# --- Форма ---
class NameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя', 'style': 'padding:8px; width:250px;'})
        }

# --- Представления (views) ---
def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(f'?name={obj.name}')
    else:
        form = NameForm()

    greeting_name = request.GET.get('name')
    html = """
    <html>
      <head><title>Приветствие</title></head>
      <body style="font-family: Arial; text-align: center; padding: 40px;">
        <h1>Добро пожаловать!</h1>
        %s
        <form method="post">
          {% csrf_token %}
          {{ form.as_p }}
          <button type="submit" style="padding:10px 20px; font-size:16px;">Submit</button>
        </form>
      </body>
    </html>
    """ % (f'<h2>Привет, {greeting_name}!</h2>' if greeting_name else '<p>Введите имя, чтобы получить приветствие.</p>')

    # Рендер с поддержкой CSRF (упрощённо)
    from django.template import Context, Template
    template = Template(html)
    context = Context({'form': form})
    return HttpResponse(template.render(context))

# --- URL-маршруты ---
urlpatterns = [path('', index)]

# --- Точка входа ---
if __name__ == '__main__':
    # Если передали аргументы (например, runserver) — выполняем команду Django
    if len(sys.argv) > 1:
        execute_from_command_line(sys.argv)
    else:
        # По умолчанию запускаем сервер
        execute_from_command_line(['manage.py', 'migrate'])
        print('Сервер запущен: http://127.0.0.1:8000')
        execute_from_command_line(['manage.py', 'runserver'])
