import re

stopwords = {'şey', 'mu', 'bu', 'da', 'eğer', 'ne', 'kim', 'az', 'biri', 'veya', 'belki', 'mı', 'neden', 'o', 'çok',
             'nereye', 'hiç', 'hepsi', 'hem', 'ise', 'kez', 'ile', 'için', 'niye', 'defa', 've', 'bazı', 'tüm', 
             'acaba', 'en', 'siz', 'nerede', 'gibi', 'aslında', 'hep', 'niçin', 'birkaç', 'ama', 'nasıl', 'çok', 
             'diye', 'çünkü', 'biz', 'daha', 'her', 'mü', 'birşey', 'ki', 'yani', 'nerde', 'de', 'sanki', 'şu', 'ya'}

def veri_on_isleme(input_dosya, output_dosya):
    with open(input_dosya, 'r', encoding='utf-8') as giris:
        icerik = giris.readlines()

    yeni_icerik = []
    for cumle in icerik:
        cumle = re.sub(r'\d+', '', cumle)
        
        cumle = re.sub(r'[^\w\s]', '', cumle)
        
        cumle = ' '.join([kelime.lower() for kelime in cumle.split() if kelime.lower() not in stopwords])
        
        cumle = cumle.lower()

        yeni_icerik.append(cumle)

    with open(output_dosya, 'w', encoding='utf-8') as cikis:
        cikis.write('\n'.join(yeni_icerik))

input_dosya = 'sonuc.txt'
output_dosya = 'yeni_sonuc.txt'

veri_on_isleme(input_dosya, output_dosya)

# Cümlelere index ekleme
with open("C:\\Users\\escan\\Desktop\\Yazılım Dilleri\\ddi\\yeni_sonuc.txt", "r", encoding="utf-8") as file:
    cumleler = file.readlines()

indeksli_cumleler = []
for index, cumle in enumerate(cumleler):
    indeksli_cumleler.append(f"{index + 1}: {cumle}")

with open("C:\\Users\\escan\\Desktop\\Yazılım Dilleri\\ddi\\indexli_sonuc.txt", "w", encoding="utf-8") as file:
    file.writelines(indeksli_cumleler)

