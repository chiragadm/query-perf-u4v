# QUERY-PERF-U4V
QUERY-PER-U4V is a script that allow users to query performance metrics out of Unisphere For VMAX. 

# Installation:
Following are prerequisites for this CLI program.
* Linux based OS
* Python3 (python2 is not supported)
  * Python Modules:
  * requests
  * json
  * time

 
* # How to install this CLI program?
  Please run following command to install this CLI program. (You will need GIT CLI installed or you can copy the repository)
  * $ cd SOME_DIRECTORY (Directory that you want to install this program)
  * $ git clone https://URL

  # Setting up configuration file (fabview.cfg):
  Once the script is installed in directory as per above instruction, now it is time to configure the script variables. You will need to uncomment following variable and update them as per your environment.
  * unimaxURI
  * username 
  * password 
  * symmId  
  ```
  Following is just example.
  unimaxURI = 'https://unisphere.abc.com:8443/univmax/restapi'
  username = 'username'
  password = 'password'
  symmId = '000196700000'
  
  ```
 * # How to use this script?
   There are lots of commented example provided with in script to query particular type of information. However, this list is not complete. You may add your queries as per your use cases. 
