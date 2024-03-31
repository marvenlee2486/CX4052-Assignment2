# Directory Format
|-- hadoop-3.4.0 (Stores Implementation of Hadoop)
assignment2.py (Implementation of Assignment 2 Experiment)

# Assignment 2 instruction
Run without any arguments will run the default graph 
'''
python3 assingment2.py
'''

Run with  '-a' to change the ALPHA (Default is 0.8)
'''
python3 assignment2.py -a 0.5
'''

Run with '-n' to set the number of nodes and '-c' to set the connectivity. If either of this arguments is shown, the code will run with a generated graph
'''
python3 assignment2.py -n 64 -c 0.1
'''

To run with custom graph, please uncomment any of the graph from lines 59 to lines 101.