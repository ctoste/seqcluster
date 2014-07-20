"""
sam2bed.py

Created by Aaron Quinlan on 2009-08-27.
Copyright (c) 2009 Aaron R. Quinlan. All rights reserved.
"""

import sys
import re
from classes import bedaligned



def processSAM(line):
        """
                Load a SAM file and convert each line to BED format.
        """            
#       f = open(file,'r')
#       for line in f.readlines():
        samLine = splitLine(line.strip())
        return makeBED(samLine)
#       f.close()      
       
                                       
def makeBED(samFields):
       
        samFlag = int(samFields.flag)
       
        # Only create a BED entry if the read was aligned
        if (not (samFlag & 0x0004)):
               
                chrom = samFields.rname
                start = str(int(samFields.pos)-1)
                end = str(int(samFields.pos) + len(samFields.seq) - 1)
                name = samFields.qname    
                strand = getStrand(samFlag)

                # Let's use the edit distance as the BED score.
                # Clearly alternatives exist.
                #editPattern = re.compile('NM\:i\:(\d+)')
                #editDistance = editPattern.findall(samFields[12])

                # Write out the BED entry
                return bedaligned("%s\t%s\t%s\t%s\t.\t%s\n" %  (chrom,start,end,name,strand))
        else:
                return False    
               
def splitLine(line, delim="\t"):
        splitline = line.split(delim)
        return splitline                


def getStrand(samFlag):
        strand = "+"
        if (samFlag & (0x10)):  # minus strand if true.
                strand = "-"            
        return strand