import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    matching_files = []
    if path is not None and suffix is not None:
        find_files_inner(suffix, path, matching_files)

    return matching_files

def find_files_inner(suffix, path, matching_files):
    entries = os.listdir(path)
    for entry in entries:
        fullpath = os.path.join(path, entry)
        if os.path.isfile(fullpath) and fullpath.endswith(suffix):
            matching_files.append(fullpath)
        elif os.path.isdir(fullpath):
            find_files_inner(suffix, fullpath, matching_files)

# Test Cases

print(find_files(".gitkeep", "testdir"))
# ['testdir/subdir4/.gitkeep', 'testdir/subdir2/.gitkeep']

print(find_files(".c", "testdir"))
# ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

print(find_files(".h", "testdir"))
# ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h']

print(find_files(".exe", "testdir"))
# []

print(find_files("", "testdir"))
# ['testdir/subdir4/.gitkeep', 'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir3/subsubdir1/b.c',
#  'testdir/t1.c', 'testdir/subdir2/.gitkeep', 'testdir/subdir5/a.h', 'testdir/subdir5/a.c', 
#  'testdir/t1.h', 'testdir/subdir1/a.h', 'testdir/subdir1/a.c']

print(find_files("", None))
# []
