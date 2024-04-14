from django.db import models

# Create your models here.
class Device(models.Model):
    battery_power = models.PositiveIntegerField()
    clock_speed = models.FloatField()
    int_memory = models.FloatField()
    m_dep = models.FloatField()
    mobile_wt = models.FloatField()
    n_cores = models.PositiveIntegerField()
    fc = models.FloatField()
    pc = models.FloatField()
    px_height = models.PositiveIntegerField()
    px_width = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    sc_h = models.FloatField()
    sc_w = models.FloatField()
    talk_time = models.FloatField()
    four_g = models.BooleanField(default=False)
    tree_g = models.BooleanField(default=False)
    touch_screen = models.BooleanField(default=False)
    dual_sim = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    blue = models.BooleanField(default=False)
    price_range = models.IntegerField(default=-1) 

