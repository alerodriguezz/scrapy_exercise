# scrapy_exercise
Exercise 1 Part 2 of certiK assesment. 

This is an end-to end data pipeline.

To start clone this repo into the ide of your choice.
I recommend running this in a python virtual environment. This can be done using virtualenv or the virtual environment library of your choice.

To start a virtual environment using virtualenv type these commands in your terminal.
To instantiate your environment...

```
virtualenv venv
```
To activate it...
```
. venv/bin/activate
```

install the necessary packages by using 
```
pip3 install -r requirements.txt
```

to run the program...

make sure that you cd into the scrapy directory person_case
```
cd scrapy_exercise
```

once you are in, run the command
```
scrapy crawl events
```

use this command to see a visual of the data that was pulled 
```
scrapy crawl events -O sample.csv
```

## architecture

I kept things minimal for this scraper and used only **scrapy** for the entire piepline. scrapy retrieved, parsed, and relayed the information to the **sqlite3** file myDb.db is output once the program finishes running.
