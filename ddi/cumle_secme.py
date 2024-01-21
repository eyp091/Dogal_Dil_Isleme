from sentence_transformers import SentenceTransformer, util
import random 

model = SentenceTransformer('dbmdz/bert-base-turkish-128k-uncased')

with open("indexli_sonuc.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

for _ in range(5):
    referans_cumle_index = random.randint(0, len(data))
    referans_cumle = data.pop(referans_cumle_index)

    embeddings = model.encode(data, convert_to_tensor=True)
    referans_embedding = model.encode(referans_cumle, convert_to_tensor=True)

    benzerlikler = util.pytorch_cos_sim(referans_embedding, embeddings)[0]

    sorted_indices = benzerlikler.argsort(descending=True)[:3]
    benzer_cumle = [data[idx] for idx in sorted_indices]

    print(f"Referans cümle (index: {referans_cumle_index}): {referans_cumle}")
    print("En Benzer 3 Cümle: ")
    for i, sentence in enumerate(benzer_cumle, start=1):
        print(f"{i}. Cümle: {sentence.strip()}")
    print("\n" + "-"*50 + "\n")