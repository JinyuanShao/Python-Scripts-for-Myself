import os
import pandas as pd

operate_dir = 'G:\\original_dataset' # 执行文件夹路径
result_dir = 'G:\\rainfall_dataset'  # 保存路径

for origindir in os.listdir(operate_dir):
    singledir = os.path.join(operate_dir, origindir)
    save_dir = os.path.join(result_dir, origindir)

    for file in os.listdir(singledir):
        file = os.path.join(singledir, file) # 文件夹和文件名合并
        f = pd.read_table(file, sep='\s+', header=None) #读取文件
        f = pd.DataFrame(f) #转换成dataframe
        rows = f.shape[0]  # 确定该文件有几行
        print(f'{file} has {rows}') 
    
        year = f.iloc[0,4]  # 确定文件的年份
        print(f'{file} indicates {year}')
    
        month = f.iloc[0,5] # 确定月份
        print(f'{file} has month{month}')
        days = f.iloc[:,6].max(axis=0)+1 # 确定这个月份最多是多少天
        print(f'this month has {days-1} days')
    

        for day in range(1,days):  # 每一天都执行：
            df = pd.DataFrame()    # 生成一个空的dataframe
        
            for row in range(rows): # 每一列都检查是否和day相等
                if f.iloc[row, 6] == day:   
                    df = df.append(f.iloc[row,:]) #相等就append到空的dataframe里
    
            df = df.drop(columns=[4,5,6,7,8,10,11,12]) # 去掉多余列
            df.replace(32700.0,0.0, inplace=True)    #去掉无效值
        
            # 保存为csv格式
            df.to_csv(f'{save_dir}\\{year}_{month}_{day}.csv', header = None, index = False)
            print(f'{year}_{month}_{day} has done!')