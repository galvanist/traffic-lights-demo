traffic-lights-demo
===================

Traffic Lights Demo for Raspberry Pi GPIO

Built on Raspbian (Raspberry Pi reference 2013-05-25 (armhf))
with the standard Python and modules.

Uses the PINs 7 (GPIO 4), 11 (GPIO 17) and 15 (GPIO 22)
hooked up to red, yellow and green LEDs
respectively via 280 Ohm resistors.

Follows the UK convention of traffic lights performing the following sequence:
1. Red (stop at the line)
2. Red and amber (get ready to go)
3. Green (go go go)
4. Amber (stop when possible)
5. Red (stop)

Very hacky, should modularise each step...

Firstly consider the time waiting on red+amber and amber, there may be a standard?

Randomised times on green and red, loop the sequence thrice.
