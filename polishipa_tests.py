def get_tests():
    tests=(
# https://en.wiktionary.org/wiki/pewnie
        ("pewnie","ˈpɛv.ɲɛ"),
# https://en.wiktionary.org/wiki/czegoś
        ("czegoś","ˈt͡ʂɛ.ɡɔɕ"),
# https://en.wiktionary.org/wiki/gdzie
        ("gdzie","ɡd͡ʑɛ"),
# https://en.wiktionary.org/wiki/grać
        ("grać","ɡrat͡ɕ"),
# https://en.wiktionary.org/wiki/rzadko
        ("rzadko","ˈʐat.kɔ"),
# https://en.wiktionary.org/wiki/dziewczynę
        ("dziewczynę","d͡ʑɛfˈt͡ʂɨ.nɛ"),
# https://en.wiktionary.org/wiki/lalkę
        ("lalkę","ˈlal.kɛ"),
# https://en.wiktionary.org/wiki/znalazłam
        ("znalazłam","znaˈla.zwam"),
# https://en.wiktionary.org/wiki/aż
        ("aż","aʂ"),
# https://en.wiktionary.org/wiki/poszło
        ("poszło","ˈpɔ.ʂwɔ"),
# https://en.wiktionary.org/wiki/mówi
        ("mówi","ˈmu.vʲi"),
# https://en.wiktionary.org/wiki/robiłeś
        ("robiłeś","rɔˈbʲi.wɛɕ"),
# https://en.wiktionary.org/wiki/kawa
        ("kawa","ˈka.va"),
# https://en.wiktionary.org/wiki/żony
        ("żony","ˈʐɔ.nɨ"),
# https://en.wiktionary.org/wiki/nudności
        ("nudności","nudˈnɔɕ.t͡ɕi"),
# https://en.wiktionary.org/wiki/rany
        ("rany","ˈra.nɨ"),
# https://en.wiktionary.org/wiki/który
        ("który","ˈktu.rɨ"),
# https://en.wiktionary.org/wiki/zrobimy
        ("zrobimy","zrɔˈbʲi.mɨ"),
# https://en.wiktionary.org/wiki/możemy
        ("możemy","mɔˈʐɛ.mɨ"),
# https://en.wiktionary.org/wiki/podobno
        ("podobno","pɔˈdɔb.nɔ"),
# https://en.wiktionary.org/wiki/widzisz
        ("widzisz","ˈvʲi.d͡ʑiʂ"),
# https://en.wiktionary.org/wiki/wziąłeś
        ("wziąłeś","ˈvʑɔ̃.wɛɕ"),
# https://en.wiktionary.org/wiki/zapamiętać
        ("zapamiętać","za.paˈmʲɛn.tat͡ɕ"),
# https://en.wiktionary.org/wiki/pobliżu
        ("pobliżu","pɔbˈlʲi.ʐu"),
# https://en.wiktionary.org/wiki/zadzwonić
        ("zadzwonić","zad͡zˈvɔ.ɲit͡ɕ"),
# https://en.wiktionary.org/wiki/wschód
        ("wschód","fsxut"),
# https://en.wiktionary.org/wiki/płacę
        ("płacę","ˈpwa.t͡sɛ"),
# https://en.wiktionary.org/wiki/mówi
        ("mówi","ˈmu.vʲi"),
# https://en.wiktionary.org/wiki/dwóch
        ("dwóch","dvux"),
# https://en.wiktionary.org/wiki/nikim
        ("nikim","ˈɲi.kʲim"),
# https://en.wiktionary.org/wiki/mojego
        ("mojego","mɔˈjɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/zobacz
        ("zobacz","ˈzɔ.bat͡ʂ"),
# https://en.wiktionary.org/wiki/wszystko
        ("wszystko","ˈfʂɨ.stkɔ"),
# https://en.wiktionary.org/wiki/roku
        ("roku","ˈrɔ.ku"),
# https://en.wiktionary.org/wiki/długa
        ("długa","ˈdwuɡa"),
# https://en.wiktionary.org/wiki/chciałbym
        ("chciałbym","ˈxt͡ɕaw.bɨm"),
# https://en.wiktionary.org/wiki/poznać
        ("poznać","ˈpɔz.nat͡ɕ"),
# https://en.wiktionary.org/wiki/Lisowski
        ("Lisowski","lʲiˈsɔf.skʲi"),
# https://en.wiktionary.org/wiki/miałam
        ("miałam","ˈmʲa.wam"),
# https://en.wiktionary.org/wiki/pomyślny
        ("pomyślny","pɔˈmɨɕ.lnɨ"),
# https://en.wiktionary.org/wiki/września
        ("września","ˈvʐɛɕ.ɲa"),
# https://en.wiktionary.org/wiki/spróbuję
        ("spróbuję","spruˈbu.jɛ"),
# https://en.wiktionary.org/wiki/całkiem
        ("całkiem","ˈt͡saw.kʲɛm"),
# https://en.wiktionary.org/wiki/dzieciom
        ("dzieciom","ˈd͡ʑɛ.t͡ɕɔm"),
# https://en.wiktionary.org/wiki/dajesz
        ("dajesz","ˈda.jɛʂ"),
# https://en.wiktionary.org/wiki/chwilę
        ("chwilę","ˈxfʲi.lɛ"),
# https://en.wiktionary.org/wiki/zna
        ("zna","zna"),
# https://en.wiktionary.org/wiki/wtedy
        ("wtedy","ˈftɛ.dɨ"),
# https://en.wiktionary.org/wiki/typowo
        ("typowo","tɨˈpɔ.vɔ"),
# https://en.wiktionary.org/wiki/robiłam
        ("robiłam","rɔˈbʲi.wam"),
# https://en.wiktionary.org/wiki/chętnie
        ("chętnie","ˈxɛn.tɲɛ"),
# https://en.wiktionary.org/wiki/takich
        ("takich","ˈta.kʲix"),
# https://en.wiktionary.org/wiki/sobą
        ("sobą","ˈsɔ.bɔ̃"),
# https://en.wiktionary.org/wiki/więcej
        ("więcej","ˈvʲɛn.t͡sɛj"),
# https://en.wiktionary.org/wiki/interesuje
        ("interesuje","in.tɛ.rɛˈsu.jɛ"),
# https://en.wiktionary.org/wiki/prawdziwa
        ("prawdziwa","pravˈd͡ʑi.va"),
# https://en.wiktionary.org/wiki/przyszła
        ("przyszła","ˈpʂɨ.ʂwa"),
# https://en.wiktionary.org/wiki/ogłoszenie
        ("ogłoszenie","ɔ.ɡwɔˈʂɛ.ɲɛ"),
# https://en.wiktionary.org/wiki/pewnego
        ("pewnego","pɛvˈnɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/paru
#        ("paru","pa.ʁy"),
# https://en.wiktionary.org/wiki/przestań
        ("przestań","ˈpʂɛ.staɲ"),
# https://en.wiktionary.org/wiki/jeździ
        ("jeździ","ˈjɛʑ.d͡ʑi"),
# https://en.wiktionary.org/wiki/spotkać
        ("spotkać","ˈspɔt.kat͡ɕ"),
# https://en.wiktionary.org/wiki/innych
        ("innych","ˈin.nɨx"),
# https://en.wiktionary.org/wiki/Jaki
        ("Jaki","ˈja.kʲi"),
# https://en.wiktionary.org/wiki/żeby
        ("żeby","ˈʐɛ.bɨ"),
# https://en.wiktionary.org/wiki/pewne
        ("pewne","ˈpɛv.nɛ"),
# https://en.wiktionary.org/wiki/miasto
        ("miasto","ˈmʲa.stɔ"),
# https://en.wiktionary.org/wiki/świetnie
        ("świetnie","ˈɕfʲɛt.ɲɛ"),
# https://en.wiktionary.org/wiki/niego
        ("niego","ˈɲɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/pisze
        ("pisze","ˈpʲi.ʂɛ"),
# https://en.wiktionary.org/wiki/zupełnie
        ("zupełnie","zuˈpɛw.ɲɛ"),
# https://en.wiktionary.org/wiki/medycyna
        ("medycyna","mɛ.dɨˈt͡sɨ.na"),
# https://en.wiktionary.org/wiki/jemy
        ("jemy","ˈjɛ.mɨ"),
# https://en.wiktionary.org/wiki/wełny
        ("wełny","ˈvɛw.nɨ"),
# https://en.wiktionary.org/wiki/udało
        ("udało","uˈda.wɔ"),
# https://en.wiktionary.org/wiki/piękny
        ("piękny","ˈpʲɛŋ.knɨ"),
# https://en.wiktionary.org/wiki/niech
        ("niech","ɲɛx"),
# https://en.wiktionary.org/wiki/miasto
        ("miasto","ˈmʲa.stɔ"),
# https://en.wiktionary.org/wiki/reszty
        ("reszty","ˈrɛʂ.tɨ"),
# https://en.wiktionary.org/wiki/restauracja
        ("restauracja","rɛ.staˈwrat͡s.ja"),
# https://en.wiktionary.org/wiki/niczym
        ("niczym","ˈɲi.t͡ʂɨm"),
# https://en.wiktionary.org/wiki/zrobić
        ("zrobić","ˈzrɔ.bʲit͡ɕ"),
# https://en.wiktionary.org/wiki/właściwie
        ("właściwie","vwaɕˈt͡ɕi.vʲɛ"),
# https://en.wiktionary.org/wiki/specjalny
        ("specjalny","spɛt͡sˈjal.nɨ"),
# https://en.wiktionary.org/wiki/boje
        ("boje","ˈbɔ.jɛ"),
# https://en.wiktionary.org/wiki/amerykańska
        ("amerykańska","a.mɛ.rɨˈkaɲ.ska"),
# https://en.wiktionary.org/wiki/podnosić
        ("podnosić","pɔdˈnɔ.ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/strasznie
        ("strasznie","ˈstraʂ.ɲɛ"),
# https://en.wiktionary.org/wiki/mogliście
        ("mogliście","mɔɡˈlʲiɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/szybko
        ("szybko","ˈʂɨp.kɔ"),
# https://en.wiktionary.org/wiki/pracę
        ("pracę","ˈpra.t͡sɛ"),
# https://en.wiktionary.org/wiki/wysokim
        ("wysokim","vɨˈsɔ.kʲim"),
# https://en.wiktionary.org/wiki/poniżej
        ("poniżej","pɔˈɲi.ʐɛj"),
# https://en.wiktionary.org/wiki/świetny
        ("świetny","ˈɕfʲɛt.nɨ"),
# https://en.wiktionary.org/wiki/żebyście
        ("żebyście","ʐɛˈbɨɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/tygodniu
        ("tygodniu","tɨˈɡɔ.dɲu"),
# https://en.wiktionary.org/wiki/wybrać
        ("wybrać","ˈvɨ.brat͡ɕ"),
# https://en.wiktionary.org/wiki/wezmę
        ("wezmę","ˈvɛz.mɛ"),
# https://en.wiktionary.org/wiki/Bać
        ("Bać","bat͡ɕ"),
# https://en.wiktionary.org/wiki/przejmuj
        ("przejmuj","ˈpʂɛj.muj"),
# https://en.wiktionary.org/wiki/żebym
        ("żebym","ˈʐɛ.bɨm"),
# https://en.wiktionary.org/wiki/wielkie
        ("wielkie","ˈvʲɛl.kʲɛ"),
# https://en.wiktionary.org/wiki/pokazać
        ("pokazać","pɔˈka.zat͡ɕ"),
# https://en.wiktionary.org/wiki/miejscu
        ("miejscu","ˈmʲɛj.st͡su"),
# https://en.wiktionary.org/wiki/czujesz
        ("czujesz","ˈt͡ʂu.jɛʂ"),
# https://en.wiktionary.org/wiki/całe
        ("całe","ˈt͡sa.wɛ"),
# https://en.wiktionary.org/wiki/przeczytać
        ("przeczytać","pʂɛˈt͡ʂɨ.tat͡ɕ"),
# https://en.wiktionary.org/wiki/dlatego
        ("dlatego","dlaˈtɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/powinien
        ("powinien","pɔˈvʲi.ɲɛn"),
# https://en.wiktionary.org/wiki/daje
        ("daje","ˈda.jɛ"),
# https://en.wiktionary.org/wiki/prezenty
        ("prezenty","prɛˈzɛn.tɨ"),
# https://en.wiktionary.org/wiki/lepsze
        ("lepsze","ˈlɛp.ʂɛ"),
# https://en.wiktionary.org/wiki/dniu
        ("dniu","dɲu"),
# https://en.wiktionary.org/wiki/ciągle
        ("ciągle","ˈt͡ɕɔŋ.ɡlɛ"),
# https://en.wiktionary.org/wiki/zajmuje
        ("zajmuje","zajˈmu.jɛ"),
# https://en.wiktionary.org/wiki/zrobiłem
        ("zrobiłem","zrɔˈbʲi.wɛm"),
# https://en.wiktionary.org/wiki/psem
        ("psem","psɛm"),
# https://en.wiktionary.org/wiki/pracujący
        ("pracujący","pra.t͡suˈjɔn.t͡sɨ"),
# https://en.wiktionary.org/wiki/oczywiście
        ("oczywiście","ɔ.t͡ʂɨˈvʲiɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/dają
        ("dają","ˈda.jɔ̃"),
# https://en.wiktionary.org/wiki/bratem
        ("bratem","ˈbra.tɛm"),
# https://en.wiktionary.org/wiki/mniej
        ("mniej","mɲɛj"),
# https://en.wiktionary.org/wiki/kapelusz
        ("kapelusz","kaˈpɛ.luʂ"),
# https://en.wiktionary.org/wiki/starsze
        ("starsze","ˈstar.ʂɛ"),
# https://en.wiktionary.org/wiki/łatwiej
        ("łatwiej","ˈwat.fʲɛj"),
# https://en.wiktionary.org/wiki/dziewczynka
        ("dziewczynka","d͡ʑɛfˈt͡ʂɨn.ka"),
# https://en.wiktionary.org/wiki/żonie
        ("żonie","ˈʐɔ.ɲɛ"),
# https://en.wiktionary.org/wiki/interesuje
        ("interesuje","in.tɛ.rɛˈsu.jɛ"),
# https://en.wiktionary.org/wiki/raczej
        ("raczej","ˈra.t͡ʂɛj"),
# https://en.wiktionary.org/wiki/łatwo
        ("łatwo","ˈwa.tfɔ"),
# https://en.wiktionary.org/wiki/widzę
        ("widzę","ˈvʲi.d͡zɛ"),
# https://en.wiktionary.org/wiki/muchę
        ("muchę","ˈmu.xɛ"),
# https://en.wiktionary.org/wiki/życiem
        ("życiem","ˈʐɨ.t͡ɕɛm"),
# https://en.wiktionary.org/wiki/znajomych
        ("znajomych","znaˈjɔ.mɨx"),
# https://en.wiktionary.org/wiki/zgubiłem
        ("zgubiłem","zɡuˈbʲi.wɛm"),
# https://en.wiktionary.org/wiki/patrzeć
        ("patrzeć","ˈpat.ʂɛt͡ɕ"),
# https://en.wiktionary.org/wiki/wracać
        ("wracać","ˈvra.t͡sat͡ɕ"),
# https://en.wiktionary.org/wiki/długie
        ("długie","ˈdwu.ɡʲɛ"),
# https://en.wiktionary.org/wiki/prawda
        ("prawda","ˈprav.da"),
# https://en.wiktionary.org/wiki/ścianę
        ("ścianę","ˈɕt͡ɕa.nɛ"),
# https://en.wiktionary.org/wiki/poproś
        ("poproś","ˈpɔ.prɔɕ"),
# https://en.wiktionary.org/wiki/jesteście
        ("jesteście","jɛˈstɛɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/uważać
        ("uważać","uˈva.ʐat͡ɕ"),
# https://en.wiktionary.org/wiki/polskie
        ("polskie","ˈpɔl.skʲɛ"),
# https://en.wiktionary.org/wiki/przychodzi
        ("przychodzi","pʂɨˈxɔ.d͡ʑi"),
# https://en.wiktionary.org/wiki/fantastyczny
        ("fantastyczny","fan.taˈstɨt͡ʂ.nɨ"),
# https://en.wiktionary.org/wiki/tramwaj
        ("tramwaj","ˈtram.vaj"),
# https://en.wiktionary.org/wiki/drzwiach
        ("drzwiach","dʐvʲax"),
# https://en.wiktionary.org/wiki/mówisz
        ("mówisz","ˈmu.vʲiʂ"),
# https://en.wiktionary.org/wiki/czuje
        ("czuje","ˈt͡ʂu.jɛ"),
# https://en.wiktionary.org/wiki/Ewa
        ("Ewa","ˈɛ.va"),
# https://en.wiktionary.org/wiki/przyjadę
        ("przyjadę","pʂɨˈja.dɛ"),
# https://en.wiktionary.org/wiki/skąd
        ("skąd","skɔnt"),
# https://en.wiktionary.org/wiki/białego
        ("białego","bʲaˈwɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/mną
        ("mną","mnɔ̃"),
# https://en.wiktionary.org/wiki/jakąś
        ("jakąś","ˈja.kɔɲɕ"),
# https://en.wiktionary.org/wiki/stanowisko
        ("stanowisko","sta.nɔˈvʲi.skɔ"),
# https://en.wiktionary.org/wiki/coś
        ("coś","t͡sɔɕ"),
# https://en.wiktionary.org/wiki/choroby
        ("choroby","xɔˈrɔ.bɨ"),
# https://en.wiktionary.org/wiki/słońca
        ("słońca","ˈswɔɲ.t͡sa"),
# https://en.wiktionary.org/wiki/kretyn
        ("kretyn","ˈkrɛ.tɨn"),
# https://en.wiktionary.org/wiki/fajne
        ("fajne","ˈfaj.nɛ"),
# https://en.wiktionary.org/wiki/przynajmniej
        ("przynajmniej","pʂɨˈnaj.mɲɛj"),
# https://en.wiktionary.org/wiki/Polakiem
        ("Polakiem","pɔˈla.kʲɛm"),
# https://en.wiktionary.org/wiki/zadzwonię
        ("zadzwonię","zad͡zˈvɔ.ɲɛ"),
# https://en.wiktionary.org/wiki/artykuł
        ("artykuł","arˈtɨ.kuw"),
# https://en.wiktionary.org/wiki/cale
#         ("cale","kal"),
# https://en.wiktionary.org/wiki/byłaś
        ("byłaś","ˈbɨ.waɕ"),
# https://en.wiktionary.org/wiki/poszli
        ("poszli","ˈpɔʂ.lʲi"),
# https://en.wiktionary.org/wiki/niedzielę
        ("niedzielę","ɲɛˈd͡ʑɛ.lɛ"),
# https://en.wiktionary.org/wiki/południem
        ("południem","pɔˈwu.dɲɛm"),
# https://en.wiktionary.org/wiki/codziennie
        ("codziennie","t͡sɔˈd͡ʑɛɲ.ɲɛ"),
# https://en.wiktionary.org/wiki/wazon
        ("wazon","ˈva.zɔn"),
# https://en.wiktionary.org/wiki/zacznijmy
        ("zacznijmy","zat͡ʂˈɲij.mɨ"),
# https://en.wiktionary.org/wiki/pojechał
        ("pojechał","pɔˈjɛ.xaw"),
# https://en.wiktionary.org/wiki/uczyć
        ("uczyć","ˈu.t͡ʂɨt͡ɕ"),
# https://en.wiktionary.org/wiki/sztuki
        ("sztuki","ˈʂtu.kʲi"),
# https://en.wiktionary.org/wiki/sporo
        ("sporo","ˈspɔ.rɔ"),
# https://en.wiktionary.org/wiki/kiedy
        ("kiedy","ˈkʲɛ.dɨ"),
# https://en.wiktionary.org/wiki/rozumiem
        ("rozumiem","rɔˈzu.mʲɛm"),
# https://en.wiktionary.org/wiki/zobaczycie
        ("zobaczycie","zɔ.baˈt͡ʂɨ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/woli
        ("woli","ˈvɔ.lʲi"),
# https://en.wiktionary.org/wiki/napisać
        ("napisać","naˈpʲi.sat͡ɕ"),
# https://en.wiktionary.org/wiki/kilka
        ("kilka","ˈkʲil.ka"),
# https://en.wiktionary.org/wiki/tygodniu
        ("tygodniu","tɨˈɡɔ.dɲu"),
# https://en.wiktionary.org/wiki/stało
        ("stało","ˈsta.wɔ"),
# https://en.wiktionary.org/wiki/kończy
        ("kończy","ˈkɔɲ.t͡ʂɨ"),
# https://en.wiktionary.org/wiki/ciastka
        ("ciastka","ˈt͡ɕa.stka"),
# https://en.wiktionary.org/wiki/wystarczy
        ("wystarczy","vɨˈstar.t͡ʂɨ"),
# https://en.wiktionary.org/wiki/najszybciej
        ("najszybciej","najˈʂɨp.t͡ɕɛj"),
# https://en.wiktionary.org/wiki/dziecko
        ("dziecko","ˈd͡ʑɛt͡s.kɔ"),
# https://en.wiktionary.org/wiki/zamiaru
        ("zamiaru","zaˈmʲa.ru"),
# https://en.wiktionary.org/wiki/przyjdzie
        ("przyjdzie","ˈpʂɨj.d͡ʑɛ"),
# https://en.wiktionary.org/wiki/jestem
        ("jestem","ˈjɛ.stɛm"),
# https://en.wiktionary.org/wiki/czuje
        ("czuje","ˈt͡ʂu.jɛ"),
# https://en.wiktionary.org/wiki/szansę
        ("szansę","ˈʂan.sɛ"),
# https://en.wiktionary.org/wiki/dumny
        ("dumny","ˈdum.nɨ"),
# https://en.wiktionary.org/wiki/mylisz
        ("mylisz","ˈmɨ.lʲiʂ"),
# https://en.wiktionary.org/wiki/milionów
        ("milionów","mʲiˈlʲɔ.nuf"),
# https://en.wiktionary.org/wiki/czego
        ("czego","ˈt͡ʂɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/niestety
        ("niestety","ɲɛˈstɛ.tɨ"),
# https://en.wiktionary.org/wiki/zapomniał
        ("zapomniał","zaˈpɔm.ɲaw"),
# https://en.wiktionary.org/wiki/piłka
        ("piłka","ˈpʲiw.ka"),
# https://en.wiktionary.org/wiki/przedwczoraj
        ("przedwczoraj","pʂɛˈtft͡ʂɔ.raj"),
# https://en.wiktionary.org/wiki/cała
        ("cała","ˈt͡sa.wa"),
# https://en.wiktionary.org/wiki/końcu
        ("końcu","ˈkɔɲ.t͡su"),
# https://en.wiktionary.org/wiki/Kopernika
        ("Kopernika","kɔ.pɛrˈɲi.ka"),
# https://en.wiktionary.org/wiki/szybkość
        ("szybkość","ˈʂɨp.kɔɕt͡ɕ"),
# https://en.wiktionary.org/wiki/pory
        ("pory","ˈpɔ.rɨ"),
# https://en.wiktionary.org/wiki/godzinę
        ("godzinę","ɡɔˈd͡ʑi.nɛ"),
# https://en.wiktionary.org/wiki/okazji
        ("okazji","ɔˈkaz.ji"),
# https://en.wiktionary.org/wiki/dlaczego
        ("dlaczego","dlaˈt͡ʂɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/swoje
        ("swoje","ˈsfɔ.jɛ"),
# https://en.wiktionary.org/wiki/kupić
        ("kupić","ˈku.pʲit͡ɕ"),
# https://en.wiktionary.org/wiki/wspaniały
        ("wspaniały","fspaˈɲa.wɨ"),
# https://en.wiktionary.org/wiki/żadna
        ("żadna","ˈʐad.na"),
# https://en.wiktionary.org/wiki/źle
        ("źle","ʑlɛ"),
# https://en.wiktionary.org/wiki/książce
        ("książce","ˈkɕɔŋ.ʂt͡sɛ"),
# https://en.wiktionary.org/wiki/wolę
        ("wolę","ˈvɔ.lɛ"),
# https://en.wiktionary.org/wiki/ciągu
        ("ciągu","ˈt͡ɕɔŋ.ɡu"),
# https://en.wiktionary.org/wiki/zdolności
        ("zdolności","zdɔlˈnɔɕ.t͡ɕi"),
# https://en.wiktionary.org/wiki/śniadanie
        ("śniadanie","ɕɲaˈda.ɲɛ"),
# https://en.wiktionary.org/wiki/wierzę
        ("wierzę","ˈvʲɛ.ʐɛ"),
# https://en.wiktionary.org/wiki/dzień
        ("dzień","d͡ʑɛɲ"),
# https://en.wiktionary.org/wiki/czytać
        ("czytać","ˈt͡ʂɨ.tat͡ɕ"),
# https://en.wiktionary.org/wiki/chodzi
        ("chodzi","ˈxɔ.d͡ʑi"),
# https://en.wiktionary.org/wiki/przychodzą
        ("przychodzą","pʂɨˈxɔ.d͡zɔ̃"),
# https://en.wiktionary.org/wiki/zwierzęta
        ("zwierzęta","zvʲɛˈʐɛn.ta"),
# https://en.wiktionary.org/wiki/chodzi
        ("chodzi","ˈxɔ.d͡ʑi"),
# https://en.wiktionary.org/wiki/lubię
        ("lubię","ˈlu.bʲɛ"),
# https://en.wiktionary.org/wiki/takie
        ("takie","ˈta.kʲɛ"),
# https://en.wiktionary.org/wiki/chodzić
        ("chodzić","ˈxɔ.d͡ʑit͡ɕ"),
# https://en.wiktionary.org/wiki/sąsiad
        ("sąsiad","ˈsɔɲ.ɕat"),
# https://en.wiktionary.org/wiki/już
        ("już","juʂ"),
# https://en.wiktionary.org/wiki/opowiedz
        ("opowiedz","ɔˈpɔ.vʲɛt͡s"),
# https://en.wiktionary.org/wiki/świeżym
        ("świeżym","ˈɕfʲɛ.ʐɨm"),
# https://en.wiktionary.org/wiki/stół
        ("stół","stuw"),
# https://en.wiktionary.org/wiki/Ponieważ
        ("Ponieważ","pɔˈɲɛ.vaʂ"),
# https://en.wiktionary.org/wiki/wolałbym
        ("wolałbym","vɔˈlaw.bɨm"),
# https://en.wiktionary.org/wiki/wszystko
        ("wszystko","ˈfʂɨ.stkɔ"),
# https://en.wiktionary.org/wiki/kłopotów
        ("kłopotów","kwɔˈpɔ.tuf"),
# https://en.wiktionary.org/wiki/półtora
        ("półtora","puwˈtɔ.ra"),
# https://en.wiktionary.org/wiki/każdym
        ("każdym","ˈkaʐ.dɨm"),
# https://en.wiktionary.org/wiki/robisz
        ("robisz","ˈrɔ.bʲiʂ"),
# https://en.wiktionary.org/wiki/zajęty
        ("zajęty","zaˈjɛn.tɨ"),
# https://en.wiktionary.org/wiki/jedziesz
        ("jedziesz","ˈjɛ.d͡ʑɛʂ"),
# https://en.wiktionary.org/wiki/pięćdziesiąt
        ("pięćdziesiąt","pʲɛɲˈd͡ʑɛ.ɕɔnt"),
# https://en.wiktionary.org/wiki/zapłacisz
        ("zapłacisz","zaˈpwa.t͡ɕiʂ"),
# https://en.wiktionary.org/wiki/czterdzieści
        ("czterdzieści","t͡ʂtɛrˈd͡ʑɛɕ.t͡ɕi"),
# https://en.wiktionary.org/wiki/magazyn
        ("magazyn","maˈɡa.zɨn"),
# https://en.wiktionary.org/wiki/zobaczyć
        ("zobaczyć","zɔˈba.t͡ʂɨt͡ɕ"),
# https://en.wiktionary.org/wiki/sprawa
        ("sprawa","ˈspra.va"),
# https://en.wiktionary.org/wiki/piętrze
        ("piętrze","ˈpʲɛn.tʂɛ"),
# https://en.wiktionary.org/wiki/tysiąc
        ("tysiąc","ˈtɨ.ɕɔnt͡s"),
# https://en.wiktionary.org/wiki/znaczy
        ("znaczy","ˈzna.t͡ʂɨ"),
# https://en.wiktionary.org/wiki/sytuacja
        ("sytuacja","sɨ.tuˈat͡s.ja"),
# https://en.wiktionary.org/wiki/chodźmy
        ("chodźmy","ˈxɔd͡ʑ.mɨ"),
# https://en.wiktionary.org/wiki/czerwony
        ("czerwony","t͡ʂɛrˈvɔ.nɨ"),
# https://en.wiktionary.org/wiki/może
        ("może","ˈmɔ.ʐɛ"),
# https://en.wiktionary.org/wiki/przerwy
        ("przerwy","ˈpʂɛr.vɨ"),
# https://en.wiktionary.org/wiki/zapomniałeś
        ("zapomniałeś","za.pɔmˈɲa.wɛɕ"),
# https://en.wiktionary.org/wiki/słucham
        ("słucham","ˈswu.xam"),
# https://en.wiktionary.org/wiki/razie
        ("razie","ˈra.ʑɛ"),
# https://en.wiktionary.org/wiki/faceta
        ("faceta","faˈt͡sɛ.ta"),
# https://en.wiktionary.org/wiki/zjeść
        ("zjeść","zjɛɕt͡ɕ"),
# https://en.wiktionary.org/wiki/niedawno
        ("niedawno","ɲɛˈdav.nɔ"),
# https://en.wiktionary.org/wiki/synowie
        ("synowie","sɨˈnɔ.vʲɛ"),
# https://en.wiktionary.org/wiki/mogłabym
        ("mogłabym","ˈmɔ.ɡwa.bɨm"),
# https://en.wiktionary.org/wiki/spróbować
        ("spróbować","spruˈbɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/będę
        ("będę","ˈbɛn.dɛ"),
# https://en.wiktionary.org/wiki/szkielet
        ("szkielet","ˈʂkʲɛ.lɛt"),
# https://en.wiktionary.org/wiki/zasada
        ("zasada","zaˈsa.da"),
# https://en.wiktionary.org/wiki/sześć
        ("sześć","ʂɛɕt͡ɕ"),
# https://en.wiktionary.org/wiki/człowiekiem
        ("człowiekiem","t͡ʂwɔˈvʲɛ.kʲɛm"),
# https://en.wiktionary.org/wiki/zapłacić
        ("zapłacić","zaˈpwa.t͡ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/weź
        ("weź","vɛɕ"),
# https://en.wiktionary.org/wiki/wody
        ("wody","ˈvɔ.dɨ"),
# https://en.wiktionary.org/wiki/dostać
        ("dostać","ˈdɔ.stat͡ɕ"),
# https://en.wiktionary.org/wiki/Nic
#         ("Nic","nʲɪc"),
# https://en.wiktionary.org/wiki/wyjść
        ("wyjść","vɨjɕt͡ɕ"),
# https://en.wiktionary.org/wiki/zamiar
        ("zamiar","ˈza.mʲar"),
# https://en.wiktionary.org/wiki/południu
        ("południu","pɔˈwu.dɲu"),
# https://en.wiktionary.org/wiki/Dobry
        ("Dobry","ˈdɔ.brɨ"),
# https://en.wiktionary.org/wiki/książkę
        ("książkę","ˈkɕɔŋ.ʂkɛ"),
# https://en.wiktionary.org/wiki/jadę
        ("jadę","ˈja.dɛ"),
# https://en.wiktionary.org/wiki/że
        ("że","ʐɛ"),
# https://en.wiktionary.org/wiki/robił
        ("robił","ˈrɔ.bʲiw"),
# https://en.wiktionary.org/wiki/robić
        ("robić","ˈrɔ.bʲit͡ɕ"),
# https://en.wiktionary.org/wiki/ziewać
        ("ziewać","ˈʑɛ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/żurnal
        ("żurnal","ˈʐur.nal"),
# https://en.wiktionary.org/wiki/zielonego
        ("zielonego","ʑɛ.lɔˈnɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/panowie
        ("panowie","paˈnɔ.vʲɛ"),
# https://en.wiktionary.org/wiki/chłopiec
        ("chłopiec","ˈxwɔ.pʲɛt͡s"),
# https://en.wiktionary.org/wiki/życiu
        ("życiu","ˈʐɨ.t͡ɕu"),
# https://en.wiktionary.org/wiki/butelka
        ("butelka","buˈtɛl.ka"),
# https://en.wiktionary.org/wiki/inną
        ("inną","ˈin.nɔ̃"),
# https://en.wiktionary.org/wiki/nowoczesny
        ("nowoczesny","nɔ.vɔˈt͡ʂɛs.nɨ"),
# https://en.wiktionary.org/wiki/przykład
        ("przykład","ˈpʂɨ.kwat"),
# https://en.wiktionary.org/wiki/Zięć
        ("Zięć","ʑɛɲt͡ɕ"),
# https://en.wiktionary.org/wiki/porównywać
        ("porównywać","pɔ.ruvˈnɨ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/mów
        ("mów","muf"),
# https://en.wiktionary.org/wiki/czas
        ("czas","t͡ʂas"),
# https://en.wiktionary.org/wiki/dnia
        ("dnia","dɲa"),
# https://en.wiktionary.org/wiki/ładny
        ("ładny","ˈwad.nɨ"),
# https://en.wiktionary.org/wiki/mówisz
        ("mówisz","ˈmu.vʲiʂ"),
# https://en.wiktionary.org/wiki/wiesz
        ("wiesz","vʲɛʂ"),
# https://en.wiktionary.org/wiki/lekarza
        ("lekarza","lɛˈka.ʐa"),
# https://en.wiktionary.org/wiki/koleżanka
        ("koleżanka","kɔ.lɛˈʐan.ka"),
# https://en.wiktionary.org/wiki/widzisz.
        ("widzisz","ˈvʲi.d͡ʑiʂ"),
# https://en.wiktionary.org/wiki/przygotować
        ("przygotować","pʂɨ.ɡɔˈtɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/bawić
        ("bawić","ˈba.vʲit͡ɕ"),
# https://en.wiktionary.org/wiki/nigdzie
        ("nigdzie","ˈɲiɡ.d͡ʑɛ"),
# https://en.wiktionary.org/wiki/imię
        ("imię","ˈi.mʲɛ"),
# https://en.wiktionary.org/wiki/dostaniecie
        ("dostaniecie","dɔ.staˈɲɛ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/słychać
        ("słychać","ˈswɨ.xat͡ɕ"),
# https://en.wiktionary.org/wiki/dokładnie
        ("dokładnie","dɔˈkwa.dɲɛ"),
# https://en.wiktionary.org/wiki/żywego
        ("żywego","ʐɨˈvɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/wyobrażam
        ("wyobrażam","vɨ.ɔˈbra.ʐam"),
# https://en.wiktionary.org/wiki/zwykle
        ("zwykle","ˈzvɨk.lɛ"),
# https://en.wiktionary.org/wiki/doskonale
        ("doskonale","dɔ.skɔˈna.lɛ"),
# https://en.wiktionary.org/wiki/łapać
        ("łapać","ˈwa.pat͡ɕ"),
# https://en.wiktionary.org/wiki/rzeczywiście
        ("rzeczywiście","ʐɛ.t͡ʂɨˈvʲiɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/innego
        ("innego","inˈnɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/wiele
        ("wiele","ˈvʲɛ.lɛ"),
# https://en.wiktionary.org/wiki/zaczął
        ("zaczął","ˈza.t͡ʂɔ̃w"),
# https://en.wiktionary.org/wiki/pójdę
        ("pójdę","ˈpuj.dɛ"),
# https://en.wiktionary.org/wiki/bardziej
        ("bardziej","ˈbar.d͡ʑɛj"),
# https://en.wiktionary.org/wiki/miała
        ("miała","ˈmʲa.wa"),
# https://en.wiktionary.org/wiki/będziecie
        ("będziecie","bɛɲˈd͡ʑɛ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/żony
        ("żony","ˈʐɔ.nɨ"),
# https://en.wiktionary.org/wiki/sprawdzić
        ("sprawdzić","ˈsprav.d͡ʑit͡ɕ"),
# https://en.wiktionary.org/wiki/zaleta
        ("zaleta","zaˈlɛ.ta"),
# https://en.wiktionary.org/wiki/zmieniłeś
        ("zmieniłeś","zmʲɛˈɲi.wɛɕ"),
# https://en.wiktionary.org/wiki/powiedz
        ("powiedz","ˈpɔ.vʲɛt͡s"),
# https://en.wiktionary.org/wiki/siebie
        ("siebie","ˈɕɛ.bʲɛ"),
# https://en.wiktionary.org/wiki/piłki
        ("piłki","ˈpʲiw.kʲi"),
# https://en.wiktionary.org/wiki/zajęta
        ("zajęta","zaˈjɛn.ta"),
# https://en.wiktionary.org/wiki/mocny
        ("mocny","ˈmɔt͡s.nɨ"),
# https://en.wiktionary.org/wiki/kilkanaście
        ("kilkanaście","kʲil.kaˈnaɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/zacznę
        ("zacznę","ˈzat͡ʂ.nɛ"),
# https://en.wiktionary.org/wiki/Polakami
        ("Polakami","pɔ.laˈka.mʲi"),
# https://en.wiktionary.org/wiki/sobie
        ("sobie","ˈsɔ.bʲɛ"),
# https://en.wiktionary.org/wiki/gdybyście
        ("gdybyście","ɡdɨˈbɨɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/otworzyć
        ("otworzyć","ɔˈtfɔ.ʐɨt͡ɕ"),
# https://en.wiktionary.org/wiki/samochodem
        ("samochodem","sa.mɔˈxɔ.dɛm"),
# https://en.wiktionary.org/wiki/jakiś
        ("jakiś","ˈja.kʲiɕ"),
# https://en.wiktionary.org/wiki/drogach
        ("drogach","ˈdrɔ.ɡax"),
# https://en.wiktionary.org/wiki/najmniej
        ("najmniej","ˈnaj.mɲɛj"),
# https://en.wiktionary.org/wiki/myślałem
        ("myślałem","mɨɕˈla.wɛm"),
# https://en.wiktionary.org/wiki/wolałabym
        ("wolałabym","vɔ.laˈwa.bɨm"),
# https://en.wiktionary.org/wiki/tysiące
        ("tysiące","tɨˈɕɔn.t͡sɛ"),
# https://en.wiktionary.org/wiki/ulicy
        ("ulicy","uˈlʲi.t͡sɨ"),
# https://en.wiktionary.org/wiki/wyjątkowo
        ("wyjątkowo","vɨ.jɔnˈtkɔ.vɔ"),
# https://en.wiktionary.org/wiki/najpierw
        ("najpierw","ˈnaj.pʲɛrf"),
# https://en.wiktionary.org/wiki/innych
        ("innych","ˈin.nɨx"),
# https://en.wiktionary.org/wiki/łyżwy
        ("łyżwy","ˈwɨʐ.vɨ"),
# https://en.wiktionary.org/wiki/prace
        ("prace","ˈpra.t͡sɛ"),
# https://en.wiktionary.org/wiki/jazdy
        ("jazdy","ˈjaz.dɨ"),
# https://en.wiktionary.org/wiki/zadzwoni
        ("zadzwoni","zad͡zˈvɔ.ɲi"),
# https://en.wiktionary.org/wiki/dawna
        ("dawna","ˈdav.na"),
# https://en.wiktionary.org/wiki/musimy
        ("musimy","muˈɕi.mɨ"),
# https://en.wiktionary.org/wiki/idę
        ("idę","ˈi.dɛ"),
# https://en.wiktionary.org/wiki/umrę
        ("umrę","ˈu.mrɛ"),
# https://en.wiktionary.org/wiki/czyż
        ("czyż","t͡ʂɨʂ"),
# https://en.wiktionary.org/wiki/miesiącu
        ("miesiącu","mʲɛˈɕɔn.t͡su"),
# https://en.wiktionary.org/wiki/mówią
        ("mówią","ˈmu.vʲɔ̃"),
# https://en.wiktionary.org/wiki/straciłem
        ("straciłem","straˈt͡ɕi.wɛm"),
# https://en.wiktionary.org/wiki/piszą
        ("piszą","ˈpʲi.ʂɔ̃"),
# https://en.wiktionary.org/wiki/iść
        ("iść","iɕt͡ɕ"),
# https://en.wiktionary.org/wiki/płaci
        ("płaci","ˈpwa.t͡ɕi"),
# https://en.wiktionary.org/wiki/papierosy
        ("papierosy","pa.pʲɛˈrɔ.sɨ"),
# https://en.wiktionary.org/wiki/przeżyje
        ("przeżyje","pʂɛˈʐɨ.jɛ"),
# https://en.wiktionary.org/wiki/pojedziesz
        ("pojedziesz","pɔˈjɛ.d͡ʑɛʂ"),
# https://en.wiktionary.org/wiki/robimy
        ("robimy","rɔˈbʲi.mɨ"),
# https://en.wiktionary.org/wiki/robić
        ("robić","ˈrɔ.bʲit͡ɕ"),
# https://en.wiktionary.org/wiki/męża
        ("męża","ˈmɛŋ.ʐa"),
# https://en.wiktionary.org/wiki/zajmuje
        ("zajmuje","zajˈmu.jɛ"),
# https://en.wiktionary.org/wiki/córkę
        ("córkę","ˈt͡sur.kɛ"),
# https://en.wiktionary.org/wiki/podam
        ("podam","ˈpɔ.dam"),
# https://en.wiktionary.org/wiki/piękne
        ("piękne","ˈpʲɛŋ.knɛ"),
# https://en.wiktionary.org/wiki/cały
        ("cały","ˈt͡sa.wɨ"),
# https://en.wiktionary.org/wiki/często
        ("często","ˈt͡ʂɛ̃.stɔ"),
# https://en.wiktionary.org/wiki/drugie
        ("drugie","ˈdru.ɡʲɛ"),
# https://en.wiktionary.org/wiki/czasu
        ("czasu","ˈt͡ʂa.su"),
# https://en.wiktionary.org/wiki/dawnych
        ("dawnych","ˈdav.nɨx"),
# https://en.wiktionary.org/wiki/ciężko
        ("ciężko","ˈt͡ɕɛŋ.ʂkɔ"),
# https://en.wiktionary.org/wiki/zawód
        ("zawód","ˈza.vut"),
# https://en.wiktionary.org/wiki/natomiast
        ("natomiast","naˈtɔ.mʲast"),
# https://en.wiktionary.org/wiki/przyszłości
        ("przyszłości","pʂɨˈʂwɔɕ.t͡ɕi"),
# https://en.wiktionary.org/wiki/połączyć
        ("połączyć","pɔˈwɔn.t͡ʂɨt͡ɕ"),
# https://en.wiktionary.org/wiki/dość
        ("dość","dɔɕt͡ɕ"),
# https://en.wiktionary.org/wiki/taty
        ("taty","ˈta.tɨ"),
# https://en.wiktionary.org/wiki/paczki
#         ("paczki","ˈpɔntʃki"),
# https://en.wiktionary.org/wiki/między
        ("między","ˈmʲɛn.d͡zɨ"),
# https://en.wiktionary.org/wiki/opowiem
        ("opowiem","ɔˈpɔ.vʲɛm"),
# https://en.wiktionary.org/wiki/oddychać
        ("oddychać","ɔdˈdɨ.xat͡ɕ"),
# https://en.wiktionary.org/wiki/sztuki
        ("sztuki","ˈʂtu.kʲi"),
# https://en.wiktionary.org/wiki/porze
        ("porze","ˈpɔ.ʐɛ"),
# https://en.wiktionary.org/wiki/dzień
        ("dzień","d͡ʑɛɲ"),
# https://en.wiktionary.org/wiki/jednocześnie
        ("jednocześnie","jɛd.nɔˈt͡ʂɛɕ.ɲɛ"),
# https://en.wiktionary.org/wiki/zrobimy
        ("zrobimy","zrɔˈbʲi.mɨ"),
# https://en.wiktionary.org/wiki/oglądać
        ("oglądać","ɔɡˈlɔn.dat͡ɕ"),
# https://en.wiktionary.org/wiki/kapała
        ("kapała","kaˈpa.wa"),
# https://en.wiktionary.org/wiki/zanim
        ("zanim","ˈza.ɲim"),
# https://en.wiktionary.org/wiki/kogoś
        ("kogoś","ˈkɔ.ɡɔɕ"),
# https://en.wiktionary.org/wiki/spraw
        ("spraw","spraf"),
# https://en.wiktionary.org/wiki/miałaś
        ("miałaś","ˈmʲa.waɕ"),
# https://en.wiktionary.org/wiki/palę
        ("palę","ˈpa.lɛ"),
# https://en.wiktionary.org/wiki/kupować
        ("kupować","kuˈpɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/dział
        ("dział","d͡ʑaw"),
# https://en.wiktionary.org/wiki/razy
        ("razy","ˈra.zɨ"),
# https://en.wiktionary.org/wiki/piękne
        ("piękne","ˈpʲɛŋ.knɛ"),
# https://en.wiktionary.org/wiki/boisz
        ("boisz","ˈbɔ.iʂ"),
# https://en.wiktionary.org/wiki/niezbyt
        ("niezbyt","ˈɲɛz.bɨt"),
# https://en.wiktionary.org/wiki/częściej
        ("częściej","ˈt͡ʂɛɲ.ɕt͡ɕɛj"),
# https://en.wiktionary.org/wiki/pomarańczowy
        ("pomarańczowy","pɔ.ma.raɲˈt͡ʂɔ.vɨ"),
# https://en.wiktionary.org/wiki/trudne
        ("trudne","ˈtrud.nɛ"),
# https://en.wiktionary.org/wiki/boję
        ("boję","ˈbɔ.jɛ"),
# https://en.wiktionary.org/wiki/dokładnie
        ("dokładnie","dɔˈkwa.dɲɛ"),
# https://en.wiktionary.org/wiki/Cały
        ("Cały","ˈt͡sa.wɨ"),
# https://en.wiktionary.org/wiki/wystarczy
        ("wystarczy","vɨˈstar.t͡ʂɨ"),
# https://en.wiktionary.org/wiki/zjem
        ("zjem","zjɛm"),
# https://en.wiktionary.org/wiki/ciasta
        ("ciasta","ˈt͡ɕa.sta"),
# https://en.wiktionary.org/wiki/ojcem
        ("ojcem","ˈɔj.t͡sɛm"),
# https://en.wiktionary.org/wiki/pomóż
        ("pomóż","ˈpɔ.muʂ"),
# https://en.wiktionary.org/wiki/padało
        ("padało","ˈpadawɔ"),
# https://en.wiktionary.org/wiki/zakład
        ("zakład","ˈza.kwat"),
# https://en.wiktionary.org/wiki/wyciągać
        ("wyciągać","vɨˈt͡ɕɔŋ.ɡat͡ɕ"),
# https://en.wiktionary.org/wiki/robicie
        ("robicie","rɔˈbʲi.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/dwie
        ("dwie","dvʲɛ"),
# https://en.wiktionary.org/wiki/rysunek
        ("rysunek","rɨˈsu.nɛk"),
# https://en.wiktionary.org/wiki/idź
        ("idź","it͡ɕ"),
# https://en.wiktionary.org/wiki/piszesz
        ("piszesz","ˈpʲi.ʂɛʂ"),
# https://en.wiktionary.org/wiki/unikać
        ("unikać","uˈɲi.kat͡ɕ"),
# https://en.wiktionary.org/wiki/stałych
        ("stałych","ˈsta.wɨx"),
# https://en.wiktionary.org/wiki/drudzy
        ("drudzy","ˈdru.d͡zɨ"),
# https://en.wiktionary.org/wiki/przyniosę
        ("przyniosę","pʂɨˈɲɔ.sɛ"),
# https://en.wiktionary.org/wiki/godziny
        ("godziny","ɡɔˈd͡ʑi.nɨ"),
# https://en.wiktionary.org/wiki/piec
        ("piec","pʲɛt͡s"),
# https://en.wiktionary.org/wiki/córką
        ("córką","ˈt͡sur.kɔ̃"),
# https://en.wiktionary.org/wiki/takim
        ("takim","ˈta.kʲim"),
# https://en.wiktionary.org/wiki/wieczór
        ("wieczór","ˈvʲɛ.t͡ʂur"),
# https://en.wiktionary.org/wiki/słyszy
        ("słyszy","ˈswɨ.ʂɨ"),
# https://en.wiktionary.org/wiki/fajnych
        ("fajnych","ˈfaj.nɨx"),
# https://en.wiktionary.org/wiki/angielskim
        ("angielskim","anˈɡʲɛl.skʲim"),
# https://en.wiktionary.org/wiki/znaleźć
        ("znaleźć","ˈzna.lɛɕt͡ɕ"),
# https://en.wiktionary.org/wiki/dostałaś
        ("dostałaś","dɔˈsta.waɕ"),
# https://en.wiktionary.org/wiki/stracić
        ("stracić","ˈstra.t͡ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/zięć
        ("zięć","ʑɛɲt͡ɕ"),
# https://en.wiktionary.org/wiki/naszyjnik
        ("naszyjnik","naˈʂɨj.ɲik"),
# https://en.wiktionary.org/wiki/czyste
        ("czyste","ˈt͡ʂɨ.stɛ"),
# https://en.wiktionary.org/wiki/popołudnie
        ("popołudnie","pɔ.pɔˈwu.dɲɛ"),
# https://en.wiktionary.org/wiki/niedaleko
        ("niedaleko","ɲɛ.daˈlɛ.kɔ"),
# https://en.wiktionary.org/wiki/Ja
#        ("Ja","-aː"),
# https://en.wiktionary.org/wiki/czym
        ("czym","t͡ʂɨm"),
# https://en.wiktionary.org/wiki/kochają
        ("kochają","kɔˈxa.jɔ̃"),
# https://en.wiktionary.org/wiki/zje
        ("zje","zjɛ"),
# https://en.wiktionary.org/wiki/zawracać
        ("zawracać","zaˈvra.t͡sat͡ɕ"),
# https://en.wiktionary.org/wiki/wkrótce
        ("wkrótce","ˈfkrut.t͡sɛ"),
# https://en.wiktionary.org/wiki/pewna
        ("pewna","ˈpɛv.na"),
# https://en.wiktionary.org/wiki/ochotę
        ("ochotę","ɔˈxɔ.tɛ"),
# https://en.wiktionary.org/wiki/łyk
        ("łyk","wɨk"),
# https://en.wiktionary.org/wiki/obiad
        ("obiad","ˈɔ.bʲat"),
# https://en.wiktionary.org/wiki/nauczyłeś
        ("nauczyłeś","na.uˈt͡ʂɨ.wɛɕ"),
# https://en.wiktionary.org/wiki/zapłacił
        ("zapłacił","zaˈpwa.t͡ɕiw"),
# https://en.wiktionary.org/wiki/wstawać
        ("wstawać","ˈfsta.vat͡ɕ"),
# https://en.wiktionary.org/wiki/zaprosić
        ("zaprosić","zaˈprɔ.ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/spotkajmy
        ("spotkajmy","spɔtˈkaj.mɨ"),
# https://en.wiktionary.org/wiki/każesz
        ("każesz","ˈka.ʐɛʂ"),
# https://en.wiktionary.org/wiki/mieszkanie
        ("mieszkanie","mʲɛʂˈka.ɲɛ"),
# https://en.wiktionary.org/wiki/osiem
        ("osiem","ˈɔ.ɕɛm"),
# https://en.wiktionary.org/wiki/gdzie
        ("gdzie","ɡd͡ʑɛ"),
# https://en.wiktionary.org/wiki/rzeczy
        ("rzeczy","ˈʐɛ.t͡ʂɨ"),
# https://en.wiktionary.org/wiki/wyżej
        ("wyżej","ˈvɨ.ʐɛj"),
# https://en.wiktionary.org/wiki/pomóc
        ("pomóc","ˈpɔ.mut͡s"),
# https://en.wiktionary.org/wiki/pasztet
        ("pasztet","ˈpaʂ.tɛt"),
# https://en.wiktionary.org/wiki/wcale
        ("wcale","ˈft͡sa.lɛ"),
# https://en.wiktionary.org/wiki/dziwne
        ("dziwne","ˈd͡ʑiv.nɛ"),
# https://en.wiktionary.org/wiki/dbają
        ("dbają","ˈdba.jɔ̃"),
# https://en.wiktionary.org/wiki/widziałam
        ("widziałam","vʲiˈd͡ʑa.wam"),
# https://en.wiktionary.org/wiki/książki
        ("książki","ˈkɕɔŋ.ʂkʲi"),
# https://en.wiktionary.org/wiki/drugim
        ("drugim","ˈdruɡʲim"),
# https://en.wiktionary.org/wiki/mnie
        ("mnie","mɲɛ"),
# https://en.wiktionary.org/wiki/dłużej
        ("dłużej","ˈdwu.ʐɛj"),
# https://en.wiktionary.org/wiki/wydał
        ("wydał","ˈvɨ.daw"),
# https://en.wiktionary.org/wiki/dwadzieścia
        ("dwadzieścia","dvaˈd͡ʑɛɕ.t͡ɕa"),
# https://en.wiktionary.org/wiki/nawet
        ("nawet","ˈna.vɛt"),
# https://en.wiktionary.org/wiki/zdolny
        ("zdolny","ˈzdɔl.nɨ"),
# https://en.wiktionary.org/wiki/pytam
        ("pytam","ˈpɨtam"),
# https://en.wiktionary.org/wiki/wolnej
        ("wolnej","ˈvɔl.nɛj"),
# https://en.wiktionary.org/wiki/życie
        ("życie","ˈʐɨ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/tuż
        ("tuż","tuʂ"),
# https://en.wiktionary.org/wiki/Niemiec
        ("Niemiec","ˈɲɛ.mʲɛt͡s"),
# https://en.wiktionary.org/wiki/wydarzyło
        ("wydarzyło","vɨ.daˈʐɨ.wɔ"),
# https://en.wiktionary.org/wiki/oczy
        ("oczy","ˈɔ.t͡ʂɨ"),
# https://en.wiktionary.org/wiki/widział
        ("widział","ˈvʲi.d͡ʑaw"),
# https://en.wiktionary.org/wiki/zostać
        ("zostać","ˈzɔ.stat͡ɕ"),
# https://en.wiktionary.org/wiki/partnera
        ("partnera","parˈtnɛ.ra"),
# https://en.wiktionary.org/wiki/dałaś
        ("dałaś","ˈda.waɕ"),
# https://en.wiktionary.org/wiki/będąc
        ("będąc","ˈbɛn.dɔnt͡s"),
# https://en.wiktionary.org/wiki/poznał
        ("poznał","ˈpɔz.naw"),
# https://en.wiktionary.org/wiki/przypadkiem
        ("przypadkiem","pʂɨˈpat.kʲɛm"),
# https://en.wiktionary.org/wiki/meble
        ("meble","ˈmɛb.lɛ"),
# https://en.wiktionary.org/wiki/córka
        ("córka","ˈt͡sur.ka"),
# https://en.wiktionary.org/wiki/piękno
        ("piękno","ˈpʲɛŋ.knɔ"),
# https://en.wiktionary.org/wiki/znasz
        ("znasz","znaʂ"),
# https://en.wiktionary.org/wiki/przedtem
        ("przedtem","ˈpʂɛt.tɛm"),
# https://en.wiktionary.org/wiki/przyjaciel
        ("przyjaciel","pʂɨˈja.t͡ɕɛl"),
# https://en.wiktionary.org/wiki/zwykły
        ("zwykły","ˈzvɨ.kwɨ"),
# https://en.wiktionary.org/wiki/spokojnie
        ("spokojnie","spɔˈkɔj.ɲɛ"),
# https://en.wiktionary.org/wiki/powiedzieć
        ("powiedzieć","pɔˈvʲɛ.d͡ʑɛt͡ɕ"),
# https://en.wiktionary.org/wiki/mogli
        ("mogli","ˈmɔɡ.lʲi"),
# https://en.wiktionary.org/wiki/sami
        ("sami","ˈsa.mʲi"),
# https://en.wiktionary.org/wiki/kolacja
        ("kolacja","kɔˈlat͡s.ja"),
# https://en.wiktionary.org/wiki/dużym
        ("dużym","ˈdu.ʐɨm"),
# https://en.wiktionary.org/wiki/wygrałem
        ("wygrałem","vɨˈɡra.wɛm"),
# https://en.wiktionary.org/wiki/jeszcze
        ("jeszcze","ˈjɛʂ.t͡ʂɛ"),
# https://en.wiktionary.org/wiki/lubi
        ("lubi","ˈlu.bʲi"),
# https://en.wiktionary.org/wiki/życia
        ("życia","ˈʐɨ.t͡ɕa"),
# https://en.wiktionary.org/wiki/sprzedać
        ("sprzedać","ˈspʂɛ.dat͡ɕ"),
# https://en.wiktionary.org/wiki/żona
        ("żona","ˈʐɔ.na"),
# https://en.wiktionary.org/wiki/dzwonił
        ("dzwonił","ˈd͡zvɔ.ɲiw"),
# https://en.wiktionary.org/wiki/Ewa
        ("Ewa","ˈɛ.va"),
# https://en.wiktionary.org/wiki/Kazała
        ("Kazała","kaˈza.wa"),
# https://en.wiktionary.org/wiki/zostawić
        ("zostawić","zɔˈsta.vʲit͡ɕ"),
# https://en.wiktionary.org/wiki/butelkę
        ("butelkę","buˈtɛl.kɛ"),
# https://en.wiktionary.org/wiki/większe
        ("większe","ˈvʲɛŋ.kʂɛ"),
# https://en.wiktionary.org/wiki/udane
        ("udane","uˈda.nɛ"),
# https://en.wiktionary.org/wiki/wakacje
        ("wakacje","vaˈkat͡s.jɛ"),
# https://en.wiktionary.org/wiki/lepiej
        ("lepiej","ˈlɛ.pʲɛj"),
# https://en.wiktionary.org/wiki/wybrał
        ("wybrał","ˈvɨ.braw"),
# https://en.wiktionary.org/wiki/masz
        ("masz","maʂ"),
# https://en.wiktionary.org/wiki/perfumy
        ("perfumy","pɛˈrfu.mɨ"),
# https://en.wiktionary.org/wiki/możemy
        ("możemy","mɔˈʐɛ.mɨ"),
# https://en.wiktionary.org/wiki/książkę
        ("książkę","ˈkɕɔŋ.ʂkɛ"),
# https://en.wiktionary.org/wiki/okazja
        ("okazja","ɔˈkaz.ja"),
# https://en.wiktionary.org/wiki/obcować
        ("obcować","ɔpˈt͡sɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/dzieci
        ("dzieci","ˈd͡ʑɛ.t͡ɕi"),
# https://en.wiktionary.org/wiki/gotowe
        ("gotowe","ɡɔˈtɔ.vɛ"),
# https://en.wiktionary.org/wiki/doskonałe
        ("doskonałe","dɔ.skɔˈna.wɛ"),
# https://en.wiktionary.org/wiki/ludźmi
        ("ludźmi","ˈlud͡ʑ.mʲi"),
# https://en.wiktionary.org/wiki/pieniędzy
        ("pieniędzy","pʲɛˈɲɛn.d͡zɨ"),
# https://en.wiktionary.org/wiki/małżeństwo
        ("małżeństwo","mawˈʐɛɲ.stfɔ"),
# https://en.wiktionary.org/wiki/nią
        ("nią","ɲɔ̃"),
# https://en.wiktionary.org/wiki/przynosi
        ("przynosi","pʂɨˈnɔ.ɕi"),
# https://en.wiktionary.org/wiki/lepiej
        ("lepiej","ˈlɛ.pʲɛj"),
# https://en.wiktionary.org/wiki/nowym
        ("nowym","ˈnɔ.vɨm"),
# https://en.wiktionary.org/wiki/byłam
        ("byłam","ˈbɨ.wam"),
# https://en.wiktionary.org/wiki/innego
        ("innego","inˈnɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/palenie
        ("palenie","paˈlɛ.ɲɛ"),
# https://en.wiktionary.org/wiki/cię
        ("cię","t͡ɕɛ"),
# https://en.wiktionary.org/wiki/byłeś
        ("byłeś","ˈbɨ.wɛɕ"),
# https://en.wiktionary.org/wiki/zdaje
        ("zdaje","ˈzda.jɛ"),
# https://en.wiktionary.org/wiki/łóżku
        ("łóżku","ˈwuʂ.ku"),
# https://en.wiktionary.org/wiki/zmęczona
        ("zmęczona","zmɛnˈt͡ʂɔ.na"),
# https://en.wiktionary.org/wiki/czekać
        ("czekać","ˈt͡ʂɛ.kat͡ɕ"),
# https://en.wiktionary.org/wiki/myśleć
        ("myśleć","ˈmɨɕ.lɛt͡ɕ"),
# https://en.wiktionary.org/wiki/picia
        ("picia","ˈpʲi.t͡ɕa"),
# https://en.wiktionary.org/wiki/wielki
        ("wielki","ˈvʲɛl.kʲi"),
# https://en.wiktionary.org/wiki/jazdy
        ("jazdy","ˈjaz.dɨ"),
# https://en.wiktionary.org/wiki/minę
        ("minę","ˈmʲi.nɛ"),
# https://en.wiktionary.org/wiki/kioski
#         ("kioski","-oski"),
# https://en.wiktionary.org/wiki/głośniej
        ("głośniej","ˈɡwɔɕ.ɲɛj"),
# https://en.wiktionary.org/wiki/wyszedł
        ("wyszedł","ˈvɨ.ʂɛdw"),
# https://en.wiktionary.org/wiki/dziś
        ("dziś","d͡ʑiɕ"),
# https://en.wiktionary.org/wiki/miesiąc
        ("miesiąc","ˈmʲɛ.ɕɔnt͡s"),
# https://en.wiktionary.org/wiki/włoska
        ("włoska","ˈvwɔ.ska"),
# https://en.wiktionary.org/wiki/przynosić
        ("przynosić","pʂɨˈnɔ.ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/pewno
        ("pewno","ˈpɛv.nɔ"),
# https://en.wiktionary.org/wiki/lasu
        ("lasu","ˈla.su"),
# https://en.wiktionary.org/wiki/nikogo
        ("nikogo","ɲiˈkɔ.ɡɔ"),
# https://en.wiktionary.org/wiki/zadowolony
        ("zadowolony","za.dɔ.vɔˈlɔ.nɨ"),
# https://en.wiktionary.org/wiki/bardzo
        ("bardzo","ˈbar.d͡zɔ"),
# https://en.wiktionary.org/wiki/niczego
        ("niczego","ɲiˈt͡ʂɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/dzwoni
        ("dzwoni","ˈd͡zvɔ.ɲi"),
# https://en.wiktionary.org/wiki/wrócić
        ("wrócić","ˈvru.t͡ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/musisz
        ("musisz","ˈmu.ɕiʂ"),
# https://en.wiktionary.org/wiki/sobotę
        ("sobotę","sɔˈbɔ.tɛ"),
# https://en.wiktionary.org/wiki/swoim
        ("swoim","ˈsfɔ.im"),
# https://en.wiktionary.org/wiki/mieszkać
        ("mieszkać","ˈmʲɛʂ.kat͡ɕ"),
# https://en.wiktionary.org/wiki/szkole
        ("szkole","ˈʂkɔ.lɛ"),
# https://en.wiktionary.org/wiki/ostatniej
        ("ostatniej","ɔˈstat.ɲɛj"),
# https://en.wiktionary.org/wiki/godzinę
        ("godzinę","ɡɔˈd͡ʑi.nɛ"),
# https://en.wiktionary.org/wiki/temu
        ("temu","ˈtɛ.mu"),
# https://en.wiktionary.org/wiki/byle
        ("byle","ˈbɨ.lɛ"),
# https://en.wiktionary.org/wiki/jego
        ("jego","ˈjɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/uwielbia
        ("uwielbia","uˈvʲɛl.bʲa"),
# https://en.wiktionary.org/wiki/znalazłeś
        ("znalazłeś","znaˈla.zwɛɕ"),
# https://en.wiktionary.org/wiki/pozwolenie
        ("pozwolenie","pɔz.vɔˈlɛ.ɲɛ"),
# https://en.wiktionary.org/wiki/myślisz
        ("myślisz","ˈmɨɕ.lʲiʂ"),
# https://en.wiktionary.org/wiki/idziesz
        ("idziesz","ˈi.d͡ʑɛʂ"),
# https://en.wiktionary.org/wiki/zbyt
        ("zbyt","zbɨt"),
# https://en.wiktionary.org/wiki/mówię
        ("mówię","ˈmu.vʲɛ"),
# https://en.wiktionary.org/wiki/wiec
        ("wiec","vʲɛt͡s"),
# https://en.wiktionary.org/wiki/drużyna
        ("drużyna","druˈʐɨ.na"),
# https://en.wiktionary.org/wiki/podać
        ("podać","ˈpɔ.dat͡ɕ"),
# https://en.wiktionary.org/wiki/bólem
        ("bólem","ˈbu.lɛm"),
# https://en.wiktionary.org/wiki/ciepłego
        ("ciepłego","t͡ɕɛˈpwɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/pół
        ("pół","puw"),
# https://en.wiktionary.org/wiki/koniecznie
        ("koniecznie","kɔˈɲɛt͡ʂ.ɲɛ"),
# https://en.wiktionary.org/wiki/podróż
        ("podróż","ˈpɔ.druʂ"),
# https://en.wiktionary.org/wiki/powiedział
        ("powiedział","pɔˈvʲɛ.d͡ʑaw"),
# https://en.wiktionary.org/wiki/smutna
        ("smutna","ˈsmut.na"),
# https://en.wiktionary.org/wiki/kazał
        ("kazał","ˈka.zaw"),
# https://en.wiktionary.org/wiki/gorąco
        ("gorąco","ɡɔˈrɔn.t͡sɔ"),
# https://en.wiktionary.org/wiki/poniedziałek
        ("poniedziałek","pɔ.ɲɛˈd͡ʑa.wɛk"),
# https://en.wiktionary.org/wiki/podałem
        ("podałem","pɔˈda.wɛm"),
# https://en.wiktionary.org/wiki/srebrne
        ("srebrne","ˈsrɛ.brnɛ"),
# https://en.wiktionary.org/wiki/żadnych
        ("żadnych","ˈʐad.nɨx"),
# https://en.wiktionary.org/wiki/radę
        ("radę","ˈra.dɛ"),
# https://en.wiktionary.org/wiki/miały
        ("miały","ˈmʲa.wɨ"),
# https://en.wiktionary.org/wiki/rzucił
        ("rzucił","ˈʐu.t͡ɕiw"),
# https://en.wiktionary.org/wiki/kupiłem
        ("kupiłem","kuˈpʲi.wɛm"),
# https://en.wiktionary.org/wiki/mówią
        ("mówią","ˈmu.vʲɔ̃"),
# https://en.wiktionary.org/wiki/niej
        ("niej","ɲɛj"),
# https://en.wiktionary.org/wiki/bratem
        ("bratem","ˈbra.tɛm"),
# https://en.wiktionary.org/wiki/nakryć
        ("nakryć","ˈna.krɨt͡ɕ"),
# https://en.wiktionary.org/wiki/mm
#         ("mm","mɛm"),
# https://en.wiktionary.org/wiki/chciała
        ("chciała","ˈxt͡ɕa.wa"),
# https://en.wiktionary.org/wiki/znajomy
        ("znajomy","znaˈjɔ.mɨ"),
# https://en.wiktionary.org/wiki/podanie
        ("podanie","pɔˈda.ɲɛ"),
# https://en.wiktionary.org/wiki/słychać
        ("słychać","ˈswɨ.xat͡ɕ"),
# https://en.wiktionary.org/wiki/tłustych
        ("tłustych","ˈtwu.stɨx"),
# https://en.wiktionary.org/wiki/wasze
        ("wasze","ˈva.ʂɛ"),
# https://en.wiktionary.org/wiki/rodzaj
        ("rodzaj","ˈrɔ.d͡zaj"),
# https://en.wiktionary.org/wiki/kolacja
        ("kolacja","kɔˈlat͡s.ja"),
# https://en.wiktionary.org/wiki/pobrać
        ("pobrać","ˈpɔ.brat͡ɕ"),
# https://en.wiktionary.org/wiki/pobliżu
        ("pobliżu","pɔbˈlʲi.ʐu"),
# https://en.wiktionary.org/wiki/woda
        ("woda","ˈvɔ.da"),
# https://en.wiktionary.org/wiki/umiem
        ("umiem","ˈu.mʲɛm"),
# https://en.wiktionary.org/wiki/ulicę
        ("ulicę","uˈlʲi.t͡sɛ"),
# https://en.wiktionary.org/wiki/chłopak
        ("chłopak","ˈxwɔ.pak"),
# https://en.wiktionary.org/wiki/kolejce
        ("kolejce","kɔˈlɛj.t͡sɛ"),
# https://en.wiktionary.org/wiki/miałby
        ("miałby","ˈmʲaw.bɨ"),
# https://en.wiktionary.org/wiki/osobistym
        ("osobistym","ɔ.sɔˈbʲi.stɨm"),
# https://en.wiktionary.org/wiki/zrobił
        ("zrobił","ˈzrɔ.bʲiw"),
# https://en.wiktionary.org/wiki/pomóc
        ("pomóc","ˈpɔ.mut͡s"),
# https://en.wiktionary.org/wiki/pracować
        ("pracować","praˈt͡sɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/Mazury
        ("Mazury","maˈzu.rɨ"),
# https://en.wiktionary.org/wiki/postęp
        ("postęp","ˈpɔ.stɛmp"),
# https://en.wiktionary.org/wiki/ostatnio
        ("ostatnio","ɔˈstat.ɲɔ"),
# https://en.wiktionary.org/wiki/pokój
        ("pokój","ˈpɔ.kuj"),
# https://en.wiktionary.org/wiki/moim
        ("moim","ˈmɔ.im"),
# https://en.wiktionary.org/wiki/zapomniałem
        ("zapomniałem","za.pɔmˈɲa.wɛm"),
# https://en.wiktionary.org/wiki/dwoje
        ("dwoje","ˈdvɔ.jɛ"),
# https://en.wiktionary.org/wiki/wypadku
        ("wypadku","vɨˈpat.ku"),
# https://en.wiktionary.org/wiki/przyjaciele
        ("przyjaciele","pʂɨ.jaˈt͡ɕɛ.lɛ"),
# https://en.wiktionary.org/wiki/zapomnij
        ("zapomnij","zaˈpɔm.ɲij"),
# https://en.wiktionary.org/wiki/dzieła
        ("dzieła","ˈd͡ʑɛ.wa"),
# https://en.wiktionary.org/wiki/mogłem
        ("mogłem","ˈmɔ.ɡwɛm"),
# https://en.wiktionary.org/wiki/sieje
        ("sieje","ˈɕɛ.jɛ"),
# https://en.wiktionary.org/wiki/płyta
        ("płyta","ˈpwɨ.ta"),
# https://en.wiktionary.org/wiki/mogłabyś
        ("mogłabyś","ˈmɔ.ɡwa.bɨɕ"),
# https://en.wiktionary.org/wiki/twoim
        ("twoim","ˈtfɔ.im"),
# https://en.wiktionary.org/wiki/jakich
        ("jakich","ˈja.kʲix"),
# https://en.wiktionary.org/wiki/pójdziemy
        ("pójdziemy","pujˈd͡ʑɛ.mɨ"),
# https://en.wiktionary.org/wiki/zrobić
        ("zrobić","ˈzrɔ.bʲit͡ɕ"),
# https://en.wiktionary.org/wiki/uprawiać
        ("uprawiać","uˈpra.vʲat͡ɕ"),
# https://en.wiktionary.org/wiki/hotelu
        ("hotelu","xɔˈtɛ.lu"),
# https://en.wiktionary.org/wiki/usunięcie
        ("usunięcie","u.suˈɲɛɲ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/urządzenie
        ("urządzenie","u.ʐɔnˈd͡zɛ.ɲɛ"),
# https://en.wiktionary.org/wiki/tamta
        ("tamta","ˈtamta"),
# https://en.wiktionary.org/wiki/zrobisz
        ("zrobisz","ˈzrɔ.bʲiʂ"),
# https://en.wiktionary.org/wiki/gatunek
        ("gatunek","ɡaˈtu.nɛk"),
# https://en.wiktionary.org/wiki/uczyć
        ("uczyć","ˈu.t͡ʂɨt͡ɕ"),
# https://en.wiktionary.org/wiki/idzie
        ("idzie","ˈi.d͡ʑɛ"),
# https://en.wiktionary.org/wiki/duża
        ("duża","ˈdu.ʐa"),
# https://en.wiktionary.org/wiki/roboty
        ("roboty","rɔˈbɔ.tɨ"),
# https://en.wiktionary.org/wiki/nauki
        ("nauki","naˈu.kʲi"),
# https://en.wiktionary.org/wiki/duża
        ("duża","ˈdu.ʐa"),
# https://en.wiktionary.org/wiki/marny
        ("marny","ˈmar.nɨ"),
# https://en.wiktionary.org/wiki/jesz
        ("jesz","jɛʂ"),
# https://en.wiktionary.org/wiki/chciałeś
        ("chciałeś","ˈxt͡ɕa.wɛɕ"),
# https://en.wiktionary.org/wiki/bierze
        ("bierze","ˈbʲɛ.ʐɛ"),
# https://en.wiktionary.org/wiki/miesięcy
        ("miesięcy","mʲɛˈɕɛn.t͡sɨ"),
# https://en.wiktionary.org/wiki/warto
        ("warto","ˈvar.tɔ"),
# https://en.wiktionary.org/wiki/praca
        ("praca","ˈpra.t͡sa"),
# https://en.wiktionary.org/wiki/Tomek
        ("Tomek","ˈtɔ.mɛk"),
# https://en.wiktionary.org/wiki/macie
        ("macie","ˈma.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/sytuację
        ("sytuację","sɨ.tuˈat͡s.jɛ"),
# https://en.wiktionary.org/wiki/wolna
        ("wolna","ˈvɔl.na"),
# https://en.wiktionary.org/wiki/południu
        ("południu","pɔˈwu.dɲu"),
# https://en.wiktionary.org/wiki/dzisiaj
        ("dzisiaj","ˈd͡ʑi.ɕaj"),
# https://en.wiktionary.org/wiki/wsią
        ("wsią","fɕɔ̃"),
# https://en.wiktionary.org/wiki/polskiego
        ("polskiego","pɔlˈskʲɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/słonie
        ("słonie","ˈswɔ.ɲɛ"),
# https://en.wiktionary.org/wiki/później
        ("później","ˈpuʑ.ɲɛj"),
# https://en.wiktionary.org/wiki/samym
        ("samym","ˈsa.mɨm"),
# https://en.wiktionary.org/wiki/żurnal
        ("żurnal","ˈʐur.nal"),
# https://en.wiktionary.org/wiki/pójdziesz
        ("pójdziesz","ˈpuj.d͡ʑɛʂ"),
# https://en.wiktionary.org/wiki/padał
        ("padał","ˈpadaw"),
# https://en.wiktionary.org/wiki/iść
        ("iść","iɕt͡ɕ"),
# https://en.wiktionary.org/wiki/przedtem
        ("przedtem","ˈpʂɛt.tɛm"),
# https://en.wiktionary.org/wiki/kłopotów
        ("kłopotów","kwɔˈpɔ.tuf"),
# https://en.wiktionary.org/wiki/sposób
        ("sposób","ˈspɔ.sup"),
# https://en.wiktionary.org/wiki/warto
        ("warto","ˈvar.tɔ"),
# https://en.wiktionary.org/wiki/jakaś
        ("jakaś","ˈja.kaɕ"),
# https://en.wiktionary.org/wiki/polskiego
        ("polskiego","pɔlˈskʲɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/śpisz
        ("śpisz","ɕpʲiʂ"),
# https://en.wiktionary.org/wiki/palić
        ("palić","ˈpa.lʲit͡ɕ"),
# https://en.wiktionary.org/wiki/wieczorem
        ("wieczorem","vʲɛˈt͡ʂɔ.rɛm"),
# https://en.wiktionary.org/wiki/wiesz
        ("wiesz","vʲɛʂ"),
# https://en.wiktionary.org/wiki/My
#         ("My","-yː"),
# https://en.wiktionary.org/wiki/musi
        ("musi","ˈmu.ɕi"),
# https://en.wiktionary.org/wiki/sprawę
        ("sprawę","ˈspra.vɛ"),
# https://en.wiktionary.org/wiki/niebezpieczny
        ("niebezpieczny","ɲɛ.bɛsˈpʲɛt͡ʂ.nɨ"),
# https://en.wiktionary.org/wiki/jaj
#         ("jaj","ˈjɒj"),
# https://en.wiktionary.org/wiki/rodzaju
        ("rodzaju","rɔˈd͡za.ju"),
# https://en.wiktionary.org/wiki/skręcić
        ("skręcić","ˈskrɛɲ.t͡ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/ważne
        ("ważne","ˈvaʐ.nɛ"),
# https://en.wiktionary.org/wiki/mogła
        ("mogła","ˈmɔ.ɡwa"),
# https://en.wiktionary.org/wiki/Krystyna
        ("Krystyna","krɨˈstɨ.na"),
# https://en.wiktionary.org/wiki/ochoty
        ("ochoty","ɔˈxɔ.tɨ"),
# https://en.wiktionary.org/wiki/swoją
        ("swoją","ˈsfɔ.jɔ̃"),
# https://en.wiktionary.org/wiki/innymi
        ("innymi","inˈnɨ.mʲi"),
# https://en.wiktionary.org/wiki/mieszkać
        ("mieszkać","ˈmʲɛʂ.kat͡ɕ"),
# https://en.wiktionary.org/wiki/miejsca
        ("miejsca","ˈmʲɛj.st͡sa"),
# https://en.wiktionary.org/wiki/weźmiemy
        ("weźmiemy","vɛʑˈmʲɛ.mɨ"),
# https://en.wiktionary.org/wiki/ptaki
        ("ptaki","ˈpta.kʲi"),
# https://en.wiktionary.org/wiki/panią
        ("panią","ˈpa.ɲɔ̃"),
# https://en.wiktionary.org/wiki/pamiętasz
        ("pamiętasz","paˈmʲɛn.taʂ"),
# https://en.wiktionary.org/wiki/zobaczysz
        ("zobaczysz","zɔˈba.t͡ʂɨʂ"),
# https://en.wiktionary.org/wiki/mocna
        ("mocna","ˈmɔt͡s.na"),
# https://en.wiktionary.org/wiki/prawdziwy
        ("prawdziwy","pravˈd͡ʑi.vɨ"),
# https://en.wiktionary.org/wiki/robiliście
        ("robiliście","rɔ.bʲiˈlʲiɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/prawda
        ("prawda","ˈprav.da"),
# https://en.wiktionary.org/wiki/którego
        ("którego","ktuˈrɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/nową
        ("nową","ˈnɔ.vɔ̃"),
# https://en.wiktionary.org/wiki/nadzieje
        ("nadzieje","naˈd͡ʑɛ.jɛ"),
# https://en.wiktionary.org/wiki/parter
        ("parter","ˈpar.tɛr"),
# https://en.wiktionary.org/wiki/dokąd
        ("dokąd","ˈdɔ.kɔnt"),
# https://en.wiktionary.org/wiki/zdam
        ("zdam","zdam"),
# https://en.wiktionary.org/wiki/oglądaliśmy
        ("oglądaliśmy","ɔɡ.lɔn.daˈlʲiɕ.mɨ"),
# https://en.wiktionary.org/wiki/piękna
        ("piękna","ˈpʲɛŋ.kna"),
# https://en.wiktionary.org/wiki/idziemy
        ("idziemy","iˈd͡ʑɛ.mɨ"),
# https://en.wiktionary.org/wiki/marzy
        ("marzy","ˈma.ʐɨ"),
# https://en.wiktionary.org/wiki/myję
        ("myję","ˈmɨ.jɛ"),
# https://en.wiktionary.org/wiki/rozmowa
        ("rozmowa","rɔzˈmɔ.va"),
# https://en.wiktionary.org/wiki/teatru
#         ("teatru","ˈte̯a.tru"),
# https://en.wiktionary.org/wiki/zachód
        ("zachód","ˈza.xut"),
# https://en.wiktionary.org/wiki/martwi
        ("martwi","ˈmar.tfʲi"),
# https://en.wiktionary.org/wiki/pieniędzmi
        ("pieniędzmi","pʲɛˈɲɛn.d͡zmʲi"),
# https://en.wiktionary.org/wiki/starzy
        ("starzy","ˈsta.ʐɨ"),
# https://en.wiktionary.org/wiki/przy
        ("przy","pʂɨ"),
# https://en.wiktionary.org/wiki/zależy
        ("zależy","zaˈlɛ.ʐɨ"),
# https://en.wiktionary.org/wiki/swoich
        ("swoich","ˈsfɔ.ix"),
# https://en.wiktionary.org/wiki/ciebie
        ("ciebie","ˈt͡ɕɛ.bʲɛ"),
# https://en.wiktionary.org/wiki/razem
        ("razem","ˈra.zɛm"),
# https://en.wiktionary.org/wiki/stoi
        ("stoi","ˈstɔ.i"),
# https://en.wiktionary.org/wiki/wieku
        ("wieku","ˈvʲɛ.ku"),
# https://en.wiktionary.org/wiki/dokąd
        ("dokąd","ˈdɔ.kɔnt"),
# https://en.wiktionary.org/wiki/gotowa
        ("gotowa","ɡɔˈtɔ.va"),
# https://en.wiktionary.org/wiki/wszystkie
        ("wszystkie","ˈfʂɨ.stkʲɛ"),
# https://en.wiktionary.org/wiki/uwielbiam
        ("uwielbiam","uˈvʲɛl.bʲam"),
# https://en.wiktionary.org/wiki/czasu
        ("czasu","ˈt͡ʂa.su"),
# https://en.wiktionary.org/wiki/można
        ("można","ˈmɔʐ.na"),
# https://en.wiktionary.org/wiki/znoszę
        ("znoszę","ˈznɔ.ʂɛ"),
# https://en.wiktionary.org/wiki/filmie
        ("filmie","ˈfʲil.mʲɛ"),
# https://en.wiktionary.org/wiki/czy
        ("czy","t͡ʂɨ"),
# https://en.wiktionary.org/wiki/mecz
        ("mecz","mɛt͡ʂ"),
# https://en.wiktionary.org/wiki/chciało
        ("chciało","ˈxt͡ɕa.wɔ"),
# https://en.wiktionary.org/wiki/szampon
        ("szampon","ˈʂam.pɔn"),
# https://en.wiktionary.org/wiki/mogłaby
        ("mogłaby","ˈmɔ.ɡwa.bɨ"),
# https://en.wiktionary.org/wiki/która
        ("która","ˈktu.ra"),
# https://en.wiktionary.org/wiki/miałem
        ("miałem","ˈmʲa.wɛm"),
# https://en.wiktionary.org/wiki/bądź
        ("bądź","bɔɲt͡ɕ"),
# https://en.wiktionary.org/wiki/sweter
        ("sweter","ˈsfɛ.tɛr"),
# https://en.wiktionary.org/wiki/wcześniej
        ("wcześniej","ˈft͡ʂɛɕ.ɲɛj"),
# https://en.wiktionary.org/wiki/teatr
        ("teatr","ˈtɛ.atr"),
# https://en.wiktionary.org/wiki/moją
        ("moją","ˈmɔ.jɔ̃"),
# https://en.wiktionary.org/wiki/dotknąć
        ("dotknąć","ˈdɔt.knɔɲt͡ɕ"),
# https://en.wiktionary.org/wiki/zimno
        ("zimno","ˈʑim.nɔ"),
# https://en.wiktionary.org/wiki/mmm
#         ("mmm","m̩ː(ː)"),
# https://en.wiktionary.org/wiki/pańska
        ("pańska","ˈpaɲ.ska"),
# https://en.wiktionary.org/wiki/państwa
        ("państwa","ˈpaɲ.stfa"),
# https://en.wiktionary.org/wiki/robiliście
        ("robiliście","rɔ.bʲiˈlʲiɕ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/ręka
        ("ręka","ˈrɛŋ.ka"),
# https://en.wiktionary.org/wiki/przed
        ("przed","pʂɛt"),
# https://en.wiktionary.org/wiki/pomogę
        ("pomogę","pɔˈmɔ.ɡɛ"),
# https://en.wiktionary.org/wiki/cielęcy
        ("cielęcy","t͡ɕɛˈlɛn.t͡sɨ"),
# https://en.wiktionary.org/wiki/chcę
        ("chcę","xt͡sɛ"),
# https://en.wiktionary.org/wiki/znam
        ("znam","znam"),
# https://en.wiktionary.org/wiki/wysłał
        ("wysłał","ˈvɨ.swaw"),
# https://en.wiktionary.org/wiki/dostałaś
        ("dostałaś","dɔˈsta.waɕ"),
# https://en.wiktionary.org/wiki/wyjątkowy
        ("wyjątkowy","vɨ.jɔnˈtkɔ.vɨ"),
# https://en.wiktionary.org/wiki/coś
        ("coś","t͡sɔɕ"),
# https://en.wiktionary.org/wiki/cyrk
        ("cyrk","t͡sɨrk"),
# https://en.wiktionary.org/wiki/mogą
        ("mogą","ˈmɔ.ɡɔ̃"),
# https://en.wiktionary.org/wiki/biednym
        ("biednym","ˈbʲɛd.nɨm"),
# https://en.wiktionary.org/wiki/czuję
        ("czuję","ˈt͡ʂu.jɛ"),
# https://en.wiktionary.org/wiki/muzykę
        ("muzykę","muˈzɨ.kɛ"),
# https://en.wiktionary.org/wiki/spróbuje
        ("spróbuje","spruˈbu.jɛ"),
# https://en.wiktionary.org/wiki/ulubione
        ("ulubione","u.luˈbʲɔ.nɛ"),
# https://en.wiktionary.org/wiki/tydzień
        ("tydzień","ˈtɨ.d͡ʑɛɲ"),
# https://en.wiktionary.org/wiki/miesiące
        ("miesiące","mʲɛˈɕɔn.t͡sɛ"),
# https://en.wiktionary.org/wiki/temat
        ("temat","ˈtɛ.mat"),
# https://en.wiktionary.org/wiki/świetne
        ("świetne","ˈɕfʲɛt.nɛ"),
# https://en.wiktionary.org/wiki/muszę
        ("muszę","ˈmu.ʂɛ"),
# https://en.wiktionary.org/wiki/już
        ("już","juʂ"),
# https://en.wiktionary.org/wiki/twoje
        ("twoje","ˈtfɔ.jɛ"),
# https://en.wiktionary.org/wiki/wychodzić
        ("wychodzić","vɨˈxɔ.d͡ʑit͡ɕ"),
# https://en.wiktionary.org/wiki/prawa
        ("prawa","ˈpra.va"),
# https://en.wiktionary.org/wiki/chwilę
        ("chwilę","ˈxfʲi.lɛ"),
# https://en.wiktionary.org/wiki/klientów
        ("klientów","klʲiˈjɛn.tuf"),
# https://en.wiktionary.org/wiki/piętro
        ("piętro","ˈpʲɛn.trɔ"),
# https://en.wiktionary.org/wiki/cudowny
        ("cudowny","t͡suˈdɔv.nɨ"),
# https://en.wiktionary.org/wiki/widziałeś
        ("widziałeś","vʲiˈd͡ʑa.wɛɕ"),
# https://en.wiktionary.org/wiki/odpowiedzieć
        ("odpowiedzieć","ɔt.pɔˈvʲɛ.d͡ʑɛt͡ɕ"),
# https://en.wiktionary.org/wiki/chciałem
        ("chciałem","ˈxt͡ɕa.wɛm"),
# https://en.wiktionary.org/wiki/należy
        ("należy","naˈlɛ.ʐɨ"),
# https://en.wiktionary.org/wiki/zresztą
        ("zresztą","ˈzrɛʂ.tɔ̃"),
# https://en.wiktionary.org/wiki/szkoły
        ("szkoły","ˈʂkɔ.wɨ"),
# https://en.wiktionary.org/wiki/dostałam
        ("dostałam","dɔˈsta.wam"),
# https://en.wiktionary.org/wiki/jedziemy
        ("jedziemy","jɛˈd͡ʑɛ.mɨ"),
# https://en.wiktionary.org/wiki/okropne
        ("okropne","ɔˈkrɔp.nɛ"),
# https://en.wiktionary.org/wiki/zamiast
        ("zamiast","ˈza.mʲast"),
# https://en.wiktionary.org/wiki/znajomego
        ("znajomego","zna.jɔˈmɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/znajdzie
        ("znajdzie","ˈznaj.d͡ʑɛ"),
# https://en.wiktionary.org/wiki/jeść
        ("jeść","jɛɕt͡ɕ"),
# https://en.wiktionary.org/wiki/musiał
        ("musiał","ˈmu.ɕaw"),
# https://en.wiktionary.org/wiki/boisz
        ("boisz","ˈbɔ.iʂ"),
# https://en.wiktionary.org/wiki/czeka
        ("czeka","ˈt͡ʂɛ.ka"),
# https://en.wiktionary.org/wiki/skończyć
        ("skończyć","ˈskɔɲ.t͡ʂɨt͡ɕ"),
# https://en.wiktionary.org/wiki/robimy
        ("robimy","rɔˈbʲi.mɨ"),
# https://en.wiktionary.org/wiki/gości
        ("gości","ˈɡɔɕ.t͡ɕi"),
# https://en.wiktionary.org/wiki/chłopcy
        ("chłopcy","ˈxwɔp.t͡sɨ"),
# https://en.wiktionary.org/wiki/kieliszek
        ("kieliszek","kʲɛˈlʲi.ʂɛk"),
# https://en.wiktionary.org/wiki/znalazł
        ("znalazł","ˈzna.lazw"),
# https://en.wiktionary.org/wiki/danie
        ("danie","ˈda.ɲɛ"),
# https://en.wiktionary.org/wiki/martwić
        ("martwić","ˈmar.tfʲit͡ɕ"),
# https://en.wiktionary.org/wiki/postój
        ("postój","ˈpɔ.stuj"),
# https://en.wiktionary.org/wiki/powodu
        ("powodu","pɔˈvɔ.du"),
# https://en.wiktionary.org/wiki/kółko
        ("kółko","ˈkuw.kɔ"),
# https://en.wiktionary.org/wiki/znalazłem
        ("znalazłem","znaˈla.zwɛm"),
# https://en.wiktionary.org/wiki/ludzi
        ("ludzi","ˈlu.d͡ʑi"),
# https://en.wiktionary.org/wiki/egzamin
        ("egzamin","ɛɡˈza.mʲin"),
# https://en.wiktionary.org/wiki/nowych
        ("nowych","ˈnɔ.vɨx"),
# https://en.wiktionary.org/wiki/nazywa
        ("nazywa","naˈzɨ.va"),
# https://en.wiktionary.org/wiki/wtorek
        ("wtorek","ˈftɔ.rɛk"),
# https://en.wiktionary.org/wiki/miejsca
        ("miejsca","ˈmʲɛj.st͡sa"),
# https://en.wiktionary.org/wiki/nazywam
        ("nazywam","naˈzɨ.vam"),
# https://en.wiktionary.org/wiki/dałeś
        ("dałeś","ˈda.wɛɕ"),
# https://en.wiktionary.org/wiki/moich
        ("moich","ˈmɔ.ix"),
# https://en.wiktionary.org/wiki/przykład
        ("przykład","ˈpʂɨ.kwat"),
# https://en.wiktionary.org/wiki/męża
        ("męża","ˈmɛŋ.ʐa"),
# https://en.wiktionary.org/wiki/niemieckiego
        ("niemieckiego","ɲɛ.mʲɛt͡sˈkʲɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/damy
        ("damy","ˈda.mɨ"),
# https://en.wiktionary.org/wiki/twoja
        ("twoja","ˈtfɔ.ja"),
# https://en.wiktionary.org/wiki/głośno
        ("głośno","ˈɡwɔɕ.nɔ"),
# https://en.wiktionary.org/wiki/bawi
        ("bawi","ˈba.vʲi"),
# https://en.wiktionary.org/wiki/czegoś
        ("czegoś","ˈt͡ʂɛ.ɡɔɕ"),
# https://en.wiktionary.org/wiki/nikt
        ("nikt","ɲikt"),
# https://en.wiktionary.org/wiki/jednej
#         ("jednej","ˈjednej"),
# https://en.wiktionary.org/wiki/lubisz
        ("lubisz","ˈlu.bʲiʂ"),
# https://en.wiktionary.org/wiki/samemu
        ("samemu","saˈmɛ.mu"),
# https://en.wiktionary.org/wiki/żaden
        ("żaden","ˈʐa.dɛn"),
# https://en.wiktionary.org/wiki/jeszcze
        ("jeszcze","ˈjɛʂ.t͡ʂɛ"),
# https://en.wiktionary.org/wiki/miesiąca
        ("miesiąca","mʲɛˈɕɔn.t͡sa"),
# https://en.wiktionary.org/wiki/naszymi
        ("naszymi","naˈʂɨ.mʲi"),
# https://en.wiktionary.org/wiki/tyle
        ("tyle","ˈtɨ.lɛ"),
# https://en.wiktionary.org/wiki/prezenty
        ("prezenty","prɛˈzɛn.tɨ"),
# https://en.wiktionary.org/wiki/czyj
        ("czyj","t͡ʂɨj"),
# https://en.wiktionary.org/wiki/doskonały
        ("doskonały","dɔ.skɔˈna.wɨ"),
# https://en.wiktionary.org/wiki/kwiaty
        ("kwiaty","ˈkfʲa.tɨ"),
# https://en.wiktionary.org/wiki/trzydzieści
        ("trzydzieści","tʂɨˈd͡ʑɛɕ.t͡ɕi"),
# https://en.wiktionary.org/wiki/sposób
        ("sposób","ˈspɔ.sup"),
# https://en.wiktionary.org/wiki/leżeć
        ("leżeć","ˈlɛ.ʐɛt͡ɕ"),
# https://en.wiktionary.org/wiki/dać
        ("dać","dat͡ɕ"),
# https://en.wiktionary.org/wiki/zmieni
        ("zmieni","ˈzmʲɛ.ɲi"),
# https://en.wiktionary.org/wiki/kilometrów
        ("kilometrów","kʲi.lɔˈmɛ.truf"),
# https://en.wiktionary.org/wiki/dokończyć
        ("dokończyć","dɔˈkɔɲ.t͡ʂɨt͡ɕ"),
# https://en.wiktionary.org/wiki/zaraz
        ("zaraz","ˈza.ras"),
# https://en.wiktionary.org/wiki/książek
        ("książek","ˈkɕɔŋ.ʐɛk"),
# https://en.wiktionary.org/wiki/dać
        ("dać","dat͡ɕ"),
# https://en.wiktionary.org/wiki/przyjmować
        ("przyjmować","pʂɨjˈmɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/dzwonisz
        ("dzwonisz","ˈd͡zvɔ.ɲiʂ"),
# https://en.wiktionary.org/wiki/pogoda
        ("pogoda","pɔˈɡɔ.da"),
# https://en.wiktionary.org/wiki/prawie
        ("prawie","ˈpra.vʲɛ"),
# https://en.wiktionary.org/wiki/cztery
        ("cztery","ˈt͡ʂtɛ.rɨ"),
# https://en.wiktionary.org/wiki/pracy
        ("pracy","ˈpra.t͡sɨ"),
# https://en.wiktionary.org/wiki/domu
        ("domu","ˈdɔ.mu"),
# https://en.wiktionary.org/wiki/dziury
        ("dziury","ˈd͡ʑu.rɨ"),
# https://en.wiktionary.org/wiki/opinia
#         ("opinia","ɔˈpʲiɲ.ja"),
# https://en.wiktionary.org/wiki/mnie
        ("mnie","mɲɛ"),
# https://en.wiktionary.org/wiki/żebyś
        ("żebyś","ˈʐɛ.bɨɕ"),
# https://en.wiktionary.org/wiki/niż
        ("niż","ɲiʂ"),
# https://en.wiktionary.org/wiki/wygląda
        ("wygląda","vɨɡˈlɔn.da"),
# https://en.wiktionary.org/wiki/miał
        ("miał","mʲaw"),
# https://en.wiktionary.org/wiki/czekać
        ("czekać","ˈt͡ʂɛ.kat͡ɕ"),
# https://en.wiktionary.org/wiki/głowie
        ("głowie","ˈɡwɔ.vʲɛ"),
# https://en.wiktionary.org/wiki/ciebie
        ("ciebie","ˈt͡ɕɛ.bʲɛ"),
# https://en.wiktionary.org/wiki/wszyscy
        ("wszyscy","ˈfʂɨs.t͡sɨ"),
# https://en.wiktionary.org/wiki/nowej
        ("nowej","ˈnɔ.vɛj"),
# https://en.wiktionary.org/wiki/dalekich
        ("dalekich","daˈlɛ.kʲix"),
# https://en.wiktionary.org/wiki/stać
        ("stać","stat͡ɕ"),
# https://en.wiktionary.org/wiki/wziąć
        ("wziąć","vʑɔɲt͡ɕ"),
# https://en.wiktionary.org/wiki/ochotę
        ("ochotę","ɔˈxɔ.tɛ"),
# https://en.wiktionary.org/wiki/płacę
        ("płacę","ˈpwa.t͡sɛ"),
# https://en.wiktionary.org/wiki/wsi
        ("wsi","fɕi"),
# https://en.wiktionary.org/wiki/chciałby
        ("chciałby","ˈxt͡ɕaw.bɨ"),
# https://en.wiktionary.org/wiki/spadł
        ("spadł","spadw"),
# https://en.wiktionary.org/wiki/krzycz
        ("krzycz","kʂɨt͡ʂ"),
# https://en.wiktionary.org/wiki/czas'(1)
        ("czas","t͡ʂas"),
# https://en.wiktionary.org/wiki/obudzić
        ("obudzić","ɔˈbu.d͡ʑit͡ɕ"),
# https://en.wiktionary.org/wiki/doceniasz
        ("doceniasz","dɔˈt͡sɛ.ɲaʂ"),
# https://en.wiktionary.org/wiki/takie
        ("takie","ˈta.kʲɛ"),
# https://en.wiktionary.org/wiki/czasem
        ("czasem","ˈt͡ʂa.sɛm"),
# https://en.wiktionary.org/wiki/straszny
        ("straszny","ˈstraʂ.nɨ"),
# https://en.wiktionary.org/wiki/przyjemnie
        ("przyjemnie","pʂɨˈjɛm.ɲɛ"),
# https://en.wiktionary.org/wiki/zamierzasz
        ("zamierzasz","zaˈmʲɛ.ʐaʂ"),
# https://en.wiktionary.org/wiki/dużą
        ("dużą","ˈdu.ʐɔ̃"),
# https://en.wiktionary.org/wiki/taką
        ("taką","ˈta.kɔ̃"),
# https://en.wiktionary.org/wiki/chcecie
        ("chcecie","ˈxt͡sɛ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/którzy
        ("którzy","ˈktu.ʐɨ"),
# https://en.wiktionary.org/wiki/wieczoru
        ("wieczoru","vʲɛˈt͡ʂɔ.ru"),
# https://en.wiktionary.org/wiki/wziąłem
        ("wziąłem","ˈvʑɔ̃.wɛm"),
# https://en.wiktionary.org/wiki/lekkiego
        ("lekkiego","lɛkˈkʲɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/spać
        ("spać","spat͡ɕ"),
# https://en.wiktionary.org/wiki/dużo
        ("dużo","ˈdu.ʐɔ"),
# https://en.wiktionary.org/wiki/polski
        ("polski","ˈpɔl.skʲi"),
# https://en.wiktionary.org/wiki/dostał
        ("dostał","ˈdɔ.staw"),
# https://en.wiktionary.org/wiki/wieczór
        ("wieczór","ˈvʲɛ.t͡ʂur"),
# https://en.wiktionary.org/wiki/szkole
        ("szkole","ˈʂkɔ.lɛ"),
# https://en.wiktionary.org/wiki/robiłaś
        ("robiłaś","rɔˈbʲi.waɕ"),
# https://en.wiktionary.org/wiki/szybciej
        ("szybciej","ˈʂɨp.t͡ɕɛj"),
# https://en.wiktionary.org/wiki/nagle
        ("nagle","ˈnaɡ.lɛ"),
# https://en.wiktionary.org/wiki/widać
        ("widać","ˈvʲi.dat͡ɕ"),
# https://en.wiktionary.org/wiki/wieczoru
        ("wieczoru","vʲɛˈt͡ʂɔ.ru"),
# https://en.wiktionary.org/wiki/kiedyś
        ("kiedyś","ˈkʲɛ.dɨɕ"),
# https://en.wiktionary.org/wiki/miasta
        ("miasta","ˈmʲa.sta"),
# https://en.wiktionary.org/wiki/kąpiel
        ("kąpiel","ˈkɔm.pʲɛl"),
# https://en.wiktionary.org/wiki/koleżanka
        ("koleżanka","kɔ.lɛˈʐan.ka"),
# https://en.wiktionary.org/wiki/Kowalska
        ("Kowalska","kɔˈval.ska"),
# https://en.wiktionary.org/wiki/bilety
        ("bilety","bʲiˈlɛ.tɨ"),
# https://en.wiktionary.org/wiki/śliczny
        ("śliczny","ˈɕlʲit͡ʂ.nɨ"),
# https://en.wiktionary.org/wiki/osobny
        ("osobny","ɔˈsɔb.nɨ"),
# https://en.wiktionary.org/wiki/mówić
        ("mówić","ˈmu.vʲit͡ɕ"),
# https://en.wiktionary.org/wiki/pomogły
        ("pomogły","pɔˈmɔ.ɡwɨ"),
# https://en.wiktionary.org/wiki/ciekawy
        ("ciekawy","t͡ɕɛˈka.vɨ"),
# https://en.wiktionary.org/wiki/siedzieć
        ("siedzieć","ˈɕɛ.d͡ʑɛt͡ɕ"),
# https://en.wiktionary.org/wiki/więc
        ("więc","vʲɛnt͡s"),
# https://en.wiktionary.org/wiki/myślę
        ("myślę","ˈmɨɕ.lɛ"),
# https://en.wiktionary.org/wiki/ciekawa
        ("ciekawa","t͡ɕɛˈka.va"),
# https://en.wiktionary.org/wiki/spory
        ("spory","ˈspɔ.rɨ"),
# https://en.wiktionary.org/wiki/typu
        ("typu","ˈtɨ.pu"),
# https://en.wiktionary.org/wiki/odkurzacz
        ("odkurzacz","ɔtˈku.ʐat͡ʂ"),
# https://en.wiktionary.org/wiki/działają
        ("działają","d͡ʑaˈwa.jɔ̃"),
# https://en.wiktionary.org/wiki/wszystkiego
        ("wszystkiego","fʂɨˈstkʲɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/dziesięć
        ("dziesięć","ˈd͡ʑɛ.ɕɛɲt͡ɕ"),
# https://en.wiktionary.org/wiki/siedział
        ("siedział","ˈɕɛ.d͡ʑaw"),
# https://en.wiktionary.org/wiki/żadnej
        ("żadnej","ˈʐad.nɛj"),
# https://en.wiktionary.org/wiki/pytania
        ("pytania","pɨˈta.ɲa"),
# https://en.wiktionary.org/wiki/papierosy
        ("papierosy","pa.pʲɛˈrɔ.sɨ"),
# https://en.wiktionary.org/wiki/kręcić
        ("kręcić","ˈkrɛɲ.t͡ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/trochę
        ("trochę","ˈtrɔ.xɛ"),
# https://en.wiktionary.org/wiki/robisz
        ("robisz","ˈrɔ.bʲiʂ"),
# https://en.wiktionary.org/wiki/rozmawiałeś
        ("rozmawiałeś","rɔz.maˈvʲa.wɛɕ"),
# https://en.wiktionary.org/wiki/kuzyn
        ("kuzyn","ˈku.zɨn"),
# https://en.wiktionary.org/wiki/każdy
        ("każdy","ˈkaʐ.dɨ"),
# https://en.wiktionary.org/wiki/programie
        ("programie","prɔˈɡra.mʲɛ"),
# https://en.wiktionary.org/wiki/lecieć
        ("lecieć","ˈlɛ.t͡ɕɛt͡ɕ"),
# https://en.wiktionary.org/wiki/najlepiej
        ("najlepiej","najˈlɛ.pʲɛj"),
# https://en.wiktionary.org/wiki/sprawie
        ("sprawie","ˈspra.vʲɛ"),
# https://en.wiktionary.org/wiki/byśmy
        ("byśmy","ˈbɨɕ.mɨ"),
# https://en.wiktionary.org/wiki/zaczynasz
        ("zaczynasz","zaˈt͡ʂɨ.naʂ"),
# https://en.wiktionary.org/wiki/Polski
        ("Polski","ˈpɔl.skʲi"),
# https://en.wiktionary.org/wiki/wsi
        ("wsi","fɕi"),
# https://en.wiktionary.org/wiki/jechać
        ("jechać","ˈjɛ.xat͡ɕ"),
# https://en.wiktionary.org/wiki/wieś
        ("wieś","ˈvʲɛɕ"),
# https://en.wiktionary.org/wiki/zapytać
        ("zapytać","zaˈpɨ.tat͡ɕ"),
# https://en.wiktionary.org/wiki/robią
        ("robią","ˈrɔ.bʲɔ̃"),
# https://en.wiktionary.org/wiki/zacząłem
        ("zacząłem","zaˈt͡ʂɔ̃.wɛm"),
# https://en.wiktionary.org/wiki/której
        ("której","ˈktu.rɛj"),
# https://en.wiktionary.org/wiki/ciemno
        ("ciemno","ˈt͡ɕɛm.nɔ"),
# https://en.wiktionary.org/wiki/troje
        ("troje","ˈtrɔ.jɛ"),
# https://en.wiktionary.org/wiki/państwo
        ("państwo","ˈpaɲ.stfɔ"),
# https://en.wiktionary.org/wiki/zjemy
        ("zjemy","ˈzjɛ.mɨ"),
# https://en.wiktionary.org/wiki/okazja
        ("okazja","ɔˈkaz.ja"),
# https://en.wiktionary.org/wiki/pozwolić
        ("pozwolić","pɔzˈvɔ.lʲit͡ɕ"),
# https://en.wiktionary.org/wiki/wreszcie
        ("wreszcie","ˈvrɛʂ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/wieczorem
        ("wieczorem","vʲɛˈt͡ʂɔ.rɛm"),
# https://en.wiktionary.org/wiki/wspaniała
        ("wspaniała","fspaˈɲa.wa"),
# https://en.wiktionary.org/wiki/widziałem
        ("widziałem","vʲiˈd͡ʑa.wɛm"),
# https://en.wiktionary.org/wiki/głodne
        ("głodne","ˈɡwɔd.nɛ"),
# https://en.wiktionary.org/wiki/prawdę
        ("prawdę","ˈprav.dɛ"),
# https://en.wiktionary.org/wiki/budzik
        ("budzik","ˈbu.d͡ʑik"),
# https://en.wiktionary.org/wiki/swojej
        ("swojej","ˈsfɔ.jɛj"),
# https://en.wiktionary.org/wiki/kłaść
        ("kłaść","kwaɕt͡ɕ"),
# https://en.wiktionary.org/wiki/zaczniemy
        ("zaczniemy","zat͡ʂˈɲɛ.mɨ"),
# https://en.wiktionary.org/wiki/mieć
        ("mieć","mʲɛt͡ɕ"),
# https://en.wiktionary.org/wiki/ciemnych
        ("ciemnych","ˈt͡ɕɛm.nɨx"),
# https://en.wiktionary.org/wiki/buty
        ("buty","ˈbu.tɨ"),
# https://en.wiktionary.org/wiki/kupić
        ("kupić","ˈku.pʲit͡ɕ"),
# https://en.wiktionary.org/wiki/opowiadać
        ("opowiadać","ɔ.pɔˈvʲa.dat͡ɕ"),
# https://en.wiktionary.org/wiki/będziemy
        ("będziemy","bɛɲˈd͡ʑɛ.mɨ"),
# https://en.wiktionary.org/wiki/jedzenie
        ("jedzenie","jɛˈd͡zɛ.ɲɛ"),
# https://en.wiktionary.org/wiki/łóżku
        ("łóżku","ˈwuʂ.ku"),
# https://en.wiktionary.org/wiki/chodzić
        ("chodzić","ˈxɔ.d͡ʑit͡ɕ"),
# https://en.wiktionary.org/wiki/ścianie
        ("ścianie","ˈɕt͡ɕa.ɲɛ"),
# https://en.wiktionary.org/wiki/jesteśmy
        ("jesteśmy","jɛˈstɛɕ.mɨ"),
# https://en.wiktionary.org/wiki/szczęśliwa
        ("szczęśliwa","ʂt͡ʂɛɲˈɕlʲi.va"),
# https://en.wiktionary.org/wiki/znowu
        ("znowu","ˈznɔ.vu"),
# https://en.wiktionary.org/wiki/nigdy
        ("nigdy","ˈɲiɡ.dɨ"),
# https://en.wiktionary.org/wiki/panie
        ("panie","ˈpa.ɲɛ"),
# https://en.wiktionary.org/wiki/lubił
        ("lubił","ˈlu.bʲiw"),
# https://en.wiktionary.org/wiki/nikomu
        ("nikomu","ɲiˈkɔ.mu"),
# https://en.wiktionary.org/wiki/takiej
        ("takiej","ˈta.kʲɛj"),
# https://en.wiktionary.org/wiki/dlaczego
        ("dlaczego","dlaˈt͡ʂɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/górnej
        ("górnej","ˈɡur.nɛj"),
# https://en.wiktionary.org/wiki/żółwie
        ("żółwie","ˈʐuw.vʲɛ"),
# https://en.wiktionary.org/wiki/kawa
        ("kawa","ˈka.va"),
# https://en.wiktionary.org/wiki/tę
        ("tę","tɛ"),
# https://en.wiktionary.org/wiki/wolny
        ("wolny","ˈvɔl.nɨ"),
# https://en.wiktionary.org/wiki/niedługo
        ("niedługo","ɲɛˈdwu.ɡɔ"),
# https://en.wiktionary.org/wiki/możesz
        ("możesz","ˈmɔ.ʐɛʂ"),
# https://en.wiktionary.org/wiki/spać
        ("spać","spat͡ɕ"),
# https://en.wiktionary.org/wiki/szkoły
        ("szkoły","ˈʂkɔ.wɨ"),
# https://en.wiktionary.org/wiki/wynająć
        ("wynająć","vɨˈna.jɔɲt͡ɕ"),
# https://en.wiktionary.org/wiki/własne
        ("własne","ˈvwas.nɛ"),
# https://en.wiktionary.org/wiki/Polsce
        ("Polsce","ˈpɔl.st͡sɛ"),
# https://en.wiktionary.org/wiki/godzina
        ("godzina","ɡɔˈd͡ʑi.na"),
# https://en.wiktionary.org/wiki/których
        ("których","ˈktu.rɨx"),
# https://en.wiktionary.org/wiki/prosić
        ("prosić","ˈprɔ.ɕit͡ɕ"),
# https://en.wiktionary.org/wiki/porządny
        ("porządny","pɔˈʐɔn.dnɨ"),
# https://en.wiktionary.org/wiki/rogu
        ("rogu","ˈrɔ.ɡu"),
# https://en.wiktionary.org/wiki/każdej
        ("każdej","ˈkaʐ.dɛj"),
# https://en.wiktionary.org/wiki/przyszłość
        ("przyszłość","ˈpʂɨ.ʂwɔɕt͡ɕ"),
# https://en.wiktionary.org/wiki/rozmów
        ("rozmów","ˈrɔz.muf"),
# https://en.wiktionary.org/wiki/widzieliśmy
        ("widzieliśmy","vʲi.d͡ʑɛˈlʲiɕ.mɨ"),
# https://en.wiktionary.org/wiki/proszę
        ("proszę","ˈprɔ.ʂɛ"),
# https://en.wiktionary.org/wiki/zrobi
        ("zrobi","ˈzrɔ.bʲi"),
# https://en.wiktionary.org/wiki/były
        ("były","ˈbɨ.wɨ"),
# https://en.wiktionary.org/wiki/Nowak
        ("Nowak","ˈnɔ.vak"),
# https://en.wiktionary.org/wiki/został
        ("został","ˈzɔ.staw"),
# https://en.wiktionary.org/wiki/widać
        ("widać","ˈvʲi.dat͡ɕ"),
# https://en.wiktionary.org/wiki/Tomek
        ("Tomek","ˈtɔ.mɛk"),
# https://en.wiktionary.org/wiki/każda
        ("każda","ˈkaʐ.da"),
# https://en.wiktionary.org/wiki/bolą
        ("bolą","ˈbɔ.lɔ̃"),
# https://en.wiktionary.org/wiki/pięknego
        ("pięknego","pʲɛŋˈknɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/długo
        ("długo","ˈdwu.ɡɔ"),
# https://en.wiktionary.org/wiki/czym
        ("czym","t͡ʂɨm"),
# https://en.wiktionary.org/wiki/włosów
        ("włosów","ˈvwɔ.suf"),
# https://en.wiktionary.org/wiki/chciałabym
        ("chciałabym","ˈxt͡ɕa.wa.bɨm"),
# https://en.wiktionary.org/wiki/lepsze
        ("lepsze","ˈlɛp.ʂɛ"),
# https://en.wiktionary.org/wiki/budzić
        ("budzić","ˈbu.d͡ʑit͡ɕ"),
# https://en.wiktionary.org/wiki/zabierać
        ("zabierać","zaˈbʲɛ.rat͡ɕ"),
# https://en.wiktionary.org/wiki/babcia
        ("babcia","ˈbap.t͡ɕa"),
# https://en.wiktionary.org/wiki/ktoś
        ("ktoś","ktɔɕ"),
# https://en.wiktionary.org/wiki/mojej
        ("mojej","ˈmɔ.jɛj"),
# https://en.wiktionary.org/wiki/stało
        ("stało","ˈsta.wɔ"),
# https://en.wiktionary.org/wiki/domu
        ("domu","ˈdɔ.mu"),
# https://en.wiktionary.org/wiki/gdzieś
        ("gdzieś","ɡd͡ʑɛɕ"),
# https://en.wiktionary.org/wiki/byłem
        ("byłem","ˈbɨ.wɛm"),
# https://en.wiktionary.org/wiki/wczoraj
        ("wczoraj","ˈft͡ʂɔ.raj"),
# https://en.wiktionary.org/wiki/wielu
        ("wielu","ˈvʲɛ.lu"),
# https://en.wiktionary.org/wiki/trudny
        ("trudny","ˈtrud.nɨ"),
# https://en.wiktionary.org/wiki/trochę
        ("trochę","ˈtrɔ.xɛ"),
# https://en.wiktionary.org/wiki/wyłącznie
        ("wyłącznie","vɨˈwɔn.t͡ʂɲɛ"),
# https://en.wiktionary.org/wiki/ktoś
        ("ktoś","ktɔɕ"),
# https://en.wiktionary.org/wiki/odebrać
        ("odebrać","ɔˈdɛ.brat͡ɕ"),
# https://en.wiktionary.org/wiki/gdybym
        ("gdybym","ˈɡdɨ.bɨm"),
# https://en.wiktionary.org/wiki/ostatni
        ("ostatni","ɔˈstat.ɲi"),
# https://en.wiktionary.org/wiki/urlop
        ("urlop","ˈur.lɔp"),
# https://en.wiktionary.org/wiki/swojego
        ("swojego","sfɔˈjɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/okropnym
        ("okropnym","ɔˈkrɔp.nɨm"),
# https://en.wiktionary.org/wiki/ostatnie
        ("ostatnie","ɔˈstat.ɲɛ"),
# https://en.wiktionary.org/wiki/trudne
        ("trudne","ˈtrud.nɛ"),
# https://en.wiktionary.org/wiki/szarej
        ("szarej","ˈʂa.rɛj"),
# https://en.wiktionary.org/wiki/córka
        ("córka","ˈt͡sur.ka"),
# https://en.wiktionary.org/wiki/zadanie
        ("zadanie","zaˈda.ɲɛ"),
# https://en.wiktionary.org/wiki/połóż
        ("połóż","ˈpɔ.wuʂ"),
# https://en.wiktionary.org/wiki/myśli
        ("myśli","ˈmɨɕ.lʲi"),
# https://en.wiktionary.org/wiki/bym
        ("bym","bɨm"),
# https://en.wiktionary.org/wiki/mogłyby
        ("mogłyby","ˈmɔ.ɡwɨ.bɨ"),
# https://en.wiktionary.org/wiki/grasz
        ("grasz","ɡraʂ"),
# https://en.wiktionary.org/wiki/lekcje
        ("lekcje","ˈlɛk.t͡sjɛ"),
# https://en.wiktionary.org/wiki/miałeś
        ("miałeś","ˈmʲa.wɛɕ"),
# https://en.wiktionary.org/wiki/kłopot
        ("kłopot","ˈkwɔ.pɔt"),
# https://en.wiktionary.org/wiki/wyszła
        ("wyszła","ˈvɨ.ʂwa"),
# https://en.wiktionary.org/wiki/dawna
        ("dawna","ˈdav.na"),
# https://en.wiktionary.org/wiki/mogę
        ("mogę","ˈmɔ.ɡɛ"),
# https://en.wiktionary.org/wiki/karmienie
        ("karmienie","karˈmʲɛ.ɲɛ"),
# https://en.wiktionary.org/wiki/dotykać
        ("dotykać","dɔˈtɨ.kat͡ɕ"),
# https://en.wiktionary.org/wiki/wyjście
        ("wyjście","ˈvɨj.ɕt͡ɕɛ"),
# https://en.wiktionary.org/wiki/stać
        ("stać","stat͡ɕ"),
# https://en.wiktionary.org/wiki/zobaczyć
        ("zobaczyć","zɔˈba.t͡ʂɨt͡ɕ"),
# https://en.wiktionary.org/wiki/będzie
        ("będzie","ˈbɛɲ.d͡ʑɛ"),
# https://en.wiktionary.org/wiki/takiego
        ("takiego","taˈkʲɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/też
        ("też","tɛʂ"),
# https://en.wiktionary.org/wiki/samolot
        ("samolot","saˈmɔ.lɔt"),
# https://en.wiktionary.org/wiki/pokazać
        ("pokazać","pɔˈka.zat͡ɕ"),
# https://en.wiktionary.org/wiki/chleb
        ("chleb","xlɛp"),
# https://en.wiktionary.org/wiki/wychodzi
        ("wychodzi","vɨˈxɔ.d͡ʑi"),
# https://en.wiktionary.org/wiki/znacznie
        ("znacznie","ˈznat͡ʂ.ɲɛ"),
# https://en.wiktionary.org/wiki/ładna
        ("ładna","ˈwad.na"),
# https://en.wiktionary.org/wiki/sweter
        ("sweter","ˈsfɛ.tɛr"),
# https://en.wiktionary.org/wiki/zaczekać
        ("zaczekać","zaˈt͡ʂɛ.kat͡ɕ"),
# https://en.wiktionary.org/wiki/tygodnia
        ("tygodnia","tɨˈɡɔ.dɲa"),
# https://en.wiktionary.org/wiki/myśli
        ("myśli","ˈmɨɕ.lʲi"),
# https://en.wiktionary.org/wiki/wyjechał
        ("wyjechał","vɨˈjɛ.xaw"),
# https://en.wiktionary.org/wiki/długo
        ("długo","ˈdwu.ɡɔ"),
# https://en.wiktionary.org/wiki/urlop
        ("urlop","ˈur.lɔp"),
# https://en.wiktionary.org/wiki/okropna
        ("okropna","ɔˈkrɔp.na"),
# https://en.wiktionary.org/wiki/czworo
        ("czworo","ˈt͡ʂfɔ.rɔ"),
# https://en.wiktionary.org/wiki/rzecz
        ("rzecz","ʐɛt͡ʂ"),
# https://en.wiktionary.org/wiki/całą
        ("całą","ˈt͡sa.wɔ̃"),
# https://en.wiktionary.org/wiki/wymagają
        ("wymagają","vɨ.maˈɡa.jɔ̃"),
# https://en.wiktionary.org/wiki/kosmos
        ("kosmos","ˈkɔs.mɔs"),
# https://en.wiktionary.org/wiki/umieć
        ("umieć","ˈu.mʲɛt͡ɕ"),
# https://en.wiktionary.org/wiki/doskonałym
        ("doskonałym","dɔ.skɔˈna.wɨm"),
# https://en.wiktionary.org/wiki/które
        ("które","ˈktu.rɛ"),
# https://en.wiktionary.org/wiki/szkielet
        ("szkielet","ˈʂkʲɛ.lɛt"),
# https://en.wiktionary.org/wiki/swoja
        ("swoja","ˈsfɔ.ja"),
# https://en.wiktionary.org/wiki/krzesła
        ("krzesła","ˈkʂɛ.swa"),
# https://en.wiktionary.org/wiki/poczekać
        ("poczekać","pɔˈt͡ʂɛ.kat͡ɕ"),
# https://en.wiktionary.org/wiki/połowę
        ("połowę","pɔˈwɔ.vɛ"),
# https://en.wiktionary.org/wiki/kupować
        ("kupować","kuˈpɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/twojej
        ("twojej","ˈtfɔ.jɛj"),
# https://en.wiktionary.org/wiki/bolec
        ("bolec","ˈbɔ.lɛt͡s"),
# https://en.wiktionary.org/wiki/jakim
        ("jakim","ˈja.kʲim"),
# https://en.wiktionary.org/wiki/kartę
        ("kartę","ˈkar.tɛ"),
# https://en.wiktionary.org/wiki/będziesz
        ("będziesz","ˈbɛɲ.d͡ʑɛʂ"),
# https://en.wiktionary.org/wiki/rozumiem
        ("rozumiem","rɔˈzu.mʲɛm"),
# https://en.wiktionary.org/wiki/masz
        ("masz","maʂ"),
# https://en.wiktionary.org/wiki/pamięć
        ("pamięć","ˈpa.mʲɛɲt͡ɕ"),
# https://en.wiktionary.org/wiki/roku
        ("roku","ˈrɔ.ku"),
# https://en.wiktionary.org/wiki/rzeczy
        ("rzeczy","ˈʐɛ.t͡ʂɨ"),
# https://en.wiktionary.org/wiki/naprawdę
        ("naprawdę","naˈprav.dɛ"),
# https://en.wiktionary.org/wiki/zostawił
        ("zostawił","zɔˈsta.vʲiw"),
# https://en.wiktionary.org/wiki/mają
        ("mają","ˈma.jɔ̃"),
# https://en.wiktionary.org/wiki/tobie
        ("tobie","ˈtɔ.bʲɛ"),
# https://en.wiktionary.org/wiki/Dzień
        ("Dzień","d͡ʑɛɲ"),
# https://en.wiktionary.org/wiki/zrozumieć
        ("zrozumieć","zrɔˈzu.mʲɛt͡ɕ"),
# https://en.wiktionary.org/wiki/wakacje
        ("wakacje","vaˈkat͡s.jɛ"),
# https://en.wiktionary.org/wiki/robiłem
        ("robiłem","rɔˈbʲi.wɛm"),
# https://en.wiktionary.org/wiki/kręci
        ("kręci","ˈkrɛɲ.t͡ɕi"),
# https://en.wiktionary.org/wiki/dzieci
        ("dzieci","ˈd͡ʑɛ.t͡ɕi"),
# https://en.wiktionary.org/wiki/dopiero
        ("dopiero","dɔˈpʲɛ.rɔ"),
# https://en.wiktionary.org/wiki/będą
        ("będą","ˈbɛn.dɔ̃"),
# https://en.wiktionary.org/wiki/ładnie
        ("ładnie","ˈwa.dɲɛ"),
# https://en.wiktionary.org/wiki/położyć
        ("położyć","pɔˈwɔ.ʐɨt͡ɕ"),
# https://en.wiktionary.org/wiki/zauważyłem
        ("zauważyłem","za.u.vaˈʐɨ.wɛm"),
# https://en.wiktionary.org/wiki/walizka
        ("walizka","vaˈlʲi.ska"),
# https://en.wiktionary.org/wiki/portfel
        ("portfel","ˈpɔr.tfɛl"),
# https://en.wiktionary.org/wiki/złośliwy
        ("złośliwy","zwɔɕˈlʲi.vɨ"),
# https://en.wiktionary.org/wiki/pokój
        ("pokój","ˈpɔ.kuj"),
# https://en.wiktionary.org/wiki/innym
        ("innym","ˈin.nɨm"),
# https://en.wiktionary.org/wiki/właśnie
        ("właśnie","ˈvwaɕ.ɲɛ"),
# https://en.wiktionary.org/wiki/twoich
        ("twoich","ˈtfɔ.ix"),
# https://en.wiktionary.org/wiki/twojego
        ("twojego","tfɔˈjɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/mogłam
        ("mogłam","ˈmɔ.ɡwam"),
# https://en.wiktionary.org/wiki/kariera
        ("kariera","karʲˈjɛ.ra"),
# https://en.wiktionary.org/wiki/proszek
        ("proszek","ˈprɔ.ʂɛk"),
# https://en.wiktionary.org/wiki/coraz
        ("coraz","ˈt͡sɔ.ras"),
# https://en.wiktionary.org/wiki/ćwiczenie
        ("ćwiczenie","t͡ɕfʲiˈt͡ʂɛ.ɲɛ"),
# https://en.wiktionary.org/wiki/babci
        ("babci","ˈbap.t͡ɕi"),
# https://en.wiktionary.org/wiki/podać
        ("podać","ˈpɔ.dat͡ɕ"),
# https://en.wiktionary.org/wiki/twoim
        ("twoim","ˈtfɔ.im"),
# https://en.wiktionary.org/wiki/plany
        ("plany","ˈpla.nɨ"),
# https://en.wiktionary.org/wiki/wychodzisz
        ("wychodzisz","vɨˈxɔ.d͡ʑiʂ"),
# https://en.wiktionary.org/wiki/morze
        ("morze","ˈmɔ.ʐɛ"),
# https://en.wiktionary.org/wiki/parę
        ("parę","ˈpa.rɛ"),
# https://en.wiktionary.org/wiki/widzi
        ("widzi","ˈvʲi.d͡ʑi"),
# https://en.wiktionary.org/wiki/przyszedł
        ("przyszedł","ˈpʂɨ.ʂɛdw"),
# https://en.wiktionary.org/wiki/potrzebuję
        ("potrzebuję","pɔt.ʂɛˈbu.jɛ"),
# https://en.wiktionary.org/wiki/ciemnej
        ("ciemnej","ˈt͡ɕɛm.nɛj"),
# https://en.wiktionary.org/wiki/najbardziej
        ("najbardziej","najˈbar.d͡ʑɛj"),
# https://en.wiktionary.org/wiki/słuchać
        ("słuchać","ˈswu.xat͡ɕ"),
# https://en.wiktionary.org/wiki/chciał
        ("chciał","xt͡ɕaw"),
# https://en.wiktionary.org/wiki/nazywa
        ("nazywa","naˈzɨ.va"),
# https://en.wiktionary.org/wiki/wracam
        ("wracam","ˈvra.t͡sam"),
# https://en.wiktionary.org/wiki/weźmie
        ("weźmie","ˈvɛʑ.mʲɛ"),
# https://en.wiktionary.org/wiki/wygrać
        ("wygrać","ˈvɨ.ɡrat͡ɕ"),
# https://en.wiktionary.org/wiki/zawsze
        ("zawsze","ˈzaf.ʂɛ"),
# https://en.wiktionary.org/wiki/pożyczyć
        ("pożyczyć","pɔˈʐɨ.t͡ʂɨt͡ɕ"),
# https://en.wiktionary.org/wiki/zjesz
        ("zjesz","zjɛʂ"),
# https://en.wiktionary.org/wiki/jeżeli
        ("jeżeli","jɛˈʐɛ.lʲi"),
# https://en.wiktionary.org/wiki/oglądam
        ("oglądam","ɔɡˈlɔn.dam"),
# https://en.wiktionary.org/wiki/ogromny
        ("ogromny","ɔˈɡrɔm.nɨ"),
# https://en.wiktionary.org/wiki/klientów
        ("klientów","klʲiˈjɛn.tuf"),
# https://en.wiktionary.org/wiki/wolne
        ("wolne","ˈvɔl.nɛ"),
# https://en.wiktionary.org/wiki/pływać
        ("pływać","ˈpwɨ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/Ania
        ("Ania","ˈa.ɲa"),
# https://en.wiktionary.org/wiki/waszego
        ("waszego","vaˈʂɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/uczy
        ("uczy","ˈu.t͡ʂɨ"),
# https://en.wiktionary.org/wiki/biuro
        ("biuro","ˈbʲu.rɔ"),
# https://en.wiktionary.org/wiki/mną
        ("mną","mnɔ̃"),
# https://en.wiktionary.org/wiki/potrzebujesz
        ("potrzebujesz","pɔt.ʂɛˈbu.jɛʂ"),
# https://en.wiktionary.org/wiki/ranić
        ("ranić","ˈra.ɲit͡ɕ"),
# https://en.wiktionary.org/wiki/człowieka
        ("człowieka","t͡ʂwɔˈvʲɛ.ka"),
# https://en.wiktionary.org/wiki/chora
        ("chora","ˈxɔ.ra"),
# https://en.wiktionary.org/wiki/zrobiłaś
        ("zrobiłaś","zrɔˈbʲi.waɕ"),
# https://en.wiktionary.org/wiki/maszyny
        ("maszyny","maˈʂɨ.nɨ"),
# https://en.wiktionary.org/wiki/zapomniałam
        ("zapomniałam","za.pɔmˈɲa.wam"),
# https://en.wiktionary.org/wiki/samochód
        ("samochód","saˈmɔ.xut"),
# https://en.wiktionary.org/wiki/pamiętam
        ("pamiętam","paˈmʲɛn.tam"),
# https://en.wiktionary.org/wiki/dałem
        ("dałem","ˈda.wɛm"),
# https://en.wiktionary.org/wiki/przyjść
        ("przyjść","pʂɨjɕt͡ɕ"),
# https://en.wiktionary.org/wiki/Jaki
        ("Jaki","ˈja.kʲi"),
# https://en.wiktionary.org/wiki/lekarza...
        ("lekarza","lɛˈka.ʐa"),
# https://en.wiktionary.org/wiki/wioski
        ("wioski","ˈvʲɔs.kʲi"),
# https://en.wiktionary.org/wiki/tobą
        ("tobą","ˈtɔ.bɔ̃"),
# https://en.wiktionary.org/wiki/miało
        ("miało","ˈmʲa.wɔ"),
# https://en.wiktionary.org/wiki/hotelu
        ("hotelu","xɔˈtɛ.lu"),
# https://en.wiktionary.org/wiki/techniczny
        ("techniczny","tɛxˈɲit͡ʂ.nɨ"),
# https://en.wiktionary.org/wiki/chcą
        ("chcą","xt͡sɔ̃"),
# https://en.wiktionary.org/wiki/samochód
        ("samochód","saˈmɔ.xut"),
# https://en.wiktionary.org/wiki/prosił
        ("prosił","ˈprɔ.ɕiw"),
# https://en.wiktionary.org/wiki/prawo
        ("prawo","ˈpra.vɔ"),
# https://en.wiktionary.org/wiki/piłkę
        ("piłkę","ˈpʲiw.kɛ"),
# https://en.wiktionary.org/wiki/jeśli
        ("jeśli","ˈjɛɕ.lʲi"),
# https://en.wiktionary.org/wiki/nowi
        ("nowi","ˈnɔ.vʲi"),
# https://en.wiktionary.org/wiki/żółwie
        ("żółwie","ˈʐuw.vʲɛ"),
# https://en.wiktionary.org/wiki/ją
        ("ją","jɔ̃"),
# https://en.wiktionary.org/wiki/pilnować
        ("pilnować","pʲilˈnɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/ostatnich
        ("ostatnich","ɔˈstat.ɲix"),
# https://en.wiktionary.org/wiki/niedzielę
        ("niedzielę","ɲɛˈd͡ʑɛ.lɛ"),
# https://en.wiktionary.org/wiki/kupię
        ("kupię","ˈku.pʲɛ"),
# https://en.wiktionary.org/wiki/nieszczęśliwie
        ("nieszczęśliwie","ɲɛʂ.t͡ʂɛɲˈɕlʲi.vʲɛ"),
# https://en.wiktionary.org/wiki/kłopoty
        ("kłopoty","kwɔˈpɔ.tɨ"),
# https://en.wiktionary.org/wiki/zraz
        ("zraz","zras"),
# https://en.wiktionary.org/wiki/nauczyłem
        ("nauczyłem","na.uˈt͡ʂɨ.wɛm"),
# https://en.wiktionary.org/wiki/kolejka
        ("kolejka","kɔˈlɛj.ka"),
# https://en.wiktionary.org/wiki/lubią
        ("lubią","ˈlu.bʲɔ̃"),
# https://en.wiktionary.org/wiki/myślisz
        ("myślisz","ˈmɨɕ.lʲiʂ"),
# https://en.wiktionary.org/wiki/rodzina
        ("rodzina","rɔˈd͡ʑi.na"),
# https://en.wiktionary.org/wiki/późno
        ("późno","ˈpuʑ.nɔ"),
# https://en.wiktionary.org/wiki/zabrać
        ("zabrać","ˈza.brat͡ɕ"),
# https://en.wiktionary.org/wiki/waza
        ("waza","ˈva.za"),
# https://en.wiktionary.org/wiki/później
        ("później","ˈpuʑ.ɲɛj"),
# https://en.wiktionary.org/wiki/ciepła
        ("ciepła","ˈt͡ɕɛ.pwa"),
# https://en.wiktionary.org/wiki/robili
        ("robili","rɔˈbʲi.lʲi"),
# https://en.wiktionary.org/wiki/Potrzeba
        ("Potrzeba","pɔtˈʂɛ.ba"),
# https://en.wiktionary.org/wiki/możecie
        ("możecie","mɔˈʐɛ.t͡ɕɛ"),
# https://en.wiktionary.org/wiki/tygodnie
        ("tygodnie","tɨˈɡɔ.dɲɛ"),
# https://en.wiktionary.org/wiki/miesiąc
        ("miesiąc","ˈmʲɛ.ɕɔnt͡s"),
# https://en.wiktionary.org/wiki/najwięcej
        ("najwięcej","najˈvʲɛn.t͡sɛj"),
# https://en.wiktionary.org/wiki/zakupy
        ("zakupy","zaˈku.pɨ"),
# https://en.wiktionary.org/wiki/jesteś
        ("jesteś","ˈjɛ.stɛɕ"),
# https://en.wiktionary.org/wiki/wygodny
        ("wygodny","vɨˈɡɔd.nɨ"),
# https://en.wiktionary.org/wiki/gramy
        ("gramy","ˈɡra.mɨ"),
# https://en.wiktionary.org/wiki/duże
        ("duże","ˈdu.ʐɛ"),
# https://en.wiktionary.org/wiki/pojedziemy
        ("pojedziemy","pɔ.jɛˈd͡ʑɛ.mɨ"),
# https://en.wiktionary.org/wiki/mężczyźni
        ("mężczyźni","mɛŋˈʂt͡ʂɨʑ.ɲi"),
# https://en.wiktionary.org/wiki/głowę
        ("głowę","ˈɡwɔ.vɛ"),
# https://en.wiktionary.org/wiki/chcesz
        ("chcesz","xt͡sɛʂ"),
# https://en.wiktionary.org/wiki/kłócą
        ("kłócą","ˈkwu.t͡sɔ̃"),
# https://en.wiktionary.org/wiki/niektóre
        ("niektóre","ɲɛkˈtu.rɛ"),
# https://en.wiktionary.org/wiki/jeździć
        ("jeździć","ˈjɛʑ.d͡ʑit͡ɕ"),
# https://en.wiktionary.org/wiki/rozmawiać
        ("rozmawiać","rɔzˈma.vʲat͡ɕ"),
# https://en.wiktionary.org/wiki/szczególnie
        ("szczególnie","ʂt͡ʂɛˈɡul.ɲɛ"),
# https://en.wiktionary.org/wiki/pięć
        ("pięć","pʲɛɲt͡ɕ"),
# https://en.wiktionary.org/wiki/zaczyna
        ("zaczyna","zaˈt͡ʂɨ.na"),
# https://en.wiktionary.org/wiki/robiłeś
        ("robiłeś","rɔˈbʲi.wɛɕ"),
# https://en.wiktionary.org/wiki/podnieść
        ("podnieść","ˈpɔ.dɲɛɕt͡ɕ"),
# https://en.wiktionary.org/wiki/tylko
        ("tylko","ˈtɨl.kɔ"),
# https://en.wiktionary.org/wiki/biorą
        ("biorą","ˈbʲɔ.rɔ̃"),
# https://en.wiktionary.org/wiki/martw
        ("martw","martf"),
# https://en.wiktionary.org/wiki/osiemdziesiąt
        ("osiemdziesiąt","ɔ.ɕɛmˈd͡ʑɛ.ɕɔnt"),
# https://en.wiktionary.org/wiki/dzieckiem
        ("dzieckiem","ˈd͡ʑɛt͡s.kʲɛm"),
# https://en.wiktionary.org/wiki/świetna
        ("świetna","ˈɕfʲɛt.na"),
# https://en.wiktionary.org/wiki/usiądź
        ("usiądź","ˈu.ɕɔɲt͡ɕ"),
# https://en.wiktionary.org/wiki/początku
        ("początku","pɔˈt͡ʂɔn.tku"),
# https://en.wiktionary.org/wiki/przez
        ("przez","pʂɛs"),
# https://en.wiktionary.org/wiki/wolisz
        ("wolisz","ˈvɔ.lʲiʂ"),
# https://en.wiktionary.org/wiki/komuś
        ("komuś","ˈkɔ.muɕ"),
# https://en.wiktionary.org/wiki/wrażliwy
        ("wrażliwy","vraʐˈlʲi.vɨ"),
# https://en.wiktionary.org/wiki/wolnych
        ("wolnych","ˈvɔl.nɨx"),
# https://en.wiktionary.org/wiki/spodnie
        ("spodnie","ˈspɔ.dɲɛ"),
# https://en.wiktionary.org/wiki/kosztować
        ("kosztować","kɔʂˈtɔ.vat͡ɕ"),
# https://en.wiktionary.org/wiki/mieszkanie
        ("mieszkanie","mʲɛʂˈka.ɲɛ"),
# https://en.wiktionary.org/wiki/chcesz
        ("chcesz","xt͡sɛʂ"),
# https://en.wiktionary.org/wiki/kimś
        ("kimś","kʲimɕ"),
# https://en.wiktionary.org/wiki/normalny
        ("normalny","nɔrˈmal.nɨ"),
# https://en.wiktionary.org/wiki/pacjent
        ("pacjent","ˈpat͡s.jɛnt"),
# https://en.wiktionary.org/wiki/wyglądasz
        ("wyglądasz","vɨɡˈlɔn.daʂ"),
# https://en.wiktionary.org/wiki/jakiego
        ("jakiego","jaˈkʲɛ.ɡɔ"),
# https://en.wiktionary.org/wiki/imieniem
        ("imieniem","iˈmʲɛ.ɲɛm"),
# https://en.wiktionary.org/wiki/przejdzie
        ("przejdzie","ˈpʂɛj.d͡ʑɛ"),
# https://en.wiktionary.org/wiki/samochodem
        ("samochodem","sa.mɔˈxɔ.dɛm"),
# https://en.wiktionary.org/wiki/słońca
        ("słońca","ˈswɔɲ.t͡sa"),
# https://en.wiktionary.org/wiki/wtorek
        ("wtorek","ˈftɔ.rɛk"),
)
    return tests
