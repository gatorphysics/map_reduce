#!/usr/bin/env python

import sys

for line in sys.stdin:
   line = line.strip()
   (id, fname, lname, addr, city, state, zip, job, email, active, salary) = line.split("\t")

   if int(salary) >= 75000:
      print "%s,1" % state
