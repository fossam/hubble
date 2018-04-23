import os

os.environ["PATH"] = '/opt/hubble/bin:/opt/hubble/libexec:' + os.environ["PATH"]
print("PATH=%s" % os.environ["PATH"])
