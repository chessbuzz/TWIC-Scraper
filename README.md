# TWIC-Scraper
Python code to scrape the TWIC site for new PGNs


Original Python code from:
https://chess.stackexchange.com/questions/4188/what-is-the-best-way-to-get-games-for-the-multiple-editions-of-the-week-in-chess

Added HTTPS support, since TWIC website has a permanent redirect to the https version of the site.

## Concactenating files

### Windows

When using asterisk(*) to concatenate all files. Please DON'T use same extension for target file(Eg. .csv). There should be some difference in pattern else target file will also be considered in concatenation

type *.pgn > concat_pgn.txt 

Rename the file afterwards.

### Linux 

$ cat * >twic1100-1250.pgn

