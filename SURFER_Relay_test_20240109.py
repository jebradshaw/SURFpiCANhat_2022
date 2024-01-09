# SURF Vessel GPIO Relay Board Power control test for enabling and
#disabling the Relay Control Board
import time
import RPi.GPIO as GPIO

# Pin Defninitions:
RelayBd_RST = 6 #
RelayBd_EN1 = 5 #

RelayMode = 0 # used to enable and disable the motor drivers from joystick events

# =====================================================
if __name__ == "__main__":
# =====================================================

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)# Broadcom pin-numbering scheme
    GPIO.setup(RelayBd_RST, GPIO.OUT)
    GPIO.setup(RelayBd_EN1, GPIO.OUT)

    # reset the board with both latch pins low
    GPIO.output(RelayBd_RST, GPIO.LOW)
    GPIO.output(RelayBd_EN1, GPIO.LOW)
    

    while True:                            
        # Detect current relay mode (toggles for test)
        if RelayMode == 0:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)# Broadcom pin-numbering scheme
            GPIO.setup(RelayBd_RST, GPIO.OUT)
            GPIO.setup(RelayBd_EN1, GPIO.OUT)

            # reset the board with both latch pins low            
            GPIO.output(RelayBd_EN1, GPIO.LOW)

        if RelayMode == 1:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)# Broadcom pin-numbering scheme            
            GPIO.setup(RelayBd_RST, GPIO.OUT)
            GPIO.setup(RelayBd_EN1, GPIO.OUT)
            GPIO.output(RelayBd_RST, GPIO.LOW)
            GPIO.output(RelayBd_EN1, GPIO.LOW)
            time.sleep(.2)

            # Enable the Relay control boards
            GPIO.output(RelayBd_RST, GPIO.HIGH)
            time.sleep(.2)
            GPIO.output(RelayBd_EN1, GPIO.HIGH)
            time.sleep(.2)
            GPIO.output(RelayBd_RST, GPIO.LOW)
            time.sleep(5.0)

        time.sleep(5.0)
        
        RelayMode = not RelayMode
