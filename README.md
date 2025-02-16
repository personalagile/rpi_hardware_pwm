# rpi hardware pwm
![CI status](https://github.com/pioreactor/rpi_hardware_pwm/actions/workflows/ci.yaml/badge.svg)
[![PyPI version](https://badge.fury.io/py/rpi-hardware-pwm.svg)](https://badge.fury.io/py/rpi-hardware-pwm)

### Why another fork?

I just wanted to performance optimize the original code. I optimized the code from the following profile:

```
$ python profiling.py
         1200129 function calls in 2.339 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100009    0.030    0.000    0.030    0.000 <frozen codecs>:186(__init__)
        2    0.000    0.000    0.000    0.000 <frozen genericpath>:39(isdir)
   100010    0.035    0.000    0.050    0.000 <frozen posixpath>:41(_get_sep)
   100010    0.182    0.000    0.282    0.000 <frozen posixpath>:71(join)
        1    0.000    0.000    2.339    2.339 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 __init__.py:107(change_frequency)
        1    0.000    0.000    0.000    0.000 __init__.py:41(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:68(is_overlay_loaded)
        1    0.000    0.000    0.000    0.000 __init__.py:71(is_export_writable)
        1    0.000    0.000    0.000    0.000 __init__.py:74(does_pwmX_exists)
   100009    0.124    0.000    1.799    0.000 __init__.py:77(echo)
        1    0.000    0.000    0.000    0.000 __init__.py:84(start)
        1    0.000    0.000    0.000    0.000 __init__.py:88(stop)
   100005    0.218    0.000    2.299    0.000 __init__.py:92(change_duty_cycle)
        1    0.040    0.040    2.339    2.339 profiling.py:4(main)
        2    0.000    0.000    0.000    0.000 {built-in method _stat.S_ISDIR}
        1    0.000    0.000    2.339    2.339 {built-in method builtins.exec}
   100010    0.015    0.000    0.015    0.000 {built-in method builtins.isinstance}
   100009    0.956    0.000    0.986    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {built-in method posix.access}
   100010    0.011    0.000    0.011    0.000 {built-in method posix.fspath}
        2    0.000    0.000    0.000    0.000 {built-in method posix.stat}
   100009    0.675    0.000    0.675    0.000 {method '__exit__' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   100010    0.017    0.000    0.017    0.000 {method 'endswith' of 'str' objects}
   100010    0.023    0.000    0.023    0.000 {method 'startswith' of 'str' objects}
   100009    0.014    0.000    0.014    0.000 {method 'write' of '_io.TextIOWrapper' objects}
```

to this profile:

```
$ python profiling.py
         500095 function calls in 0.820 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.000    0.000    0.000    0.000 <frozen codecs>:186(__init__)
   100009    0.014    0.000    0.014    0.000 <frozen codecs>:203(reset)
        2    0.000    0.000    0.000    0.000 <frozen genericpath>:39(isdir)
        4    0.000    0.000    0.000    0.000 <frozen posixpath>:41(_get_sep)
        4    0.000    0.000    0.000    0.000 <frozen posixpath>:71(join)
        1    0.000    0.000    0.820    0.820 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:100(start)
        1    0.000    0.000    0.000    0.000 __init__.py:104(stop)
   100005    0.083    0.000    0.789    0.000 __init__.py:108(change_duty_cycle)
        2    0.000    0.000    0.000    0.000 __init__.py:120(change_frequency)
        1    0.000    0.000    0.000    0.000 __init__.py:48(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:78(__del__)
        1    0.000    0.000    0.000    0.000 __init__.py:82(is_overlay_loaded)
        1    0.000    0.000    0.000    0.000 __init__.py:85(is_export_writable)
        1    0.000    0.000    0.000    0.000 __init__.py:88(does_pwmX_exists)
   100009    0.089    0.000    0.706    0.000 __init__.py:91(echo)
        1    0.031    0.031    0.820    0.820 profiling.py:4(main)
        2    0.000    0.000    0.000    0.000 {built-in method _stat.S_ISDIR}
        1    0.000    0.000    0.820    0.820 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        3    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {built-in method posix.access}
        4    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        2    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        3    0.000    0.000    0.000    0.000 {method 'close' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
   100009    0.591    0.000    0.605    0.000 {method 'seek' of '_io.TextIOWrapper' objects}
        4    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
   100009    0.012    0.000    0.012    0.000 {method 'write' of '_io.TextIOWrapper' objects}
```

I could increase the performance from 2.339 seconds to 0.82 seconds which is an performance increase of 2.85 times. 

## Hardware PWM on Raspberry PI 5

Access the hardware PWM of a Raspberry Pi with Python. More lightweight than alternatives.

### Installation

1. On the Raspberry Pi, add `dtoverlay=pwm-2chan` to `/boot/firmware/config.txt`. This defaults to `GPIO_18` as the pin for `PWM0` and `GPIO_19` as the pin for `PWM1`.
    - Alternatively, you can change `GPIO_18` to `GPIO_12` and `GPIO_19` to `GPIO_13` using `dtoverlay=pwm-2chan,pin=12,func=4,pin2=13,func2=4`.
    - On the Pi 5, use channels 0 and 1 to control GPIO_12 and GPIO13, respectively; use channels 2 and 3 to control GPIO_18 and GPIO_19, respectively
    - On all other models, use channels 0 and 1 to control GPIO-18 and GPIO_19, respectively
2. **Reboot your Raspberry Pi**.
    - You can check everything is working on running `lsmod | grep pwm` and looking for `pwm_bcm2835`
3. Install this library: `sudo pip3 install rpi-hardware-pwm`



### Examples


> For Rpi 1,2,3,4, use chip=0; For Rpi 5, use chip=2



```python
from rpi_hardware_pwm import HardwarePWM

pwm = HardwarePWM(pwm_channel=0, hz=60, chip=0)
pwm.start(100) # full duty cycle

pwm.change_duty_cycle(50)
pwm.change_frequency(25_000)

pwm.stop()


```

### History

The original code is from [jdimpson/syspwm](https://github.com/jdimpson/syspwm), We've updated it to Python3 and
made it look like the `RPi.GPIO` library's API (but more Pythonic than that.), and we use it in [Pioreactor](https://pioreactor.com) bioreactor system.

