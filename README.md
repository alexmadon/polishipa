# polishipa

https://mowicpopolsku.com/polish-alphabet-pronunciation/
https://github.com/dmort27/epitran

root@hp:~# pip3 install epitran

pip3 install epitran
Requirement already satisfied: epitran in /usr/local/lib/python3.5/dist-packages
Requirement already satisfied: unicodecsv in /usr/local/lib/python3.5/dist-packages (from epitran)
Requirement already satisfied: panphon>=0.12 in /usr/local/lib/python3.5/dist-packages (from epitran)
Requirement already satisfied: regex in /usr/local/lib/python3.5/dist-packages (from epitran)
Requirement already satisfied: marisa-trie in /usr/local/lib/python3.5/dist-packages (from epitran)
Requirement already satisfied: setuptools in /usr/lib/python3/dist-packages (from epitran)
Requirement already satisfied: munkres in /usr/local/lib/python3.5/dist-packages (from panphon>=0.12->epitran)
Requirement already satisfied: PyYAML in /usr/local/lib/python3.5/dist-packages (from panphon>=0.12->epitran)
Requirement already satisfied: editdistance in /usr/local/lib/python3.5/dist-packages (from panphon>=0.12->epitran)
Requirement already satisfied: numpy in /usr/local/lib/python3.5/dist-packages (from panphon>=0.12->epitran)



https://github.com/mphilli/English-to-IPA


https://pypi.org/project/regex/
https://bitbucket.org/mrabarnett/mrab-regex


pip3 show epitran
Name: epitran
Version: 0.57
Summary: Tools for transcribing languages into IPA.
Home-page: http://github.com/dmort27/epitran
Author: David R. Mortensen
Author-email: dmortens@cs.cmu.edu
License: MIT
Location: /usr/local/lib/python3.5/dist-packages
Requires: setuptools, unicodecsv, panphon, regex, marisa-trie


## Usage

to use the package call the setup() function and then convert() on the text you want to convert to IPA.
