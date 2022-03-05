n=int(input().strip())

# def multipleSum(k,m):
#     assert k>=0 and k>=m, "k should be positive integer and grater the m"
#     sumMult=set(())
#     while(k>=m):
#         if( k%m == 0 ):
#             sumMult.add(k)
#         k=k-1    
#     return sumMult
while(n>0):
    k=int(input().strip())
    oneUnderK= k-1
    # print(oneUnderK,"ola")
    # sumThree=set(multipleSum(k-1,3))    
    # sumFive=set(multipleSum(k-1,5))
    # sumAll=sumThree.union(sumFive)
    # print(sum(sumAll))
    nForThree = int(((oneUnderK-3)/3)+1)
    nForFive = int(((oneUnderK-5)/5)+1)
    nForFifteen = int(((oneUnderK-15)/15)+1)
    # print( nForThree, nForFive, nForFifteen )
    sumForThree = int((nForThree/2)*(2*3+(nForThree-1)*3))
    sumForFive = int((nForFive/2)*(2*5+(nForFive-1)*5))
    sumForFifteen = int((nForFifteen/2)*(2*15+(nForFifteen-1)*15))
    print( sumForThree+sumForFive-sumForFifteen )
    n=n-1   