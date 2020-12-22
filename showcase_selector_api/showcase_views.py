from rest_framework import viewsets
from rest_framework.response import Response
from .showcase_filters import showcase_filter, filter_showcase_itens
from .showcase_models import (
    Showcase,
    PageRoute,
)
from .showcase_serializers import ShowCaseSerializer, PageRouteSerializer


class PageRouterViewSet(viewsets.ModelViewSet):
    queryset = PageRoute.objects.all()
    serializer_class = PageRouteSerializer


class ShowcaseViewSet(viewsets.ModelViewSet):
    queryset = Showcase.objects.all()
    serializer_class = ShowCaseSerializer

    def list(self, request):
        queryset = showcase_filter(request.data)
        serializer = ShowCaseSerializer(queryset, many=True)
        serializer = filter_showcase_itens(request.data, serializer)
        return Response(serializer.data)
