import shortuuid
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import Case
from .serializers import CaseSerializer



@api_view(['GET'])
def case_list(request):
    cases = Case.objects.all()
    serializer = CaseSerializer(cases, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def case_create(request):
    serializer = CaseSerializer(data=request.data)
    uuid_create = shortuuid.ShortUUID().random(length=8)
    if serializer.is_valid():
        serializer.save(uuid=uuid_create)
        return Response(serializer.data)


class CaseViewSet(viewsets.ModelViewSet):
    serializer_class = CaseSerializer
    def get_queryset(self):
        queryset = Case.objects.all()
        uuid = self.request.query_params.get('uuid')
        if uuid is not None:
            queryset = queryset.filter(uuid=uuid)
            return queryset

class DelCaseViewSet(APIView):
    serializer_class = CaseSerializer
    def delete(self, request):
        uuid = request.query_params.get('uuid')
        case_delete = get_object_or_404(Case, uuid=uuid)
        case_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)