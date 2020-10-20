from Bio import SeqIO

input_file = open('/Users/clairehill/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/AugustwithJana/6_FIMO/ALL_May_2020/Running_only_smaller_groups/EV_only_plus_EV_enriched_CDS/EV_only_plus_EV_enriched_CDS_mart_export.txt', 'r')
output_file = open('/Users/clairehill/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/AugustwithJana/6_FIMO/ALL_May_2020/Running_only_smaller_groups/EV_only_plus_EV_enriched_CDS/EV_only_plus_EV_enriched_CDS_mart_export_above1.fasta','w')
output_file2 = open('/Users/clairehill/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/AugustwithJana/6_FIMO/ALL_May_2020/Running_only_smaller_groups/EV_only_plus_EV_enriched_CDS/EV_only_plus_EV_enriched_CDS_mart_export_seq_unavailable.fasta','w')
        
sequences = []
sequences_unavailable = []
    
    
for record in SeqIO.parse(input_file, "fasta") :
    if record.seq == 'Sequenceunavailable':
        #print(record.name)
        #print("More or equal to 30")
        sequences_unavailable.append(record)

    else:
        sequences.append(record)
        #print(record.name)
        #print("Less than 30")
        #print(len(record.seq))


SeqIO.write(sequences, output_file, "fasta")


SeqIO.write(sequences_unavailable, output_file2, "fasta")

    
input_file.close()
output_file.close()
output_file2.close()
