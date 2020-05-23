import requests
import json
from alive_progress import alive_bar
import hashlib

class WikiURL:

    def __init__(self, file_path, output_path):
        with open(file_path) as json_load:
            self.data = json.load(json_load)
        self.start = -1
        self.file_output = open(output_path, 'a')


    def __iter__(self):
        return self
    

    def __next__(self):
        self.start += 1
        try:
            next_country = self.data[self.start]['name']['common']
        except IndexError:
            self.file_output.close()
            raise StopIteration
        self.file_output.write(next_country+' - https://en.wikipedia.org/wiki/'+next_country.replace(' ', '_')+'\n')
        return next_country
        

def hash_links(path):
    with open(path, 'r') as f:
        for line in f.readlines():
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    for i in WikiURL('countries.json', 'countries.txt'):
            pass
    print('\nDone\n')
    
    for lines in hash_links('countries.txt'):
        print(lines)



