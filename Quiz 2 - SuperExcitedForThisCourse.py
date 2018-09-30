# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    string = ""
    i = 0
    while i < 5:
        string += "I am super excited for this course! "
        i += 1
    return string

print show_excitement()

# To remove the trailing space at the end of the 5th string, I could just loop over the string till len(string)-2
# and print it out.

 # Find the oldest Manatee in manatees.

 def example4(manatees):
 	oldest_manatee = "There is no manatee here!"

 	for i in range(len(manatees)-1):
 		oldest = manatee[i]['age']
 		j = i+1
 		if oldest < manatees[j]['age']:
 			oldest_manatee = manatee[j]
 		else:
 			oldest_manatee = oldest

 	return oldest_manatee