input_file = open('/Users/Claire/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/8_4_19/dmel-all-three_prime_UTR-r6.26.fasta', 'r') 
output_file = open('length_of_all-three_prime_UTR-r6.26.txt','w')
#output_file.write('Gene\tlength\n') 
from Bio import SeqIO 
for cur_record in SeqIO.parse(input_file, "fasta") :
    gene_name = cur_record.name
    length = len(cur_record.seq)
    output_line = '>%s\t%i\n' % \
                  (gene_name, length)
    output_file.write(output_line)
     
output_file.close() 
input_file.close()
