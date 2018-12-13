# demo-cross-build

src/  ---  Source code for hello library   
test_package/  ---  Test code for hello library   
profiles/  ---  Profiles for cross build   
conanfile.py ---   Conan Recipe for hello library    
JenkinsFile   ---    Jenkins pipeline to generate and upload cross build conan packages of hello library 

- Note:   
  Install g++ 32-bits library for cross build at first!   
  
  ```
  Debian Linux: 
  $ sudo apt-get install libc6-dev

  Ubuntu Linux:
  $ sudo apt-get install libc6-dev-i386

  OpenSUSE / Novell Suse Linux (SLES):
  \# zypper in glibc-devel-32bit

  RHEL / Fedora / CentOS / Scientific Linux:
  $ sudo yum install glibc-devel.i686
  ```
