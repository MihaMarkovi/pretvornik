print("Zivijo")
while True:
    prvo_vprasanje = int(raw_input("vnesi km: "))
    odgovor = prvo_vprasanje * 1.609344
    print("To je " + str(odgovor) + " milj")
    drugo_vprasanje = raw_input("Zelite nadaljevati?(da/ne) ")

    if drugo_vprasanje == "ne":
        print("Hvala za sodelovanje!!!")
        break
        
    
