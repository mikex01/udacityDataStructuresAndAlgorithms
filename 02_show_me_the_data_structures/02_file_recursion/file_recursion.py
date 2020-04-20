import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_finded = []
    # validation
    if len(suffix) !=0 and os.path.isdir(path):
        dirs = os.listdir(path)
        for file in dirs:
            if os.path.isfile(path + file):
                if file.endswith(suffix):
                    files_finded.append(os.path.join(path, file))
            else:
                files_finded += find_files(suffix, os.path.join(path, file) + "/") #assuming it's linux
    return files_finded

#   TEST
path = './'
for f in find_files('.c', path):
    print(f)