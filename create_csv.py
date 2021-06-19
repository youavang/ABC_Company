import csv

data = [
    ["first_name","last_name","salary","dept_name","salary_increment"], 
    ["Darius","Mufutau",3901,"Finance",10],
    ["Tiger","Elliott",5489,"IT",15], 
    ["Malik","Macaulay",5444,"Sales",17],
    ["Ali","Vance",8993,"Marketing",16], 
    ["Randall","Deacon",9515,"IT",15],
    ["Josiah","Lee",8113,"Sales",17], 
    ["Dante","Mohammad",8446,"Sales",17],
    ["Wyatt","Kuame",4817,"Marketing",16], 
    ["Quinn","Oliver",5513,"Finance",10],
    ["Oliver","Gary",5158,"IT",15], 
    ["Thane","Phelan",4957,"Sales",17],
    ["Walter","Lester",3864,"Finance",10], 
    ["Samson","Dolan",6855,"IT",15],
    ["Beck","Walker",7077,"Sales",17], 
    ["Lucas","Marshall",7499,"Marketing",16], 
    ["John","Nash",4269,"IT",15], 
    ["Quinlan","Elliott",7503,"Sales",17],
    ["Ivan","Dennis",4048,"Sales",17], 
    ["Wang","Ronan",9319,"Marketing",16], 
    ["Stone","Jameson",9354,"Finance",10], 
    ["Clayton","Jarrod",4102,"IT",15], 
    ["Cain","Sean",7353,"Sales",17]]

with open('flat_data.csv', mode = 'w', newline= '') as csvfile:
     writer = csv.writer(csvfile)
     writer.writerows(data)
