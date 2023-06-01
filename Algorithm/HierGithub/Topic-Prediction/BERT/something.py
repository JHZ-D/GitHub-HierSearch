# with open('pybert/dataset/159/labels.txt', 'w') as f:
#     f.write(" ".join(map(str, range(159))))
import pandas as pd
df = pd.read_csv("pybert/dataset/159/test.csv")
df.insert(1, "repo", "")
df.to_csv("pybert/dataset/159/test.csv", index=False)