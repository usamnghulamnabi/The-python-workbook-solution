"""The following table lists the sound level in decibels for several common noises.
Noise Decibel Level
Jackhammer   130 dB
Gas Lawnmower  106 dB
Alarm Clock  70 dB
Quiet Room 40 dB
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the value is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table."""

user = int(input("Enter the sound level in decibels: "))

if user > 130:
    print("The sound level is higher than Jackhammer.")

if user == 130:
    print("Jackhammer")

if user < 130 and user > 106:
    print("The sound level is between Jackhammer and Gas Lawnmower.")

if user == 106:
    print("Gas Lawnmower")

if user < 106 and user > 70:
    print("The sound level is between Gas Lawnmower and Alarm clock.")

if user == 70:
    print("Alarm Clock.")

if user < 70 and user > 40:
    print("The sound level is between Alarm clock and Quiet room.")

if user == 40:
    print("Quite room.")

if user < 40:
    print("The sound level is less than a quite room.")


