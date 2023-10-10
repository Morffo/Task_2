from catalog import converters, views

from django.urls import path, re_path, register_converter


register_converter(converters.SimpleConverter, "lol")

urlpatterns = [
    path("", views.item_list),
    path("<int:item_id>/", views.item_detail),
    re_path(r"^re/(?P<item_id>[1-9][\d*]*)/$", views.re_item_detail),
    path("converter/<lol:item_id>/", views.converted_item_detail),
]
