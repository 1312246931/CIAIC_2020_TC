from skimage import data_dir,io,transform

def convert_gray(f):

     rgb=io.imread(f)

     dst=transform.resize(rgb,(508,730))

     return dst
for i in range(1,5):
    f='C:/Users/LSP/Desktop/python学习笔记/django0814/app001/static/app001/image/就你话多/'+str(i)+'.png'
    dst=convert_gray(f)
    io.imsave('C:/Users/LSP/Desktop/python学习笔记/django0814/app001/static/app001/image/就你话多_处理后/'+str(i)+'.png',dst)