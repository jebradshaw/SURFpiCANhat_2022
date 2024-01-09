# SURFpiCANhat_2022
WRC Surface Vessel Raspberry Pi CAN Hat for VESC control and Relay Power Board Control

  This Surface vessel Raspberry Pi CAN HAT board is for controlling four VESC motor controllers over CAN bus for the WRC Surface Vessel designed by TSD from 2020-2023.  The board uses an MCP2515 SPI CAN controller and an MCP2561 CAN transceiver to break out to 4 JST-PH connectors for ease of cabling to the VESC motor controllers.  There is a two pin connector that uses GPIO-5 and GPIO-6 to control the power relay board for remote control of enabling power to the VESC motor controllers.  The board has the ability to interface to a Yost Labs 3-Space Nano IMU board through I2C or SPI, and also brings out an external I2C connector from the RasPi on pins GPIO-2 (SDA) and GPIO-3 (SCL).  NOTE* - These are I2C pins are accidentally swapped on U1 connector v1.1

![PCB_Snapshot](https://github.com/jebradshaw/SURFpiCANhat_2022/assets/5246863/cf995864-8840-4994-aade-0c529b141e38)

Snapshot of Printed Circuit Board from Express PCB

![SURF RasPi Hat v1 1 20240109](https://github.com/jebradshaw/SURFpiCANhat_2022/assets/5246863/22c2b551-7714-411a-9be4-bb150892ba81)
Schematic Diagram

![SURFpiCANhat_PCB_Assembled](https://github.com/jebradshaw/SURFpiCANhat_2022/assets/5246863/a934c435-7087-47a5-ba32-5a3ec37ee055)
Assembled Board Installed on RasPi 4 Surface vessel

![CAN_GPIO_Setup_SurfVessel_configTxt](https://github.com/jebradshaw/SURFpiCANhat_2022/assets/5246863/fb81ffef-6d9c-4030-9f87-dba4a796d6f7)

  Be Sure to enable SPI and update the config.txt on the RasPi to use the CAN interface.  The MCP2515 uses GPIO-12 for the Interrupt pin.  Crystal 
oscillator is 16MHz (X1) on the MCP2515.



