# In February, Elmer got hired by the Acme construction company. His HR department informed 
# him that his bonus will grow every year. 
#
# His first year's Christmas bonus was going to be $B. After that, on every even year with
# the company (i.e., his 2nd, 4th, 6th years .... etc.) his bonus would increased by a growth rate r
# over the  previous year. So, he would get $B*(1+r) as his bonus in year 2,  where 0 < r < 0.05.
# On every odd year,  (i.e., his 3rd, 5th, 7th .... etc.) his bonus is calculated by adding
# $K to the bonus of the previous year. So, for example, in year 3, his bonus would be 
# $(K + B*(1+r)).
# 
# The bonus calculation will stop in year 10. From year 11 onwards, the bonus is the same
# every year as in year 10.
#
# Helpful explanation of bonus calculation is as follows:
# 
# year 1: B
# year 2: B*(1+r)
# year 3: K + B*(1+r)
# year 4: (K + B*(1+r)) * (1+r)
# year 5: K + (K + B*(1+r)) * (1+r)
# .
# .
# year 10: amount X (Calculated by the above pattern)
# year 11: amount X
# year 12: amount X
# .
# .
#
# Though the HR department did not tell Elmer the exact values of K, B and r, he became
# excited enough to want to write a function get_total_bonus(N,B,K,r) to compute the 
# total amount he was going to receive as pure bonus in N years, for any N >=1, 0<= B<= 1000,  
# 0 <= K <= 100, and rate r, 0 < r <= 0.05. 
#
# INPUT:
# initial year bonus B        : A dollar value, type: Integer
# odd year increment K        : A dollar value, type: Integer
# even year growth rate r     : A fraction value, type: Float
# number of years N           : A number, type: Integer
#
# RETURNS:
# An error value of type integer as follows:
#   -1 : if input B is less than 0 or input B is greater than 1000
#   -1: if  input K is less than 0, or input K is greater than 100
#   -1 : if input growth_rate r < 0, or growth_rate > 0.05
#   -1 : if  input number of years N is less than 0. 
#
# Or if the inputs are correct:  
#    the total bonus received in N years, type: Float
#
# (Remember that the function should return the *total* bonus received in N years,
#  not the bonus of Nth year.)
# 
# SAMPLE INPUT/OUTPUT:
#
# get_total_bonus(1,100,50,0.01) should return 100.0
# get_total_bonus(2,100,50,0.01) should return 201.0
# get_total_bonus(3,100,50,0.01) should return 352.0
# get_total_bonus(4,100,50,0.01) should return 504.51
# get_total_bonus(8,100,50,0.01) should return 1423.1706510000001
# get_total_bonus(9,100,50,0.01) should return 1730.2511020000002
# get_total_bonus(10,100,50,0.01) should return 2040.4023575100002
# get_total_bonus(11,100,50,0.01) should return 2350.5536130200003
# get_total_bonus(12,100,50,0.01) should return 2660.70486853
# get_total_bonus(16,300,10,0.02) should return 5599.3167539199985
# get_total_bonus(16,150,25,0.04) should return 3945.6419635199995
# get_total_bonus(-10,150,25,0.04) should return -1
# get_total_bonus(10,150,-25,0.04) should return -1
# get_total_bonus(10,150,25,0.3) should return -1
#

def get_total_bonus(N,B,K,r):
    if B < 0 or B > 1000:
        return -1
    if K < 0 or K > 100:
        return -1
    if r < 0 or r > .05:
        return -1
    if N < 0:
        return -1
    

    i = 2
    total = B
    bonus = total * (1+r)
    while i != N+1:
        if i > 10:
            total += bonus
            i = i+1
            continue
        if i % 2 == 0:
            if i != 2:
                bonus = bonus * (1+r)
            total += bonus
        if i % 2 != 0:
            bonus = K + bonus
            total += bonus
        i = i+1
    return total
