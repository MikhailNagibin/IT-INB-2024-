F = open("passwords.md", "w")
A = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_-+=<>/|,.'`~[]{}”:;'\\"
for x in range (len(A)):
    first_symbol = A[x]
    for y in range(len(A)):
        second_symbol = A[y]
        for z in range(len(A)):
            third_symbol = A[z]
            End = first_symbol + second_symbol + third_symbol
            F.write(End)
            F.write("\n")

