"""Δημοσίευση 15.11.2026: «Το χρώμα της τίγρης», με σκίτσο και μεταφράσεις."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sketch_tigri

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG = sketch_tigri.svg()


def fig(cap):
    return f'<figure class="sketch">{SVG}<figcaption>{cap}</figcaption></figure>'


def body(ps):
    return ''.join(f'<p>{p}</p>' for p in ps)


EL = [
    'Οι γονείς μου μού έλεγαν να προσέχω τους ξένους. Δεν μου είπαν να προσέχω και τους συγγενείς μου.',
    'Δύο μέρες μετά το μνημόσυνο της τελευταίας θείας μου, βρέθηκα μπροστά σε ένα γράμμα του πατέρα μου, γραμμένο το 2010 στην οικογένειά του για μένα. Δεν το αναζητούσα. Το βρήκα μέσα από μια γενικότερη αναζήτηση στην παλιά του αλληλογραφία. Είχαν περάσει δεκαέξι χρόνια από τότε που γράφτηκε και δεκατέσσερα από τον θάνατό του.',
    'Μέσα από αυτό έμαθα ότι η παρουσία μου στην οικογένεια δεν ήταν μόνο χαρά. Για κάποιους ήταν και μια απώλεια: δεν θα κληρονομούσαν εκείνοι τον άτεκνο θείο τους. Ο πατέρας μου δεν απευθύνθηκε στα αδέλφια του, αλλά σε μία από τις κόρες τους, ζητώντας της να μιλήσει στη μητέρα της και στη θεία της. Ήθελε να μη σταθούν εμπόδιο στην προσπάθειά του να νιώσω μέλος της οικογένειας, ακόμη κι όταν εκείνος δεν θα ήταν πια εκεί.',
    'Αυτό που ζητούσε ήταν η δωρεά ενός μικρού ισόγειου διαμερίσματος από τον άλλο μου θείο, εν ζωή, ώστε να μη δημιουργηθούν αμφισβητήσεις αργότερα. Ο πατέρας μου ήθελε ο Ιβάν να μη λάβει μόνο από τους γονείς του, αλλά και από τους συγγενείς του.',
    'Με το ζόρι παντρειά δεν γίνεται, Αθανασόπουλε. Αυτό θα του έλεγα, αν ήξερα τότε την αλήθεια.',
    'Η υιοθεσία μου είχε ολοκληρωθεί κανονικά. Είχε γίνει, όμως, έναν χρόνο πριν αλλάξει ο νόμος, με τον οποίο τα παιδιά που υιοθετούνταν αποκτούσαν πλέον συγγένεια και με την υπόλοιπη οικογένεια. Έτσι, ενώ ήμουν παιδί των γονιών μου, δεν είχα την ίδια νομική συγγένεια με τα αδέλφια τους και τις οικογένειές τους. Αυτό έμαθα από το γράμμα. Δεν ήταν μόνο ότι η θέση μου ήταν διαφορετική από εκείνη που πίστευα. Ήταν ότι κάποιοι γνώριζαν αυτή τη διαφορά, ενώ εγώ όχι.',
    'Για χρόνια έζησα τη σιωπή και τη σκληρότητα της ανιψιάς του θείου μου χωρίς να καταλαβαίνω από πού προέρχονταν. Μου έλεγαν να είμαι ευγνώμων, ενώ δεν είχα ζητήσει τίποτα. Μου καλλιεργούσαν την ιδέα ότι ήμουν κληρονόμος και ότι είχα υποχρεώσεις απέναντί τους, ενώ γνώριζαν τη διαφορετική νομική μου θέση. Εκείνοι υπολόγιζαν τι θα απέμενε από τα χρήματα του θείου μου. Εγώ έμενα κοντά του και τον φρόντιζα, για να έχει έναν άνθρωπο δίπλα του και να μη μείνει μόνος.',
    'Πέθανε και η τελευταία αδελφή. Μόνο τότε έμαθα την αλήθεια για όλους τους. Δεν υπήρχε πια κανείς από εκείνη τη γενιά για να ρωτήσω τι γνώριζε, τι είχε συμβεί, τι είχε ειπωθεί και τι είχε αποφασιστεί πριν από μένα.',
    'Η τίγρη έχει το χρώμα της φύσης γύρω της. Οι ρίγες της την κάνουν δυσδιάκριτη μέσα στη βλάστηση. Το θήραμά της μπορεί να βρίσκεται κοντά της και να μην την αναγνωρίζει.',
    'Κι εγώ δεν αναγνώρισα αυτό που συνέβαινε, γιατί εκείνοι έμοιαζαν με οικογένεια. Το χρώμα τους ήταν οι λέξεις της συγγένειας: «είμαστε όλοι ανίψια του θείου», «να είσαι ευγνώμων», «έχεις κι εσύ υποχρέωση, αφού είσαι κληρονόμος». Δεν γνώριζα ότι πίσω από αυτές τις λέξεις υπήρχε μια διαφορά που οι άλλοι γνώριζαν. Δεν μπορούσα να τη δω, επειδή κανείς δεν μου την είχε δείξει.',
    'Η τίγρη δεν διάλεξε τις ρίγες της, ούτε μακιγιάρεται για να βγει από τη φωλιά της. Είναι το σώμα της. Πεινάει, κρύβεται, τρώει, και δεν φταίει. Ο άνθρωπος διαλέγει το χρώμα του. Μπορεί να μιλήσει και σωπαίνει. Μπορεί να πει την αλήθεια για τη συγγένεια και λέει μόνο τις λέξεις της. Γι\' αυτό η μοχθηρία δεν υπάρχει στη φύση. Υπάρχει μόνο εκεί όπου υπάρχει επιλογή.',
    'Το γράμμα του πατέρα μου είχε θέμα «Για βοήθεια». Δεν ήταν καταγγελία. Ήταν μια έκκληση προς συγκεκριμένους ανθρώπους να βοηθήσουν το παιδί του να βρει τη θέση του στην οικογένεια. Και ήξερε. Η άλλη θεία είχε κι εκείνη κόρη, με τα ίδια δικαιώματα. Σε εκείνη δεν απευθύνθηκε. Δεν την αναφέρει καν. Δεν έγραψε το χρώμα. Το έδειξε.',
    'Δεκαέξι χρόνια αργότερα, η βοήθεια έφτασε σε μένα από το ίδιο το γράμμα. Όχι από εκείνους στους οποίους είχε απευθυνθεί. Ο πατέρας μου δεν ήταν πια εδώ για να μου εξηγήσει. Και οι άνθρωποι που θα μπορούσαν να απαντήσουν είχαν φύγει.',
    'Οι λέξεις μπορεί να φτάνουν. Η πρόθεση όμως είναι πάντα του ανθρώπου.',
    'Η τίγρη δεν χρειάζεται να απολογηθεί για το χρώμα της. Εγώ χρειάστηκε να περιμένω να πεθάνουν όλοι για να μάθω τι έκρυβε το χρώμα εκείνων που αποκαλούσα συγγενείς μου.',
]

EN = [
    'My parents told me to beware of strangers. They did not tell me to beware of my relatives as well.',
    'Two days after the memorial service for my last aunt, I came upon a letter from my father, written in 2010 to his family about me. I was not looking for it. I found it during a broader search through his old correspondence. Sixteen years had passed since it was written, and fourteen since his death.',
    'Through it I learned that my presence in the family had not been only a joy. For some it was also a loss: they would not be the ones to inherit their childless uncle. My father did not turn to his siblings but to one of their daughters, asking her to speak to her mother and her aunt. He wanted them not to stand in the way of his effort to make me feel a member of the family, even when he would no longer be there.',
    'What he asked for was the donation, during his lifetime, of a small ground-floor flat from my other uncle, so that no disputes would arise later. My father wanted Ivan to receive not only from his parents, but from his relatives as well.',
    'You cannot force a marriage, Athanasopoulos. That is what I would have told him, had I known the truth then.',
    'My adoption had been completed properly. It had taken place, however, one year before the law changed, the law by which adopted children came to be related to the rest of the family as well. So, although I was my parents’ child, I did not have the same legal kinship with their siblings and their families. That is what I learned from the letter. It was not only that my position was different from what I had believed. It was that some people knew of this difference, while I did not.',
    'For years I lived with the silence and the harshness of my uncle’s niece without understanding where they came from. I was told to be grateful, though I had asked for nothing. They cultivated in me the idea that I was an heir and that I had obligations towards them, while they knew my different legal position. They were calculating what would be left of my uncle’s money. I stayed near him and looked after him, so that he would have someone beside him and would not be left alone.',
    'The last sister died as well. Only then did I learn the truth about all of them. There was no one left from that generation whom I could ask what they knew, what had happened, what had been said and what had been decided before me.',
    'The tiger has the colour of the nature around it. Its stripes make it hard to make out among the vegetation. Its prey may be close to it and not recognise it.',
    'Nor did I recognise what was happening, because they looked like family. Their colour was the words of kinship: “we are all the uncle’s nephews and nieces”, “be grateful”, “you have an obligation too, since you are an heir”. I did not know that behind these words lay a difference the others knew. I could not see it, because no one had shown it to me.',
    'The tiger did not choose its stripes, nor does it put on make-up to leave its lair. They are its body. It is hungry, it hides, it eats, and it is not to blame. Man chooses his colour. He can speak, and he keeps silent. He can tell the truth about kinship, and he says only its words. That is why malice does not exist in nature. It exists only where there is choice.',
    'The subject line of my father’s letter was “For help”. It was not an accusation. It was an appeal to particular people to help his child find his place in the family. And he knew. The other aunt had a daughter too, with the same rights. He did not write to her. He does not even mention her. He did not write the colour down. He pointed to it.',
    'Sixteen years later, the help reached me from the letter itself. Not from those to whom it had been addressed. My father was no longer here to explain it to me. And the people who could have answered were gone.',
    'Words may be enough. The intention, though, always belongs to the human being.',
    'The tiger need not apologise for its colour. I had to wait for all of them to die to learn what the colour of those I called my relatives was hiding.',
]

FR = [
    'Mes parents me disaient de me méfier des étrangers. Ils ne m’ont pas dit de me méfier aussi de ma famille.',
    'Deux jours après la commémoration de ma dernière tante, je me suis trouvé devant une lettre de mon père, écrite en 2010 à sa famille à mon sujet. Je ne la cherchais pas. Je l’ai trouvée au cours d’une recherche plus générale dans sa vieille correspondance. Seize ans s’étaient écoulés depuis qu’elle avait été écrite, et quatorze depuis sa mort.',
    'J’y ai appris que ma présence dans la famille n’avait pas été seulement une joie. Pour certains, elle était aussi une perte : ce ne seraient pas eux qui hériteraient de leur oncle sans enfants. Mon père ne s’est pas adressé à ses frères et sœurs, mais à l’une de leurs filles, en lui demandant de parler à sa mère et à sa tante. Il voulait qu’ils ne fassent pas obstacle à ses efforts pour que je me sente membre de la famille, même quand il ne serait plus là.',
    'Ce qu’il demandait, c’était la donation, de son vivant, d’un petit appartement en rez-de-chaussée par mon autre oncle, afin qu’aucune contestation ne survienne plus tard. Mon père voulait qu’Ivan ne reçoive pas seulement de ses parents, mais aussi de sa famille.',
    'On ne force pas un mariage, Athanassopoulos. C’est ce que je lui aurais dit, si j’avais su alors la vérité.',
    'Mon adoption s’était faite en bonne et due forme. Elle avait eu lieu, pourtant, un an avant que la loi ne change, la loi par laquelle les enfants adoptés devenaient parents aussi du reste de la famille. Ainsi, alors que j’étais l’enfant de mes parents, je n’avais pas la même parenté légale avec leurs frères et sœurs et leurs familles. Voilà ce que j’ai appris par la lettre. Ce n’était pas seulement que ma place était différente de celle que je croyais. C’était que certains connaissaient cette différence, et moi non.',
    'Pendant des années, j’ai vécu le silence et la dureté de la nièce de mon oncle sans comprendre d’où ils venaient. On me disait d’être reconnaissant, alors que je n’avais rien demandé. On cultivait en moi l’idée que j’étais héritier et que j’avais des obligations envers eux, alors qu’on connaissait ma situation légale différente. Eux calculaient ce qui resterait de l’argent de mon oncle. Moi, je restais près de lui et je prenais soin de lui, pour qu’il ait quelqu’un à ses côtés et ne reste pas seul.',
    'La dernière sœur est morte à son tour. C’est seulement alors que j’ai appris la vérité sur eux tous. Il ne restait plus personne de cette génération à qui demander ce qu’on savait, ce qui s’était passé, ce qui s’était dit et ce qui avait été décidé avant moi.',
    'Le tigre a la couleur de la nature qui l’entoure. Ses rayures le rendent difficile à distinguer dans la végétation. Sa proie peut se trouver tout près de lui sans le reconnaître.',
    'Moi non plus, je n’ai pas reconnu ce qui se passait, parce qu’ils ressemblaient à une famille. Leur couleur, c’étaient les mots de la parenté : « nous sommes tous les neveux de l’oncle », « sois reconnaissant », « toi aussi tu as une obligation, puisque tu es héritier ». Je ne savais pas que derrière ces mots se trouvait une différence que les autres connaissaient. Je ne pouvais pas la voir, parce que personne ne me l’avait montrée.',
    'Le tigre n’a pas choisi ses rayures, et il ne se maquille pas pour sortir de sa tanière. Elles sont son corps. Il a faim, il se cache, il mange, et il n’est pas coupable. L’homme choisit sa couleur. Il peut parler, et il se tait. Il peut dire la vérité sur la parenté, et il n’en dit que les mots. C’est pourquoi la méchanceté n’existe pas dans la nature. Elle n’existe que là où il y a un choix.',
    'La lettre de mon père avait pour objet « Pour de l’aide ». Ce n’était pas une accusation. C’était un appel à des personnes précises pour qu’elles aident son enfant à trouver sa place dans la famille. Et il savait. L’autre tante avait elle aussi une fille, avec les mêmes droits. Il ne s’est pas adressé à elle. Il ne la mentionne même pas. Il n’a pas écrit la couleur. Il l’a montrée.',
    'Seize ans plus tard, l’aide m’est parvenue de la lettre elle-même. Pas de ceux à qui elle avait été adressée. Mon père n’était plus là pour me l’expliquer. Et ceux qui auraient pu répondre étaient partis.',
    'Les mots peuvent suffire. L’intention, pourtant, appartient toujours à l’homme.',
    'Le tigre n’a pas à s’excuser de sa couleur. Moi, j’ai dû attendre qu’ils meurent tous pour apprendre ce que cachait la couleur de ceux que j’appelais ma famille.',
]

DE = [
    'Meine Eltern sagten mir, ich solle mich vor Fremden in Acht nehmen. Sie sagten mir nicht, ich solle mich auch vor meinen Verwandten in Acht nehmen.',
    'Zwei Tage nach der Gedenkfeier für meine letzte Tante stand ich vor einem Brief meines Vaters, 2010 an seine Familie über mich geschrieben. Ich habe ihn nicht gesucht. Ich fand ihn bei einer allgemeineren Suche in seiner alten Korrespondenz. Sechzehn Jahre waren vergangen, seit er geschrieben wurde, und vierzehn seit seinem Tod.',
    'Durch ihn erfuhr ich, dass meine Anwesenheit in der Familie nicht nur Freude gewesen war. Für manche war sie auch ein Verlust: Nicht sie würden ihren kinderlosen Onkel beerben. Mein Vater wandte sich nicht an seine Geschwister, sondern an eine ihrer Töchter und bat sie, mit ihrer Mutter und ihrer Tante zu sprechen. Er wollte, dass sie seinem Bemühen nicht im Weg stünden, mich als Mitglied der Familie fühlen zu lassen, auch wenn er nicht mehr da sein würde.',
    'Worum er bat, war die Schenkung einer kleinen Erdgeschosswohnung durch meinen anderen Onkel, zu Lebzeiten, damit später keine Anfechtungen entstünden. Mein Vater wollte, dass Ivan nicht nur von seinen Eltern empfange, sondern auch von seinen Verwandten.',
    'Mit Gewalt wird keine Ehe, Athanasopoulos. Das hätte ich ihm gesagt, hätte ich damals die Wahrheit gekannt.',
    'Meine Adoption war ordnungsgemäß abgeschlossen worden. Sie hatte jedoch ein Jahr vor der Änderung des Gesetzes stattgefunden, durch das adoptierte Kinder fortan auch mit der übrigen Familie verwandt wurden. So war ich zwar das Kind meiner Eltern, hatte aber nicht dieselbe rechtliche Verwandtschaft mit ihren Geschwistern und deren Familien. Das erfuhr ich aus dem Brief. Es war nicht nur, dass meine Stellung eine andere war, als ich geglaubt hatte. Es war, dass manche diesen Unterschied kannten und ich nicht.',
    'Jahrelang erlebte ich das Schweigen und die Härte der Nichte meines Onkels, ohne zu verstehen, woher sie kamen. Man sagte mir, ich solle dankbar sein, obwohl ich um nichts gebeten hatte. Man pflegte in mir die Vorstellung, ich sei Erbe und hätte ihnen gegenüber Pflichten, während man um meine andere rechtliche Stellung wusste. Sie rechneten aus, was vom Geld meines Onkels übrig bleiben würde. Ich blieb in seiner Nähe und kümmerte mich um ihn, damit er einen Menschen an seiner Seite hatte und nicht allein blieb.',
    'Auch die letzte Schwester starb. Erst dann erfuhr ich die Wahrheit über sie alle. Es gab niemanden mehr aus jener Generation, den ich hätte fragen können, was man wusste, was geschehen war, was gesagt und was vor mir entschieden worden war.',
    'Der Tiger hat die Farbe der Natur um ihn herum. Seine Streifen machen ihn im Gewächs schwer erkennbar. Seine Beute kann ganz in seiner Nähe sein und ihn nicht erkennen.',
    'Auch ich erkannte nicht, was geschah, denn sie sahen aus wie Familie. Ihre Farbe waren die Wörter der Verwandtschaft: „Wir sind alle Neffen und Nichten des Onkels“, „sei dankbar“, „auch du hast eine Pflicht, du bist ja Erbe“. Ich wusste nicht, dass hinter diesen Wörtern ein Unterschied lag, den die anderen kannten. Ich konnte ihn nicht sehen, weil ihn mir niemand gezeigt hatte.',
    'Der Tiger hat seine Streifen nicht gewählt, und er schminkt sich nicht, um aus seinem Lager zu kommen. Sie sind sein Körper. Er hungert, er versteckt sich, er frisst, und er ist nicht schuld. Der Mensch wählt seine Farbe. Er kann sprechen und schweigt. Er kann die Wahrheit über die Verwandtschaft sagen und sagt nur ihre Wörter. Darum gibt es Bosheit in der Natur nicht. Es gibt sie nur dort, wo es eine Wahl gibt.',
    'Der Brief meines Vaters hatte den Betreff „Um Hilfe“. Er war keine Anklage. Er war ein Appell an bestimmte Menschen, seinem Kind zu helfen, seinen Platz in der Familie zu finden. Und er wusste es. Die andere Tante hatte ebenfalls eine Tochter, mit denselben Rechten. An sie wandte er sich nicht. Er erwähnt sie nicht einmal. Er hat die Farbe nicht aufgeschrieben. Er hat auf sie gezeigt.',
    'Sechzehn Jahre später erreichte mich die Hilfe aus dem Brief selbst. Nicht von denen, an die er gerichtet war. Mein Vater war nicht mehr da, um es mir zu erklären. Und die Menschen, die hätten antworten können, waren gegangen.',
    'Die Wörter mögen genügen. Die Absicht aber gehört immer dem Menschen.',
    'Der Tiger muss sich für seine Farbe nicht entschuldigen. Ich musste warten, bis sie alle gestorben waren, um zu erfahren, was die Farbe derer verbarg, die ich meine Verwandten nannte.',
]

post = dict(
    slug='to-chroma-tis-tigris',
    date='2026-11-15T19:30:00.000+02:00',
    title='Το χρώμα της τίγρης',
    html=fig('Δεν έγραψε το χρώμα. Το έδειξε.') + body(EL),
    translations=dict(
        en=dict(slug='the-colour-of-the-tiger', title='The colour of the tiger',
                html=fig('He did not write the colour down. He pointed to it.') + body(EN)),
        fr=dict(slug='la-couleur-du-tigre', title='La couleur du tigre',
                html=fig('Il n’a pas écrit la couleur. Il l’a montrée.') + body(FR)),
        de=dict(slug='die-farbe-des-tigers', title='Die Farbe des Tigers',
                html=fig('Er hat die Farbe nicht aufgeschrieben. Er hat auf sie gezeigt.') + body(DE)),
    ),
)
out = os.path.join(ROOT, 'content', 'new-posts', '2026-11-15-tigri.json')
json.dump(post, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(out)
