[![Build Status](https://travis-ci.org/mingisi/url-sorter.svg?branch=master)](https://travis-ci.org/mingisi/url-sorter)

#### Summary

takes a file with list of URLs and outputs to the console all the unique hostnames and the number of occurrences of that hostname found in the file. The result in the format:

`<num_of_occurences> <hostname>`

the output is a sorted in a descending order based on number of occurrences, then alphabetical order

** please use python 3.4 or above  **

#### Create Virual environment 

    virtualenv -p /usr/local/opt/python/bin/python3.7 .pevenv  
    
#### Activate virtual dev environment.

    source ./.pevenv/bin/activate

#### Installing dev dependencies

    pip install -r requirements.txt

#### Running The script

    python url_parser.py ./tests/files/test3.txt

#### Running unit test

    pytest --cov-report term-missing --cov=. tests/ 

#### Assumption:

    -  only www or naked URLs are present 
    -  URLs are in valid format 
    -  all environments are using python 3.4 and above
    -  more than 140 terabyte will not be used 
    -  have enough disk space 
    -  there is no www in middle of the hostname
    -  non-english characters don't appear in the URL 


#### Todo(improvements):

    - enable logging to log file instead of console
    - make it compatible with python2 


### How it works

`get_file` 
 
Function is used to get the file name from the console args
    

`store` 
 
Function is used to read a file with URLs, line at a time. Each line is processes/manipulated and stored in the db(SQLite) and then moved to next line, the previous line would should be garbage collected. This enabled the way of reading a large file.

Storing and sorting large file(multi-gigabyte) in memory can be intensive. Therefore, a file base database was used to store and sort the data.

SQLite should be able to run on wide varies of platform and shouldn't need any special database installations.

`process_line`

The function uses `murl` module (`https://github.com/berkerpeksag/murl`) to process URL.

When processing an URL an assumption is made that the URL are is in a valid format `<scheme>://<netloc>/<path>;<params>?<query>#<fragment>` as part of the RFC 3986 URI syntax.

 Another assumption function makes wwww only appears at the beginning of the hostname.

 `display` 
 
 The function takes a set of rows return by the db and displays it
