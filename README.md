# Doğal Dil İşleme Projesi:

## 1.Adım: Veri Çekme:
- Programda ilk başta ürün yorumu çekme işlemi uygulanır. (selenium ile)
- Daha sonra çekilen veriler bir txt dosyasına kaydedilir.

## 2.Adım: Veri Ön İşleme:
- Veri işleme kısmında cümleler önce stopwords'lerden ayıklanır.(nltk kütüphanesi)
- Daha sonra sayılardan ve noktalama işaretlerinden ayıklanır.(re)
- Daha sonra cümlelere index eklenerek yeni bir dosyaya kaydedilir.

## 3.Adım: En Çok Geçen Kelimeleri Bulma:
- Ön işleme yaptığımız dosyayı açarız ve bir değişkene atarız.
- Veriler küçük harflere dönüştürülüp tokenize işlemi ile kelimelere ayrılır.(nltk kütüphanesinden word_tokenize fonksiyonu)
- En çok geçen 20 kelime belirlenir.(Counter)
- Daha sonra word2vec modeli oluşturulur.
- Daha sonra oluşturulan bu modeli kullanarak seçilen kelimeye en çok benzeyen 5 kelime belirlenir.

## 4.Adım: Seçilen Cümleye En Çok Benzeyen Cümle:
- Dosyadaki veri okunur ve bir değişkene atanır.
- sentence_transformers kütüphanesinden SentenceTransformer ve util modülleri içe aktarılır.
- Rastgele bir referans cümle seçilir.
- Seçilen referans cümle ile geri kalan cümlelerin gömme vektörleri oluşturulur.
- convert_to_tensor=True parametresi, pyTorch tensor'ları olarak gömme vektörlerini almayı sağlar.
- PyTorch kütüphanesinde bulunan kosinüs benzerliği fonksiyonu kullanılarak referans cümlesi ile diğer cümleler arasındaki benzerlik skorları hesaplanır.
- Benzerlik skorlarına göre sıralama yapılır ve en benzer üç cümle seçilir.
