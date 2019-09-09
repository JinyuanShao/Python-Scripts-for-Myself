import os

class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''
    def __init__(self):
        self.path = './test'  #表示需要命名处理的文件夹

    def rename(self):
        filelist = os.listdir(self.path) #获取文件路径
        total_num = len(filelist) #获取文件长度（个数）
        i = 1  #表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.tiff'):  #定义初始图片格式是tiff
                src = os.path.join(os.path.abspath(self.path), item)
                #dst = os.path.join(os.path.abspath(self.path), ''+str(i) + '.jpg')#处理后的格式也为jpg格式的，当然这里可以改成png格式
                dst = os.path.join(os.path.abspath(self.path), 'img-' + format(str(i)) + '.PNG')      #命名为img-*.PNG格式的文件，
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



#image.save(save_dir + "img-%d.png" % image_id, "PNG")