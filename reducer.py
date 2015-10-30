#!/usr/bin/env python

import sys

previous_state = ''
count_for_state = 0

for line in sys.stdin:
   line = line.strip()

   (state, number) = line.split(",")

   if state == previous_state:
      count_for_state = count_for_state + int(number)
   else:
      if previous_state != '':
         if count_for_state >= 2:
            print "%s\t%d" % (previous_state, count_for_state)
      previous_state = state
      count_for_state = int(number)

if count_for_state >= 2:
   print "%s\t%d" % (state, count_for_state)
