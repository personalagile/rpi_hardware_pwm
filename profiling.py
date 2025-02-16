from rpi_hardware_pwm import HardwarePWM
import cProfile

def main():
    # CHANGE TO CHIP 0 ON NONE PI 5 SYSTEMS
	pwm = HardwarePWM(pwm_channel=0, hz=60, chip=2)
	pwm.start(100) # full duty cycle
	pwm.change_frequency(25_000)
	for i in range(1000):
		for x in range(100):
			pwm.change_duty_cycle(x)
	pwm.stop()

# main()
cProfile.run("main()")
