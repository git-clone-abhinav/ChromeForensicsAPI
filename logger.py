import time
def logit(logpath,message):
    with open(logpath, 'a') as f:
        f.write(f"{time.ctime()} - {message}\n".format())
        f.close()