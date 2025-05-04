from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

genbank_file = r"D:\333\test\sequence.gb"


cds_entries = []
for record in SeqIO.parse(genbank_file, "genbank"):
    for feat in record.features:
        if feat.type == "CDS" and "translation" in feat.qualifiers:
            cds_entries.append({
                "id": record.id,
                "description": record.description,
                "location": feat.location,
                "gc": gc_fraction(feat.extract(record.seq)),
                "translation": feat.qualifiers["translation"][0]
            })

print("\n----- Задание 2: CDS по возрастанию GC-состава -----")
for entry in sorted(cds_entries, key=lambda x: x["gc"]):
    print(f"{entry['id']}: {entry['description']}, GC = {entry['gc']}")

print("\n----- Задание 3: Белковые последовательности -----")
for entry in cds_entries:
    print(f"{entry['id']}: {entry['description']}")
    print(f"  Coding sequence location = {entry['location']}")
    print(f"  Translation = {entry['translation']}\n")