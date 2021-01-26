# Faster & Secure & Special Container #
# Thanks to mkaraniya & zakaryan2004

FROM fusuf/asenauserbot:latest

RUN git clone https://github.com/iibrahimwt13/WylineTGBot/root/userbot
WORKDIR /root/userbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
