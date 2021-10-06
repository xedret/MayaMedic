#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Dexter Scott Belmont"
__credits__ = [ "Dexter Scott Belmont" ]
__tags__ = [ "Maya", "Virus", "Removal" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Dexter Scott Belmont"
__email__ = "dexter@kerneloid.com"
__status__ = "alpha"


#jobs = cmds.scriptJob(lj=True)
#for job in jobs:
found = False

for job in cmds.scriptJob( lj=True ) :
 if "leukocyte.antivirus()" in job :
  id = job.split( ":" )[ 0 ]
  if id.isdigit() :
   cmds.scriptJob( k=int(id), f=True )
  if found == False :
   found = True
   print( "Virus Found" )

script_nodes = cmds.ls( "vaccine_gene", type="script" )
if script_nodes :
 if found == False :
  found = True
  print( "Virus Found" )
 cmds.delete( script_nodes )