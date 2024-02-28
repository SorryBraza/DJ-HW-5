# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms import model_to_dict
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        post_sensor = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'status': 'Датчик добавлен'})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        update_sensor = SensorDetailSerializer(sensor, data=request.data, partial=True)
        if update_sensor.is_valid():
            update_sensor.save()
        return Response({'status': 'Датчик обновлен'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        post_measurement = MeasurementSerializer(data=request.data, partial=True)
        if post_measurement.is_valid():
            post_measurement.save()
        return Response({'status': 'Измерение температуры добавлено'})
