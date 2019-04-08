#!/usr/bin/python3
import re
# import regex as re
import unicodedata
import json
xx="main"
do_debug=False
def debug(*args, sep=' ', end='\n'):
    if do_debug:
        print("DEBUG ",end='')
        print(*args, sep=sep, end=end)
    else:
        pass
def get_rules_text():
    # madon@hp:~/epitran/epitran/data/pre$ cat pol-Latn.txt 
    rules_text="""
% Symbols
::nasal_vowel:: = ą|ę
::vowel:: = a|ą|e|ę|i|o|ó|u|y
::vow_not_i:: = a|ą|e|ę|o|ó|u|y
::consonant:: = b|c|ć|cz|d|dź|dż|f|g|h|ch|j|k|l|ł|m|n|ń|p|r|s|ś|sz|t|w|z|ź|ż|rz
% exceptions
marzn -> mar2zn / # _
ą -> ɔm / _ b|p
ą -> ɔɲ / _ ć|dź|dzi|ci|dź
ą -> ɔn / _ d|t|c|dz
ą -> ɔŋ / _ g|k|ż
ąź -> ɔɲɕ / _
ę -> ɛm / _ b|p
ę -> ɛɲ / _ ć|dź|dzi|ci|dź
ę -> ɛn / _ d|t|c|dz
ę -> ɛŋ / _ g|k
% Palatalized consonants
ci -> t͡ɕ / _ (::vow_not_i::|ɛ|ɔ)
dzi -> d͡ʑ / _ (::vow_not_i::|ɛ|ɔ)
si -> ɕ / _ (::vow_not_i::|ɛ|ɔ)
zi -> ʑ / _ (::vow_not_i::|ɛ|ɔ)
ni -> ɲ / _ (::vow_not_i::|ɛ|ɔ)
ki -> kʲ / _ e
gi -> ɡʲ / _ e
% alex: more ʲ
świ -> ɕfʲ / _ (ę|ɛ)
kwi -> kfʲ / _ (ę|ɛ|e)
szw -> ʂf / _ (e|ɛ)
gwi -> ɡvʲ / _ a
wi -> vʲ / _ a
ższ -> ʂʂ / _
mi -> mʲ / _ (e|ę#|ɛ|a)
bi -> bʲ / _ (e|ę#|ɛ)
pi -> pʲ / _ (e|ę#|ɛ|a)
wi -> wʲ / _ (e|ę#|ɛ|o|ɔ)
wi -> wʲi / _ #
mi -> mʲi / _ (ł|l|n)
bi -> bʲi / _ (ć|ł|l)
pi -> pʲi / _ (ć|n|s)
fi -> fʲi / _ (ł|l)
li -> lʲi / _ (k|s|c|#)
wi -> vʲi / _ (ć|n|s)
% 
v -> f / _ (sz|ʂ|cz|k|s)
w -> f / _ (sz|ʂ|cz|k|s)
d -> t / _ (p|k)
% alex: Final obstruent devoicing
% b -> p / _ #|(::consonant::)(::vowel::)
zd -> st / _ #
zg -> sk / _ #
zb -> sp / _ #
gł -> kł / _ #
b -> p / _ #
d -> t / _ #
g -> k / _ #
w -> f / _ #
z -> s / (::vowel::) _ #
ź -> ś / (::vowel::) _ #
ż -> sz / _ #
rz -> sz /_ #
dź -> ć / _ #
dz -> c / _ #
k -> g / _ ż
ś -> ʑ / _ b
ź -> ɕ / _ k
si -> ɕ / _ ɔ
zi -> ʑ / _ ɔ
ci ->  t͡ɕ  / _ ɔ
c -> t͡ɕ / _ i
dz -> d͡ʑ / _ i
s -> ɕ / _ i
z -> ʑ / _ i
n -> ɲ / _ i
k -> kʲ / _ i
g -> ɡʲ / _ i
% Glide formation
u -> w / (::vowel::) _
% i -> j / (::vowel::) _ (::consonant::)
i -> j / _ (::vowel::)
% Even Poles may have problems with pronounciation "rz" after k, ch, p, or t. Pronouncing it as "sh" is fine in those cases
% https://en.wikibooks.org/wiki/Polish/Polish_pronunciation
rz -> ʂ / (k|ch|p|t) _
ż -> ʂ / _ (k|c)
% Denasalization
ą -> ɔ / _ (l|ł|m|n|ɲ|ŋ)
ę -> ɛ / _ (l|ł|m|n|ɲ|ŋ)
ę -> ɛ / _ #
"""
    return rules_text
def get_g2p_map():
    # madon@hp:~/epitran/epitran/data/map$ more pol-Latn.csv 
    g2p_map=[
        ("a","a"),
        ("ą","ɔ̃"),
        ("e","ɛ"),
        ("ę","ɛ̃"),
        ("i","i"),
        ("o","ɔ"),
        ("ó","u"),
        ("u","u"),
        ("y","ɨ"),
        ("b","b"),
        ("c","t͡s"),
        ("ć","t͡ɕ"),
        ("cz","t͡ʂ"),
        ("d","d"),
        ("dz","d͡z"),
        ("dź","d͡ʑ"),
        ("dż","d͡ʐ"),
        ("f","f"),
        ("g","ɡ"),
        ("h","x"),
        ("ch","x"),
        ("j","j"),
        ("k","k"),
        ("l","l"),
        ("ł","w"),
        ("m","m"),
        ("n","n"),
        ("ń","ɲ"),
        ("p","p"),
        ("r","r"),
        ("s","s"),
        ("ś","ɕ"),
        ("sz","ʂ"),
        ("t","t"),
        ("w","v"),
        ("z","z"),
        ("ź","ʑ"),
        ("ż","ʐ"),
        ("rz","ʐ"),
        ("r2z","rz"),
    ]
    return g2p_map
def get_symbols(rules_text):
    xx="get_symbols"
    symbols={}
    rules_with_symbols=[]
    lines=rules_text.split('\n')
    
    for line in lines:
        line=line.strip()
        if not re.match('\s*%', line):
            if line=="":
                pass
            else:
                debug(xx,line)
                line = unicodedata.normalize('NFC', unicodedata.normalize('NFD', line))
                debug(xx,line)
                s = re.match(r'(?P<symbol>::\w+::)\s*=\s*(?P<value>.+)', line)
                if s:
                    symbol_key=s.group('symbol')
                    symbol_value=s.group('value')
                    debug(xx,"symbol",symbol_key,symbol_value)
                    symbols[symbol_key]=symbol_value
                else:
                    debug(xx,"no symbol")
                    rules_with_symbols.append(line)
    return (symbols,rules_with_symbols)
def get_rules(rules_with_symbols,symbols):
    xx="get_rules"
    rules=[]
    for line in rules_with_symbols:
        debug(xx,line)
        line = unicodedata.normalize('NFC', unicodedata.normalize('NFD', line))
        debug(xx,line)
        while re.search(r'::\w+::', line):
            s = re.search(r'::\w+::', line).group(0)
            if s in symbols:
                line = line.replace(s,symbols[s])
            else:
                raise Exception('Undefined symbol: {}'.format(s))
        rules.append(line)
    return rules
def none2str(x):
    return x if x else ''
def fields_to_function(a, b, X, Y):
    xx="fields_to_function"
    left = r'(?P<X>{})(?P<a>{})(?P<Y>{})'.format(X, a, Y)
    debug(xx,"left",left)
    regexp = re.compile(left)
    
    def rewrite(m):
        d = {k: none2str(v) for k, v in m.groupdict().items()}
        return '{}{}{}'.format(d['X'], b, d['Y'])
    
    return lambda w: regexp.sub(rewrite, w, re.U)
def get_rerules(rules):
    xx="get_rerules"
    rerules=[]
    for rule in rules:
        r = re.match(r'(\S+)\s*->\s*(\S+)\s*/\s*(\S*)\s*[_]\s*(\S*)', rule)
        a, b, X, Y = r.groups()
        debug(xx,"a, b, X, Y",(a, b, X, Y))
        X=X.replace('#', '^')
        Y=Y.replace('#', '$')
        if re.search(r'[?]P[<]sw1[>].+[?]P[<]sw2[>]', a):
            debug(xx,"function_metathesis",(a, X, Y))
        else:
           debug(xx,"function",(a, b, X, Y))
           fct=fields_to_function(a, b, X, Y)
           rerules.append(fct)
    return rerules
def apply_rules(rerules,rules_with_symbols,text):
    xx="apply_rules"
    text = unicodedata.normalize('NFC', text.lower())
    previous_text=text
    zipped=list(zip(rerules,rules_with_symbols))
    for rerule,desc in zipped:
        debug(xx,rerule,desc)
        debug(xx,"before",text)
        text = rerule(text)
        debug(xx,"after",text)
        if previous_text!= text:
            debug(xx,"MATCH")
        previous_text=text
    return text
def contruct_regex_from_map(g2p_dict):
    xx="contruct_regex_from_map"
    g2p_keys=g2p_dict.keys()
    graphemes=sorted(g2p_keys, key=len, reverse=True) # sort by length, longer first
    pattern="("+'|'.join(graphemes)+")"
    debug(xx,pattern)
    regex=re.compile(pattern,re.I)
    return regex
def apply_map(text,g2p_dict,regex):
    text = unicodedata.normalize('NFC', text.lower())
    result=[]
    while text:
        m=regex.match(text)
        if m:
            source=m.group(0)
            target=g2p_dict[source]
            result.append(target)
            text=text[len(source):]
        else:
            result.append(text[0])
            text=text[1:]
    text=''.join(result)
    return text
def convert(text,rerules,rules_with_symbols,g2p_dict,regex):
    text=apply_rules(rerules,rules_with_symbols,text)   
    text=apply_map(text,g2p_dict,regex)
    return text
def setup():
    rules_text=get_rules_text()
    (symbols,rules_with_symbols)=get_symbols(rules_text)
    debug(xx,symbols)
    debug(xx,json.dumps(symbols,indent=4, default=str))
    debug(xx,rules_with_symbols)
    rules=get_rules(rules_with_symbols,symbols)
    for rule in rules:
        debug(xx,rule)
    rerules=get_rerules(rules)
    for rerule in rerules:
        debug(xx,rerule)
    # text="Moja kochana... miesiąc "
    # text=apply_rules(rerules,rules_with_symbols,text)
    g2p_map=get_g2p_map()
    g2p_dict=dict(g2p_map)
    regex=contruct_regex_from_map(g2p_dict)
    # text_t=apply_map(text,g2p_dict,regex)
    # print(">",text)
    # print("<",text_t)
    return (rerules,rules_with_symbols,g2p_dict,regex)
if __name__ == "__main__":
    (rerules,rules_with_symbols,g2p_dict,regex)=setup()
    
    # def trans(a):
    #     return a
    
    # https://mowicpopolsku.com/polish-alphabet-pronunciation/ (with sound)
    
    tests=(
        ("umieć","ˈu.mʲɛt͡ɕ"),
        ("umiem","ˈu.mʲɛm"),
        ("siebie","ˈɕɛ.bʲɛ"),
        ("nasz","naʂ"),
        ("naszych","ˈna.ʂɨx"),
        ("sen","sɛn"),
        ("snów","snuf"),
        
        ("głowa","ˈɡwɔ.va"), # Understanding Polish voicing PDF
        ("głowie","ˈɡwɔ.vʲɛ"),
        ("pić","pʲit͡ɕ"),
        ("bić","bʲit͡ɕ"),
        ("płotem","ˈpwɔ.tɛm"),
        ("błotem","bwɔ.tɛm"),
        ("rysa","ˈrɨ.sa"),
        ("ryza","ˈrɨ.za"),
        ("ogień","ˈɔ.ɡʲɛɲ"),
        ("waga","ˈva.ɡa"),
        ("wag","vak"),
        ("mózgu","ˈmuz.ɡu"),
        ("mózg","musk"),
        ("dobro","ˈdɔ.brɔ"),
        
        
        # https://mowicpopolsku.com/polish-alphabet-pronunciation/
        # alphabet
        ("praca","ˈpra.t͡sa"), # a
        ("mąż","mɔŋʂ"), # ą
        ("niebo","ˈɲɛ.bɔ"), #  b
        ("co","t͡sɔ"), # c
        ("być","bɨt͡ɕ"), # ć
        ("daleko","daˈlɛ.kɔ"), # d
        ("też","tɛʂ"), # e
        ("imię","ˈi.mʲɛ"), # ę
        ("film","fʲilm"), # f
        ("gość","ɡɔɕt͡ɕ"), # g
        ("herbata","xɛrˈba.ta"), # h
        ("iść","iɕt͡ɕ"), # i
        ("jechać","ˈjɛ.xat͡ɕ"), # j
        ("kawa","ˈka.va"), # k
        ("lubić","ˈlu.bʲit͡ɕ"), # ll
        ("miły","ˈmʲi.wɨ"), # ł
        ("miły","ˈmʲi.wɨ"), # m
        ("rano","ˈra.nɔ"), # n
        ("tańczyć","ˈtaɲ.t͡ʂɨt͡ɕ"), # ń
        ("okno","ˈɔknɔ"), # o
        ("móc","mut͡s"), # ó
        ("przerwa","ˈpʂɛr.va"), # p
        ("robić","ˈrɔ.bʲit͡ɕ"), # r
        ("syn","sɨn"), # s
        ("środa","ˈɕrɔ.da"), # ś
        ("teraz","ˈtɛ.ras"), # t
        ("szukać","ˈʂu.kat͡ɕ"), # u
        ("wolny","ˈvɔl.nɨ"), # w
        ("czy","t͡ʂɨ"), # y
        ("zamek","ˈza.mɛk"), # z
        ("jeździć","ˈjɛʑ.d͡ʑit͡ɕ"), # ź
        ("żona","ˈʐɔ.na"), # ż
        
        ("mąż","mɔŋʂ"), # The letter ą
        ("ząb","zɔmp"), 
        ("miesiąc","ˈmʲɛ.ɕɔnt͡s"),
        ("wziąć","vʑɔɲt͡ɕ"),
        ("pociąg","ˈpɔ.t͡ɕɔŋk"),
        
        ("często","ˈt͡ʂɛ̃.stɔ"), # The letter ę
        ("imię","ˈi.mʲɛ"),
        ("zęby","ˈzɛm.bɨ"),
        ("wszędzie","ˈfʂɛɲ.d͡ʑɛ"),
        ("pięć","pʲɛɲt͡ɕ"),
        ("piękny","ˈpʲɛŋ.knɨ"),
        
        ("chory","ˈxɔ.rɨ"),          # digraphs # ch
        ("czuć","t͡ʂut͡ɕ"),            #  cz
        ("dzwon","d͡zvɔn"),           # dz
        ("odpowiedź","ɔtˈpɔ.vʲɛt͡ɕ"), # dź
        ("dżem","d͡ʐɛm"),             # dż
        ("rzadko","ˈʐat.kɔ"),        # rz
        ("szukać","ˈʂu.kat͡ɕ"),       # sz
        
        ("dzień","d͡ʑɛɲ"),                # Trigraphs # dzi
        
        # list from Iwona Sadowska: Polish a Comprehensive grammar
        ("fala","ˈfa.la"),
        ("są","sɔ̃"),
        ("banan","ˈba.nan"),
        ("noc","nɔt͡s"),
        ("robić","ˈrɔ.bʲit͡ɕ"),
        ("dobry","ˈdɔ.brɨ"),
        ("tekst","tɛkst"),
        ("język","ˈjɛ̃.zɨk"),
        ("fajka","ˈfaj.ka"),
        ("góra","ˈɡu.ra"),
        ("handel","ˈxan.dɛl"),
        ("lis","lʲis"),
        ("jutro","ˈju.trɔ"),
        ("królik","ˈkru.lʲik"),
        ("lampa","ˈlam.pa"),
        ("mały","ˈma.wɨ"),
        ("mapa","ˈma.pa"),
        ("koń","kɔɲ"),
        ("noga","ˈnɔ.ɡa"),
        ("ósmy","ˈus.mɨ"),
        ("praca","ˈpra.t͡sa"),
        ("rano","ˈra.nɔ"),
        ("sobota","sɔˈbɔ.ta"),
        ("środa","ˈɕrɔ.da"),
        ("tam","tam"),
        ("ulica","uˈlʲi.t͡sa"),
        ("wino","ˈvʲi.nɔ"),
        ("syn","sɨn"),
        ("zupa","ˈzu.pa"),
        ("późno","ˈpuʑ.nɔ"),
        ("życie","ˈʐɨ.t͡ɕɛ"),
        ("chleb","xlɛp"),
        ("ciało","ˈt͡ɕa.wɔ"),
        ("czas","t͡ʂas"),
        ("dzwon","d͡zvɔn"),
        ("dziecko","ˈd͡ʑɛt͡s.kɔ"),
        ("budzik","ˈbu.d͡ʑik"),
        ("fajka","fajka"),
        ("góra","ɡura"),
        ("lis","lʲis"),
        ("jutro","jutrɔ"),
        ("królik","krulʲik"),
        ("lampa","lam.pa"),
        ("mały","mawɨ"),
        ("mapa","mapa"),
        ("noc","ˈnɔt͡s"),
        ("koń","kɔɲ"),
        ("noga","nɔɡa"),
        ("ósmy","usmɨ"),
        ("praca","ˈpra.t͡sa"),
        ("rano","ˈra.nɔ"),
        ("sobota","sɔˈbɔta"),
        ("środa","ɕrɔda"),
        ("tam","ˈtam"),
        ("ulica","uˈlʲi.t͡sa"),
        ("wino","ˈvʲinɔ"),
        ("późno","puʑnɔ"),
        ("życie","ˈʐɨ.t͡ɕɛ"),
        ("chleb","xlɛp"),
        ("ciało","ˈt͡ɕa.wɔ"),
        ("czas","t͡ʂas"),
        ("dzwon","d͡zvɔn"),
        ("dziecko","ˈd͡ʑɛt͡s.kɔ"),
        ("budzik","ˈbu.d͡ʑik"),
        ("dźwięk","d͡ʑvʲɛŋk"),
        ("dżem","d͡ʐɛm"),
        ("nic","ɲit͡s"),
        ("morze","ˈmɔ.ʐɛ"),
        ("siła","ɕiwa"),
        ("siedem","ˈɕɛ.dɛm"),
        ("szynka","ˈʂɨn.ka"),
        ("zima","ˈʑi.ma"),
        ("zielony","ʑɛˈlɔ.nɨ"),
        ("fala","fala"),
        ("tekst","tɛkst"),
        ("lis","lʲis"),
        ("noga","nɔɡa"),
        ("ósmy","usmɨ"),
        ("syn","sɨn"),
        ("język","ˈjɛ̃.zɨk"),
        ("wziął","vʑɔw"),
        ("wzięła","ˈvʑɛ.wa"),
        ("wzięli","ˈvʑɛ.lʲi"),
        ("ząb","zɔmp"),
        ("kąpiel","ˈkɔm.pʲɛl"),
        ("zęby","ˈzɛm.bɨ"),
        ("pępek","ˈpɛm.pɛk"),
        ("ręcznik","ˈrɛn.t͡ʂɲik"),
        ("rząd","ʐɔnt"),
        ("zdjęcie","ˈzdjɛɲ.t͡ɕɛ"),
        ("zdjąć","zdjɔɲt͡ɕ"),
        ("bądź","bɔɲt͡ɕ"),
        ("dziękować","d͡ʑɛŋˈkɔ.vat͡ɕ"),
        ("pociąg","ˈpɔ.t͡ɕɔŋk"),
        ("siew","ɕɛf"),
        ("siła","ˈɕi.wa"),
        ("nici","ɲit͡ɕi"),
        ("chleb","xlɛp"),
        ("ciało","ˈt͡ɕa.wɔ"),
        ("czas","t͡ʂas"),
        ("dzwon","d͡zvɔn"),
        ("dziecko","ˈd͡ʑɛt͡s.kɔ"),
        ("dźwięk","d͡ʑvʲɛŋk"),
        ("dżem","d͡ʐɛm"),
        ("niebo","ˈɲɛ.bɔ"),
        ("morze","ˈmɔ.ʐɛ"),
        ("siedem","ˈɕɛ.dɛm"),
        ("szynka","ˈʂɨn.ka"),
        ("gracz","ɡrat͡ʂ"),
        ("mecz","mɛt͡ʂ"),
        ("spinacz","ˈspʲi.nat͡ʂ"),
        ("być","bɨt͡ɕ"),
        ("bić","bʲit͡ɕ"),
        ("nowy","ˈnɔ.vɨ"),
        ("nowi","ˈnɔ.vʲi"),
        ("mała","ˈmawa"),
        ("miała","ˈmʲa.wa"),
        ("pasek","ˈpa.sɛk"),
        ("piasek","ˈpʲa.sɛk"),
        ("polski","ˈpɔl.skʲi"),
        ("gimnazjum","ɡʲimˈnaz.jum"),
        ("reżim","ˈrɛ.ʐim"),
        ("maszyna","maˈʂɨ.na"),
        ("życie","ˈʐɨ.t͡ɕɛ"),
        ("kasa","kasa"),
        ("Kasia","ˈka.ɕa"),
        ("kobieta","kɔˈbʲɛ.ta"),
        ("kobiecie","kɔˈbʲɛ.t͡ɕɛ"),
        ("teatr","ˈtɛ.atr"),
        ("koń","kɔɲ"),
        ("konia","ˈkɔ.ɲa"),
        ("koniowi","kɔˈɲɔ.vʲi"),
        ("koniu","ˈkɔ.ɲu"),
        ("konie","ˈkɔ.ɲɛ"),
        ("ślub","ɕlup"),
        ("silny","ˈɕil.nɨ"),
        ("chodźmy","ˈxɔd͡ʑ.mɨ"),
        ("koń","kɔɲ"),
        ("koni","ˈkɔ.ɲi"),
        ("gałąź","ˈɡa.wɔɲɕ"),
        ("siostra","ˈɕɔ.stra"),
        ("siódmy","ˈɕud.mɨ"),
        ("siusiu","ˈɕu.ɕu"),
        ("siwy","ˈɕi.vɨ"),
        ("Oświęcim","ɔɕˈfʲɛɲ.t͡ɕim"),
        ("Wrocław","ˈvrɔ.t͡swaf"),
        ("Radom","ˈra.dɔm"),
        ("jedwab","ˈjɛd.vap"),
        ("gołąb","ˈɡɔ.wɔmp"),
        ("krew","krɛf"),
        ("marchew","ˈmar.xɛf"),
        ("brew","brɛf"),
        ("barze","ˈba.ʐɛ"),
        ("Węgier","ˈvɛŋ.ɡʲɛr"),
        ("teatr","ˈtɛ.atr"),
        ("marzec","ˈma.ʐɛt͡s"),
        ("anioł","ˈa.ɲɔw"),
        ("Szwed","ʂfɛt"),
        ("Francuz","ˈfran.t͡sus"),
        ("siostra","ˈɕɔ.stra"),
        ("aktor","ˈak.tɔr"),
        ("aktorzy","akˈtɔ.ʐɨ"),
        ("dobry","ˈdɔ.brɨ"),
        ("dobrzy","ˈdɔb.ʐɨ"),
        ("dobrze","ˈdɔb.ʐɛ"),
        ("gorszy","ˈɡɔr.ʂɨ"),
        ("gorzej","ˈɡɔ.ʐɛj"),
        ("dworzec","ˈdvɔ.ʐɛt͡s"),
        ("dworcu","ˈdvɔr.t͡su"),
        ("dziennikarz","d͡ʑɛnˈɲi.kaʂ"),
        ("dziennikarka","d͡ʑɛn.ɲiˈkar.ka"),
        ("Włoch","vwɔx"),
        ("blacha","ˈbla.xa"),
        ("brzuch","bʐux"),
        ("brzuszek","ˈbʐu.ʂɛk"),
        ("Stach","stax"),
        ("Staszek","staʂɛk"),
        ("Magda","ˈmaɡda"),
        ("woda","ˈvɔ.da"),
        ("wodzie","ˈvɔ.d͡ʑɛ"),
        ("Szwed","ʂfɛt"),
        ("tydzień","ˈtɨ.d͡ʑɛɲ"),
        ("tygodniu","tɨˈɡɔ.dɲu"),
        ("lód","lut"),
        ("lodzie","ˈlɔ.d͡ʑɛ"),
        ("samochód","saˈmɔ.xut"),
        ("samochodzik","samɔxɔd͡ʑik"),
        ("młody","ˈmwɔdɨ"),
        ("młodzi","ˈmwɔ.d͡ʑi"),
        ("młodo","ˈmwɔdɔ"),
        ("chodzić","ˈxɔ.d͡ʑit͡ɕ"),
        ("droga","ˈdrɔ.ɡa"),
        ("drodze","ˈdrɔ.d͡zɛ"),
        ("drugi","ˈdruɡʲi"),
        ("drudzy","ˈdru.d͡zɨ"),
        ("pedagog","pɛˈda.ɡɔk"),
        ("nagi","ˈnaɡʲi"),
        ("nadzy","ˈna.d͡zɨ"),
        ("mogę","ˈmɔ.ɡɛ"),
        ("możesz","ˈmɔ.ʐɛʂ"),
        ("drogi","ˈdrɔɡʲi"),
        ("droższy","ˈdrɔʂ.ʂɨ"),
        ("drogo","ˈdrɔɡɔ"),
        ("matka","ˈmatka"),
        ("matce","ˈmat.t͡sɛ"),
        ("Polska","ˈpɔl.ska"),
        ("Polsce","ˈpɔl.st͡sɛ"),
        ("Polak","ˈpɔ.lak"),
        ("Polacy","pɔˈla.t͡sɨ"),
        ("piec","pʲɛt͡s"),
        ("urzędnik","uˈʐɛn.dɲik"),
        ("urzędniczka","u.ʐɛnˈdɲit͡ʂ.ka"),
        ("rok","rɔk"),
        ("szkoła","ˈʂkɔ.wa"),
        ("szkole","ˈʂkɔ.lɛ"),
        ("stół","stuw"),
        ("stole","ˈstɔlɛ"),
        ("stolik","ˈstɔ.lʲik"),
        ("miły","ˈmʲiwɨ"),
        ("milszy","ˈmʲil.ʂɨ"),
        ("stały","ˈsta.wɨ"),
        ("stale","ˈsta.lɛ"),
        ("niski","ˈɲis.kʲi"),
        ("nisko","ˈɲi.skɔ"),
        ("niżej","ˈɲi.ʐɛj"),
        ("Wisła","ˈvʲi.swa"),
        ("wiosna","ˈvʲɔs.na"),
        ("wczesny","ˈft͡ʂɛs.nɨ"),
        ("wcześnie","ˈft͡ʂɛɕ.ɲɛ"),
        ("jasno","ˈjas.nɔ"),
        ("jaśniej","ˈjaɕ.ɲɛj"),
        ("jasny","jasnɨ"),
        ("jaśniejszy","jaɕˈɲɛj.ʂɨ"),
        ("czysto","ˈt͡ʂɨ.stɔ"),
        ("czyściej","ˈt͡ʂɨɕ.t͡ɕɛj"),
        ("artysta","arˈtɨ.sta"),
        ("miasto","ˈmʲa.stɔ"),
        ("mieście","ˈmʲɛɕ.t͡ɕɛ"),
        ("most","mɔst"),
        ("dwieście","ˈdvʲɛɕ.t͡ɕɛ"),
        ("nasz","naʂ"),
        ("nasi","ˈna.ɕi"),
        ("wasz","vaʂ"),
        ("wasi","ˈva.ɕi"),
        ("starszy","ˈstar.ʂɨ"),
        ("starsi","ˈstar.ɕi"),
        ("prosić","ˈprɔ.ɕit͡ɕ"),
        ("proszę","ˈprɔ.ʂɛ"),
        ("student","ˈstu.dɛnt"),
        ("tata","ˈtata"),
        ("tacie","ˈta.t͡ɕɛ"),
        ("kobieta","kɔˈbʲɛ.ta"),
        ("kobiecie","kɔˈbʲɛ.t͡ɕɛ"),
        ("brat","brat"),
        ("bracia","ˈbra.t͡ɕa"),
        ("tort","tɔrt"),
        ("kwiecień","ˈkfʲɛ.t͡ɕɛɲ"),
        ("duży","ˈdu.ʐɨ"),
        ("duzi","ˈdu.ʑi"),
        ("wozić","ˈvɔʑit͡ɕ"),
        ("wożę","ˈvɔ.ʐɛ"),
        ("wożą","ˈvɔ.ʐɔ̃"),
        ("wyjazd","ˈvɨ.jast"),
        ("gwiazda","ˈɡvʲaz.da"),
        ("gwieździe","ˈɡvʲɛʑ.d͡ʑɛ"),
        ("jeździć","ˈjɛʑ.d͡ʑit͡ɕ"),
        ("mój","muj"),
        ("moi","ˈmɔ.i"),
        ("czyj","t͡ʂɨj"),
        ("Maja","maja"),
        ("soja","ˈsɔja"),
        ("kleić","ˈklɛ.it͡ɕ"),
        ("kroić","ˈkrɔ.it͡ɕ"),
        ("kroją","ˈkrɔ.jɔ̃"),
        ("my","mɨ"),
        ("był","bɨw"),
        ("bił","ˈbʲiw"),
        ("choroba","xɔrɔba"),
        ("blacha","ˈbla.xa"),
        ("ambasada","am.baˈsa.da"),
        ("szafa","ˈʂa.fa"),
        ("droga","ˈdrɔ.ɡa"),
        ("drodze","ˈdrɔ.d͡zɛ"),
        ("książka","ˈkɕɔŋ.ʂka"),
        ("książce","ˈkɕɔŋ.ʂt͡sɛ"),
        ("szkoła","ˈʂkɔ.wa"),
        ("szkole","ˈʂkɔ.lɛ"),
        ("żona","ˈʐɔ.na"),
        ("żonie","ˈʐɔ.ɲɛ"),
        ("kanapa","kaˈna.pa"),
        ("góra","ˈɡura"),
        ("górze","ˈɡu.ʐɛ"),
        ("klasa","ˈklasa"),
        ("klasie","ˈkla.ɕɛ"),
        ("kobieta","kɔˈbʲɛ.ta"),
        ("kobiecie","kɔˈbʲɛ.t͡ɕɛ"),
        ("Warszawa","varˈʂa.va"),
        ("Ameryka","aˈmɛ.rɨ.ka"),
        ("Praga","ˈpra.ɡa"),
        ("kolega","ˈkɔlɛɡa"),
        ("koledzy","kɔˈlɛ.d͡zɨ"),
        ("Anglik","ˈan.ɡlʲik"),
        ("pisać","ˈpʲi.sat͡ɕ"),
        ("wysokie","vɨˈsɔ.kʲɛ"),
        ("kiedy","ˈkʲɛ.dɨ"),
        ("żakiet","ˈʐa.kʲɛt"),
        ("embargo","ɛmˈbar.ɡɔ"),
        ("kurczak","ˈkur.t͡ʂak"),
        ("mleko","ˈmlɛ.kɔ"),
        ("ołówek","ɔˈwu.vɛk"),
        ("Polak","ˈpɔ.lak"),
        ("Polakiem","pɔˈla.kʲɛm"),
        ("sok","sɔk"),
        ("szpieg","ʂpʲɛk"),
        ("wysoki","vɨˈsɔ.kʲi"),
        ("chleb","xlɛp"),
        ("samochód","saˈmɔ.xut"),
        ("jedz","jɛt͡s"),
        ("śnieg","ɕɲɛk"),
        ("mógł","mukw"),
        ("kurz","kuʂ"),
        ("krew","krɛf"),
        ("teraz","ˈtɛ.ras"),
        ("weź","vɛɕ"),
        ("już","juʂ"),
        ("chodź","xɔt͡ɕ"),
        ("tusz","tuʂ"),
        ("tuż","tuʂ"),
        ("śnieg","ɕɲɛk"),
        ("chodź","xɔt͡ɕ"),
        ("chodzi","ˈxɔ.d͡ʑi"),
        ("tusz","tuʂ"),
        ("łóżko","ˈwuʂ.kɔ"),
        ("także","ˈta.ɡʐɛ"),
        ("prośba","ˈprɔʑ.ba"),
        ("buźka","ˈbuɕ.ka"),
        ("stół","stuw"),
        ("stoły","ˈstɔ.wɨ"),
        ("ósmy","ˈus.mɨ"),
        ("osiem","ˈɔ.ɕɛm"),
        ("kościół","ˈkɔɕ.t͡ɕuw"),
        ("kościele","kɔɕˈt͡ɕɛ.lɛ"),
        ("siódmy","ˈɕud.mɨ"),
        ("siedem","ˈɕɛ.dɛm"),
        ("skrócić","ˈskru.t͡ɕit͡ɕ"),
        ("skracać","ˈskra.t͡sat͡ɕ"),
        ("wymówić","vɨˈmu.vʲit͡ɕ"),
        ("wymawiać","vɨˈma.vʲat͡ɕ"),
        ("mój","muj"),
        ("moja","ˈmɔ.ja"),
        ("samochód","saˈmɔ.xut"),
        ("samochodem","sa.mɔˈxɔ.dɛm"),
        ("stół","stuw"),
        ("stoły","ˈstɔ.wɨ"),
        ("stój","stuj"),
        ("stoję","ˈstɔ.jɛ"),
        ("stróż","struʂ"),
        ("podróż","ˈpɔ.druʂ"),
        ("morze","ˈmɔ.ʐɛ"),
        ("mórz","muʂ"),
        ("woda","ˈvɔ.da"),
        ("dużo","ˈdu.ʐɔ"),
        ("krówka","ˈkruf.ka"),
        ("starówka","staˈrufka"),
        ("starucha","staˈru.xa"),
        ("dziadziuś","ˈd͡ʑa.d͡ʑuɕ"),
        ("brzuszek","ˈbʐu.ʂɛk"),
        ("malutki","maˈlut.kʲi"),
        ("może","ˈmɔ.ʐɛ"),
        ("morze","ˈmɔ.ʐɛ"),
        ("morski","ˈmɔr.skʲi"),
        ("karać","ˈka.rat͡ɕ"),
        ("powietrze","pɔˈvʲɛt.ʂɛ"),
        ("wiatr","vʲatr"),
        ("może","ˈmɔ.ʐɛ"),
        ("mogę","ˈmɔ.ɡɛ"),
        ("przyjaciel","pʂɨˈja.t͡ɕɛl"),
        ("przedwojenny","pʂɛd.vɔˈjɛn.nɨ"),
        ("przemoc","ˈpʂɛ.mɔt͡s"),
        ("pszczoła","ˈpʂt͡ʂɔ.wa"),
        ("pszenica","pʂɛˈɲi.t͡sa"),
        ("nuż","nuʂ"),
        ("cóż","t͡suʂ"),
        ("już","juʂ"),
        ("niż","ɲiʂ"),
        ("hełm","xɛwm"),
        ("charakter","xaˈrak.tɛr"),
        ("charytatywny","xa.rɨ.taˈtɨv.nɨ"),
        ("alkohol","alˈkɔxɔl"),
        ("hermetyczny","xɛr.mɛˈtɨt͡ʂ.nɨ"),
        ("nowych","ˈnɔ.vɨx"),
        ("mucha","ˈmuxa"),
        ("muszka","ˈmuʂ.ka"),
        ("dach","dax"),
        ("brzuch","bʐux"),
        ("brzuszek","ˈbʐu.ʂɛk"),
        ("ściskać","ˈɕt͡ɕi.skat͡ɕ"),
        ("ścigać","ˈɕt͡ɕi.ɡat͡ɕ"),
        ("wspominać","fspɔˈmʲi.nat͡ɕ"),
        ("wspierać","ˈfspʲɛ.rat͡ɕ"),
        ("wesprzeć","ˈvɛ.spʂɛt͡ɕ"),
        ("chłopiec","ˈxwɔ.pʲɛt͡s"),
        ("cudzoziemiec","t͡su.d͡zɔˈʑɛ.mʲɛt͡s"),
        ("ojciec","ˈɔj.t͡ɕɛt͡s"),
        ("wdowiec","ˈvdɔ.vʲɛt͡s"),
        ("kupiec","ˈku.pʲɛt͡s"),
    )
            
    errornb=0
    i=0
    for (a,b) in tests:
        if a:
            print('------------')
            print("ST",a)
            b=b.replace('ˈ','').replace('.','')
            print("WI",b)
            bb=convert(a,rerules,rules_with_symbols,g2p_dict,regex)
            if b != bb:
                error="     <---- ERROR "+str(errornb)
                errornb=errornb+1
            else:
                error=""
                
            print("AL",bb, error)
            i=i+1
    print("------------ errors",errornb,"/",i)
