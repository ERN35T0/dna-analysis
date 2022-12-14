### This program take a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs.

A short tandem repeat (STR) is a microsatellite with repeat units that are 2-7 base pairs in length, and the number of repeats varies between individuals, making STRs effective for human identification.

## Testing


    Run python dna.py databases/small.csv sequences/1.txt. output Bob.
    Run python dna.py databases/small.csv sequences/2.txt. output No match.
    Run python dna.py databases/small.csv sequences/3.txt. output No match.
    Run python dna.py databases/small.csv sequences/4.txt. output Alice.
    Run python dna.py databases/large.csv sequences/5.txt. output Lavender.
    Run python dna.py databases/large.csv sequences/6.txt. output Luna.
    Run python dna.py databases/large.csv sequences/7.txt. output Ron.
    Run python dna.py databases/large.csv sequences/8.txt. output Ginny.
    Run python dna.py databases/large.csv sequences/9.txt. output Draco.
    Run python dna.py databases/large.csv sequences/10.txt. output Albus.
    Run python dna.py databases/large.csv sequences/11.txt. output Hermione.
    Run python dna.py databases/large.csv sequences/12.txt. output Lily.
    Run python dna.py databases/large.csv sequences/13.txt. output No match.
    Run python dna.py databases/large.csv sequences/14.txt. output Severus.
    Run python dna.py databases/large.csv sequences/15.txt. output Sirius.
    Run python dna.py databases/large.csv sequences/16.txt. output No match.
    Run python dna.py databases/large.csv sequences/17.txt. output Harry.
    Run python dna.py databases/large.csv sequences/18.txt. output No match.
    Run python dna.py databases/large.csv sequences/19.txt. output Fred.
    Run python dna.py databases/large.csv sequences/20.txt. output No match.

What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.

name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25


The data in the above file would suggest that Alice has the sequence AGAT repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 18, and 25 times, respectively.

So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated AGATs and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of AATG is 22 repeats long, and the longest sequence of TATC is 19 repeats long, that would provide pretty good evidence that the DNA was Bob???s. Of course, it???s also possible that once you take the counts for each of the STRs, it doesn???t match anyone in your DNA database, in which case you have no match.

In practice, since analysts know on which chromosome and at which location in the DNA an STR will be found, they can localize their search to just a narrow section of DNA. But we???ll ignore that detail for this problem

In a file called dna.py, implement a program that identifies to whom a sequence of DNA belongs.
