import io
import os

def save_file(text=0,filename='junk.txt'):
    with io.open(filename,'w',encoding='utf8') as f:
        text=str(text)
        f.write(text)
        
def load_file(filename='junk.txt'):
    print('FXN load_file is tying to open ', filename)
    try:
        with io.open(filename, 'r',encoding='utf8') as f:
            text=f.read()
            print('FXN load file contains the text\n>>>', text)
            return text
    except:
        print('!! FATAL : Cannot find file: ', filename)
        exit(1)
        
text=input('Type something to save to file: ') or 'BLAH !!';

save_file(text);

load_file()
