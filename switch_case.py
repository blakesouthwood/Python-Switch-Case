# Blake Southwood Software Engineer
# Sept 29, 2019 Silicon Valley (updated)
# Tested with PyDev on Eclipse on Macbook pro
#C and C++ and JavaScript have switch case
# and now Python has it(sort of) easier on the eyes
# then bland if elif else
# it looks nice especially in Atom and Sublime

# it's also legal and possible to use continue instead of a break
# and change the case value after the triggered case value but
# before and above using a continue do this: case = "newvalue"
# just added fallthru() Sept 9th, 2019. if you use fallthru() don't use break in that case

# unless you use a fallthru which doesn't need a break after it
# at this point you can only use one fallthru inside of a case
# remember that when using fallthru you can't have a break after it

# break is necessary after each case statement(s) unless you use fallthru("casename")
# break is necessary after your statements at the end of the default (else:) block


# currently working on def fallthru_until("name"):
# so that it will be possible to fallthru a set of sequential cases
# from the current case down to and including the last case name in the set
# noted by fallthru_until("name")

# new feature added comparable to       case "google":
# several case names for a section      case "fishfood":
#                                       case "probability":
#
# just added elif case in ['google', 'fishfood', 'probability']:  #so large list is doable
# can also be done case == "google" or case == "fishfood": but above line is cleaner

# the switch case evolved and morphed and I just added fallthru() and multiple cases on one line
# I first wrote the switch method and then used case for the var since it's expressive and looks clean
# and I started with a while True: and changed it to a single pass loop. The loop is so breaks can be used.
# fallthru() was added after studying Swift and JavaScript switch case on Mozilla.
# The multiple cases idea came from if var in list from stack overflow.
# so in theory a listname could be used >>  elif case in mylist: (but then you can't see the contents of the list)

#################################
##     S W I T C H   C A S E   ##
#################################

# value you want to run thru switch case

global x
x = "word"                             #<<=== x must be a string just as matching case == "string", 
                                       #<<=== if using a number it will be converted to a string
                                       #<<=== so x = 22   will work and be converted to "22"
# =======  main  ===================================
def main():
    testfunction(x)


# =======  switch  =================================
def switch(x):
    if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
        x = str(x)
    global case
    case = x.lower() 


# =======   fallthru       =========================
def fallthru(y):
    eval("switch('" + y + "')")




#=====  SWITCH CASE CODE  demonstration is inside function testfunction(x) below =========

# =======   testfunction    ========================
def testfunction(x):
    print('test function testing switch case behavior')

# ========  switch case code =======================
    switch(x)                           #<<====== switch() method is here

    for i in range(1):                  #<==== loop once to allow using breaks
        if   case  == "one":
            print("yes it's one")
            break

        elif case  == "word":
            print ("switch case behavior works in Python now!")
            fallthru("rudolph")         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "rudolph":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "phrase":
            print ("testing")
            break

        elif case in ['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("coding", case)                            #<<==== I just put case here to show which word matched
            break

        elif case  == "facebook":
            print ("gui design")
            break

    #default:
        else:
            print('none')
            break         
#end loop
#end switch


# ====   end of switch case  ======================
#        end testfunction

if __name__ == "__main__":
    main()
