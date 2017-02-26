# AWS_EMR
Map Reduce 
Learn to run a Map Reduce program(using Python) in the Amazon cloud EMR service

We will use AWS EMR on the Enron email dataset:
http://aws.amazon.com/datasets/enron-email-data/
https://en.wikipedia.org/wiki/Enron_scandal
This dataset contains 1,227,255 eMails from Enron employees. The version we use consists of 50 GB of compressed files.

Input files - Accessing the enron data
http://s3.amazonaws.com/enron-scripts/enron-urls-small.txt (smaller set)
http://s3.amazonaws.com/enron-scripts/enron-urls.txt (Larger set)

- Step-1: From the above input files, we extract the required data(DateTimestamp, sender, recipient)

- Step-2: The output of Step-1 is passed to the Enron-Wordcount-Mapper.py, which selects the following records
            Filter the data to
            - only consider emails between 2001-09-05 and 2001-09-08 (including)
            - only consider messages going from ENRON employees to someone not part of the organization
            - Count the number of such foreign interactions and only include accounts (senders) that have more than one outside contact that week.
            
- Step-3: The output of the mapper function will be passed to the Enron-Wordcount-Reducer.py

- Step-4: Merges the output file(s) from Reducer jobs into one single file, using s3distcp(s3-dist-cp in AWS EMR)
      Add a step in AWS EMR, JAR location "command-runner.jar" and in the 'Arguments' give the following:
      s3-dist-cp --src=s3://bucket-name/folder --dest=s3://bucket-name/folder2 --groupBy=.*(to_be_grouped_by).*
 Note: The groupBy argument is quite useful, The files will be grouped by the wildcards(regexp) inside the parenthesis. Refer http://mlpebbles.blogspot.nl/2014/03/note-to-myself-on-s3distcp.html
    
Instructions on how to use Amazon EMR
http://homepages.cwi.nl/~manegold/UvA-ABS-MBA-BDBA-BDIT-2017/MapReduceEnron.pdf


Tips:
Before running the code in AWS EMR, try running the python code locally in your laptop. It would be easier to debug locally than in EMR
python Enron-Wordcount-Mapper-Details.py < part-000000 | python sort.py > temp0.out
python Enron-Wordcount-Reducer.py < temp0.out > final0.out

When the code is run in AWS EMR, the output of the mapper step is automatically shuffled and sorted before passed as input to the reducer job(s).  However when we run it locallyin the laptop, we need to sort it explicitly. could use the sort.py for that purposes.


References
https://www.tutorialspoint.com/python/time_strptime.htm

How to install dateutil package in Python?  http://stackoverflow.com/questions/879156/how-to-install-python-dateutil-on-windows
python -m pip install python-dateutil




