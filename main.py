from translate import Translator
import subprocess, os, platform

'''
1. python3 install -r requirements.txt
2. python3 main.py
3. File will open, paste your text there 
4. Press ENTER
5. Translated File should open, else open it yourself
'''

TRANSLATE_FROM = 'en'
TRANSLATE_TO = 'de'

translator = Translator(to_lang=TRANSLATE_TO)


def translate():
    try:
        filepath = 'text.txt'
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(filepath)
        else:  # linux variants
            subprocess.call(('xdg-open', filepath))

        input('\npress [ENTER] to translate: ')

        with open('text.txt', mode='r') as my_file:
            text = my_file.read()
            translation = translator.translate(text)
            with open(f'text-{TRANSLATE_TO}.txt', mode='w') as my_file2:
                try:
                    my_file2.write(translation)
                    my_file.close()
                    print('Created File with Translation')
                    filepath2 = f'text-{TRANSLATE_TO}.txt'
                    if platform.system() == 'Darwin':  # macOS
                        subprocess.call(('open', filepath2))
                    elif platform.system() == 'Windows':  # Windows
                        os.startfile(filepath2)
                    else:  # linux variants
                        subprocess.call(('xdg-open', filepath2))
                except:
                    print('something went wrong...')
    except FileNotFoundError as e:
        print('check your file path silly!')


if __name__ == '__main__':
    translate()
