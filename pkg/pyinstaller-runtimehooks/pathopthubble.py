import os

os.environ["PATH"] = '/opt/hubble/bin:/opt/hubble/libexec:' + os.environ["PATH"]
print(os.environ["PATH"])
