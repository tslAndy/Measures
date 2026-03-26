import json

tiedosto = open("ehdokkaat.txt", "r")

ehdokkaat = []
for rivi in tiedosto:
    rivi = rivi.rstrip()

    osat = rivi.split()

    ehdokas = {}
    ehdokas["etunimi"] = osat[0]
    ehdokas["sukunimi"] = osat[1]
    ehdokas["puolue"] = osat[2]
    ehdokas["aanimaara"] = int(osat[3])
    ehdokkaat.append(ehdokas)

tiedosto.close()

# järjesteään ehdokkaat äänimäärän mukaan
ehdokkaatSorted = sorted(ehdokkaat, key=lambda x: (x["puolue"], x["aanimaara"]), reverse=True)

# muunnetaan json-muotoon
ehdokkaatJson = json.dumps(ehdokkaatSorted, indent=True)
print(ehdokkaatJson)

# kirjoitetaan json tiedostoon
out = open("ehdokkaa.json", "w")
out.write(ehdokkaatJson)
out.close()

