#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Dexter Scott Belmont"
__credits__ = [ "Dexter Scott Belmont", "Javier Prieto", "Boxel Studio" ]
__tags__ = [ "Maya", "Virus", "Removal", "MayaMedic" ]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Dexter Scott Belmont"
__email__ = "dexter@kerneloid.com"
__status__ = "Production"

import os
import sys
import glob
import argparse

parser = argparse.ArgumentParser( prog='MayaMedic', description="Maya virus removal tool", usage='mayamedic [-t | --target] [ -s | --silent] [ -d | --dry]' )
parser.add_argument( "-t", "--target", default=0, metavar='path', help="scan specific file or directory, clean if necessary and exit." )
parser.add_argument( "-s", "--silent", default=0, action='store_true', help="run script, scan default directories, clean if necessary and exit." )
parser.add_argument( "-d", "--dry", default=0, action='store_true', help="scan specific file or directory, report infections without cleaning and exit." )
args = parser.parse_args()

class CliStyle() :
 BLACK = '\033[30m'
 RED = '\033[31m'
 GREEN = '\033[32m'
 YELLOW = '\033[33m'
 BLUE = '\033[34m'
 MAGENTA = '\033[35m'
 CYAN = '\033[36m'
 WHITE = '\033[37m'
 UNDERLINE = '\033[4m'
 RESET = '\033[0m'

def pWarn( msg ) :
 print( CliStyle.YELLOW + msg + CliStyle.RESET )

def pError( msg ) :
 print( CliStyle.RED + msg + CliStyle.RESET )

def pQuote( msg ) :
 print( CliStyle.GREEN + msg + CliStyle.RESET )

class MayaMedic( object ) :

 """MayaMedic Class definition"""

 def __init__( self ) :

  """Auto executed upon instantiation"""

  super( MayaMedic, self ).__init__()
  # self.location = os.path.dirname( os.path.realpath( __file__ ) )
  self.infected = False
  self.files_infected = False

  self.user = os.environ.get( "USERNAME" ).title()
  home = os.environ.get( "HOME" )
  if home is None :
   home = os.path.expanduser( "~" )
  scripts_dir = home + "\\Documents\\maya\\scripts\\"
  appdata_dir = home + "\\AppData\\"
  self.infected_files = [ scripts_dir + "vaccine.py", scripts_dir + "userSetup.py", appdata_dir + "userSetup.py" ]
  os.system( "" )
  if args.target :
   if os.path.isfile( args.target ) and not args.target.lower().strip().endswith( ".ma" ) :
    pError( "I can only scan .ma files :(" )
   elif os.path.isfile( args.target ) and args.target.lower().strip().endswith( ".ma" ) :
    self.__scan( args.target, 'file' )
   elif os.path.isdir( args.target ) :
    if not args.target.endswith( '/' ) :
     args.target += '/'
    os.path.isdir( args.target )
    for filename in glob.iglob( args.target + '**/*.ma', recursive=True ) :
     print( "filename: " + filename )
     self.__scan( filename, 'dir' )
   sys.exit()
  elif args.silent :
   self.__checkForScripts()
   sys.exit()
  elif args.dry :
   self.__checkForScripts( dry=True)
   sys.exit()
  pQuote( "\nHi " + self.user + ", it seems that you have met with a terrible fate..." )
  print( "But don't worry I'll help you out by checking your system for a couple of malicious files\n" )
  pQuote( "You can press [CTRL]+[C] at any time to quit :)\n" )
  self.__checkForScripts()
  self.__scanner()

 def __checkForScripts( self, dry=False ) :
  print( "We are going to start by checking a couple directories for those infected scripts." )
  for file in self.infected_files :
   print( "Checking " + file + " contents for viruses..." )
   if os.path.exists( file ) :
    pError( "Infected file found: " + file )
    if dry:
     pWarn( "Running on dry mode, infected file will not be removed!!!" )
    else:
     pWarn( "Removing infected file" )
     # os.remove( file )
     os.rename( file , file + "_" ) 
    self.infected = True
  if self.infected == False :
   print( "\nCongratulations, I was unable to find any viruses in the usual/expected directories." )
   print( "But that doesn't mean the virus can't be in individual files.\n" )

 def __scanner( self ) :
  scan_choice = self.__input( "Would you like to scan a folder or individual .ma files? [Y]/[n]: ", [ "y", "n" ], "y" )
  if scan_choice.lower() == "y" :
   while True :
    scan_path = self.__inputDir( "Please enter directory or drag and drop your Maya (.ma) file here: " )
    if os.path.isfile( scan_path ) and not scan_path.lower().strip().endswith( ".ma" ) :
     print( "I can only scan .ma files :(" )
     continue
    elif os.path.isfile( scan_path ) and scan_path.lower().strip().endswith( ".ma" ) :
     self.__scan( scan_path, 'file' )
    elif os.path.isdir( scan_path ) :
     if not scan_path.endswith( '/' ) :
      scan_path += '/'
     os.path.isdir( scan_path )
     for filename in glob.iglob( scan_path + '**/*.ma', recursive=True ) :
      print( "filename: " + filename )
      self.__scan( filename, 'dir' )
  elif scan_choice.lower() == "n" :
   pQuote( '\nA sword wields no strength unless the hand that holds it has courage...\n\n' )
   print( 'Exiting now...' )
   sys.exit()
  else :
   print( "I didn't quite get that..." )
   self.__scanner()

 def __scan( self, scan_file, mode='file' ) :
  self.files_infected = False
  virus_nodes = [ 'vaccine_gene', 'breed_gene' ]
  scan_file_obj = open( scan_file, 'r' )
  original_lines = scan_file_obj.readlines()
  scan_file_obj.close()
  for line in original_lines :
   if self.files_infected :
    break
   for node in virus_nodes :
    if node in line :
     pError( 'Virus found: \n' + line[ : 60 ] + '...' )
     self.files_infected = True
  if self.files_infected :
   print( "Cleaning file..." )
   clean_file = os.path.splitext( scan_file )[ 0 ] + "_clean.ma"
   new_file = open( clean_file , "w" )
   node_lock = False
   for line in original_lines :
    if not line.startswith( "\t" ) and node_lock :
     node_lock = False
    if not any( node in line for node in virus_nodes ) and not node_lock :
     new_file.write( line )
    else :
     node_lock = True
   new_file.close()
   os.rename( scan_file, os.path.splitext( scan_file )[ 0 ] + "_infected.ma" )
   os.rename( clean_file, scan_file )
   print( "File cleaned successfully: " + scan_file )
  else :
   if mode == 'file' :
    print( "The selected file contains no infected nodes." )

 def __input( self, question, answers = [], default = "" ) :
  while True :
   try :
    response = input( question ).replace( '"', '' ) or default
    if (response and not answers) or (response in answers) :
     return response
    else :
     print( "Unexpected input" )
     print( "Input: " + response )
   except ValueError :
    print( "Sorry, I didn't understand that." ) # User entered something unintelligible to the CLI
    continue
   except KeyboardInterrupt :
    print( "\n\nKeyboard Interrupt, exiting now." )
    sys.exit()

 def __inputDir( self, question ) :
  while True :
   try :
    response = input( question ).replace( '"', '' )
    if os.path.exists( response ) :
     return response
   except ValueError :
    print( "Sorry, I didn't understand that." ) # User entered something unintelligible to the CLI
    continue
   except FileNotFoundError :
    print( "Sorry, that file doesn't exist or I don't have access to it, try again." ) # Cannot locate file or directory
    continue
   except KeyboardInterrupt :
    print( "\n\nKeyboard Interrupt, exiting now." )
    sys.exit()

autoexec = MayaMedic()