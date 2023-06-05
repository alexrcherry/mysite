from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Sensor
from .serial_utils import init_serial, read_serial

import serial


def index(request):
    sensor_list = Sensor.objects.all()
    context = {"sensor_list": sensor_list}
    return render(request, "solids/index.html", context)


def detail(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    return render(request, "solids/detail.html", {"sensor": sensor})


class ResultsView(generic.DetailView):
    model = Sensor
    template_name = "solids/results.html"


print("hello")


@csrf_exempt
def measure(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)

    try:
        reader1 = init_serial(sensor.sensor_com_port, 115200)
        read_serial(reader1)
        print(sensor.sensor_com_port)
    except serial.SerialException:
        return HttpResponse("COM port unavailable")

    else:
        print("test")
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("solids:results", args=(sensor.id,)))
