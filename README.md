# E-posta Kimlik Bilgisi Denetleyici

Bu proje hakkında Türkçe ve İngilizce dillerinde bilgi alabilirsiniz.

- [Türkçe Dokümantasyon (Varsayılan)](README.md)
- [English Documentation](README_EN.md)

Bu Python betiği, bir metin dosyasındaki e-posta kimlik bilgilerinin geçerliliğini kontrol eder ve çalışan ve çalışmayan hesapları belirler. Betik, yalnızca `@hotmail.com` ve `@outlook.com` alan adlarına sahip e-posta adreslerini kontrol eder. Kimlik bilgilerini kontrol ettikten sonra, betik çalışmayan hesapları dosyadan silme seçeneği sunar.

## Özellikler
- SMTP kullanarak e-posta kimlik bilgilerini (kullanıcı adı ve şifre) doğrular.
- Sadece `@hotmail.com` ve `@outlook.com` alan adlarına sahip e-posta adreslerini kontrol eder.
- Birden fazla e-posta hesabını asenkron olarak kontrol eder.
- Çalışmayan hesapları .txt dosyasından kaldırma.

## Gereksinimler
- Makinenizde Python 3.x yüklü olmalıdır.
- Gerekli kütüphaneler `requirements.txt` dosyasında listelenmiştir.

## Kurulum
1. Depoyu klonlayın veya dosyaları indirin.
2. Gerekli Python paketlerini yüklemek için:
    ```bash
    pip install -r requirements.txt
    ```

## Kullanım
1. Her satırda iki nokta (`:`) ile ayrılmış bir e-posta ve şifre içeren bir `mails.txt` dosyası hazırlayın. Örnek:
    ```
    user1@hotmail.com:password1
    user2@outlook.com:password2
    ```
2. Betiği çalıştırın:
    ```bash
    python Checker.py
    ```
3. İlk çalıştırmada dil seçmeniz istenecektir:
    ```
    Hangi dili kullanmak istersiniz?
    1) Türkçe
    2) English
    ```
   Bu seçim gelecekteki kullanım için kaydedilecektir.
   
4. Kimlik bilgisi denetimleri tamamlandıktan sonra şu soru sorulacaktır:
    ```
    Çalışmayan hesaplar dosyadan silinsin mi? (Y/N)
    ```

## Dosyalar
- `Checker.py`: E-posta kimlik bilgisi denetimi yapan ana betik.
- `lang.pkl`: Dil tercihini ve dile özgü mesajları saklar.
- `mails.txt`: E-posta kimlik bilgilerini içeren giriş dosyası.
- `requirements.txt`: Yüklenmesi gereken bağımlılıkların listesi.
