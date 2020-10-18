A= ['a','b','c','d','e','f']
B= ['b','M', 'e']
count = [1,1]

for i in range(len(B)):
    c = i
    for j in range(len(A)):
        print(B[i])
        print(A[j])
        if c < len(B)-1:
            if(A[j] == B[c]):
                c+=1
            print('match',c)
    count[i] = count[i] +1

print("count", count)
