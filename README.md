You'll need python3.8 in order to run this.

1 - Create a virtual environment and activate it.

2 - Install following dependencies using pip in your virtual environment:
    -Scrapy version 2.0.1
    -pymongo version 3.10.1
    -pypi version 2.1

3 - Start the mongod service using the following command:
    $ sudo systemctl start mongod 
 
4 - Navigate to project directory in terminal and run the following command:
    $ scrapy crawl stack
