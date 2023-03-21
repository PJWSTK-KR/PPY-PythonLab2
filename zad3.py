def question(q="", a=[]):
    print("pytanie: " + q)
    for i in range(0, len(a)):
        print(str(i + 1) + ". " + a[i])
    return a[int(input("number odpowiedzi: ")) - 1]


print("pytanie: Jak masz na imię oraz nazwisko?")
answears = [input("odpowiedź: "),
            question("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie?",
                                           ["oglądanie telewizji/filmów/seriali",
                                            "czytanie książek/czasopism",
                                            "uprawianie sportu"]),
            question("W jakich okolicznościach czytasz książki najczęściej?", ["podczas pracy/nauki (to ich element)",
                                                                               "podczas podróży",
                                                                               "w czasie wolnym (po pracy, na urlopie)"]),
            question("Po książki w jakiej formie sięgasz najczęściej?", ["e-booki na tablecie/telefonie",
                                                                         "papierowej (tradycyjnej)",
                                                                         "e-booki na specjalnym czytniku (np. Kindle)"])]
print("Odpowidzi na pytania to: ")
for i in answears:
    print(i + "\n")
