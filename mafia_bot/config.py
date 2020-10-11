
#токен старый и уже не работает
token = 'NzY0ODU5NTM0NTY0MTMwODY4.X4MY8w.kuJqUAb6KhNIVXmY9qQx_e5h3so'

try:
    with open('token.txt', 'r') as token_file:
        token = token_file.readline()
except FileNotFoundError:
    with open('token.txt', 'a') as token_file:
        token_file.close()



client_id = '764859534564130868'
bot_name = 'AJlKO3ABPUK'
link = 'https://discordapp.com/oauth2/authorize?&client_id='+client_id+'&scope=bot&permissions=8'


settings = {
        'token' : token, 
        'bot' : bot_name,
        'id' : int(client_id),
        #'prefix' : '4JlEH '
        'prefix' : '!'
        }

