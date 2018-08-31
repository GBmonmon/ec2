filenames = ['getvpcandsubnet.py', 'securitygrp.py', 'run.py','getip.py','stopterminate.py']
for fh in filenames:
    input('Press enter to run: %s'%(fh,))
    exec(open('./'+fh).read())
