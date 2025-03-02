import pandas as pd

def read_examples(filename):
    """Read examples from filename."""
    examples=[]
    df = pd.read_csv(filename)
    df = df.reset_index()
    for idx, row in df.iterrows():
        print(idx)
        code=row.code
        nl=row.summary   
    return examples


"""for file_path in ['test.csv', 'train.csv', 'valid.csv']:
    df = pd.read_csv(file_path)
    print(df.head(30))
    df1 = df["code"]
    df1 = df1.replace(r'\n',' ', regex=True)
    df1 = df1.replace(r'\t',' ', regex=True)
    df1 = df1.replace(r'\s', ' ', regex = True)
    df["code"] = df1
    print(df.head(30))    
    df.to_csv(file_path, index=False)"""


for file_path in ['test.csv', 'train.csv', 'valid.csv']:
    read_examples(file_path)

