**Shell Permissions**
- su -> change current user to another user
- whoami -> print the effective username of the current user
- groups -> print all the groups of current user
- chown -> change owner of a file to another owner
- touch -> create an empty file
- chmod u+x -> add execute permission to owner of file(s)
- chmod 754 -> add execute permission to the owner and the group owner and read permission to other users
- chmod ugo+x -> add execute permission to everybody
- chmod 007 -> sets all the permission to other users
- chmod 753 -> allows other users to write and execute
- chmod --reference -> allows other user to read only
- chmod a+x */ -> directories permission
- mkdir -m 751 -> permission to create directory
- chgrp -> change group permission
- chown -> owner and group permission
- chown -h -> change owner of a symbolic link
- chown -from -> if only permission
- telnet -> open web page in terminal
