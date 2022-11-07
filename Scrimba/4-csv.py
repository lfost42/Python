csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

friends_list = csv.replace(';',',').replace(':',',').split(',')

print(friends_list)