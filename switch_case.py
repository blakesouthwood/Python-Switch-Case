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
# if you forget to use a  "break" you will get an infinite loop
# unless you use a fallthru which doesn't need a break after it
# at this point you can only use one fallthru inside of a case
# remember that when using fallthru you can't have a break after it

# currently working on def fallthru_until("name"):
# so that it will be possible to fallthru a set of sequential cases
# from the current case down to and including the last case name in the set
# noted by fallthru_until("name")


#################################
##     S W I T C H   C A S E   ##
#################################

# value you want to run thru switch case

global x
x = "word"

def main():
    testfunction(x)


# =======  switch  =============================
def switch(x):
    global case
    case = x.lower()  # converts string to lowercase


# =======  fallthru =============================
def fallthru(y):
    eval("switch('" + y + "')")



def testfunction(x):
    print('test function testing switch case behavior')

# ========  switch case code =====================
    switch(x)                    #<<====== switch() method is here

    while True:                  #<<====== infinite loop to use breaks
        if   case  == "one":
            print("yes it's one")
            break

        elif case  == "word":
            print ("switch case behavior works in Python now!")
            fallthru("rudolph")   #<<===== fallthru() method is here no break

        elif case  == "rudolph":
            print ("go reindeer")
            break

        elif case  == "phrase":
            print ("testing")
            break

        elif case  == "google":
            print ("coding")
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


# ====   end of switch case  ====================


if __name__ == "__main__":
    main()
