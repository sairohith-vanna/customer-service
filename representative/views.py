from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from representative.serializers import RepresentativeSerializer
from representative.models import Representative

class RepresentativeDetail(APIView):

    def post(self, request):
        serializer = RepresentativeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        representatives =  Representative.objects.all()
        serializer = RepresentativeSerializer(representatives, many = True)
        return Response(serializer.data)

class RepresentativeDetails(APIView):

    def get_representative(self, rep_id) -> Representative:
        try:
            representative = Representative.objects.get(pk=rep_id)
            return representative
        except Representative.DoesNotExist:
            raise Http404

    def get(self, request, rep_id):
        try:
            representative = self.get_representative(rep_id)
            serializer = RepresentativeSerializer(representative)
            return Response(serializer.data)
        except Representative.DoesNotExist:
            raise Http404
    
    def put(self, request, rep_id):
        representative = self.get_representative(rep_id)
        serializer = RepresentativeSerializer(representative, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rep_id):
        representative = self.get_representative(rep_id)
        representative.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)