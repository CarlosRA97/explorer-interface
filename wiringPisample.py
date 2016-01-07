# GPIO port numbers
import wiringpi2 as wiringpi
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(25, 0) # sets GPIO 25 to input
wiringpi.pinMode(24, 1) # sets GPIO 24 to output
wiringpi.pinMode(18, 2) # sets GPIO 18 to PWM mode

# wiringpi numbers
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()
wiringpi.pinMode(6, 0) # sets WP pin 6 to input
wiringpi.pinMode(5, 1) # sets WP pin 5 to output
wiringpi.pinMode(1, 2) # sets WP pin 1 to PWM mode

# Physical P1 header pin numbers
import wiringpi2 as wiringpi
wiringPiSetupPhys()
wiringpi.pinMode(22, 0) # sets P1 pin 22 to input
wiringpi.pinMode(18, 1) # sets P1 pin 18 to output
wiringpi.pinMode(12, 2) # sets P1 pin 12 to PWM mode
