import pandas as pd
df = pd.read_parquet('globalterrorismdb')
dim = df.shape
lt, step = 0, dim[0]//10
cnt = 1
print(dim)
while lt <= dim[0]+1:
    #print(df.iloc[:lt+step, :].shape)
    if dim[0]-(lt+step) > 10:
        df.iloc[lt:lt+step, :].to_csv('globalterrorismdb_{}'.format(cnt))
        #print("Still Inside", dim[0]-lt, lt, lt+step, df.iloc[lt:lt+step, :].shape[0])
        lt += step 
    else:
        df.iloc[lt:dim[0], :].to_csv('globalterrorismdb_{}'.format(cnt))
        #print("Now Outside", dim[0]-lt, lt, lt+step, df.iloc[lt:dim[0], :].shape[0])
        lt += step + (dim[0]-lt)
    cnt += 1
    #print(dim[0]-lt, lt, lt+step, df.iloc[lt:lt+step, :].shape[0])
    #lt += step 
# print(df.shape)