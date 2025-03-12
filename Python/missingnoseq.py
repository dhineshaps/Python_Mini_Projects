'''
To Find the Missing Sequence. 

Taken a sample list of numbers in the list.

To Get the missing number in the sequence, used the for loop with enumerate which gives the index position
and the iterating value.

Here the validation is done by adding the 1 to the current iterate value which gives the expected 
next value in the sequence - storing it in a variable and the index value is incremented with 1 and stored in a variable.

While validating the list is accessed with incremented index value and the variable which has incremented with 1 
in current iteration.

if the both values didn't match then stop the loop and give the response

nxtvalexp == nos[it+1]
 
Multiple Validation is possible in the scenario

'''
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
