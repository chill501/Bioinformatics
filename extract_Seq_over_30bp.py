from Bio import SeqIO

input_file = open('/Users/Claire/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/AugustwithJana/For_Lizzie/High_stringency_0.5mM_Cellonly.fasta', 'r')
output_file = open('/Users/Claire/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/AugustwithJana/For_Lizzie/30bp_or_more_High_stringency_0.5mM_Cellonly.fasta','w')
##output_file2 = open('/Users/Claire/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/AfterJulywithJana/6_New_grouping/EV_only_plus_DESEQ2_mRNA_3UTR_log2FC>1 _below30.fasta','w')
        
long_sequences = []
less_than_30seq = []
    
    
for record in SeqIO.parse(input_file, "fasta") :
    if len(record.seq) >= 30:
        #print(record.name)
        #print("More or equal to 30")
        long_sequences.append(record)

    else:
        less_than_30seq.append(record)
        #print(record.name)
        #print("Less than 30")
        #print(len(record.seq))


SeqIO.write(long_sequences, output_file, "fasta")


##SeqIO.write(less_than_30seq, output_file2, "fasta")

    
input_file.close()
output_file.close()
##output_file2.close()
