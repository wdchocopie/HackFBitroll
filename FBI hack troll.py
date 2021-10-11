import time
import os
from tqdm import tqdm

os.system("cls")
print("Hack FBI tool")
ab = input("Enter Username: ")
ba = input("Enter Password: ")
print("Start hacking FBI")
time.sleep(1)
print("sending package")
for i in tqdm(range(100)):
    time.sleep(0.05)
print("injecting Trojan to database")
a = 0
for i in range(11):
    print("Injecting process: " , a ,"%")
    a = a + 10
    time.sleep(0.5)
time.sleep(0.5)
print("Successfuly Injected")
time.sleep(0.5)
a = input("Want to download FBI database? (y/n): ")
if a == str("y"):
    for i in tqdm(range(100)):
        time.sleep(0.01)
    print("File successfuly downloaded")
    time.sleep(1)
    exit()
else:
    exit()