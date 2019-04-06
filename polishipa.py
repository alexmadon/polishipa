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
]



# madon@hp:~/epitran/epitran/data/pre$ cat pol-Latn.txt 
rules_text="""
% Symbols
::nasal_vowel:: = ą|ę
::vowel:: = a|ą|e|ę|i|o|ó|u|y
::vow_not_i:: = a|ą|e|ę|o|ó|u|y
::consonant:: = b|c|ć|cz|d|dź|dż|f|g|h|ch|j|k|l|ł|m|n|ń|p|r|s|ś|sz|t|w|z|ź|ż|rz

% After nasalized vowels
0 -> m / (::nasal_vowel::) _ b|p
0 -> n / (::nasal_vowel::) _ d|t|c|dz
0 -> ɲ　/ (::nasal_vowel::) _ ć|dź
0 -> ŋ　/ (::nasal_vowel::) _ g|k

% Palatalized consonants
ci -> t͡ɕ / _ (::vow_not_i::)
dzi -> d͡ʑ / _ (::vow_not_i::)
si -> ɕ / _ (::vow_not_i::)
zi -> ʑ / _ (::vow_not_i::)
ni -> ɲ / _ (::vow_not_i::)
ki -> kʲ / _ e
gi -> ɡʲ / _ e
c -> t͡ɕ / _ i
dz -> d͡ʑ / _ i
s -> ɕ / _ i
z -> ʑ / _ i
n -> ɲ / _ i
k -> kʲ / _ i
g -> ɡʲ / _ i

% Glide formation
u -> w / (::vowel::) _
i -> j / (::vowel::) _ (::consonant::)
i -> j / _ (::vowel::)

% Denasalization
ą -> ɔ / _ (l|ł|m|n|ɲ|ŋ)
ę -> ɛ / _ (l|ł|m|n|ɲ|ŋ)
ę -> ɛ / _ #

"""




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


text="Moja kochana... miesiąc "
text=apply_rules(rerules,rules_with_symbols,text)   
g2p_dict=dict(g2p_map)
regex=contruct_regex_from_map(g2p_dict)

text_t=apply_map(text,g2p_dict,regex)
print(">",text)
print("<",text_t)
# quit()



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
    
)

for (a,b) in tests:
    print(a,b.replace('ˈ','').replace('.',''))
    bb=convert(a,rerules,rules_with_symbols,g2p_dict,regex)
    print(a,bb)
