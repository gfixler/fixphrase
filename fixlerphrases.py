"""
NOTES:

    - verb "to be" has 8 forms and is handled separately

    - some verbs have alternate forms; in the following
        pairings I use the first line, and not the second:

        beat   beat    beaten
        beat   beat    beat

        burn   burned  burned
        burn   burnt   burnt

        dream  dreamed dreamed
        dream  dreamt  dreamt

        lay     laid    laid
        lie     lay     lain

        learn  learned learned
        learn  learnt  learnt
"""

"""
Irregular verbs group 1
same base form, past simple, and past participle
"""
irreg1 = [
    "bet",
    "bid",
    "cost",
    "cut",
    "hit",
    "hurt",
    "let",
    "put",
    "read",
    "shut",
]

"""
Irregular verbs group 2
same past simple and past participle (omitted)
different base form
"""
irreg2 = [
    ("beat", "beaten"),
    ("bend", "bent"),
    ("bring", "brought"),
    ("build", "built"),
    ("burn", "burned"),
    ("buy", "bought"),
    ("catch", "caught"),
    ("dig", "dug"),
    ("dream", "dreamed"),
    ("feel", "felt"),
    ("fight", "fought"),
    ("find", "found"),
    ("hang", "hung"),
    ("have", "had"),
    ("hear", "heard"),
    ("hold", "held"),
    ("keep", "kept"),
    ("lay", "laid"),
    ("lead", "led"),
    ("learn", "learned"),
    ("leave", "left"),
    ("lend", "lent"),
    ("light", "lit"),
    ("lose", "lost"),
    ("make", "made"),
    ("mean", "meant"),
    ("meet", "met"),
    ("pay", "paid"),
    ("read", "read"),
    ("say", "said"),
    ("sell", "sold"),
    ("send", "sent"),
    ("shoot", "shot"),
    ("sit", "sat"),
    ("sleep", "slept"),
    ("spend", "spent"),
    ("stand", "stood"),
    ("teach", "taught"),
    ("tell", "told"),
    ("think", "thought"),
    ("understand", "understood"),
    ("win", "won"),
]

"""
Irregular verbs group 3
same base form and past participle (omitted)
different past simple
"""
irreg3 = [
    ("become", "became"),
    ("come", "came"),
    ("run", "ran"),
]

"""
Irregular verbs group 4
different base form, past simple, past participle
"""
irreg4 = [
    ("begin", "began", "begun"),
    ("bite", "bit", "bitten"),
    ("blow", "blew", "blown"),
    ("break", "broke", "broken"),
    ("choose", "chose", "chosen"),
    ("dive", "dove", "dived"),
    ("do", "did", "done"),
    ("draw", "drew", "drawn"),
    ("drink", "drank", "drunk"),
    ("drive", "drove", "driven"),
    ("eat", "ate", "eaten"),
    ("fall", "fell", "fallen"),
    ("fly", "flew", "flown"),
    ("forget", "forgot", "forgotten"),
    ("forgive", "forgave", "forgiven"),
    ("freeze", "froze", "frozen"),
    ("get", "got", "gotten"),
    ("give", "gave", "given"),
    ("go", "went", "gone"),
    ("grow", "grew", "grown"),
    ("hide", "hid", "hidden"),
    ("know", "knew", "known"),
    ("ride", "rode", "ridden"),
    ("ring", "rang", "rung"),
    ("rise", "rose", "risen"),
    ("see", "saw", "seen"),
    ("show", "showed", "shown"),
    ("sing", "sang", "sung"),
    ("speak", "spoke", "spoken"),
    ("swim", "swam", "swum"),
    ("take", "took", "taken"),
    ("tear", "tore", "torn"),
    ("throw", "threw", "thrown"),
    ("wake", "woke", "woken"),
    ("wear", "wore", "worn"),
    ("write", "wrote", "written"),
]

