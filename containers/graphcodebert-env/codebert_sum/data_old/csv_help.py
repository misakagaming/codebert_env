import pandas as pd




for file_path in ['test.csv', 'train.csv', 'valid.csv']:
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        df["code"][index] = df["code"][index].replace("\n",' ').replace("\t", ' ')
    df.to_csv(file_path, index=False) 