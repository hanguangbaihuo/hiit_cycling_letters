#!/usr/bin/env python
import unittest
from collections import Counter
from copy import copy
"""
如果一个单词通过循环右移获得的单词，我们称这些单词都为一种循环单词。 现在给出一个单词集合，需要统计这个集合中有多少种不同的循环单词。

输入 : dict = ["picture", "turepic", "icturep", "word", "ordw", "lint"]
输出 : 3
说明 : 
"picture", "turepic", "icturep" 是相同的旋转单词。
"word", "ordw" 也相同。
"lint" 是第三个不同于前两个的单词。
"""
def cal_lack_sum(c_l):
    c_l = [ord(_) for _ in c_l]
    count = 1
    for i in range(len(c_l)-1):
        between = c_l[i+1] - c_l[i]
        count *= between if between else 1
    lack = c_l[0] - c_l[-1]
    count *= lack if lack else 1
    return count + sum(c_l)


def count_loop_string(L):
    counter = Counter()
    for word in L:
        sp = list(word.lower())
        tmp_sp = copy(sp)
        sp.sort()
        sp.extend([str(cal_lack_sum(tmp_sp))])
        key = "-".join(sp)
        counter[key] += 1
    return len(counter.keys())


if __name__ == "__main__":
    L = ["along", "acute", "baAba", "adsorbate", "altruism", "accomplish", "adsorptive", "airbrush", "adoptive", "Alvin", "basha", "achieve", "amniotic", "anaconda", "Alcmena", "accompany", "acrobat", "admissible", "accolade", "adaptation", "afterimage", "Aeneas", "alia", "Alva", "analyst", "abrade", "alphabet", "abstractor", "absorptive", "abort", "Analects", "adoption", "admire", "Andre", "Ada", "acrylate", "allusive", "allotting", "Abelson", "almighty", "Alamo", "alone", "Altair", "almost", "acre", "acorn", "Achilles", "dominalab", "Alvarez", "accentuate", "alabaster", "otabb", "Agatha", "airmail", "Anatole", "address", "amperage", "aboveboard", "abscissae", "abaAb", "ancestral", "airedale", "afraid", "amphibious", "amongst", "Angelo", "Aaron", "amaranth", "alumnus", "anaphoric", "teaba", "anchovy", "accent", "anastigmatic", "adsorption", "abnormal", "ambient", "Andorra", "abacus", "analogue", "amok", "anger", "onAar", "alfresco", "aforethought", "altogether", "abroad", "Alcestis", "Allyn", "Anastasia", "adjoint", "Andover", "rkaardva", "advantageous", "acidify", "anAbeli", "Algiers", "afire", "Abelian", "aluminate", "albeit", "anachronistic", "aboveground", "abjure", "Aiken", "adulterous", "agrimony", "accrue", "Andrea", "alphabetic", "Angeline", "ambrose", "Adkins", "AMA", "abetted", "acrobacy", "aminobenzoic", "amra", "aficionado", "aftermath", "ancillary", "aisle", "academia", "teaba", "anagram", "Africa", "abscissa", "anarch", "aloe", "Adair", "alto", "afoot", "rkaardva", "airmen", "ana", "eabas", "alewife", "angel", "anchorage", "botab", "acrid", "accusation", "Alsatian", "allmsgs", "Albrecht", "agony", "absinthe", "affect", "ajar", "actuarial", "acrobatic", "afferent", "alliance", "ctabdu", "also", "acronym", "anatomy", "aerie", "adorn", "Anglo", "Alberto", "abridge", "Aires", "alleviate", "Alex", "ambiguity", "anent", "ackab", "affair", "Ahmedabad", "Alasdair", "alfonso", "administrate", "amateurish", "Aladdin", "Aerobacter", "advertise", "acquittal", "amateur", "agitate", "ashab", "aggressive", "abstruse", "Akers", "altercate", "Aden", "absurdum", "affix", "alveoli", "abandon", "Angles", "baAba", "abdicate", "accusative", "amphibole", "Ackley", "airline", "ahead", "acupuncture", "abysmal", "absent", "absurd", "bbottA", "bbeya", "abut", "air", "amity", "amplify", "Albright", "accentual", "Andes", "absentee", "addict", "abolish", "adjutant", "alcove", "aborigine", "acid", "allele", "airmass", "amuse", "alb", "aloud", "acropolis", "dicateab", "amorphous", "anatomist", "affectate", "adenoma", "Allstate", "aesthete", "afforestation", "allocate", "abscess", "acidulous", "adventure", "actual", "algorithmic", "acetate", "admonition", "admission", "amicable", "ambulant", "absenteeism", "Agricola", "ndonaba", "abreact", "affiliate", "ahem", "abhorred", "Ames", "alginate", "adjust", "Allah", "afresh", "alienate", "again", "adjectival", "afterword", "amply", "airplane", "affectionate", "accidental", "Anglophobia", "Alger", "Aaron", "Alhambra", "accede", "anatomic", "acclamation", "able", "alabdomin", "abeyant", "amass", "acquaintance", "agate", "Ali", "alan", "Angelica", "ail", "nalabdomi", "algebra", "Alberta", "afternoon", "abbey", "airlift", "Afghan", "Acapulco", "Alabamian", "Alexis", "ado", "Agee", "ale", "abolition", "Allegheny", "airstrip", "airborne", "allemand", "ambrosial", "abound", "allow", "aerofoil", "algorithm", "botab", "domenab", "anamorphic", "Alice", "Andrew", "Anaheim", "amalgam", "abscond", "affluent", "academic", "yabbe", "Amsterdam", "adequate", "Abernathy", "Abram", "abaAb", "AL", "rhusAa", "adhere", "abridgment", "Alicia", "airlock", "allegiant", "ambiguous", "Alec", "agricultural", "absorption", "amoeba", "Alison", "Algeria", "ablution", "Aegean", "addendum", "afflict", "alliterate", "agronomy", "ampere", "alizarin", "airdrop", "alchemy", "abide", "anastigmat", "age", "amanuensis", "aloft", "Alastair", "adverbial", "aggressor", "Angelina", "albino", "anachronism", "advantage", "acuity", "Ampex", "adulate", "accompaniment", "accordion", "actress", "alley", "acquisitive", "addend", "abacus", "accessory", "alumna", "acrylic", "aerate", "amplitude", "anchorite", "allure", "abuilding", "agriculture", "amber", "admittance", "accreditation", "amend", "Algonquin", "among", "inalabdom", "akin", "Alfred", "anecdotal", "admitted", "agar", "adventitious", "alien", "accessible", "airframe", "adamant", "Abner", "amble", "Adirondack", "across", "accord", "advert", "ad", "adapt", "dvarkaar", "Anabel", "amygdaloid", "alluvium", "adject", "algae", "airy", "afford", "acquiesce", "anarchy", "album", "amende", "airflow", "Ackerman", "ablate", "ala", "abrupt", "altimeter", "advisor", "abstention", "actuate", "Aldrich", "alternate", "abominable", "alias", "ammo", "agglutinin", "algaecide", "abnegation", "elianAb", "afterlife", "aggregate", "accident", "amphioxis", "amanita", "angle", "accusatory", "agreeing", "amide", "absolve", "airtight", "advice", "aforesaid", "Andy", "alibi", "an", "account", "afterward", "eabat", "analogy", "aldehyde", "ambiance", "advisee", "ammonite", "ago", "Aesop", "allegro", "alert", "allege", "aerodynamic", "Amos", "ambidextrous", "admit", "abominate", "abode", "Alpert", "Angeles", "alimony", "elianAb", "acanthus", "acquitting", "absorb", "acquit", "Acadia", "abandon", "acquire", "allot", "adenosine", "Ajax", "amphibology", "abbas", "abovementioned", "administer", "actinide", "adrenaline", "ablaze", "Abo", "aerospace", "adhesive", "abyss", "allspice", "analytic", "Adonis", "Adrienne", "administrable", "alluvial", "alloy", "afreet", "affidavit", "adolescent", "aghast", "alacrity", "alimentary", "academy", "Alsop", "Aeolus", "adult", "aching", "AK", "acquiescent", "ahoy", "alkaloid", "amnesiac", "aesthetic", "adopt", "albatross", "amputate", "affine", "allotropic", "anaerobic", "advocate", "Afrikaans", "aid", "allude", "adulterate", "Addison", "amidst", "agave", "ambush", "adept", "abeyance", "academician", "ameliorate", "aeronautic", "aldrin", "actinic", "allocable", "admix", "Alcott", "almond", "angelic", "accomplice", "bacusa", "aloof", "abacus", "adrenal", "agglutinate", "anecdote", "andesine", "affront", "ample", "afloat", "aloha", "aircraft", "amniocentesis", "Adamson", "aforementioned", "accurate", "neabalo", "aborning", "alumni", "amulet", "angiosperm", "anaphora", "Alberich", "admiration", "adroit", "Abidjan", "accountant", "Adlerian", "adequacy", "advise", "andesite", "alp", "allay", "usAarh", "alight", "affirmation", "accumulate", "algal", "allowance", "alumnae", "aleph", "allotted", "abhor", "amalgamate", "agglomerate", "allyl", "admitting", "ambrosia", "alpha", "add", "amp", "acknowledgeable", "acetaminophen", "Allentown", "alarm", "adventurous", "ambitious", "addle", "Amazon", "ancient", "alkaline", "Adelia", "advisable", "align", "tabduc", "already", "access", "Acton", "agenda", "abject", "ambulatory", "adore", "afar", "ancestry", "airman", "allegate", "amatory", "Allis", "alterate", "Andrei", "and", "abdicate", "absorbent", "aboriginal", "afterthought", "affiance", "bducta", "admixture", "Abyssinia", "alcohol", "Americana", "androgen", "albacore", "ace", "Alexandra", "adjudge", "absolute", "afield", "abutting", "Allen", "agnostic", "accredit", "Alexander", "Amerada", "alcoholic", "almagest", "amid", "basab", "althea", "Agnes", "aerosol", "abrasion", "adjudicate", "analysis", "allegoric", "anchor", "Albania", "Abramson", "aberrate", "acolyte", "adipic", "Adele", "adverse", "adjunct", "amy", "abreast", "alter", "acrimonious", "alai", "adversary", "ambition", "nabdome", "basab", "abstain", "analyses", "ami", "accept", "advocacy", "agog", "Algol", "babaA", "acknowledge", "advance", "alveolus", "analeptic", "Agway", "AC", "Adler", "advent", "although", "allegory", "alleyway", "amphibian", "Actaeon", "Amherst", "achromatic", "adagio", "afterbirth", "abuse", "alphanumeric", "alma", "aliquot", "abduct", "acrimony", "ammonium", "Anglican", "adjoin", "alive", "accuse", "alpaca", "analgesic", "inalabdom", "Alpheratz", "Alphonse", "altruist", "Aleutian", "Alexandre", "afforest", "agile", "adenine", "ductab", "Adolphus", "Andean", "acceptant", "agent", "adiabatic", "adage", "Amman", "oneabal", "alpine", "aldermen", "alveolar", "ammoniac", "amethystine", "absentminded", "America", "Amtrak", "acerbic", "affirmative", "Albert", "aerobic", "aflame", "anew", "Agamemnon", "Aldebaran", "Aeneid", "all", "arkaardv", "almanac", "Alexei", "aboard", "anemone", "Alameda", "aberrant", "Andersen", "Amharic", "afterglow", "actinium", "amphetamine", "addition", "abbey", "acidic", "amaze", "seaba", "always", "ally", "Adelaide", "accouter", "Allegra", "acrophobic", "amiss", "above", "abusable", "acerbity", "ague", "acoustic", "abutted", "Alabama", "aerial", "addenda", "Aides", "altar", "enabdom", "allergy", "against", "admonish", "actor", "affable", "acetic", "algebraic", "ache", "adposition", "analogous", "aegis", "Aitken", "acquaint", "alum", "ammunition", "abbreviate", "accost", "altern", "Agnew", "Allan", "Akron", "onaband", "aardvark", "Ainu", "absolution", "adverb", "Addis", "adrift", "abdomen", "affricate", "alundum", "acclaim", "airway", "adoration", "Almaden", "airspeed", "altitude", "abstract", "afro", "Aberdeen", "Afghanistan", "Amarillo", "cusaba", "aggression", "agrarian", "Achaean", "ACM", "Andromeda", "ah", "ambassador", "abrasive", "agribusiness", "amethyst", "aileron", "acceptor", "admiral", "aeolian", "aile", "albumin", "adrenalin", "aggravate", "aide", "anaglyph", "accustom", "adhesion", "adobe", "Angela", "acyclic", "abbey", "amort", "accordant", "acidulate", "acreage", "Amoco", "Aaron", "alumina", "agree", "Aleck", "adherent", "alligator", "alongside", "accompanist", "amoebae", "acacia", "amnesty", "Algenib", "additive", "act", "abstinent", "administratrix", "airfield", "aim", "amigo", "acculturate", "usabac", "Allison", "nAaro", "allergic", "anastomotic", "Ammerman", "airpark", "affirm", "accipiter", "abhorrent", "Albany", "acme", "accelerometer", "agone", "Alton", "abrogate", "allusion", "adjourn", "airport", "Algonquian", "Anderson", "Alcoa", "alyssum", "Alfredo", "americium", "Adrian", "acclimate", "abetting", "aerogene", "acetone", "agronomist", "Angie", "Alaska", "absentia", "ammonia", "Anacreon", "ambivalent", "amoeboid", "abusive", "alike", "agnomen", "Abraham", "acquisition", "ailanthus", "ancestor", "alga", "Alexandria", "anarchic", "Andromache", "nabando", "seaba", "Adolph", "Alistair", "alder", "agreeable", "Aida", "Aeschylus", "Alden", "am", "actinometer", "acrophobia", "accommodate", "about", "alpenstock", "angelfish", "ammeter", "adduce", "amino", "alkali", "belianA", "amnesia", "aggrieve", "Adriatic", "anathema", "addressee", "airfare", "accession", "Addressograph", "adieu", "alba", "agleam", "Adam", "Amadeus", "advisory", "Abigail", "alderman", "ambuscade", "alfalfa", "aftereffect", "Albuquerque", "admiralty", "A&M", "amount", "adjacent", "aliphatic", "acetylene", "abet", "Amelia", "Accra", "anastomosis", "alchemist", "accrual", "agouti", "abundant", "accelerate", "Anabaptist", "amoral", "acumen", "adultery", "aft", "amen", "Andalusia", "Afrikaner", "ampersand", "adaptive", "actinolite", "accuracy", "anaplasmosis", "activate", "accretion", "adsorb"]
    print(count_loop_string(L))