# Blake Southwood Software Engineer
# Sept 5, 2019 Silicon Valley
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

#################################
##     S W I T C H   C A S E   ##
#################################

# value you want to run thru switch case

global x
x = "word"

# =======  main  ===================================
def main():
    testfunction(x)


# =======  switch  =================================
def switch(x):
    global case
    case = x.lower()  # converts string to lowercase


# =======   fallthru       =========================
def fallthru(y):
    eval("switch('" + y + "')")


# =======   testfunction    ========================
def testfunction(x):
    print('test function testing switch case behavior')

# ========  switch case code =======================
    switch(x)                    #<<====== switch() method is here

    for i in range(1):                  #<==== loop once to use breaks
        if   case  == "one":
            print("yes it's one")
            break

        elif case  == "word":
            print ("switch case behavior works in Python now!")
            fallthru("rudolph")   #<<===== fallthru() method is here don't use break

        elif case  == "rudolph":
            print ("go reindeer")
            break

        elif case  == "phrase":
            print ("testing")
            break

        elif case in ['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("coding", case)
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
