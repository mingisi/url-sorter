[![Build Status](https://travis-ci.org/mingisi/url-sorter.svg?branch=master)](https://travis-ci.org/mingisi/url-sorter)

#### Summary

takes a file with list of URLs and outputs to the console all the unique hostnames and the number of occurrences of that hostname found in the file. The result in the format:

`<num_of_occurences> <hostname>`

the output is a sorted in a descending order based on number of occurrences, then alphabetical order


** please use python 3 **


#### Activate virtual dev environment.

    source ./.pevenv/bin/activate

#### Installing dev dependencies

    pip install -r requirements.txt

#### Running The script

    python url_parser.py ./tests/files/test3.txt

#### Running unit test

    pytest ./tests/ -v
    pytest --cov-config=.coveragerc ./tests/ 

#### Assumption:

    -  only www or naked url are present 
    -  urls provided are always lowcase
    -  urls are in valid format 
    -  python 3 is can be used on the enviroment 
    -  sorting very large file in meomory isn't greate idea 
    -  more than 140 terabyte will not be need
    -  their is know www in midle of the host name
    -   non english charaters iUTF-8

#### Todo(improvements):

    - enable loggin to log file instead of console
    - ignore invalid url formates
    - test it on python2


### How it works


 `get_file` function is used get the file name from the console args

 `get_lines` function is used to read the file line at a time and the previous will be garbage collected, so to this  enable reading a large files the line processes/manipulated the string at the time of reading the line and then stored in the sqllite db on disk. SQLite database is limited in size to 140 terabyte guess
<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
 `get_full_domain` function is used go through a list of valid url(Parts for RFC 3986 URI syntax) using `murl` module(`https://github.com/berkerpeksag/murl`). the function returns a list of hostname with the www. removed

 `get_domain_dict` takes a list of hostnames and put it into dictionery `key: hostname value: count/occrance` and returns a dictionary of hostname and occurrence  

 `get_sorted_domain_dict` take a dictionary of hostname and occurrence  and sorts it in descending order based on number of occurrences and then hostname alphabetical order. sorting is done through build-in sort function `sorted`, uses a lambda function for the `key` parameter. the lambda function takes two parameters, the occurrence as a negative count value and the hostname as it is, this will transform the items before they can be compared

 `display` is the funciton that take dictionary and displays it on the screen
