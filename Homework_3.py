#1
def save_shoping_list(items):
    with open ("shopping.txt","w") as file:
        for item in items:
            file.write(item+ "/n")
items = [
    "Milk",
    "Bread",
    "Apples",
    "Coffee"
]
save_shoping_list(items)

#2
import csv
with open("students.csv", "w") as file:
    file.write("name,age\n")
    file.write("Anna,21\n")
    file.write("Tom,19\n")
    file.write("Kate,22\n")

def read_students(filename):
    with open(filename,"r") as file:
        reader= csv.DictReader(file)
        for row in reader:
            print(f"Student : {row['name']}({row['age']}")
read_students("students.csv")

#3

import json

def save_profile(name,age,city):
    profile ={
        "Name":name,
        "age":age,
        "City": city
    }
    with open("profile.json","w") as file:
        json.dump(profile,file)
save_profile("Maria",30,"Haifa")
