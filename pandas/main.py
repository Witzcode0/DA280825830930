# pip install pandas

import pandas as pd
import numpy as np

# print(pd.__version__)

# marks = [56, 78, 89, 40, 90]

# s = pd.Series(marks)
# s = pd.Series(marks, index=["Math", "English", "Hindi", "Science", "Python"])

# print(s)
# print(s["Hindi"])
# print(type(s))

# marks = {
#     "Math":50,
#     "English":78,
#     "Java":98,
#     "Python":67,
#     "PHP":90
# }

# s = pd.Series(marks)

s = pd.Series(np.array([1,2,3,4,5]))

# print(s)
# print(dir(s))
# print(dir(pd))
# print(s.size)
# print(s)
# print(s.min())
# print(s.max())
# print(s.mean())
# print(s.median())
# print(s.std())

subs = {
    "name": ["Java", "Python", "Php", "Html", "Css"],
    "price": [400, 500.67, 56, 54, 78],
    "pages": [400, 500, 30, 40, 50]
}

df = pd.DataFrame(subs)
df["tech"] = ["BE", "BE", "BE", "FE", "FE"]
print(df)

