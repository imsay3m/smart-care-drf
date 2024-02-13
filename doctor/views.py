from django.shortcuts import render
from rest_framework import pagination, viewsets
from .models import AvailableTime, Specialization, Designation, Doctor, Review
from .serializers import AvailableTimeSerializer, SpecializationSerializer, DesignationSerializer, DoctorSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

# Create your views here.

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get("doctor_id")
        if  doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=AvailableTime.objects.all()
    serializer_class=AvailableTimeSerializer
    filter_backends=[AvailableTimeForSpecificDoctor]

class SpecializationViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Specialization.objects.all()
    serializer_class=SpecializationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Designation.objects.all()
    serializer_class = DesignationSerializer

class DoctorPagination(pagination.PageNumberPagination):
    page_size=1 #item per page
    page_size_query_param=page_size
    max_page_size=100

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class=DoctorPagination
    filter_backends=[filters.SearchFilter]
    search_fields=['user__first_name', 'user__last_name','user__email', 'designation__name', 'specialization__name']

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer