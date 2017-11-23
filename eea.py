int_1 = input("Please enter integer one: ")
int_2 = input("Please enter integer two: ")

if int_1 < 0 or int_2 < 0:
    print "\nError: Both integers have to be positive."
    quit()

if int_1 < int_2:
    print "\nSubstitute: " + str(int_2) + " mod " + str(int_1) + " = " + str(int_2 - int_1)
    int_2 -= int_1

q = ['-', '-']
r = [int_1, int_2]
s = [1, 0]
t = [0, 1]

print "\ni:  q_i-1:     r_i:     s_i:     t_i:  "

for i in range (0, 2):
    print '{:>2}'.format(str(i)) + "      " + '{:>2}'.format(str(q[i])) + "    " + '{:>5}'.format(str(r[i])) + "     " + '{:>4}'.format(str(s[i])) + "     " + '{:>4}'.format(str(t[i]))

i = 2

while r[i-1] != 0:
    q.append(r[i-2]/r[i-1])
    r.append(r[i-2]%r[i-1])
    s.append(s[i-2]-q[i]*s[i-1])
    t.append(t[i-2]-q[i]*t[i-1])
    print '{:>2}'.format(str(i)) + "      " + '{:>2}'.format(str(q[i])) + "    " + '{:>5}'.format(str(r[i])) + "     " + '{:>4}'.format(str(s[i])) + "     " + '{:>4}'.format(str(t[i]))
    i += 1

print "\nGCD of (" + str(int_1) + ", " + str(int_2) + "): " + str(r[i-2])

if r[i-2] == 1:
    if t[i-2] < 0:
        print "Substitute: " + str(t[i-2]) + " = " + str(t[i-2]+int_1) + " mod " + str(int_1)
        t[i-2] += int_1
    print "Inverse of " + str(int_2) + " mod " + str(int_1) + ": " + str(t[i-2])
else:
    print "Inverse of " + str(int_2) + " mod " + str(int_1) + " non-existent since GCD != 1."
