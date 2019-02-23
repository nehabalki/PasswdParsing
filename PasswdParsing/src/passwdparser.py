'''
Created on 22-Feb-2019

@author: Neha Balki
'''
import json
import os
from collections import OrderedDict
#Username:Password:UserID(UID):GroupID(GID):UserIDInfo:HomeDirectory:Command/shell 
#GroupName:passwd:GID:List of members,separated by commas 

while True:
    file_pswd = raw_input('Enter the path of the passwd file: \n')
    type(file_pswd)
    if os.path.exists(file_pswd):
        while True:
            file_group = raw_input('Enter the path of the group file: \n')
            type(file_group)
            if os.path.exists(file_group):
                break
            else:  
                print "File not found: "+str(file_group)+"\n" 
        break
    else:  
        print "File not found: "+str(file_pswd)+"\n"
try:
    pswd = file(file_pswd, "r" )
    member_dict = OrderedDict()
    for aLine in pswd:
        userdetails= aLine.split( ":" )   
        groupfile = file(file_group, "r" )
        groupnames = []
        group = "" 
        for aLine in groupfile:
            groups= aLine.split( ":" )
            members = groups[3].split(",")
            members[-1] = members[-1].strip()
            if userdetails[0] in members:
                groupnames.append(groups[0])     
        groupfile.close()

        info_dict = OrderedDict()
    
        info_dict["uid"] = userdetails[2]
        info_dict["full_name"] = userdetails[4]
        info_dict["groups"] = groupnames
    
        member_dict[userdetails[0]] = info_dict
    pswd.close()

    print json.dumps(member_dict, indent = 4)

except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except:
    print "Unexpected error: Please check input files."
