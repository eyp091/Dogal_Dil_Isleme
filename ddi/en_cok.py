from collections import Counter
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

dosya_adi = "yeni_sonuc.txt"
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    veri_seti = dosya.read()

tokenized_veri_seti = word_tokenize(veri_seti.lower())

model = Word2Vec([tokenized_veri_seti], vector_size=200, window=10, min_count=10, workers=5)

en_cok_gecen_kelimeler = [kelime for kelime, sayi in Counter(tokenized_veri_seti).most_common(20)]

en_cok_tekrar_eden = Counter(tokenized_veri_seti).most_common(20)

for  sayi, kelime in en_cok_tekrar_eden:
    print(f"{kelime} : Toplam Tekrar Sayısı: {sayi}")

print("\n\n")

for ana_kelime in en_cok_gecen_kelimeler:
    benzer_kelimeler = model.wv.most_similar(ana_kelime, topn=5)

    print(f"{ana_kelime} kelimesine en çok benzeyen 5 kelime:")
    for kelime, benzerlik_skoru in benzer_kelimeler:
        print(f"{kelime}: Benzerlik Skoru {benzerlik_skoru:.2f}")
    print("\n")
