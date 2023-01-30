# Direct Chat Mini Project

The Direct-chat is a mini project writen by django-channels.

## Navigation
- [About](#about)
- [Run](#run)
- [URLs](#urls)  


## About
When you enter the chat section, a list of users you have talked to will be loaded as contacts.    
You can start a conversation by entering a username.   
You can delete conversations bilaterally.    
Things like notification, istyping, online status, block/unblock, infinit scroll have also been implemented.    
By clicking on a contact, `n` recent messages will be loaded, and by scrolling up, `m` previous messages will be loaded and ... (infinit scroll).   
By sending or receiving a new message, the contacts will be sorted according to the time of the last message.  
Test direct-chat by opening several incognito windows and logging in with different users.  

## Run  
Clone and cd to the direct-chat directory: 
``` bash
git clone git@github.com:mhrashvand1/truth_social.git   

cd direct-chat   
```  
Then: 
``` bash  
docker-compose -f docker-compose.dev.yml up    
``` 
Wait until the program is ready to use.
(Whenever you see the following log in the terminal, it means that the program is ready to be used:)

``` bash
directchat    | 2023-01-30 15:16:05,154 INFO     Listening on TCP address 0.0.0.0:8000

```  
Now you can go to the following address and test the program:   
``` shell
http://127.0.0.1/
```

## URLs
- `http://127.0.0.1/`
- `http://127.0.0.1/account/login/` 
- `http://127.0.0.1/account/signup/`
- `http://127.0.0.1/account/profile/`