from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, item_id):
    return HttpResponse("<body>Подробно элемент</body>")


def re_item_detail(request, item_id):
    return HttpResponse(item_id)


def converted_item_detail(request, item_id):
    return HttpResponse(item_id)
