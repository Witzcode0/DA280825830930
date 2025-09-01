# Logical Operators:
# Used to combine conditional statements.
# and (Logical AND)
# or (Logical OR)
# not (Logical NOT)

# c1 = 10 < 20 =  True
# c2 = 20 < 10 = False

# C1 C2 C3 and or 
# T  T  T  T   T
# F  T  T  F   T
# T  F  T  F   T
# T  T  F  F   T
# F  F  F  F   F
 
# c not
# T F
# F T


c1 = 10 < 20 # True
c2 = False
c3 = 200 > 400 # False
c4 = True
c5 = 0 # False
c6 = 1 # True

# print(c1 and c2) # False
# print(c1 and c4 and c6) # True
# print(c1 or c2) # True
# print(c1 and c2 or c3)  # False
 
# print(not c6) # False

# print(not (c1 and c3 or c4 and c5 or c6) )
# (F or F) or T
# F or T = T
# F