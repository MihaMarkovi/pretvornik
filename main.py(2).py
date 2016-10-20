print("Zivijo")
while True:
    prvo_vprasanje = int(raw_input("vnesi km: "))
    odgovor = prvo_vprasanje * 1.609344
    print(odgovor)
    drugo_vprasanje = raw_input("Zelite nadaljevati? ")

    if drugo_vprasanje == "ne":
        print("Hvala za sodelovanje!!!")
        break
        
    
