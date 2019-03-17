import random
from __future__ import division



def write_onfile(solution,fermat = False,mr = False,carmichael = False):
    #s = map(str, solution)
    
    if fermat== True and mr == False and carmichael == True:
        outF = open("Carmichael_numbers_F.txt", "w")
    elif fermat == False and mr == True and carmichael == True:
        outF = open("Carmichael_numbers_MR.txt", "w")
    elif fermat== True and mr == False and carmichael == False:
        outF = open("odd_numbers_F.txt", "w")
    elif fermat == False and mr == True and carmichael == False:
        outF = open("odd_numbers_MR.txt", "w")
    #print type(solution)
    #solution1 = str(solution)
   
    #print newstr1
    
    for i in solution:
            stringa = "Number = "+str(i[0])+"\t Witnesses = "+str(i[1])+"\t Error = "+str(i[2])+"\n"
            outF.write(stringa)

        
    
        
        
       
        
        
        #outF.write("\n")
    outF.close()    


def test_fermat(n,a):
    #a = random.randint(2,n-2)
    if pow(a, n-1, n) != 1:
        return True
    return False


# Implementiamo il test di primalita'  di Miller-Rabin
def scomponi(m):
    ''' Restituisce la coppia "(d, r)" tale che "d" e' dispari e "m = d * 2^r"'''
    r = 0
    while(m%2 == 0):
        #print m
        r += 1
        m = m//2
    return m, r

def test_mr(n,a= None):
    
    d, r = scomponi(n-1)
    #a = random.randint(2,n-2)
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return False
    for _ in range(r-1):
        x = pow(x, 2, n)
        if x == 1:
            return True
        if x == n-1:
            return False
    #return True

def get_fermat_witnesses(n):
    #controllo se n è dispari 
    if n%2 == 0:
        print "n dev'essere dispari!"
        return 0
    
    witnesses_c_fermat = 0
    liar_c_fermat = 0 
    for t_num in range(2,n-1):
        if test_fermat(n,t_num):
            witnesses_c_fermat +=1 
        else:

            liar_c_fermat += 1
    #Stampa 0 non capisco perchè controlla
    #print witnesses_c_fermat
    tot = witnesses_c_fermat + liar_c_fermat
    err_fermat = 1 - witnesses_c_fermat/ tot
    #print tot
    #print witnesses_c_fermat/ tot
    return witnesses_c_fermat,err_fermat

def get_mr_witnesses(n):
    
    witnesses_c_mr = 0
    liar_c_mr =0 
    if n%2 == 0:
        print "n dev'essere dispari!"
        return 0
    for t_n in range(2,n-1):
        if test_mr(n,t_n):
            witnesses_c_mr += 1
        else:
            liar_c_mr += 1
    #print witnesses_c_mr,liar_c_mr
    tot = witnesses_c_mr+liar_c_mr
    err_mr = 1 - (witnesses_c_mr/tot)
    return witnesses_c_mr,err_mr

dispari =[x for x in xrange(2000,3000) if x%2 == 1]
witnesses_fermat = []
witnesses_f_d = []

for i in dispari:
    w_f,e_f = get_fermat_witnesses(i)
    witnesses_fermat.append([w_f,e_f])
k=0
for i in dispari:
    witnesses_f_d.append([i,witnesses_fermat[k][0],witnesses_fermat[k][1]])
    k+=1


write_onfile(witnesses_f_d,fermat = True)

witnesses_mr = []
witnesses_mr_d = []

for i in dispari: 
    w_mr,e_mr = get_mr_witnesses(i)
    witnesses_mr.append([w_mr,e_mr])
    
k=0
for i in dispari:
    witnesses_mr_d.append([i,witnesses_mr[k][0],witnesses_mr[k][1]])
    k+=1

write_onfile(witnesses_mr_d,mr = True)


carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361]


witnesses_fermat_cm = []
witnesses_f_d_cm = []


for i in carmichael_numbers: 
    w_c_f,e_c_f = get_fermat_witnesses(i)
    witnesses_fermat_cm.append([w_c_f,e_c_f])
k=0
for i in carmichael_numbers:
    witnesses_f_d_cm.append([i,witnesses_fermat_cm[k][0],witnesses_fermat_cm[k][1]])
    k+=1



write_onfile(witnesses_f_d_cm,fermat = True,carmichael = True)


witnesses_mr_cm = []
witnesses_mr_d_cm = []


for i in carmichael_numbers: 
    w_c_mr,e_c_mr = get_mr_witnesses(i)
    witnesses_mr_cm.append([w_c_mr,e_c_mr])
k=0
for i in carmichael_numbers:
    witnesses_mr_d_cm.append([i,witnesses_mr_cm[k][0],witnesses_mr_cm[k][1]])
    k+=1


write_onfile(witnesses_mr_d_cm,mr = True,carmichael = True)



