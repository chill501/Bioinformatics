from Bio import SeqIO
import itertools
path = '/Users/clairehill/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/AugustwithJana/8_Length/'
fasta_file = open(path+'mRNA_Transcripts_whole_seq.fasta', 'r') # Input fasta file
wanted_file = open(path+'IDS_whole_length_less_7500.txt', 'r') # Input interesting sequence IDs, one per line
result_file = "mRNA_Transcripts_whole_seq_less7500only.fasta" # Output fasta file
miss_file = open(path+"mRNA_Transcripts_whole_seq_MISSING.txt", 'w') # Output fasta file
fasta=SeqIO.parse(fasta_file,"fasta")
seq_dict={}
keep_dict={}
                  
seq_dict = SeqIO.to_dict(fasta)
x = list(itertools.islice(seq_dict.items(), 0, 4))
print(x)
for line in wanted_file:
       
        line=line.strip()
    
        if line in seq_dict.keys():
                
            keep_dict[line]=seq_dict[line]
##              print("YES", ">"+line)
##              print(keep_dict[line]) 
##              print("keep_dict updated")
               
        else: 
##            print("Wanted_line not in fasta reference file", ">"+line)
            miss_file.write(line)
            miss_file.write("\n")
##            print("miss_file wirtten")

with open(path + result_file, 'w') as handle:
    SeqIO.write(keep_dict.values(), handle, 'fasta')
    print("keep_dict written")

miss_file.close()
