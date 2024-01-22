PROKEKTA SKAIDROJUMS:

Projekta galvenais uzdevums ir nolasīt datus no mājaslapas un pārkopēt tos excel failā sakārtotā secībā, lai tos varētu vieglāk apskatīt. Šim uzdevumam vajadzēja importēt šīs bibliotēkas - Salenium, webdriver, Service, By, time, pandas. Es izmantoju savam projektam mājaslapu ss.lv, jo es to izmantoju ikdienā un tajā ir viegli pārskatāmi dati. Pirmais solis kodam ir atvērt mājaslapu, un to ielādēt Webdriver. Nākamais solis bija navigēt mājaslapā, lai nonāktu pie izvēlētās kategorijas. Šādi izskatās soļu secība - ss.lv => mēbeles un interjers => Seifi. Lai dabūtu datus no mājaslapas, jeb web scraping es izmantoju XPATH metodi. Izmantoju inspect funkciju, lai atrastu līdzīgos elementus (tos kas atradās vienā kolonnā). Šo procesu atkārtoju ar nākamajiem elementiem, un saglabāju ražotājs_result- nosaukums, ražotājs, stavoklis un cena. Saglabāju datus excel failā izmantojot pandas bibliotēku. Koda beigās ir atrodamas galvenās komandas.

PYTHON BIBLIOTĒKAS:
1. Salenium - Es izmantoju šo bibliotēku, lai automātiski pārlūkotu internetu, un lai navigētu pa lapām.
1.1. webdriver - atbildīgs par interneta pārlūka kontroli.
1.2. Service - ļauj konfigurēt Chrome pakalpojumus.
1.3. By - izmanto lai specifisētu klasi, id, XPATH, uc.
2. Time - Šī bibliotēka ļāva man apturēt programmas kodu uz noteiktu laiku, lai ļautu mājaslapai ielādēties.
3. Pandas - Es izmantoju šo bibliotēku, lai secīgi sakārtotu datus un saglābāt tos excel failā.

PROGRAMATŪRAS IZMANTOŠANAS METODES:
1. setup_driver(): Izveido un konfigurē Chrome pārlūkprogrammu.
2. navigate_to_page(driver, url): Pārvieto pārlūkprogrammas logu uz norādīto URL un gaida 2 sekundes, lai ļautu lapai ielādēties.
3. click_element_by_id(driver, element_id): Atrod HTML elementu pēc ID un veic klikšķi uz tā, gaidot 2 sekundes.
4. scrape_data(driver): Atrod vairākus HTML elementus, izmantojot By.XPATH, un saglabā tos sarakstos.
5. save_to_excel(data, filename="projekts.xlsx"): Saglabā datus no saraksta Excel failā, izmantojot pandas bibliotēku.
6. main(): Galvenā programma, kur tiek izsauktas iepriekš minētās funkcijas secīgā secībā. Šeit ir arī try un finally bloki, lai nodrošinātu, ka pārlūkprogramma tiek pareizi aizvērta pat, ja notiek kļūda izpildes laikā.

Es pildīju darbu VS Studio un man neiet kods github.
