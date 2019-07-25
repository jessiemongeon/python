# This is a script to tell you some people's birthdays
# All of these people are cast members from the 90s sitcom, Seinfeld.

birthday_dictionary = {
        "Jerry Seinfeld": "April 29th, 1954",
        "Jason Alexander": "September 23rd, 1959",
        "Julia Louis-Dreyfus": "January 13th, 1961",
        "Michael Richards": "July 24th, 1949",
        "Larry David": "July 2nd, 1947",
        "Jerry Stiller": "June 8th, 1927",
        "Wayne Knight": "August 7th, 1955",
        "Estelle Harris": "April 4th, 1928",
        "John O'Hurley": "October 10th, 1954"
}


print("Welcome to the Seinfeld birthday dictionary. We know the birthdays of:")
	
for x in birthday_dictionary:
	print(x)

nameinput = raw_input("Who's birthday would you like to know?")
if nameinput == '':
	with open("birthday.txt") as f:
		list = f.readlines()
	list = [x.strip() for x in list]
	for name in list:
		if name in birthday_dictionary:
 			print(name + "'s birthday is " + birthday_dictionary[name])
		else:
       			print("Sadly, we don't have the birthday for " + name )
else:
	if nameinput in birthday_dictionary:
		print(nameinput + "'s birthday is " + birthday_dictionary[nameinput])
	else:
		print("Sadly, we don't have the birthday for " + nameinput)


