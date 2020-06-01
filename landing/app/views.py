from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    click = request.GET.get('from-landing')
    if click == 'original':
        counter_click['landing'] += 1
    elif click == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')

def landing(request):
    landing = request.GET.get('ab-test-arg')
    if landing == 'original':
        counter_show['landing'] += 1
        return render_to_response('landing.html')
    elif landing == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')

def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    try:
        test_conversion = round(counter_click['test']/counter_show['test'], 2)
    except ZeroDivisionError:
        test_conversion = 0
    try:
        original_conversion = round(counter_click['landing'] / counter_show['landing'],2)
    except ZeroDivisionError:
        original_conversion = 0
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
