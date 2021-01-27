# Faster & Secure & Special Container #
# Thanks to mkaraniya & zakaryan2004

FROM iibrahimwt13/repobash:latest

RUN git clone https://github.com/iibrahimwt13/WylineTGBot
WORKDIR /WylineTGBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
