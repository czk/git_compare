import os, sys, shutil

def del_content(path):
    try:
        for item in os.listdir(path):
            if True == os.path.isfile(os.path.join(path,item)):
                os.unlink(os.path.join(path,item))
            if True == os.path.isdir(os.path.join(path,item)):
                shutil.rmtree(os.path.join(path,item))
        return True
    except OSError as err:
        print err
        return False


def init_dir(path):
    try:
        if False == os.path.exists(path):
            os.makedirs(path)
            return True
        if True == os.path.isfile(path):
            os.rename(path, path + '_bak')
            os.makedirs(path)
            return True
        return del_content(path)            
    except OSError as err:
        print err
        return False


class log_error:
    def __init__(self, str):
        self._log_str = str
    
    def log_write():
        print self._log_str


class self_except(Exception):
    def __init__(self, string):
        self.value = string


if __name__ == '__main__':
    init_dir('/Users/chenzhengkun/workspace/git_compare/a')
    print 'haha'
