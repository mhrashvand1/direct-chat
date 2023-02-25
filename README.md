# Direct Chat Mini Project

## Navigation
- [Description](#description)
- [Run](#run)
- [URLs](#urls)  

## Description
The Direct-Chat is a mini project written using Django-Channels and provides a text-based chat system using WebSockets. When you enter the chat section, a list of users you have previously communicated with will be loaded as contacts. You can initiate a conversation by entering a username. Conversations can be deleted bilaterally. Features such as notifications, is typing, online status, block/unblock, and infinite scrolling have also been implemented. By clicking on a contact, the `n` most recent messages will be loaded. By scrolling up, `m` previous messages will be loaded (using infinite scrolling). Contacts are sorted based on the time of the last message received or sent. You can test the Direct-Chat by opening multiple incognito windows and logging in as different users.

## Run  
To run the Direct-Chat mini project, follow these steps:

1. Clone and navigate to the `direct-chat` directory:   

``` bash
git clone git@github.com:mhrashvand1/direct-chat.git   
cd direct-chat   
```   

2. Run the following command:   

``` bash  
docker-compose -f docker-compose.dev.yml up --build  
``` 

3. Wait until the program is ready to use. You can tell that it is ready by seeing the following log in the terminal:   

``` bash
directchat    | 2023-01-30 15:16:05,154 INFO     Listening on TCP address 0.0.0.0:8000

```  

4. Now you can access the program at the following address:  
(The project will be accessed on `localhost` at port `80`.)    

``` shell
http://127.0.0.1/
```

## URLs
- `http://127.0.0.1/`
- `http://127.0.0.1/account/login/` 
- `http://127.0.0.1/account/signup/`   
Edit profle:  
- `http://127.0.0.1/account/profile/`