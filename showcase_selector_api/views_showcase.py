from rest_framework import viewsets
from rest_framework.response import Response
from .filters_showcase import showcase_filter, filter_showcase_itens
from .models_showcase import (
    Showcase,
    PageRoute,
)
from .serializers_showcase import ShowCaseSerializer, PageRouteSerializer


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
