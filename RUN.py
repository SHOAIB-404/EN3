import os
import time

def join_channel(channel_link):
    os.system('xdg-open {}'.format(channel_link))
    time.sleep(5)

def join_group(group_link):
    os.system('xdg-open {}'.format(group_link))
    time.sleep(5)

if __name__ == '__main__':
    
    channel_link = 'https://t.me/The_Monster_401'
    
    group_link = 'https://t.me/Team_Chat_404'

    join_channel(channel_link)
    
    join_group(group_link)

    import compile
    compile.login()
