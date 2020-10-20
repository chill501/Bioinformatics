from Bio import SeqIO
# Input fasta
fasta_file = open('/Users/Claire/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/26_4_19**/Biomart_3UTR_geneID.fasta', 'r')
# Input interesting sequence IDs, one per line
wanted_file = open('/Users/Claire/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/26_4_19**/EV_only_activegenes_mRNA.txt', 'r') 
# Output fasta
output_file = open('/Users/Claire/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/26_4_19**/Biomart_3UTR_geneID_only.fasta', 'w')


for cur_record in SeqIO.parse(fasta_file, "fasta") :
    full_name = cur_record.name
##    print(full_name)
    gene_ID = full_name.split("|")[0]
    cur_seq = cur_record.seq
##    print(gene_ID)
    output_line = '>%s\t%s\n' % \
                  (gene_ID, cur_seq)

##SeqIO.write(output_line, output_file, "fasta")

    output_file.write(output_line)
     
output_file.close() 
fasta_file.close()
wanted_file.close()
    
