from django.urls import path, register_converter
from datetime import datetime

class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> datetime:
        print('to_python', value)
        return datetime.strptime(value, "%Y-%m-%d").date()

    def to_url(self, value: datetime) -> str:
        print('to_url', value)
        return value.strftime("%Y-%m-%d")

from app.views import file_list, file_content

register_converter(DateConverter, 'dt')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dt:date>/', file_list, name='file_list'),
    path('files/<name>/', file_content, name='file_content'),
]
