from django.db import models


class Sensor(models.Model):
    sensor_name = models.CharField(max_length=200)
    sensor_description = models.TextField(max_length=500)
    sensor_com_port = models.CharField(default="COM1", max_length=10)

    def __str__(self):
        return self.sensor_name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date_time = models.DateTimeField("time at measurement")
    raw_value = models.FloatField(default=0)
