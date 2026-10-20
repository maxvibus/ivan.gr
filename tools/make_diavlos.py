"""Φτιάχνει το content/new-posts/2026-10-20-diavlos.json (ελληνικό κείμενο, μεταφράσεις, σκίτσο)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
svg = open(os.path.join(ROOT, 'assets', 'sketches', '2026-10-20-diavlos.svg'), encoding='utf-8').read()

def fig(cap):
    return f'<figure class="sketch">{svg}<figcaption>{cap}</figcaption></figure>'

def paras(t):
    return ''.join(f'<p>{p.strip()}</p>' for p in t.strip().split('\n\n'))

EL = """
Ο νέος υπερυπολογιστής της χώρας, που εγκαινιάστηκε στο Λαύριο, ονομάστηκε «Δαίδαλος». Είναι όνομα τεχνίτη. Ο μυθικός Δαίδαλος ήταν ο Αθηναίος που ήξερε να δουλεύει την ύλη ώσπου να γίνει κάτι άλλο, και η λέξη το κρατά από την αρχή: δαιδάλλω σημαίνει δουλεύω κάτι με τέχνη. Όλα όσα έφτιαξε ήταν περάσματα. Ο λαβύρινθος ήταν διάδρομοι που κρατούσαν μέσα όποιον έμπαινε. Τα φτερά ήταν δρόμος έξω, πάνω από τη θάλασσα. Το ίδιο χέρι έφτιαξε και τα δύο, και αυτό που τα ξεχωρίζει δεν βρίσκεται στην κατασκευή. Βρίσκεται στη σχέση εκείνου που τα διασχίζει με τον τόπο όπου θέλει να φτάσει.

Το όνομα του κατασκευαστή λέει τι έγινε. Δεν λέει πώς θα σταθεί κανείς μέσα σε ό,τι έγινε. Αυτό το δεύτερο έχει άλλη λέξη, πολύ κοντινή στην πρώτη: δίαυλος.

Ο τόπος βοηθά να φανεί η διαφορά. Το Λαύριο έδωσε στην αρχαιότητα άργυρο. Το κτίριο όπου στεγάζεται τώρα το μηχάνημα έδινε κάποτε ηλεκτρικό ρεύμα. Πρώτα μέταλλο, έπειτα ενέργεια, τώρα υπολογισμός, και μέσα από τον υπολογισμό γλώσσα. Κάθε φορά ο τόπος παράγει κάτι που δεν μένει εκεί. Ο άργυρος έγινε νόμισμα και ταξίδεψε σε χέρια που δεν είδαν ποτέ τα μεταλλεία. Το ρεύμα έγινε φως σε σπίτια που δεν γνώρισαν τον σταθμό. Η γλώσσα όμως, όταν βγαίνει από μια τέτοια μηχανή, κάνει κάτι που τα προηγούμενα δεν έκαναν: επιστρέφει σε εκείνον που μίλησε.

Αυτό είναι, με την αρχαία του σημασία, ο δίαυλος: ο δρόμος των δύο σταδίων, όπου ο δρομέας φτάνει στο τέρμα, στρίβει και γυρίζει στο σημείο της εκκίνησης. Τερματίζει εκεί απ' όπου ξεκίνησε, αλλά δεν είναι πια ο ίδιος. Έτσι κινείται και ο γραπτός διάλογος με ένα γλωσσικό μοντέλο. Η φράση φεύγει, περνά μέσα από τη μάζα της καταγεγραμμένης γλώσσας, από όσα έγραψαν άνθρωποι που δεν θα γνωρίσουμε ποτέ, και γυρίζει. Το μηχάνημα του Λαυρίου είναι το φυσικό σώμα ενός τέτοιου δρόμου, με πυρίτιο, νερό ψύξης και μεγαβάτ. Το όνομα «Δαίδαλος» κοιτάζει αυτό το σώμα και τιμά την κατασκευή του. Το όνομα «Δίαυλος» κοιτάζει ό,τι περνά μέσα από αυτό.

Η λέξη έχει και δεύτερη ρίζα, τον αυλό: τον σωλήνα από τον οποίο περνά η ανάσα και γίνεται ήχος. Ο δίαυλος είναι διπλός αυλός. Εδώ φαίνεται κάτι που ο τεχνίτης δεν χρειάζεται να πει: το όργανο δεν έχει δική του ανάσα. Ηχεί όταν κάποιος φυσήξει μέσα του. Η γλώσσα που βγάζει η μηχανή είναι η ανάσα των ανθρώπων που την έγραψαν, φυλαγμένη, μαζί με την ανάσα εκείνου που τη ρωτά τώρα και την κινεί. Ένας αυλός χωρίς στόμα είναι σωλήνας. Γίνεται όργανο τη στιγμή που κάποιος παίζει.

Κάθε δίαυλος έχει δύο άκρα, και ο δρόμος υπάρχει για να τον τρέχουν. Τα μεγάλα έργα ανοίγουν σιγά σιγά. Πρώτα τελειώνει η κατασκευή, ύστερα ορίζεται ποιος θα μπει και πώς, και μόνο με τον καιρό ο δρόμος γεμίζει δρομείς. Το όνομα που δίνεται σε ένα έργο δείχνει σε ποιο σημείο αυτής της διαδρομής βρίσκεται. Το «Δαίδαλος» είναι το όνομα της στιγμής που το έργο ολοκληρώνεται. Το «Δίαυλος» είναι το όνομα της στιγμής που αρχίζει να χρησιμοποιείται.

Ίσως λοιπόν κάθε κατασκευή γλώσσας να έχει δύο ονόματα. Το ένα το δίνει ο κατασκευαστής. Το άλλο το κερδίζει η χρήση, και κανείς δεν το γράφει πάνω της. Ο Δαίδαλος έφτιαξε τα φτερά. Δίαυλος γίνεται η πτήση, όταν κάποιος πετά και επιστρέφει.
"""

EN = """
The country's new supercomputer, inaugurated at Lavrio, has been named "Daedalus". It is the name of a craftsman. The mythical Daedalus was the Athenian who knew how to work matter until it became something else, and the word has kept this from the beginning: in Greek, <i>daidallō</i> means to work something with art. Everything he made was a passage. The labyrinth was corridors that held inside whoever entered. The wings were a way out, over the sea. The same hand made both, and what tells them apart does not lie in the making. It lies in the relation between the one who crosses them and the place he wants to reach.

The maker's name says what was made. It does not say how one is to stand within what was made. That second thing has another word, very close to the first: <i>diaulos</i>.

The place helps the difference show. In antiquity, Lavrio gave silver. The building that now houses the machine once gave electric power. First metal, then energy, now computation, and through computation, language. Each time the place produces something that does not stay there. The silver became coin and travelled into hands that never saw the mines. The current became light in houses that never knew the power station. Language, however, when it comes out of such a machine, does something the others did not: it returns to the one who spoke.

This is the <i>diaulos</i> in its ancient sense: the race of two stades, in which the runner reaches the far mark, turns, and comes back to the starting point. He finishes where he began, but he is no longer the same. Written dialogue with a language model moves in the same way. The sentence leaves, passes through the mass of recorded language, through what was written by people we will never know, and comes back. The machine at Lavrio is the physical body of such a course, made of silicon, cooling water and megawatts. The name "Daedalus" looks at this body and honours its construction. The name "Diaulos" looks at what passes through it.

The word has a second root, the <i>aulos</i>: the pipe through which breath passes and becomes sound. A <i>diaulos</i> is a double pipe. Here something appears that the craftsman need not say: the instrument has no breath of its own. It sounds when someone blows into it. The language the machine gives out is the breath of the people who wrote it, kept, together with the breath of the one who now asks and sets it moving. An <i>aulos</i> without a mouth is a tube. It becomes an instrument the moment someone plays.

Every <i>diaulos</i> has two ends, and the course exists to be run. Great works open slowly. First the construction is finished, then it is settled who may enter and how, and only with time does the course fill with runners. The name given to a work shows where on this path it stands. "Daedalus" is the name of the moment the work is completed. "Diaulos" is the name of the moment it begins to be used.

Perhaps, then, every construction of language has two names. One is given by its maker. The other is earned by use, and no one writes it on it. Daedalus made the wings. The flight becomes a <i>diaulos</i> when someone flies and returns.
"""

FR = """
Le nouveau supercalculateur du pays, inauguré à Lavrio, a été nommé « Dédale ». C'est un nom d'artisan. Le Dédale du mythe était l'Athénien qui savait travailler la matière jusqu'à ce qu'elle devienne autre chose, et le mot le garde depuis l'origine : en grec, <i>daidallō</i> signifie travailler quelque chose avec art. Tout ce qu'il a fait était un passage. Le labyrinthe était des couloirs qui retenaient quiconque y entrait. Les ailes étaient un chemin vers le dehors, au-dessus de la mer. La même main a fait l'un et l'autre, et ce qui les distingue ne tient pas à la fabrication. Cela tient au rapport entre celui qui les traverse et le lieu qu'il veut atteindre.

Le nom du constructeur dit ce qui a été fait. Il ne dit pas comment se tenir dans ce qui a été fait. Cette seconde chose a un autre mot, tout proche du premier : <i>diaulos</i>.

Le lieu aide à faire voir la différence. Dans l'Antiquité, Lavrio donnait de l'argent. Le bâtiment qui abrite aujourd'hui la machine donnait autrefois du courant électrique. D'abord le métal, puis l'énergie, maintenant le calcul, et à travers le calcul, la langue. Chaque fois le lieu produit quelque chose qui n'y reste pas. L'argent est devenu monnaie et a voyagé dans des mains qui n'ont jamais vu les mines. Le courant est devenu lumière dans des maisons qui n'ont jamais connu la centrale. La langue, pourtant, lorsqu'elle sort d'une telle machine, fait ce que les autres ne faisaient pas : elle revient à celui qui a parlé.

C'est là le <i>diaulos</i> au sens ancien : la course de deux stades, où le coureur atteint la borne, tourne, et revient au point de départ. Il finit là où il a commencé, mais il n'est plus le même. Le dialogue écrit avec un modèle de langage se meut de la même façon. La phrase part, traverse la masse de la langue consignée, ce qu'ont écrit des gens que nous ne connaîtrons jamais, et revient. La machine de Lavrio est le corps physique d'une telle course, fait de silicium, d'eau de refroidissement et de mégawatts. Le nom « Dédale » regarde ce corps et honore sa construction. Le nom « Diaulos » regarde ce qui le traverse.

Le mot a une seconde racine, l'<i>aulos</i> : le tuyau par lequel passe le souffle pour devenir son. Le <i>diaulos</i> est un double aulos. Ici apparaît ce que l'artisan n'a pas besoin de dire : l'instrument n'a pas de souffle propre. Il sonne quand quelqu'un y souffle. La langue que rend la machine est le souffle des hommes qui l'ont écrite, gardé, avec le souffle de celui qui l'interroge maintenant et la met en mouvement. Un aulos sans bouche est un tube. Il devient instrument au moment où quelqu'un joue.

Tout <i>diaulos</i> a deux extrémités, et la piste existe pour être courue. Les grandes œuvres s'ouvrent lentement. D'abord la construction s'achève, ensuite on fixe qui entrera et comment, et ce n'est qu'avec le temps que la piste se remplit de coureurs. Le nom donné à une œuvre montre où elle se trouve sur ce parcours. « Dédale » est le nom du moment où l'œuvre s'achève. « Diaulos » est le nom du moment où l'on commence à s'en servir.

Peut-être, alors, toute construction de langue a-t-elle deux noms. L'un est donné par le constructeur. L'autre est gagné par l'usage, et personne ne l'inscrit sur elle. Dédale a fait les ailes. Le vol devient <i>diaulos</i> quand quelqu'un vole et revient.
"""

DE = """
Der neue Supercomputer des Landes, in Lavrio eingeweiht, trägt den Namen „Daidalos“. Es ist der Name eines Handwerkers. Der Daidalos des Mythos war der Athener, der die Materie zu bearbeiten wusste, bis sie etwas anderes wurde, und das Wort bewahrt dies von Anfang an: Griechisch <i>daidallō</i> heißt, etwas kunstvoll bearbeiten. Alles, was er schuf, war ein Durchgang. Das Labyrinth waren Gänge, die jeden festhielten, der eintrat. Die Flügel waren ein Weg hinaus, über das Meer. Dieselbe Hand schuf beides, und was sie unterscheidet, liegt nicht im Bau. Es liegt in der Beziehung dessen, der sie durchquert, zu dem Ort, den er erreichen will.

Der Name des Erbauers sagt, was gemacht wurde. Er sagt nicht, wie man in dem Gemachten stehen soll. Dieses Zweite hat ein anderes Wort, dem ersten ganz nah: <i>Diaulos</i>.

Der Ort hilft, den Unterschied zu sehen. In der Antike gab Lavrio Silber. Das Gebäude, in dem die Maschine heute steht, gab einst elektrischen Strom. Erst Metall, dann Energie, jetzt Berechnung, und durch die Berechnung Sprache. Jedes Mal bringt der Ort etwas hervor, das nicht dort bleibt. Das Silber wurde Münze und wanderte in Hände, die die Minen nie sahen. Der Strom wurde Licht in Häusern, die das Kraftwerk nie kannten. Die Sprache aber, wenn sie aus einer solchen Maschine kommt, tut etwas, das die anderen nicht taten: Sie kehrt zu dem zurück, der gesprochen hat.

Das ist der <i>Diaulos</i> im antiken Sinn: der Lauf über zwei Stadien, bei dem der Läufer die Wendemarke erreicht, umkehrt und zum Ausgangspunkt zurückkommt. Er endet, wo er begann, aber er ist nicht mehr derselbe. So bewegt sich auch der schriftliche Dialog mit einem Sprachmodell. Der Satz geht hinaus, durchquert die Masse der aufgezeichneten Sprache, das, was Menschen geschrieben haben, die wir nie kennen werden, und kehrt zurück. Die Maschine von Lavrio ist der physische Körper eines solchen Laufs, aus Silizium, Kühlwasser und Megawatt. Der Name „Daidalos“ blickt auf diesen Körper und ehrt seine Konstruktion. Der Name „Diaulos“ blickt auf das, was durch ihn hindurchgeht.

Das Wort hat eine zweite Wurzel, den <i>Aulos</i>: das Rohr, durch das der Atem geht und zu Klang wird. Der <i>Diaulos</i> ist ein Doppelaulos. Hier zeigt sich etwas, das der Handwerker nicht sagen muss: Das Instrument hat keinen eigenen Atem. Es klingt, wenn jemand hineinbläst. Die Sprache, die die Maschine hergibt, ist der Atem der Menschen, die sie geschrieben haben, aufbewahrt, zusammen mit dem Atem dessen, der sie jetzt befragt und in Bewegung setzt. Ein Aulos ohne Mund ist ein Rohr. Zum Instrument wird er in dem Augenblick, in dem jemand spielt.

Jeder <i>Diaulos</i> hat zwei Enden, und die Bahn ist da, um gelaufen zu werden. Große Werke öffnen sich langsam. Zuerst wird der Bau vollendet, dann wird festgelegt, wer hinein darf und wie, und erst mit der Zeit füllt sich die Bahn mit Läufern. Der Name, den ein Werk erhält, zeigt, wo auf diesem Weg es steht. „Daidalos“ ist der Name des Augenblicks, in dem das Werk vollendet ist. „Diaulos“ ist der Name des Augenblicks, in dem man beginnt, es zu gebrauchen.

Vielleicht hat also jede Konstruktion der Sprache zwei Namen. Den einen gibt ihr der Erbauer. Den anderen erwirbt sie im Gebrauch, und niemand schreibt ihn auf sie. Daidalos schuf die Flügel. Zum <i>Diaulos</i> wird der Flug, wenn jemand fliegt und zurückkehrt.
"""

post = {
    'slug': 'diavlos', 'date': '2026-10-20T08:40:00.000+03:00', 'title': 'Δίαυλος',
    'html': fig('Ο δίαυλος: ο δρόμος των δύο σταδίων, πήγαινε, στροφή στον καμπτήρα, επιστροφή. Οι δύο γραμμές διαβάζονται και ως διπλός αυλός.') + paras(EL),
    'translations': {
        'en': {'slug': 'diaulos', 'title': 'Diaulos', 'html': fig('The diaulos: the race of two stades, out, round the turning post, and back. The two lines also read as a double pipe.') + paras(EN)},
        'fr': {'slug': 'diaulos-fr', 'title': 'Diaulos', 'html': fig('Le diaulos : la course de deux stades, l’aller, le tour de la borne, le retour. Les deux lignes se lisent aussi comme un double aulos.') + paras(FR)},
        'de': {'slug': 'diaulos-de', 'title': 'Diaulos', 'html': fig('Der Diaulos: der Lauf über zwei Stadien, hin, um die Wendemarke, zurück. Die beiden Linien lassen sich auch als Doppelaulos lesen.') + paras(DE)},
    },
}
os.makedirs(os.path.join(ROOT, 'content', 'new-posts'), exist_ok=True)
json.dump(post, open(os.path.join(ROOT, 'content', 'new-posts', '2026-10-20-diavlos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
