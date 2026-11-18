"""Δημοσίευση 18.11.2026: «Μου απαντούν όσοι έχουν καρδιά, όχι χαρτιά», με σκίτσο και μεταφράσεις."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sketch_kardia

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG = sketch_kardia.svg()


def fig(cap):
    return f'<figure class="sketch">{SVG}<figcaption>{cap}</figcaption></figure>'


def body(ps):
    return ''.join(f'<p>{p}</p>' for p in ps)


EL = [
    'Αυτές τις εβδομάδες ζήτησα πολλά, και όλα γραπτά, γιατί έτσι μιλώ. Ζήτησα εξηγήσεις, έγγραφα, μια επιστροφή χρημάτων, μια λογοδοσία. Ζήτησα και πράγματα πιο λεπτά: να με ακούσει κάποιος για ένα έργο, για ένα παλιό χαρτί, για μια ιστορία που κουβαλώ.',
    'Κάποια στιγμή κατάλαβα ότι δεν χρειάζεται να περιμένω τις απαντήσεις για να ξέρω από ποιον θα έρθουν. Αρκεί να δω τι θα του κόστιζε να απαντήσει.',
    'Ένα μουσείο στην Αμερική προώθησε το γράμμα μου την ίδια μέρα. Μια ειδικός στη Γαλλία, που δεν με ήξερε, απάντησε την επομένη. Πριν από δύο χρόνια είχα ρωτήσει έναν παλαιοβιβλιοπώλη για μια ιστορική επιστολή. Μου απάντησε τυπικά ότι είχε πουληθεί. Του ξανάγραψα τώρα, και μου έστειλε αντίγραφό της χωρίς ούτε μία λέξη παραπάνω. Δεν του το ζήτησα έτσι, και δεν ήταν υποχρέωσή του. Κανείς τους δεν είχε τίποτα να προστατέψει από μένα.',
    'Όπου ζήτησα χαρτιά που θα έδειχναν κάτι για εκείνον που τα κρατά, βρήκα σιωπή. Ή κάτι χειρότερο: αυτόματα μηνύματα, ένα τηλεφώνημα στη θέση μιας γραπτής απάντησης, ένα «δεν έχω φωνή, είμαι άρρωστη» σε κάποιον που δεν ζήτησε ποτέ να ακούσει φωνή.',
    'Ανάμεσα σε αυτούς υπάρχουν και όσοι απλώς δεν νοιάζονται, γιατί ένας πελάτης είναι για εκείνους διαδικασία. Ο εκτυπωτής-σκάνερ μου, με τον οποίο ψηφιοποιώ εδώ και μήνες αρχεία ολόκληρων ζωών, χάλασε μέσα στην εγγύηση. Η εγγύηση σημαίνει δωρεάν επισκευή ή αντικατάσταση, κι αν αυτά δεν γίνονται, επιστροφή των χρημάτων. Πιστωτικό, μόνο αν το διαλέξεις εσύ. Το κατάστημα μού έγραψε ότι «εγκρίθηκε πιστωτικό». Σαν να ζήτησα χάρη, και σαν να μπορούσε εκείνο να ορίσει πού θα ξοδέψω τα χρήματά μου. Μου έδωσε τη δική του επιλογή, όχι αυτή που ο νόμος προβλέπει και για μένα.',
    'Ένας εξωτερικός διαχειριστής πολυκατοικίας μοιάζει να τα έχει κάνει όλα μαντάρα, και ίσως όχι κατά λάθος. Ένοικοι σωπαίνουν. Τράπεζες παίζουν με τις λέξεις, ώστε να μπλεχτείς στην αντιπαράθεση κι όχι στην ουσία. Ακόμη κι όταν κάθε γραπτή τους απόκριση μοιάζει με απάντηση, δεν λένε αυτό που ρωτήθηκαν. Κι αυτό είναι σιωπή.',
    'Υπάρχει και μια άλλη περίπτωση. Ένας γείτονας στην Αθήνα με ρώτησε «θέλεις να μπεις στην ομάδα με τους υπόλοιπους γείτονες;», με έβαλε, και σώπασε μαζί με όλους όταν μίλησα σε όλους. Η απάντηση σε έναν άνθρωπο δεν κοστίζει. Γίνεται σιωπή όταν έχει κι εκείνος κάτι να πει μπροστά στους άλλους.',
    'Και ύστερα έφτασε η σειρά μου. Ήμουν ήδη τόσο κουρασμένος από καταστήματα, τράπεζες, γραφεία, συγγενείς, που όταν ένας γείτονας στο χωριό ρώτησε τη μητέρα μου «τι κάνει ο Ιβάν;», δεν άκουσα ερώτηση. Άκουσα κατηγορία που ζητούσε απολογία. Του έγραψα θυμωμένος και τον φόρτωσα με πράγματα παλιά, που δεν ήταν δικά του. Με πήρε αμέσως τηλέφωνο. Δεν το σήκωσα, γιατί δεν το σηκώνω πια ούτε στον Θεό. Μου έγραψε, του εξήγησα, του ζήτησα συγγνώμη. Στο τέλος μου έγραψε κάτι που έχει πει κάθε άνθρωπος στον κόσμο:',
    '«Πάντα μπορείς να υπολογίζεις σε εμένα ό,τι ώρα και να είναι.»',
    'Δεν του απάντησα. Ξέρω ότι είναι άνθρωπος. Και κάθε άνθρωπος πονά.',
]

EN = [
    'These past weeks I have asked for a great deal, and all of it in writing, because that is how I speak. I asked for explanations, documents, a refund, an account. I also asked for subtler things: for someone to hear me about a work, about an old paper, about a story I carry.',
    'At some point I understood that I need not wait for the answers to know whom they will come from. It is enough to see what answering would cost them.',
    'A museum in America forwarded my letter the same day. A specialist in France, who did not know me, replied the next. Two years ago I had asked an antiquarian bookseller about a historical letter. He replied formally that it had been sold. I wrote to him again now, and he sent me a copy of it without a single word more. I had not asked for it that way, and it was not his obligation. None of them had anything to protect from me.',
    'Wherever I asked for papers that would show something about the one who holds them, I found silence. Or something worse: automatic messages, a phone call in place of a written reply, an “I have no voice, I am ill” to someone who never asked to hear a voice.',
    'Among them there are also those who simply do not care, because to them a customer is a procedure. My printer-scanner, with which I have been digitising for months the archives of entire lives, broke down under warranty. A warranty means free repair or replacement, and if neither is possible, a refund. Store credit, only if you choose it. The shop wrote to me that “store credit has been approved”. As if I had asked a favour, and as if it could decide where I would spend my own money. It gave me its own choice, not the one the law provides for me too.',
    'An outside building manager seems to have made a mess of everything, and perhaps not by accident. Residents keep silent. Banks play with words, so that you get tangled in the dispute and not in the substance. Even when each written response of theirs looks like an answer, they do not say what they were asked. And that is silence too.',
    'There is another case as well. A neighbour in Athens asked me, “would you like to join the group with the other neighbours?”, added me, and fell silent with everyone else when I spoke to everyone. Answering one person costs nothing. It becomes silence when he too has something to say in front of the others.',
    'And then it was my turn. I was already so tired of shops, banks, offices, relatives, that when a neighbour in the village asked my mother “how is Ivan?”, I did not hear a question. I heard an accusation demanding a defence. I wrote to him in anger and loaded him with old things that were not his. He called me at once. I did not pick up, because I no longer pick up even for God. He wrote to me, I explained, I asked his forgiveness. In the end he wrote something every person in the world has said:',
    '“You can always count on me, whatever the hour.”',
    'I did not reply. I know he is a human being. And every human being hurts.',
]

FR = [
    'Ces dernières semaines, j’ai demandé beaucoup, et tout par écrit, parce que c’est ainsi que je parle. J’ai demandé des explications, des documents, un remboursement, une reddition de comptes. J’ai demandé aussi des choses plus fines : que quelqu’un m’écoute à propos d’une œuvre, d’un vieux papier, d’une histoire que je porte.',
    'À un moment, j’ai compris que je n’avais pas besoin d’attendre les réponses pour savoir de qui elles viendraient. Il suffit de voir ce que répondre leur coûterait.',
    'Un musée en Amérique a transmis ma lettre le jour même. Une spécialiste en France, qui ne me connaissait pas, a répondu le lendemain. Il y a deux ans, j’avais interrogé un libraire ancien au sujet d’une lettre historique. Il m’avait répondu, formellement, qu’elle était vendue. Je lui ai réécrit maintenant, et il m’en a envoyé une copie, sans un mot de plus. Je ne la lui avais pas demandée ainsi, et ce n’était pas son obligation. Aucun d’eux n’avait rien à protéger de moi.',
    'Là où j’ai demandé des papiers qui montreraient quelque chose de celui qui les détient, j’ai trouvé le silence. Ou pire : des messages automatiques, un coup de téléphone à la place d’une réponse écrite, un « je n’ai pas de voix, je suis malade » adressé à quelqu’un qui n’a jamais demandé à entendre une voix.',
    'Parmi eux, il y a aussi ceux qui ne s’en soucient tout simplement pas, parce qu’un client n’est pour eux qu’une procédure. Mon imprimante-scanner, avec laquelle je numérise depuis des mois les archives de vies entières, est tombée en panne sous garantie. La garantie, c’est la réparation gratuite ou le remplacement, et si ni l’un ni l’autre n’est possible, le remboursement. Un avoir, seulement si c’est vous qui le choisissez. Le magasin m’a écrit qu’« un avoir a été approuvé ». Comme si j’avais demandé une faveur, et comme s’il pouvait décider où je dépenserais mon propre argent. Il m’a donné son choix à lui, pas celui que la loi prévoit aussi pour moi.',
    'Un syndic extérieur semble avoir tout mis sens dessus dessous, et peut-être pas par erreur. Des copropriétaires se taisent. Des banques jouent avec les mots, pour que l’on s’empêtre dans la querelle et non dans le fond. Même quand chacune de leurs réponses écrites ressemble à une réponse, elles ne disent pas ce qu’on leur a demandé. Et cela aussi, c’est du silence.',
    'Il y a encore un autre cas. Un voisin à Athènes m’a demandé : « veux-tu entrer dans le groupe avec les autres voisins ? », m’y a ajouté, et s’est tu avec tous les autres quand j’ai parlé à tous. Répondre à une seule personne ne coûte rien. Cela devient silence quand lui aussi a quelque chose à dire devant les autres.',
    'Et puis ce fut mon tour. J’étais déjà si las des magasins, des banques, des bureaux, de la famille, que lorsqu’un voisin du village a demandé à ma mère « comment va Ivan ? », je n’ai pas entendu une question. J’ai entendu une accusation qui exigeait une défense. Je lui ai écrit en colère et je l’ai chargé de vieilles choses qui n’étaient pas les siennes. Il m’a appelé aussitôt. Je n’ai pas décroché, parce que je ne décroche plus, même pour Dieu. Il m’a écrit, je lui ai expliqué, je lui ai demandé pardon. À la fin, il m’a écrit ce que tout être humain au monde a déjà dit :',
    '« Tu peux toujours compter sur moi, à n’importe quelle heure. »',
    'Je ne lui ai pas répondu. Je sais qu’il est un être humain. Et tout être humain a mal.',
]

DE = [
    'In diesen Wochen habe ich um vieles gebeten, und alles schriftlich, weil ich so spreche. Ich bat um Erklärungen, Dokumente, eine Rückerstattung, eine Rechenschaft. Ich bat auch um Feineres: dass mir jemand zuhört, wegen eines Werks, eines alten Papiers, einer Geschichte, die ich trage.',
    'Irgendwann begriff ich, dass ich nicht auf die Antworten warten muss, um zu wissen, von wem sie kommen werden. Es genügt zu sehen, was eine Antwort sie kosten würde.',
    'Ein Museum in Amerika leitete meinen Brief noch am selben Tag weiter. Eine Fachfrau in Frankreich, die mich nicht kannte, antwortete am nächsten. Vor zwei Jahren hatte ich einen Antiquar nach einem historischen Brief gefragt. Er antwortete förmlich, er sei verkauft. Ich schrieb ihm jetzt erneut, und er schickte mir eine Kopie davon, ohne ein Wort mehr. Ich hatte ihn nicht so darum gebeten, und es war nicht seine Pflicht. Keiner von ihnen hatte etwas vor mir zu schützen.',
    'Wo ich um Papiere bat, die etwas über den zeigen würden, der sie hält, fand ich Schweigen. Oder Schlimmeres: automatische Nachrichten, einen Anruf anstelle einer schriftlichen Antwort, ein „Ich habe keine Stimme, ich bin krank“ an jemanden, der nie darum gebeten hatte, eine Stimme zu hören.',
    'Unter ihnen gibt es auch jene, denen es einfach gleich ist, weil ein Kunde für sie ein Vorgang ist. Mein Drucker-Scanner, mit dem ich seit Monaten die Archive ganzer Leben digitalisiere, ging in der Garantiezeit kaputt. Garantie heißt kostenlose Reparatur oder Ersatz, und wenn beides nicht möglich ist, Erstattung des Geldes. Eine Gutschrift nur, wenn man sie selbst wählt. Das Geschäft schrieb mir, „eine Gutschrift wurde genehmigt“. Als hätte ich um einen Gefallen gebeten, und als könnte es bestimmen, wo ich mein eigenes Geld ausgebe. Es gab mir seine eigene Wahl, nicht die, die das Gesetz auch für mich vorsieht.',
    'Ein externer Hausverwalter scheint alles verpfuscht zu haben, und vielleicht nicht aus Versehen. Bewohner schweigen. Banken spielen mit Wörtern, damit man sich im Streit verstrickt und nicht in der Sache. Selbst wenn jede ihrer schriftlichen Erwiderungen wie eine Antwort aussieht, sagen sie nicht, wonach sie gefragt wurden. Und auch das ist Schweigen.',
    'Es gibt noch einen anderen Fall. Ein Nachbar in Athen fragte mich: „Möchtest du in die Gruppe mit den anderen Nachbarn?“, fügte mich hinzu und schwieg mit allen anderen, als ich zu allen sprach. Einem einzelnen Menschen zu antworten kostet nichts. Es wird zu Schweigen, wenn auch er vor den anderen etwas zu sagen hat.',
    'Und dann war ich an der Reihe. Ich war schon so müde von Geschäften, Banken, Ämtern, Verwandten, dass ich, als ein Nachbar im Dorf meine Mutter fragte: „Wie geht es Ivan?“, keine Frage hörte. Ich hörte eine Anklage, die eine Verteidigung verlangte. Ich schrieb ihm zornig und lud ihm alte Dinge auf, die nicht die seinen waren. Er rief mich sofort an. Ich nahm nicht ab, weil ich nicht einmal mehr für Gott abnehme. Er schrieb mir, ich erklärte es ihm, ich bat ihn um Verzeihung. Am Ende schrieb er mir etwas, das jeder Mensch auf der Welt schon gesagt hat:',
    '„Du kannst immer auf mich zählen, zu jeder Stunde.“',
    'Ich habe ihm nicht geantwortet. Ich weiß, dass er ein Mensch ist. Und jeder Mensch leidet.',
]

post = dict(
    slug='kardia-ochi-chartia',
    date='2026-11-18T21:45:00.000+02:00',
    title='Μου απαντούν όσοι έχουν καρδιά, όχι χαρτιά',
    og='og/2026/11/kardia-ochi-chartia.png',   # κάρτα κοινοποίησης: το σκίτσο, ώστε το τετράγωνο κόψιμο κρατά τον άνθρωπο και το γράμμα
    html=fig('Από απέναντι.') + body(EL),
    translations=dict(
        en=dict(slug='hearts-not-papers', title='Those who answer me have hearts, not papers',
                html=fig('From across the way.') + body(EN)),
        fr=dict(slug='des-coeurs-pas-des-papiers', title='Ceux qui me répondent ont un cœur, pas des papiers',
                html=fig('D’en face.') + body(FR)),
        de=dict(slug='herzen-nicht-papiere', title='Mir antworten die, die ein Herz haben, keine Papiere',
                html=fig('Von gegenüber.') + body(DE)),
    ),
)
out = os.path.join(ROOT, 'content', 'new-posts', '2026-11-18-kardia.json')
json.dump(post, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(out)
