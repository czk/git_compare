import os
from git import *
from utl import *

def getRepo(git_path):
    try:
        repository = Repo(git_path)
    except (NoSuchPathError,InvalidGitRepositoryError) as err:
        print err
        return None
    return repository

def write_blob(blob, compare_root, sub_dir):
    if None == blob:
        return
    path, item = os.path.split(blob.path)
    path = os.path.join(compare_root, sub_dir, path)
    if False == os.path.exists(path):
        os.makedirs(path)
    f = open(os.path.join(path,item), 'w')
    f.write(blob.data_stream.read())
    f.close()


def show_diff(config, commit_nums):
    repository = getRepo(config['GITDIR'])
    if None == repository:
        print 'failed to get repository, the DITDIR maybe wrong'  
        return False
    commit_1 = repository.commit(commit_nums[0])
    diffs = commit_1.diff(commit_nums[1])
    init_dir(os.path.join(config['COMPARE_ROOT'],'a'))
    init_dir(os.path.join(config['COMPARE_ROOT'],'b'))
    for i in diffs:
        write_blob(i.a_blob, config['COMPARE_ROOT'], 'a')
        write_blob(i.b_blob, config['COMPARE_ROOT'], 'b')
