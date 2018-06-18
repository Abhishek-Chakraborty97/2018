import itertools

#Constant values

#nt list
nts = ['A','C','G','T']

#Translation Table
tt = {"TTT":"F|Phe","TTC":"F|Phe","TTA":"L|Leu","TTG":"L|Leu","TCT":"S|Ser","TCC":"S|Ser","TCA":"S|Ser","TCG":"S|Ser", "TAT":"Y|Tyr","TAC":"Y|Tyr","TAA":"*|Stp","TAG":"*|Stp","TGT":"C|Cys","TGC":"C|Cys","TGA":"*|Stp","TGG":"W|Trp", "CTT":"L|Leu","CTC":"L|Leu","CTA":"L|Leu","CTG":"L|Leu","CCT":"P|Pro","CCC":"P|Pro","CCA":"P|Pro","CCG":"P|Pro","CAT":"H|His","CAC":"H|His","CAA":"Q|Gln","CAG":"Q|Gln","CGT":"R|Arg","CGC":"R|Arg","CGA":"R|Arg","CGG":"R|Arg", "ATT":"I|Ile","ATC":"I|Ile","ATA":"I|Ile","ATG":"M|Met","ACT":"T|Thr","ACC":"T|Thr","ACA":"T|Thr","ACG":"T|Thr", "AAT":"N|Asn","AAC":"N|Asn","AAA":"K|Lys","AAG":"K|Lys","AGT":"S|Ser","AGC":"S|Ser","AGA":"R|Arg","AGG":"R|Arg","GTT":"V|Val","GTC":"V|Val","GTA":"V|Val","GTG":"V|Val","GCT":"A|Ala","GCC":"A|Ala","GCA":"A|Ala","GCG":"A|Ala", "GAT":"D|Asp","GAC":"D|Asp","GAA":"E|Glu","GAG":"E|Glu","GGT":"G|Gly","GGC":"G|Gly","GGA":"G|Gly","GGG":"G|Gly"}
#Following functions or their combinations produce randomized or scrambled nucleotide sequence from input sequence.
#Amino-acid sequence of derived sequence is identical to the input sequence, but nucleotide composition (GC-, nucleotide, or dinucleotide content) may differ slightly for randomized sequences.

#Analysis tools
gc = 0
at = 0

def translate(sequence):
        
    i = 0
    retStr = []
    #print sequence
    while i < len(sequence):
        codon = sequence[i:i+3]
    
        if codon not in tt:
            print ("Incomplete or unrecognizable codon")
            break 

        retStr.append(tt[codon])
        i += 3
    
    return retStr


def altNucleotides(aa):
    retList = []
    for aminoacid in aa:
        retList.append([key for key, value in tt.iteritems() if aminoacid == value])
    return retList


def generateList(combo):
    retList = []
    for L in list(itertools.product(*combo)):
        merged = ""
        for c in L:
            merged += c
        #print translate(merged)
        retList.append(merged)
    return retList


#tS = raw_input("Please enter your sequence: ").upper()
tS = "GGCGGAGATCCTTGCGATCCTAATTTCTACTGTTGTAGAT"

seq1 =  translate(tS)
combo1 =  altNucleotides(seq1)
list1 =  generateList(combo1)
list2 = sorted(list1,key=lambda list: list.count("T"))
tlist =  [l.count("T") for l in list2]

print [l.count("T") for l in list2[0:10]]
