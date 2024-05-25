import os
import datetime
import xml.etree.ElementTree as ET
import logging

def get_file_names(path):
    # Check if the path exists and is a directory
    if os.path.isdir(path):
        # List all files in the directoryzz
        files = os.listdir(path)
        return files
    else:
        logging.error("The provided path (%s) is not a directory", path)
        # print("Error: The provided path is not a directory.")
        return []
    

def has_repeated_immediate_child_tags(root):
    seen_tags = set() 
    for child in root:
        tag_name = child.tag
        if tag_name in seen_tags:
            return True  
        seen_tags.add(tag_name)
    return False  


def find_repeated_tags_for_tag(root, tag_name):
    repeated_tags = []
    target_tag = root.find(tag_name)
    if target_tag is not None and len(list(target_tag))>0:
        print(target_tag.tag)
        temp = [target_tag[0].tag]
        for i in target_tag[1:]:
            if i.tag in temp:
                repeated_tags.append(i.tag)
    return repeated_tags


def reccursiveMethod(root,target_tag,path,out,Flist,repeatTags):
     
    repeatTags.extend(find_repeated_tags_for_tag(root, target_tag.tag))
    #print('out received: ',out)
    
    #print('root',root.tag)
    if target_tag is not None:
        if len(list(target_tag)) == 0: 
            if target_tag is not None:
                if len(list(target_tag)) == 0:
                    try:
                        # Try to convert to int (for Id)
                        value = int(target_tag.text.strip())
                    except (ValueError, AttributeError):
                        try:
                            #datetime
                            if target_tag.text is not None:
                                value = datetime.datetime.strptime(target_tag.text.strip(), "%Y-%m-%dT%H:%M:%S")
                            else:
                                value=None
                        except ValueError:
                            # If conversion fails or target_tag.text is None,
                            value = target_tag.text.strip() if target_tag.text else ''
         
                    # Check if 'Id' is in the tag name
                    if 'Id' in target_tag.tag or'Date' in target_tag.tag :
                        out.update({f'{str(path)}_{target_tag.tag}': value})
                    else:
                        out.update({f'{str(path)}_{target_tag.tag}': str(value)})
                        
                    return out

        
        if len(list(target_tag)) >0:
            
            for child in target_tag:
                #print('child in for:',child.tag)
                #print('before out:',out)
                out.update(reccursiveMethod(target_tag, child,f'{str(path)}_{target_tag .tag}',out,Flist,repeatTags))
                #print('after out:',out)
                #print('repeated tags',repeatTags)
                if (child.tag in repeatTags):
                    if out not in Flist:
                        Flist.append(out.copy())
                        #print('mada flist',Flist)
                        print('inserted into Flist')
                        print('current Flist record number',len(Flist))
                        out={key: value for key, value in out.items() if child.tag not in key}
     
    return out


def parallelProcess(root,target_tag,path,result_queue,repeatTags):
    out={}
    Flist=[]
    datasets= reccursiveMethod(root,target_tag,path,out,Flist,repeatTags)
    result_queue.append(Flist)
