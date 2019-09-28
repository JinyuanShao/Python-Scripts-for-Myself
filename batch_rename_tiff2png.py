import os

class BatchRename():
    '''
    用于切片过的遥感图像重命名
    '''
    def __init__(self):
        self.path = './test'  #定义文件夹

    def rename(self):
        filelist = os.listdir(self.path) 
        total_num = len(filelist) 
        i = 1  #文件命名从1开始
        for item in filelist:
            if item.endswith('.tiff'):  #定义初始图片格式是tiff，其他图片格式也可以，自由选择
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'img-' + format(str(i)) + '.PNG')  #命名为img-*.PNG格式的文件，
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i-1))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
