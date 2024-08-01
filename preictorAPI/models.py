from django.db import models

"""
battery_power   :       500     ..  3000
blue            :       0           1
clock_speed     :       0.1   0.2   ..  3
dual_sim        :       0           1
fc              :       1   2   ..  90
four_g          :       0           1
int_memory      :       1   2   ..  90
m_dep           :       0.1   0.2   ..  1
mobile_wt       :       50      ..  90
n_cores         :       1   2   ..  90
pc              :       1   2   ..  90
px_height       :       20     ..  3000
px_width        :       500     ..  3000
ram             :       500     ..  3000
sc_h            :       1   2   ..  90
sc_w            :       1   2   ..  90
talk_time       :       1   2   ..  90
three_g         :       0           1
touch_screen    :       0           1
wifi            :       0           1
price_range     :       1   2   3   4



""" 

class Device(models.Model):
    battery_power = models.IntegerField()
    blue = models.BooleanField()
    clock_speed = models.FloatField()
    dual_sim = models.BooleanField()
    fc = models.IntegerField()
    four_g = models.BooleanField()
    int_memory = models.IntegerField()
    m_dep = models.FloatField()
    mobile_wt = models.IntegerField()
    n_cores = models.IntegerField()
    pc = models.IntegerField()
    px_height = models.IntegerField()
    px_width = models.IntegerField()
    ram = models.IntegerField()
    sc_h = models.IntegerField()
    sc_w = models.IntegerField()
    talk_time = models.IntegerField()
    three_g = models.BooleanField()
    touch_screen = models.BooleanField()
    wifi = models.BooleanField()
 
    def __str__(self):
        return f"Device {self.id} - RAM: {self.ram}MB "
