

#lambda and map function
celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
fahrenheit_temps = list(map(lambda temp: (temp * 9/5) + 32, celsius_temps))
print(fahrenheit_temps)


#lambda and filter function
grades = [91, 32, 83, 44, 75, 56, 67]
passing_grades = list(filter(lambda grade: grade >= 60, grades))
print(passing_grades)