#Requirements Twilio SID token Twilio Auth Token Ngrok Auth token

#Deploy on Termux
1. apt update && upgrade
2. apt install python3 && python2

#Install Ngrok:-
1. pkg install zip wget -y
2. wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
3. unzip ngrok-stable-linux-arm.unzip
4. chmod +x ngrok-stable-linux-arm

#Ngrok Authtoken
1. Create an Account on Ngrok
2. copy Your Auth token
3. Open Termux 
4. ./ngrok authtoken YOUR_AUTH_TOKEN_HERE

#Connect To ngrok
1. ngrok http 5000

#Deployment
1. unzip Telegram-Otp-Bot.zip
2. cd Telegram-Otp-Bot
3. nano cred.py
4. Replace with your Auth token , Bot token ,Sid token , Twilio number , Ngrok url
5. Exit editor
6. python3 mainn.py

# Telegram Setup
1. Type 'Admin Mode' in your Telegram bot