# credit: Szymon Palucha
# https://chess.stackexchange.com/questions/4188/what-is-the-best-way-to-get-games-for-the-multiple-editions-of-the-week-in-chess

# pycurl libary is used to download the files
import pycurl
from io import BytesIO
import os
import certifi # needed for SSL curl Transfer
 # reads files and extracts them
import zipfile
from pathlib import Path

# c = pycurl.Curl()

# set the start and end ranges for the volumes you want to download
for i in range(start, end + 1):

# actual file name on site: https://theweekinchess.com/zips/twic1356g.zip

   url = "https://theweekinchess.com/zips/twic" + str(i) + "g.zip"

# change to reflect your folder structure
   save_location_path = Path("/twic/twic" + str(i) + ".zip")
   unzipped_location_path = Path("/twic")

# wb is binary mode for writing
   with open(save_location_path, 'wb') as f:
       c = pycurl.Curl()
       c.setopt(c.VERBOSE, True) # for debugging purposes...
       c.setopt(c.URL, url) # set URL value
       c.setopt(c.WRITEDATA, f) # write
       c.setopt(c.CAINFO, certifi.where()) # for SSL transfer
       c.perform() # perform a file transfer

  # reading zip file that was downloaded
   with zipfile.ZipFile(save_location_path, 'r') as myzip:
       myzip.extractall(unzipped_location_path)
# deletes the unused zip files
   os.remove(save_location_path)

 # note download the files as PGN so you can use the cat command # TODO:
 # merge into one file ($ cat * > twic1100-1250.pgn)
   c.close()
