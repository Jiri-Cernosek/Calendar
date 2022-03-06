# Calendar
# Planner
Můj vlastní projekt. Původní myšlenkou je přehlednější plánování podřízených mechaniků, především vizualizace adres jejich práce. 
Vizualizace pracovních cest má být na mapovém podkladě. 
Cílem není vypočítávat trasu apod., ale pouze zobrazit vlaječkou místo a následně naplánovat pořadí návštěv u zákazníků. 
Je neekonomické jezdit chaoticky sem a tam místo postupných zastávek hezky za sebou.
Aplikace na základě zadaných servisních ticketů automaticky umístí vlaječku do mapového podkladu.
Bude možnost zobrazovat místa na základě dne, mechanika, oblasti apod.

# Finder
Pro plánování servisních zakázek je potřeba si "navolat" zákazníky, většinou, když je plánovaná pouze jedna zastávka.
Např. mechanik má zakázku v Pardubicích a žádný další požadavek ze stran zákazníků není evidován.
Je vhodné si na základě oblasti vyhledat zákazníky, kterým v nejbližších dnech (týden, měsíc) končí roční revize nebo je potřeba provést roční servisní prohlídku.
Aplikace má za úkol na základě zadané obce, okresu, kraje nebo PSČ vyhledat z databáze zákazníky v okolí zadaných dat. 
Okolí bude možné určit na základě vzdálenosti, okresu nebo kraje.

Aplikace na základě vstupních dat vyhledá a definuje množinu PSČ z databáze PSČ a pomocí této množiny vyhledá odpovídající zákazníky z databáze zákazníků.
Výsledkem bude výpis zákazníků s kontaktními údaji a možností rozkliknutí detailu, který zobrazí všechna dostupná data z databáze.
