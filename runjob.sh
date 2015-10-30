#!/bin/sh

# Path of Hadoop streaming JAR library
STREAMJAR=/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-*.jar

# Directory in which we'll store job output
OUTPUT=/user/training/empcounts

# Make sure we don't have output from a previous run.
# The -r option removes the directory recursively, and
# the -f option prevents Hadoop from warning us if the
# directory doesn't exist.
hadoop fs -rm -r -f $OUTPUT

# Run this job
hadoop jar $STREAMJAR \
   -mapper mapper.py -file mapper.py  \
   -reducer reducer.py -file reducer.py  \
   -input /dualcore/employees \
   -output $OUTPUT
