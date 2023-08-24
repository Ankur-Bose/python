record = 'Leo Tolstroy|1900-02-14|1965-02-14'
fields = record.split("|")      #splitting using the |
born = fields[1].split("-")     #splitting using the -
died = fields[2].split("-")
age=int(died[0])-int(born[0])

print(fields)
print("Born",born)
print("Died",died)
print("lived about",age)