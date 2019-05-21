"""
Pentagonal numbers are generated by the formula, P_n = (n*(3n−1))/2. The first ten pentagonal numbers are:

                            1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k, for which their sum and difference are pentagonal and D = |Pk − P_j| is minimised; what is the value of D?

"""

success = False
pent = [0,1]
counter = 2
while not success:
    new_pent = counter * ( 3 * counter - 1) * 0.5
    
    for idx, value in enumerate(pent):
        diff_pent = new_pent - value
        if diff_pent in pent:
            diff_success = (idx, value, counter, new_pent, diff_pent)
            sum_pent = new_pent + value
            pent_ref = pent.copy()
            count_ref = counter
            while sum_pent > max(pent_ref):
                new_pent_ref = count_ref * ( 3 * count_ref - 1) * 0.5
                pent_ref.append(new_pent_ref)
                count_ref = count_ref + 1
            if sum_pent in pent_ref:
                sum_success = (idx, value, counter, new_pent, count_ref, sum_pent)
                print(sum_success)
                print(diff_success)
                
    pent.append(new_pent)
    counter = counter + 1
    
    if 'sum_success' in locals():
        success = True

# (1020, 1560090.0, 2167, 7042750.0, 2396, 8602840.0 )
# (1020, 1560090.0, 2167, 7042750.0, 5482660.0)
# 5482660.0