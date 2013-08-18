#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Upload a file to S3 bucket using method initiate_multipart_upload. Note should be 5MB
- Info   : Upload a file to S3 bucket using method initiate_multipart_upload. Note should be 5MB
 	   * myfile.txt
	  Perform a multipart upload
"""

import boto

files = ["file1.txt","file2.txt","file3.txt"]
def uploadfile():
   bucket = conn.get_bucket("101-s3-aws")
#   obj = bucket.new_key("multi.txt")
   mp = bucket.initiate_multipart_upload("multi.txt")
   index = 1
   for file in files:
       print file
       fp = open(file,'rb')
       print mp.upload_part_from_file(fp, index)
       fp.close()
       index += 1
   mp.complete_upload() 
   for part in mp:
        print part.part_number, part.size
       

if __name__ == "__main__":
   conn = boto.connect_s3()
   uploadfile()
