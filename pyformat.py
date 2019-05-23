#!/usr/bin/python                                                                                                                                                                                           
import sys                                                                     
import subprocess                                                              
from subprocess import PIPE, Popen                                             
import os                                                                      
import re                                                                      
import time                                                                    
                                                                               
docfile="add1.txt"                                                             
script="bsh"                                                                   

def run_cmd(cmd):                                                              
    f1=open(script,"w+")                                                       
    f1.write(cmd)                                                              
    f1.close()                                                                 
    os.system("chmod 777 %s"%(script))                                         
    os.system("./%s"%(script))                                                 
    os.remove(script)                                                          
                                                                               
def adddocstring(line,file):                                                   
    fn=re.search(' (.*)\\(',line)                                              
    f_name=fn.group(1)                                                         
    p=re.search(r"\((.*?)\)", line)                                            
    params=(p.group(1)).split(',')                                             
                                                                               
    doc_string='    """\n.. function::%s\n\n'%(f_name+'('+p.group(1)+')')         
    for p in params:                                                           
        p=p.strip()                                                            
        doc_string=doc_string+"   :param::%s\n"%(p)                            
    doc_string = doc_string+"   :return [on success]::\n   :return [on failure]::\n**Example**\n\n.. code block::python\n\n.. \
    codeauthor::Dipak Wani \n\n    \"\"\"" +"\n"
                                                                               
    f= open(docfile,"w+")                                                      
    f.write("%s"%(doc_string))                                                 
    f.close()                                                                  
    cmd="sed -i -E \'/^def %s/r %s\' %s"%(f_name, docfile, file)               
    run_cmd(cmd)                                                               
    os.remove(docfile)                                                         
if __name__ == "__main__":                                                     
    file = sys.argv[1]                                                         
    with open(file) as f:                                                      
        line = f.readline()                                                    
        while line:                                                            
            if line.startswith("def"):                                         
                line1=f.readline().strip()                                     
                if not(line1.startswith("\"\"\"")):                            
                    adddocstring(line,file)                                    
            line=f.readline() 
