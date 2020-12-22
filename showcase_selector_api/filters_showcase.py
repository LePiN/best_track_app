from .models_showcase import Showcase


def showcase_filter(request):
    queryset = Showcase.objects.all()
    if "page_routes" in request:
        queryset = _filter_page_route(request, queryset)
    if "status_showcase" in request:
        queryset = _filter_status_showcase(request, queryset)
    return queryset


def _filter_page_route(request, queryset):
    queryset = (
        queryset.filter(routes__page_identifier__in=request["page_routes"]).distinct()
        if request["page_routes"]
        else queryset
    )
    return queryset


def _filter_status_showcase(request, queryset):
    queryset = (
        queryset.filter(status__in=request["status_showcase"]).distinct()
        if request["status_showcase"]
        else queryset
    )
    return queryset


def filter_showcase_itens(request, serializer):
    if "target_citys" in request:
        serializer = (
            _filter_itens_city(request, serializer)
            if request["target_citys"]
            else serializer
        )
    elif "target_states" in request:
        serializer = (
            _filter_itens_state(request, serializer)
            if request["target_states"]
            else serializer
        )
    elif "target_countrys" in request:
        serializer = (
            _filter_itens_country(request, serializer)
            if request["target_countrys"]
            else serializer
        )

    if "target_category" in request:
        serializer = (
            _filter_itens_category(request, serializer)
            if request["target_category"]
            else serializer
        )

    if "itens_limit" in request:
        serializer = (
            _filter_itens_limit(request, serializer)
            if request["itens_limit"]
            else serializer
        )

    if "itens_price_order" in request:
        serializer = (
            _filter_itens_price_order(request, serializer)
            if request["itens_price_order"]
            else serializer
        )
    return serializer


def _filter_itens_city(request, serializer):
    for showcase in serializer.data:
        for hotel in reversed(showcase["itens"]):
            if hotel["city"]["name"] not in request["target_citys"]:
                showcase["itens"].remove(hotel)
    return serializer


def _filter_itens_state(request, serializer):
    for showcase in serializer.data:
        for hotel in reversed(showcase["itens"]):
            if hotel["city"]["state"] not in request["target_states"]:
                showcase["itens"].remove(hotel)
    return serializer


def _filter_itens_country(request, serializer):
    for showcase in serializer.data:
        for hotel in reversed(showcase["itens"]):
            if hotel["country"]["name"] not in request["target_countrys"]:
                showcase["itens"].remove(hotel)
    return serializer


def _filter_itens_category(request, serializer):
    for showcase in serializer.data:
        for hotel in reversed(showcase["itens"]):
            if hotel["category"]["name"] not in request["target_category"]:
                showcase["itens"].remove(hotel)
    return serializer


def _filter_itens_limit(request, serializer):
    for showcase in serializer.data:
        showcase["itens"] = showcase["itens"][: request["itens_limit"]]
    return serializer


def _filter_itens_price_order(request, serializer):
    order_by = 1 if request["itens_price_order"] == "decrescent" else 0
    for showcase in serializer.data:
        showcase["itens"] = sorted(
            showcase["itens"], key=lambda hotel: hotel["price"], reverse=order_by
        )
    return serializer
