import csv
import os


def verzamel_gegevens():
    print("Voer de details van je werkdag in.")
    datum = input("Datum (YYYY-MM-DD): ")
    uren = input("Aantal gewerkte uren: ")
    project = input("Projectnaam: ")
    opmerkingen = input("Opmerkingen (optioneel): ") or "Geen opmerkingen"
    return datum, uren, project, opmerkingen


def sla_op_in_csv(bestandsnaam, gegevens, schrijf_header=False):
    with open(bestandsnaam, 'a', newline='') as bestand:
        writer = csv.writer(bestand)
        if schrijf_header:
            writer.writerow(["Datum", "Uren", "Project", "Opmerkingen"])
        writer.writerow(gegevens)


def hoofd():
    bestandsnaam = "urenregistratie.csv"
    schrijf_header = not os.path.exists(bestandsnaam)

    while True:
        gegevens = verzamel_gegevens()
        sla_op_in_csv(bestandsnaam, gegevens, schrijf_header)
        schrijf_header = False  # Na de eerste keer is de header al geschreven

        doorgaan = input("Wil je nog een werkdag toevoegen? (ja/nee): ").lower()
        if doorgaan != 'ja':
            break


if __name__ == "__main__":
    hoofd()
