"""
wutangy.py
~~~~~~~~

wutangy is a module that creates WuTang Clan inspired lorem ipsum text.
Enter the 36 Chambers of the Shaolin, WuTang Killah Bees on the swarm.

suuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu


RIP ODB.

:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""
import sys
from random import randint
bringDa = [
    "Shaolin", "shadowboxing", "and", "the", "Wu-Tang", "sword", "style.",
    "If", "what", "you", "say", "is", "true,", "Shaolin", "and", "Wu-Tang",
    "could", "be", "dangerous.", "Do", "you", "think", "your", "Wu-Tang",
    "sword", "can", "defeat", "me", "En", "garde,", "I'll", "let", "you",
    "try", "my", "Wu-Tang", "style", "Bring", "da", "motherfucking", "ruckus",
    "Bring", "da", "motherfucking", "ruckus", "Bring", "da", "mother,",
    "bring", "da", "motherfucking", "ruckus", "Bring", "da", "motherfucking",
    "ruckus", "Ghostface", "catch", "blast", "of", "hype", "verse", "My",
    "Glock", "burst,", "leave", "in", "hearse,", "did", "worse", "come",
    "rough,", "tough", "like", "an", "elephant", "tusk", "Ya", "head", "rush,",
    "fly", "like", "Egyptian", "musk", "Aww", "shit", "Wu-Tang", "Clan",
    "spark", "wicks", "an'", "However", "master", "trick", "just", "like",
    "Nixon", "Causing", "terror,", "quick", "damage", "your", "whole", "era",
    "Hardrocks", "is", "locked", "fuck", "up", "or", "found", "shot", "P.L.O.",
    "style,", "hazardous", "cause", "wreck", "this", "dangerous", "blow",
    "spots", "like", "Waco", "Texas", "watch", "my", "back", "like", "I'm",
    "locked", "down,", "hardcore", "Hitting", "sound,", "watch", "me", "act",
    "bugged", "and", "tear", "it", "down", "Illiterate", "type", "asshole,",
    "songs", "going", "gold", "no", "doubt", "And", "you", "watch", "corny",
    "nigga", "fold", "Yeah", "they", "fake", "and", "all", "that", "carrying",
    "gats", "but", "yo", "My", "Clan", "rolling", "like", "forty", "Macs",
    "Now", "ya", "act", "convinced,", "guess", "it", "makes", "sense",
    "Wu-Tang,", "yo", "soooooo,", "represent", "wait", "for", "one", "act",
    "up,", "now", "got", "him", "backed", "up", "Gun", "his", "neck", "now,",
    "react", "what", "And", "that's", "one", "in", "chamber", "Wu-Tang",
    "banger,", "36", "styles", "of", "danger", "rip", "it", "hardcore,",
    "like", "porno-flick", "bitches", "roll", "with", "groups", "of", "ghetto",
    "bastards", "with", "biscuits", "Check", "it,", "my", "method", "on",
    "microphone's", "banging", "Wu-Tang", "slang'll", "leave", "your",
    "headpiece", "hanging", "Bust", "this,", "I'm", "kicking", "like",
    "Seagal,", "Out", "for", "Justice", "The", "roughness,", "yes",
    "rudeness,", "ruckus", "Redrum,", "verbally", "assault", "with", "tongue",
    "Murder", "one,", "my", "style", "shock", "ya", "knot", "like", "stun-gun",
    "I'm", "hectic,", "wreck", "it", "with", "quickness", "Set", "it", "on",
    "microphone,", "and", "competition", "get", "blown", "By", "this",
    "nasty-ass", "nigga", "with", "my", "nigga,", "RZA", "Charged", "like",
    "bull", "and", "got", "pull", "like", "trigger", "So", "bad,", "stabbing",
    "up", "pad", "with", "vocab,", "crab", "scream", "on", "your", "ass",
    "like", "your", "dad,", "bring", "it", "on", "I'm", "more", "rugged",
    "than", "slaveman", "boots", "New", "recruits,", "I'm", "fucking", "up",
    "MC", "troops", "break", "loose,", "and", "trample", "shit,", "while",
    "stomp", "A", "mudhole", "in", "that", "ass", "cause", "I'm", "straight",
    "out", "swamp", "Creeping", "up", "on", "site,", "now", "it's", "Fright",
    "Night", "My", "Wu-Tang", "slang", "is", "mad", "fucking", "dangerous",
    "And", "more", "deadly", "than", "stroke", "of", "an", "axe", "Chopping",
    "through", "your", "back", "*swish*,", "giving", "bystanders",
    "heart-attacks", "Niggas", "try", "flip,", "tell", "me", "who", "is",
    "him", "blow", "up", "his", "fucking", "prism,", "make", "it", "vicious",
    "act", "of", "terrorism", "You", "wanna", "bring", "it,", "so", "fuck",
    "it,", "come", "on", "and", "bring", "ruckus", "And", "provoke", "niggas",
    "kick", "buckets", "I'm", "wetting", "cream,", "ain't", "wetting", "fame",
    "Who", "selling", "cain,", "I'm", "giving", "out", "deadly", "game",
    "It's", "not", "Russian", "it's", "Wu-Tang", "crushing", "roulette",
    "Slip", "up", "and", "get", "fucked", "like", "Suzette", "Bring", "da",
    "fucking", "ruckus"
]

shameOn = [
    "Shame", "on", "nigga", "who", "try", "run", "game", "on", "nigga", "Wu",
    "buck", "wild", "with", "trigger", "Shame", "on", "nigga", "who", "try",
    "run", "game", "on", "nigga", "I'll", "fuck", "your", "ass", "up!", "(Yo",
    "hut", "one,", "hut", "two,", "hut", "three,", "hut!", "Ol'", "Dirty",
    "Bastard,", "live", "and", "uncut", "Styles", "unbreakable,",
    "shatterproof", "To", "young", "youth,", "you", "wanna", "get", "gun?",
    "Shoot!", "Blaow!", "How", "you", "like", "me", "now?", "Don't", "fuck",
    "style,", "ruthless", "wild", "Do", "you", "wanna", "get", "your", "teeth",
    "knocked", "fuck", "out?", "Wanna", "get", "on", "it", "like", "that,",
    "well", "then", "shout", "Yo", "RZA,", "yo", "razor,", "hit", "me", "with",
    "major", "The", "damage,", "my", "Clan", "understand", "it", "be",
    "flavor", "Gunning,", "humming", "coming", "at", "ya", "First", "I'm",
    "gonna", "get", "ya,", "once", "got", "ya,", "gat", "ya", "You", "could",
    "never", "capture", "Method", "Man's", "stature", "For", "rhyme", "and",
    "for", "rapture,", "got", "niggas", "resigning,", "now", "master", "My",
    "style?", "Never!", "put", "fucking", "buck", "in", "wild", "kid,", "I'm",
    "terror", "Razor", "sharp,", "sever", "The", "head", "from", "shoulders,",
    "I'm", "better,", "than", "my", "competta", "You", "mean", "competitor,",
    "whatever,", "let's", "get", "together", "react", "so", "thick,", "I'm",
    "phat", "and", "yo", "Rae", "came", "blowing", "and", "blew", "off",
    "your", "headphones", "black", "Rap", "from", "yo", "Cali", "Texas",
    "Smoother", "than", "Lexus,", "now's", "my", "turn", "wreck", "this",
    "Brothers", "approach", "and", "half", "step,", "but", "ain't", "heard",
    "half", "of", "it", "yet", "And", "bet", "you're", "not", "fucking", "vet",
    "So,", "when", "you", "see", "me", "on", "real,", "forming", "like",
    "Voltron", "Remember", "got", "deep", "like", "Navy", "Seal", "Yo!",
    "come", "with", "that", "ol'", "loco,", "style", "from", "my", "vocal",
    "Couldn't", "peep", "it", "with", "pair", "of", "bi-focals", "I'm", "no",
    "joker,", "play", "me", "as", "joker", "Be", "on", "you", "like", "house",
    "on", "fire,", "smoke", "ya", "Crews", "be", "acting", "like", "they",
    "gangs,", "anyway", "Be", "like,", "Warriors,", "come", "out", "and",
    "pla", "Burn", "me,", "get", "into", "shit,", "let", "it", "out", "like",
    "diarrhea", "Got", "burnt", "once,", "but", "that", "was", "only",
    "gonorrhea", "Dirty,", "keep", "shit", "stains", "in", "my", "drawers",
    "So", "can", "get", "fizza-funky", "for", "you", "Murder,", "taste",
    "flame", "of", "Wu-Tang,", "rah!", "Here", "comes", "Tiger", "vs.",
    "Crane", "I'll", "be", "like", "wild", "with", "my", "style", "Punk,",
    "you", "play", "me", "chump,", "you", "get", "jumped", "Wu", "is",
    "coming", "through", "at", "theater", "near", "you", "And", "get", "funk",
    "like", "shoe", "What?"
]

clanIn = [
    "Up", "from", "36", "Chambers...", "Heheh..", "it's",
    "Ghost..*Face*..*Killah*", "Hehheheh", "Wu-Tang", "Wu-Tang", "Killa",
    "Beez,", "we", "on", "swarm", "Wu-Tang", "Killa", "Beez,", "we", "on",
    "swarm", "Wu-Tang", "Killa", "Beez,", "we", "on", "swarm", "Wu-Tang",
    "Killa", "Beez,", "we", "on", "swarm", "The", "RZA,", "GZA,", "Ol'",
    "Dirty", "Bastard,", "Inspectah", "Deck,", "U-God", "Ghostface", "Killah,",
    "Method", "Man,", "Raekwon", "Chef,", "Masta", "Killa", "Raw", "Desire,",
    "LeVon,", "Power", "Cipher", "12", "O'Clock,", "60", "Second", "Assassin,",
    "4th", "Disciple", "The", "Brown", "Hornet", "K.D.", "Down", "Low",
    "Recka,", "Shyheim", "AKA", "The", "Rugged", "Child", "Due-Due", "Lilz,",
    "Mista", "Hezekiah", "--", "better", "known", "as", "Yin", "and", "Yang",
    "The", "True", "Master,", "Isham,", "DJ", "Skane,", "The", "True",
    "Robocop", "comin", "thru", "Scientific", "Shabazz,", "my", "motherfuckin",
    "man", "Wise", "Civilized", "The", "Shaolin", "Soldiers", "Daddy-O", "and",
    "Poppa", "Ron", "comin", "down", "from", "motherfuckin", "South", "end",
    "of", "things", "Killa", "beez", "all", "over", "your", "fuckin", "planet",
    "Thirty-six", "chambers", "of", "death", "Three-hundred", "and", "sixty",
    "degrees", "of", "perfected", "styles", "Choppin", "off", "your",
    "motherfuckin", "dome...", "...piece,", "and", "every", "fuckin",
    "borough", "Brooklyn,", "Manhattan,", "and", "Queens,", "Staten", "Island",
    "The", "motherfuckin", "Bronx,", "Killa", "Beez....", "The", "sword?",
    "C'mon,", "give", "him", "sword", "Clan", "in", "front,", "let", "your",
    "feet", "stomp", "Niggas", "on", "left,", "rag", "shit", "death", "Hoods",
    "on", "right,", "wild", "for", "night", "Punks", "in", "back,", "come",
    "on", "in", "track", "what", "The", "Wu", "is", "coming", "through,",
    "outcome", "is", "critical", "Fucking", "with", "my", "style", "is",
    "sort", "of", "like", "miracle", "On", "34th", "Street,", "in", "Square",
    "of", "Herald", "gamed", "Ella,", "bitch", "caught", "Fitz", "like",
    "Gerald-", "-ine", "Ferraro,", "who's", "full", "of", "sorrow", "cause",
    "ho", "didn't", "win", "But", "sun", "will", "still", "come", "out",
    "tomorrow", "And", "shine", "shine", "shine", "like", "gold", "mine",
    "Here", "comes", "drunk", "monk,", "with", "quart", "of", "Ballantine",
    "Pass", "bone,", "kid", "pass", "bone", "Let's", "get", "on", "this",
    "mission", "like", "Indiana", "Jones,", "GZA", "One", "who", "just",
    "represent", "Wu-Tang", "clique", "With", "game", "and", "soul", "of",
    "an", "old", "school", "flick", "Like", "Mack", "and", "Dolemite,", "who",
    "both", "did", "bids", "Claudine", "went", "Cooley", "High", "and", "had",
    "mad", "kids", "So", "stop,", "life", "you", "save", "may", "be", "your",
    "motherfucking", "own", "I'll", "hang", "your", "ass", "with", "this",
    "microphone", "Make", "way", "for", "merge", "of", "traffic", "Wu-Tang's",
    "coming", "through", "with", "full", "metal", "jackets", "God", "squad",
    "that's", "mad", "hard", "serve", "Come", "fronting", "hard,", "then",
    "Bernhard", "Goetz", "what", "he", "deserves", "No", "response", "while",
    "bomb", "that", "ass", "You", "ain't", "shit,", "your", "wack", "ass",
    "town", "had", "you", "gassed", "Egos", "is", "something", "Wu-Tang",
    "crush", "Souped-up", "niggas", "on", "stage", "get", "rushed", "don't",
    "give", "goddamn", "on", "shows", "you", "did", "How", "many", "rhymes",
    "you", "got", "or", "who", "knows", "you", "kid", "Cause", "don't", "know",
    "you", "therefore", "show", "me", "what", "you", "know", "come", "sharp",
    "as", "blade", "and", "cut", "you", "slow", "You", "become", "so", "Pat",
    "as", "my", "style", "increases", "What's", "that", "in", "your", "pants",
    "ahh", "human", "feces", "Throw", "your", "shitty", "drawers", "in",
    "hamper", "Next", "time", "come", "strapped", "with", "fucking", "Pamper",
    "How", "you", "sound", "B?", "You're", "better", "off", "quitter", "I'm",
    "on", "mound,", "G,", "and", "it's", "no-hitter", "And", "my", "DJ",
    "catcher,", "he's", "my", "man", "In", "way", "he's", "one", "who",
    "devised", "plan", "He", "throws", "signs", "hook", "up", "beats", "with",
    "clout", "throw", "rhymes", "mic", "and", "strike", "em", "out", "So",
    "it", "really", "doesn't", "matter", "on", "how", "you", "intrigue", "You",
    "can't", "fuck", "with", "those", "in", "major", "leagues"
]

longAssList = bringDa + shameOn + clanIn

first = filter(lambda x: x[0] == x[0].upper(), longAssList)


def sentence(size):
    print(first)


def wu(chambers=0):
    ipsum = []
    if not chambers:
        if (len(sys.argv) > 1):
            chambers = sys.argv[1]
        else:
            chambers = 5

    print('WUTANG COMING AT YOU IN DUE TIME')
