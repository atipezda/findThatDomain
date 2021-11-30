from domainFinder import DomainFinder

extension = ".com"

freeWebsites = []

with open('words.txt') as f, open('taken.txt', "a+", buffering=1) as taken, open('free.txt', "a+", buffering=1) as free:
    # try:
    words = [line.rstrip() for line in f]
    taken.seek(0)
    free.seek(0)
    takenDomains = [line.rstrip() for line in taken]
    freedomains = [line.rstrip() for line in free]
    print(takenDomains)
    print(freedomains)
    for firstWord in words:
        if firstWord.startswith('-'):
            continue
        for secondWord in words:
            if not secondWord.endswith("-"):
                name = firstWord.replace("\n", "").replace("-", "") + secondWord.replace('\n', "").replace("-",
                                                                                                           "") + extension

                if name not in takenDomains and name not in freedomains:
                    print(name)
                    if not DomainFinder.domainExsit(name):
                        print(name)
                        if DomainFinder.ensureFreeDomain(name):
                            free.write(name + "\n")
                            freeWebsites.append(name)
                        else:
                            taken.write(name + "\n")
                    else:
                        taken.write(name + "\n")
# except Exception as e:
#     print(e)
#     taken.close()
#     free.close()

print(freeWebsites)
