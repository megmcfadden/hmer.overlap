# Finding homopolymers in FASTA file
#

#num must be one smaller then desired - if looking for lengths of 4 and above imput 3
def find_hmer(pair, num):
    for i in range(len(pair[0])):
        with open(pair[0][i], "r") as infile, open(pair[1][i], "w+") as w:
            contig = id = base = start = end = -1
            for line in infile:
                if line[0] == '>':
                    if end - start > 1:
                        w.write('\t'.join(map(str,[contig,id,start,end,end-start,base]))+'\n')
                    contig = line.strip().split()[0][1:]
                    id = pair[2][i]
                    base = -1
                    start = end = 1
                else:
                    for b in line.strip():
                        if b !=base:
                            if end - start > num:
                                w.write('\t'.join(map(str,[contig,id,start,end,end-start,base]))+'\n')
                            start = end
                            base = b
                        end +=1
                if end - start > num:
                    w.write('\t'.join(map(str,[contig,id,start,end,end-start,base]))+'\n')
        ++i
