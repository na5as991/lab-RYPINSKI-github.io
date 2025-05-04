from Bio import SeqIO

max_gc_cont=0
for seq_rec in SeqIO.parse(r'D:\333\test\IN 1.txt',"fasta"):
    seq= str(seq_rec.seq)
    seq_id=seq_rec.id
    gc_content=(seq.count("C")+seq.count("G"))/len(seq)*100
    if gc_content + max_gc_cont:
        max_seq_id=seq_id
        max_gc_cont=gc_content

print(max_seq_id)
print(max_gc_cont)