from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from employee.helper_function import count_total_experience
from employee.models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET', 'POST'])
def candidate(request):
    if request.method == 'POST':
        data = request.data
        work_expirience = data['workExperience']
        work_expirience.sort(key=lambda exper: (int(exper['start'][-4:]), int(exper['end'][-4:])))
        res = {
            'name': data['name'],
            'workExperience': work_expirience,
            'totalExperience': count_total_experience(work_expirience)[0],
            'month_remainder': count_total_experience(work_expirience)[1]
        }
        serializer = EmployeeSerializer(data=res)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    emp = Employee.objects.order_by('total_experience')
    serializer = EmployeeSerializer(emp, many=True)
    data = {"candidates": serializer.data}
    return Response(status=status.HTTP_200_OK, data=data)


# Create your views here.
