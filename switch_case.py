# Blake Southwood Software Engineer
# Sept 5, 2019 Silicon Valley
#C and C++ and JavaScript have switch case
# and now Python has it(sort of) easier on the eyes
# then bland if elif else
# it looks nice especially in Atom and Sublime

# it's also legal and possible to use continue instead of a break
# and change the case value after the triggered case value but
# before and above using a continue do this: case = "newvalue"

#################################
##     S W I T C H   C A S E    #
#################################
#value you want to run thru switch case

x = "phrase"

case = switch(x)
while True:
    if  case  == "one":
        print("yes it's one")
        break
    elif case == "wilson":
        print ("we have a wilson winner")
        break
    elif case == "rudolph":
        print ("go reindeer")
        break
    elif case == "phrase":
        print ("testing")
        break
#default:
    else:
        print('none ')
        break
#end switch



def switch(x):
    return x.lower() #converts string to lowercase
