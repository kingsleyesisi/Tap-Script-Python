# Auto clicker
import os
# from time import sleep

print('WELCOME TO THE KINGS WORLD CLICKER')

taps = int(input('How many per tap: '))
coin_limit = int(input('What is your coin limit(eg. 10000): '))

number_of_tap1 = coin_limit // taps
number_of_tap = number_of_tap1 // 5

# sleep(20)
print(f'''We are tapping: {number_of_tap1} for you,
please wait while the taping is in progress''')
# remaining = number_of_tap1 - number_of_tap


for i in range(1, number_of_tap):
    # print(f" {i}. Remaining {number_of_tap1 - i} taps")
    clicker = os.system('adb shell input tap 360 802 && adb shell input tap 260 1087 && adb shell input tap 531 917 '
                        '&& adb shell input tap 350 1099 && adb shell input tap 518 837')
else:
    print('Your Tapping is   done :) see you later')
