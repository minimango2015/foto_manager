# info python the file adopts encoding=utf-8
# encoding=utf-8
# count the title # of *jpg file
import os

#iterate folder
#deb 391 folders

def iter_folder(lst, cnt, file_set, file_expend_type, path):
    
    for sub_folder in os.listdir(path):
      #print 'L1: ' + sub_folder
      cur_path = path + sub_folder

      if os.path.isdir(cur_path) is True:

        print 'current folder: ' + cur_path
        lst.append(cur_path)
        iter_folder(lst, cnt,file_set, file_expend_type, cur_path + '\\')

      else:

        if sub_folder.lower().find(file_expend_type) > 0:
          #if the file is .jpg type, push the local + file name to list
          #print sub_folder
          cur_path = path + '\\' + sub_folder
          cnt.append(cur_path)

          if len(file_set) == 0:
              file_set.add(sub_folder.lower())
          else:
              isExit = sub_folder in file_set
              if isExit is True:
                print 'same file name exit ' + sub_folder
              else:
                file_set.add(sub_folder.lower())
 
    return
   
   

lst = list()
cnt = list()
file_set = set()
path = 'D:\Photo\\'
# set unicode to read foler name with chinese characters 
upath = unicode(path, 'utf-8')

print "---------------------------"
iter_folder(lst, cnt, file_set, '.jpg', upath)
print "---------------------------"
#for item in cnt:
  #print item
  
print 'Read # of jpg files ' + str(len(cnt))
print '# of jpg have uni name ' + str(len(file_set))
print '# of opened folder ' + str(len(lst))
for item in file_set:
    print item


