#   CSCI 1301 – Section: 002
#   Python Lab 5
#   References: Abir

"""
 Purpose:
    We need to write a program that can wake Road Runner 40 min before via alarm & to find the time left before alarm.
    Pre-conditions (input): 
    Hours = Alarm time input
    Minutes = Alarm time input
    Actual time = Another input that must be split
    Post-conditions (output): 
    Our outputs are the final alarm clock times and final actual time as well as the Minutes left between Actual time and Alarm time.
"""


def main():
    # Our two main pre-conditions or INPUTS.
    hours = int(input("HOURS> "))
    minutes = int(input("MINUTES> "))

    # Calculating the Alarm time hours - by using floor divison.
    alarm_timeHours = (((hours * 60) + minutes) - 40) // 60
    # Testing if after the calculation, and we got a -1, TO then set it to 23.
    if alarm_timeHours == -1:
        alarm_timeHours = 23
    # Calculating the Alarm time minutes - by using modulo.
    alarm_timeMinutes = (((hours * 60) + minutes) - 40) % 60

    # Our first print statement - I also format it to take in the Actual Time Input.
    print(
        f"Alarm Time: {alarm_timeHours:02d} {alarm_timeMinutes:02d} Actual Time: ",
        end="",
    )
    time = input()

    # I first took the third input and split it into 2 strings.
    actual_time = time.split(" ")
    # I then took the split string index and Converted it into a Integer list with map(int) - Finally converted both of them into a List.
    actual_timeIntegers = list(map(int, actual_time))
    # This next few lines are here to get the difference of actual time and alarm time (The time left till alarm)
    totaltime = (((hours * 60) + minutes) - 40) - (
        (actual_timeIntegers[0] * 60) + actual_timeIntegers[1]
    )
    actual_timeMinutes = totaltime % 60

    # Final output
    print(
        f"OUTPUT {alarm_timeHours:02d} {alarm_timeMinutes:02d}, {actual_timeMinutes} Minutes"
    )


main()

"""
Who did you collaborate with on this assignment? 
    I worked with Abir
what resource did you use?), and approximate time taken to do the assignment. 
    I used zybooks and the powerpoints.

    I took around 4 hours total to complete.
Be sure to cite any allowed external references used to complete the assignment. 
    I used this site, https://bobbyhadz.com/blog/python-split-string-into-list-of-integers - this was to learn about list(map(int))
"""
