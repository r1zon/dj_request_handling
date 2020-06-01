import os
from django.shortcuts import render

from app import settings
from app.templates.timestamp_converter import timestamp_converter

def file_list(request, date = None):
    template_name = 'index.html'
    files_list = os.listdir(settings.FILES_PATH)
    files = []
    for i in range(len(files_list)):
        files.append({'name': files_list[i],
                      'ctime': timestamp_converter(os.stat('files/'+files_list[i])[9]),
                      'mtime': timestamp_converter(os.stat('files/'+files_list[i])[8]),
                      'date': ''})
    print(files)
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files
            # {'name': files}
             # 'ctime': datetime.datetime(2018, 1, 1),
             # 'mtime': datetime.datetime(2018, 1, 2)}
        # 'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    with open('files/'+ str(name), encoding='cp1251') as f:
        file = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file}
    )

