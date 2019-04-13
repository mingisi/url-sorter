
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

    `pytest ./tests/ -v`

#### Assumption:

    -  only www or naked url are present 
    -  urls provided are always lowcase
    -  urls are in valid format
    -  python 3 is can be used on the enviroment 

#### Todo(improvements):

    - enable loggin to log file instead of console
    - ignore invalid url formates
    - test it on python2


