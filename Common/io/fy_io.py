# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 23:05:56 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#this file is for output and input!


#---------read a matrix file,split by  , blank etc..---------
def readfile(filename,sp='\t'):
  lines=[line for line in file(filename)]
  
  # First line is the column titles
  colnames=lines[0].strip().split(sp)[1:]
  rownames=[]
  data=[]
  for line in lines[1:]:
    p=line.strip().split(sp)
    # First column in each row is the rowname
    rownames.append(p[0])
    # The data for this row is the remainder of the row
    data.append([float(x) for x in p[1:]])
  return rownames,colnames,data
  
'''
Function:  extract and output file
Author  : deepblue
Remark  :
@create : 
@modify :
''' 
# fy_io.extractfile('blogdata.txt','blogdata_part',0,31,0,41)

def extractfile(infilename,outfilename='test.txt',cb=0,col=1,rb=0,row=1,sp='\t'): 
    lines=[line for line in file(infilename) if len(line) > row] 
    if cb>col or rb >row:
        return 'failcode = 1'
    if col < 1 or row < 1:
        return 'failcode = 2'
    outfile=[]       
    
    for line in lines[rb:row]:   
        orig = line.strip().split(sp)
        outline  = []
        for x in orig[cb:col]:
            outline.append(x)
            outline.append(sp)
        outline.pop()
        outfile.append(outline) 
        
    f = file(outfilename,'w+')  
    for line in lines[rb:row]:
        orig = line.strip().split(sp)
        for  x in orig[cb:col-1]:
            f.write(x)
            f.write(sp)            
        f.write(orig[col-1])
        f.write('\n')
    f.close()  
    
    
    return 'success'

   
                   
    
def temp():    
    f = file('test.txt','w+')
    f.write('1')
    k = 'hello it'
    f.write(k)
    f.close()
  
print 'reload fy_io'
  
  
#------------1.input a tsv file-------------
#f1 = 'D:\\Git\\python\\PCI\\chapter3\\1.txt'
#for line in file(f1):
#    print line
#lines = [line for line in file(f1)]
#print lines;
#
#colnames=lines[0].strip().split('\t')[1:]
#rownames=[]
#data=[]
#for line in lines[1:]:
#    p=line.strip().split('\t')
#    # First column in each row is the rowname
#    rownames.append(p[0])
#    # The data for this row is the remainder of the row
#    data.append([float(x) for x in p[1:]])
#
#print data[0],data[1]