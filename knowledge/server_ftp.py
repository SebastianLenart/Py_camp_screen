from ftplib import FTP
from credentials import config

with FTP(config["host"], config["username"], config["password"]) as ftp, open("screenshot.png", "rb") as file:
    # upload pliku
    ftp.storbinary(f"STOR test.png", file)

    # zawartosc katalogu
    print(ftp.retrlines("LIST"))
    print("*"*10)

    # iterowalna zawartosc katalogu
    for entry in ftp.nlst():
        print(entry)

