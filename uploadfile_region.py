#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Upload a file to S3 bucket using method set_contents_from_filename. Bucket in a different region
- Info   : Upload a file named
 	   * myfile.txt
	  set_contents_from_filename vs send_file. set_contents_from_filename uses send_file

"""
import boto

#def searchabucket():
#   bucket = conn.lookup("eu-west-1.101-s3-aws")
#   print bucket.name

def uploadfile():
   bucket = conn.get_bucket("eu-west-1.101-s3-aws")
   obj = bucket.new_key("myfile2.txt")
   obj.set_contents_from_filename("myfile.txt") 

if __name__ == "__main__":
   conn = boto.connect_s3(host='s3-eu-west-1.amazonaws.com')
   uploadfile()
