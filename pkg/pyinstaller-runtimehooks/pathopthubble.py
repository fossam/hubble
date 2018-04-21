# this runtimehook prepends paths to its environment so that the code
# would always find the binaries that we ship in the package

import os

os.environ["PATH"] = '/opt/hubble/bin:/opt/hubble/libexec:' + os.environ["PATH"]
