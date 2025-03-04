import sys
nos = [1,2,3,4,5,6,7,9,10]
valstop = len(nos) -1
for it, i in enumerate(nos):
    nxtvalexp = i + 1
    nxtvalitr = it + 1
    if(nxtvalitr <= valstop):
        if(nxtvalexp == nos[it+1]):
            pass
        else:
            print("there is mismatch at ",nos[it+1] , "which expected value should be ",nxtvalexp )
            break
    else:
        print("End of validation, All Numbers are in correct Sequence")
