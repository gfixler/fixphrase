"""
NOTES:

    - verb "to be" has 8 forms and is handled separately

    - some verbs have alternate forms; in the following
        pairings I use the first line, and not the second:

        abide       abided      abided
        abide       abode       abidden

        alight      alighted    alighted
        alight      alit        alit

        bid         bid         bid
        bid         bade        bidden

        beat        beat        beaten
        beat        beat        beat

        burn        burned      burned
        burn        burnt       burnt

        bust        busted      busted
        bust        bust        bust

        clothe      clothed     clothed
        clothe      clad        clad

        dive        dove        dove
        dive        dived       dived

        dream       dreamed     dreamed
        dream       dreamt      dreamt

        dwell       dwelled     dwelled
        dwell       dwelt       dwelt

        forbid      forbade     forbidden
        forbid      forbad      forbidden

        forget      forgot      forgotten
        forget      forgot      forgot

        get         got         gotten
        get         got         got

        input       input       input
        input       inputted    inputted

        kneel       kneeled     knelt
        kneel       kneeled     kneeled
        kneel       knelt       knelt

        knit        knit        knit
        knit        knitted     knitted

        lay         laid        laid
        lay         lain        lain
        lie         lay         lain

        lean        leaned      leaned
        lean        lent        lent

        leap        leaped      leapt
        leap        leapt       leapt
        leap        leaped      leaped

        learn       learned     learned
        learn       learnt      learnt

        light       lit         lit
        light       lighted     lighted

        hang        hung        hung
        hang        hanged      hanged

        misspell    misspelled  misspelled
        misspell    misspelt    misspelt

        prove       proved      proven
        prove       proved      proven

        rid         rid         rid
        rid         ridded      ridded

        saw         sawed       sawn
        saw         sawed       sawn

        sew         sewed       sewn
        sew         sewed       sewn

        shave       shaved      shaven
        shave       shaved      shaven

        shear       sheared     shorn
        shear       shore       sheared

        shoe        shoed       shoed
        shoe        shod        shod

        shrive      shrived     shriven
        shrive      shrove      shrived

        smell       smelled     smelled
        smell       smelt       smelt

        sneak       snuck       snuck
        sneak       sneaked     sneaked

        sow         sowed       sowed
        sow         sown        sowed

        speed       sped        sped
        speed       speeded     speeded

        spill       spilled     spilled
        spill       spilt       spilt

        spin        spun        spun
        spin        span        spun

        spit        spat        spit
        spit        spat        spat
        spit        spit        spit

        spoil       spoiled     spoiled
        spoil       spoilt      spoilt

        strew       strewed     strewn
        strew       strewed     strewn

        strike      struck      stricken
        strike      struck      stricken

        strip       stripped    stripped
        strip       stript      stript

        strive      strived     striven
        strive      strove      strived

        thrive      thrived     thriven
        thrive      throve      thrived

        weave       wove        weaved
        weave       weaved      woven
"""

"""
Irregular verbs group 1
same base form, past simple, and past participle
"""
irreg1 = [
    "beset",
    "bet",
    "bid",
    "broadcast",
    "burst",
    "cast",
    "cost",
    "cut",
    "fit",
    "forcast",
    "hit",
    "hurt",
    "input",
    "knit",
    "let",
    "put",
    "quit",
    "read",
    "rid",
    "set",
    "shed",
    "shut",
    "slit",
    "split",
    "spread",
    "sublet",
    "thrust",
    "undercut",
    "upset",
]

"""
Irregular verbs group 2
same past simple and past participle (omitted)
different base form
"""
irreg2 = [
    ("abide", "abided"),
    ("alight", "alighted"),
    ("babysit", "babysat"),
    ("beat", "beaten"),
    ("behold", "beheld"),
    ("bend", "bent"),
    ("bind", "bound"),
    ("bleed", "bled"),
    ("breed", "bred"),
    ("bring", "brought"),
    ("build", "built"),
    ("burn", "burned"),
    ("bust", "busted"),
    ("buy", "bought"),
    ("catch", "caught"),
    ("cling", "clung"),
    ("clothe", "clothed"),
    ("creep", "crept"),
    ("deal", "dealt"),
    ("dig", "dug"),
    ("dream", "dreamed"),
    ("dwell", "dwelled"),
    ("feed", "fed"),
    ("feel", "felt"),
    ("fight", "fought"),
    ("find", "found"),
    ("flee", "fled"),
    ("fling", "flung"),
    ("foretell", "foretold"),
    ("hang", "hung"),
    ("have", "had"),
    ("hear", "heard"),
    ("hold", "held"),
    ("keep", "kept"),
    ("lay", "laid"),
    ("lead", "led"),
    ("lean", "leaned"),
    ("learn", "learned"),
    ("leave", "left"),
    ("lend", "lent"),
    ("light", "lit"),
    ("lose", "lost"),
    ("make", "made"),
    ("mean", "meant"),
    ("meet", "met"),
    ("mislead", "misled"),
    ("misspell", "misspelled"),
    ("misunderstand", "misunderstood"),
    ("pay", "paid"),
    ("say", "said"),
    ("seek", "sought"),
    ("sell", "sold"),
    ("send", "sent"),
    ("shine", "shone"),
    ("shoe", "shoed"),
    ("shoot", "shot"),
    ("sit", "sat"),
    ("sleep", "slept"),
    ("slide", "slid"),
    ("sling", "slung"),
    ("slink", "slunk"),
    ("smell", "smelled"),
    ("sneak", "snuck"),
    ("speed", "sped"),
    ("spell", "spelt"),
    ("spend", "spent"),
    ("spill", "spilled"),
    ("spin", "spun"),
    ("spoil", "spoiled"),
    ("stand", "stood"),
    ("sting", "stung"),
    ("string", "strung"),
    ("strip", "stripped"),
    ("sweep", "swept"),
    ("swing", "swung"),
    ("teach", "taught"),
    ("tell", "told"),
    ("think", "thought"),
    ("unbind", "unbound"),
    ("understand", "understood"),
    ("unwind", "unwound"),
    ("win", "won"),
    ("wind", "wound"),
    ("withhold", "withheld"),
    ("withstand", "withstood"),
    ("wring", "wrung"),
]

"""
Irregular verbs group 3
same base form and past participle (omitted)
different past simple
"""
irreg3 = [
    ("become", "became"),
    ("come", "came"),
    ("overcome", "overcame"),
    ("run", "ran"),
    ("spit", "spat"),
]

"""
Irregular verbs group 4
different base form, past simple, past participle
"""
irreg4 = [
    ("arise", "arose", "arisen"),
    ("awake", "awoke", "awoken"),
    ("bear", "bore", "born"),
    ("befall", "befell", "befallen"),
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
    ("forbid", "forbade", "forbidden"),
    ("foresee", "foresaw", "foreseen"),
    ("forget", "forgot", "forgotten"),
    ("forgive", "forgave", "forgiven"),
    ("forsake", "forsook", "forsaken"),
    ("freeze", "froze", "frozen"),
    ("get", "got", "gotten"),
    ("give", "gave", "given"),
    ("go", "went", "gone"),
    ("grow", "grew", "grown"),
    ("hide", "hid", "hidden"),
    ("interweave", "interwove", "interwoven"),
    ("kneel", "kneeled", "knelt"),
    ("know", "knew", "known"),
    ("leap", "leaped", "leapt"),
    ("mistake", "mistook", "mistaken"),
    ("prove", "proved", "proven"),
    ("ride", "rode", "ridden"),
    ("ring", "rang", "rung"),
    ("rise", "rose", "risen"),
    ("saw", "sawed", "sawn"),
    ("see", "saw", "seen"),
    ("sew", "sewed", "sewn"),
    ("shake", "shook", "shaken"),
    ("shave", "shaved", "shaven"),
    ("shear", "sheared", "shorn"),
    ("show", "showed", "shown"),
    ("shrink", "shrank", "shrunk"),
    ("shrive", "shrived", "shriven"),
    ("sing", "sang", "sung"),
    ("sink", "sank", "sunk"),
    ("slay", "slew", "slain"),
    ("sow", "sowed", "sowed"),
    ("speak", "spoke", "spoken"),
    ("spring", "sprang", "sprung"),
    ("steal", "stole", "stolen"),
    ("stink", "stank", "stunk"),
    ("strew", "strewed", "strewn"),
    ("stride", "strode", "stridden"),
    ("strike", "struck", "stricken"),
    ("strive", "strived", "striven"),
    ("swear", "swore", "sworn"),
    ("swell", "swelled", "swollen"),
    ("swim", "swam", "swum"),
    ("take", "took", "taken"),
    ("tear", "tore", "torn"),
    ("thrive", "thrived", "thriven"),
    ("throw", "threw", "thrown"),
    ("tread", "trod", "trodden"),
    ("underlie", "underlay", "underlain"),
    ("undertake", "undertook", "undertaken"),
    ("undo", "undid", "undone"),
    ("unedrgo", "underwent", "undergone"),
    ("unsee", "unsaw", "unseen"),
    ("wake", "woke", "woken"),
    ("wear", "wore", "worn"),
    ("weave", "wove", "weaved"),
    ("withdraw", "withdrew", "withdrawn"),
    ("write", "wrote", "written"),
]

