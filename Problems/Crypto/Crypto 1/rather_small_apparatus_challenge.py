from Crypto.Util.number import getPrime


def generate_challenge(flag):
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q

    e = 0x10001

    c = []
    for char in flag:
        c.append(pow(ord(char), e, n))

    with open("rational_security_adjustment.txt", 'w') as f:
        f.write(f"n={n}\ne={e}\nc={c}\n")

'''
output
n=23918323783201783592301552875422005416512375700821686720680497813403457434212512089991089307959580661251176075538399013711982403636976357436702299722578838423223706141945543400877405821040977835826292367657772848849402629095589981952987868490675315686746150795534900276931235617207484940865873545443176457269335251201093192853074551308603027327410728242701464438305796468397027872659995423203337847848597799067003736792160564357148222181643276956864096543868069315064565291619299852707266131398099958914990118767502124313326749672791201979669578798181163768273559746391469503666995897735658311717712406317794209111893
e=65537
c=[20831444646471245558214361629836687962309810223852878528004068473800511650969964780856836758305632800198989587865909145314925031872071585405223044224874662214651407061117330972603509623628193572840431530743712358136027890768398860123206910622599303677987200857472356685168223371080741531703137111583226314496663867807880721571400651635995774931638220799790447332198248202969124173304339960871085197738253144327363679198172333443548223546949950905883491862937993092489527269492136049391486990441756673931792177751340407333258148344981513088838110979772856808841070511743080780088611622463292884202055950777410156915382, 1097348292307128879823779707039818502136010223518168760922049547858226743860217433906385587444422094590606257499943569601115666832782334959226410208077558212554864366119912843277951503586729546476567505821206462132951748396959704395396592958053859394861816038395492303852504990747835859711696829867659680960081822576973836487811489365581654037087846857255799214558489550500354924067719727771263895107267802465099775923196032736701225166566762341903373057574678869103433814248286201138427141570403847801987566553626285413520105462699843992246446227540931239934952057690474836418564494234314452951972427048800962871922, 21202844801402136038352119446424092455866253014000697343341909479447787177544506118889262865075270094553150816063813837615235188182198685732866552127817888741380965273353384727056967274286013776231277876096221604495787339246750177700519027713707179193341543487649190348592716119360984416904534716054066108756810473683119207067372245169091581667640047925542085997810879619737460597398306694599394315094088911128453036238429364450159471783387648572993891718699530892286145856444346652085019036261083866394340634190681176058460660774753969697059554889932550675406172694862072350863146770051660593374837848143819391257778, 21202844801402136038352119446424092455866253014000697343341909479447787177544506118889262865075270094553150816063813837615235188182198685732866552127817888741380965273353384727056967274286013776231277876096221604495787339246750177700519027713707179193341543487649190348592716119360984416904534716054066108756810473683119207067372245169091581667640047925542085997810879619737460597398306694599394315094088911128453036238429364450159471783387648572993891718699530892286145856444346652085019036261083866394340634190681176058460660774753969697059554889932550675406172694862072350863146770051660593374837848143819391257778, 15312365422849438966393153549806195628840236746563317402304711515713593526509553039249369817271127155609515147144844582726847663123094396507556432905888288269333548404961635374808388515728327970038429878551109336017678132557571146062572272506322167412775826634103405338327689838083762762897263244744440198524401094321457350698033064669875480174092492747455163323450184393515970231956740661506405610644579143262330453442839843419027629484833162453962818265312847997880957057770297137115276900977025668480233916010485938146978180560750409564796278695493868907557739238399624856612031523869987327483779518947255417921922, 7782824589572789101004942640086027817826692303273118160076282972929809938180500258819728182748746825199819215006139077056940355976658818925491348247918416376881921706487784848816482055610950351214206722976330372084626335777395965365740807014301505818286909492214029983473376313427235455784028400416343522559722281240895993088918279186160239291517913275984279595981049578288070253627616170816473993397417674443741490722629661044506878440814238382677177761001782911600898151670106315178346296573775080506159021898408225261183532054733491511586398380693261407098018831464679933036854017543224575766538907866530927256599, 4521141175608997270154067455189713945676815318686545079148761488047981769208804758174261888239279708309205828485458650317746021051074214298317714178771588407094620088079227648555531806429506072785325363802181486333600444680193622786528938032096559365888874143356898074623781816428371952768365949735419551390292817000897717317508790568153354308998810693872644557751781104246206682939052330251023148213832705670617404989072186655833154202641570935229213448805084253704550592677663282782823073673705663205002292632421859224580660652376551085167692349639886056302426576578394409288176958888003801420557805403452683855320, 22630408637178910336078149804790772477162661003464143477659559809606569844082498279081572042697181913270227548993895930733573210670164393269934684457370200172712657178446265813181026408207044747600803345912045739737373606421384194066243289785559627934394033946505259608780697360035571807137605959935922987393195178081525069096404088909987240905526664847290937689115460320131778415594286052690575761890573259657360139843804042964145162030772686906270448637155647065522169261051099324730006171885035147264274213888846793867928111091875210570579302535048101327733041854435457334935472989211850928514343502939275848956503, 19271835951614781719846899541007721519258056045649784169308864887984962100475810141529455485545422206155513402142951939893877585871964655990590750938835400744088060885098727532121174001784183090238141194244172556231993187056110285158882446944629890633725018811891837830742967697127998034762247687380885254705887494087403346526021548997517293226749613577342642566880821446537528775701108814456913487357094810949012938356060543710261433581262682986190664231673332134149855476180229500798453724804771736654239474061599170204568369451161797028615456957676422053013909833282388019750846351907069809784944068572587886103804, 7534856991221851484255326394983261708152772426501509591646488617784815155227143918109718682064493274428189064662804866411906843116755261798720958796179702427185260354022172049035341987960743055856718450238305210714340816922201660005419259431521311473574874992215926640618863151320704686238955931817706080392732819737023385135240692221399192122081021994939215302016008211087005668258718008890702969025829552555416314030013916522980580485436345197164286224944760475445578761218429968028316731641827892113690268562701162190985058517726445453989956860286182189699103379283862460892444597420165044977441330724725483957029, 4521141175608997270154067455189713945676815318686545079148761488047981769208804758174261888239279708309205828485458650317746021051074214298317714178771588407094620088079227648555531806429506072785325363802181486333600444680193622786528938032096559365888874143356898074623781816428371952768365949735419551390292817000897717317508790568153354308998810693872644557751781104246206682939052330251023148213832705670617404989072186655833154202641570935229213448805084253704550592677663282782823073673705663205002292632421859224580660652376551085167692349639886056302426576578394409288176958888003801420557805403452683855320, 4708314618979803203692946904847162207492836265107184001979539861813316701228298205765248972708885737347463589230850828006461016568327947028344362539342154159948022980689438395094689830895065615036068596509836053090916490188353277762423098429251988308239298882151316156081393237580053696662664356353723249629187564650764103343620120936452516606643306709236055696517938065861902935315666052762019985421323559529546698156332651347774484936511717826466828762765259901785049775631059068855865971169193423707795617647657177858809423726047347533240572576631762081859949413055145780320338747299543439441667260654657536414834, 3706373666334832124603978901043134659621959013512162651459857335191661034730596432715603582800418931644875996336917915669189522679240020741753180949947097302439432114346613403216094635122853658333306495860859112920224167013970018766168174999708757635055832753333075129301525462541404505866176256610356863329312707920425328621605687222200386715779334693561943344437787669181888161321490579875857103645489049903693701530463942555440248430543681147983960650444978063274921773345197139176563039589346885992519099054290494199882489445669786605589199730248319392003465885434102866734610810044197557269709716751604980499476, 19271835951614781719846899541007721519258056045649784169308864887984962100475810141529455485545422206155513402142951939893877585871964655990590750938835400744088060885098727532121174001784183090238141194244172556231993187056110285158882446944629890633725018811891837830742967697127998034762247687380885254705887494087403346526021548997517293226749613577342642566880821446537528775701108814456913487357094810949012938356060543710261433581262682986190664231673332134149855476180229500798453724804771736654239474061599170204568369451161797028615456957676422053013909833282388019750846351907069809784944068572587886103804, 13067402761740335161364258055850271441888360895824272970778956723336359629158216080429514556849158958559034850403357268081705428381013969267864155642649463974762777459371189314211191371079777821559021831462324760486814757027129092326679487003072923192948087379742572312127195439163244663854156154399900695413906372193509565797851869152773484019225815811206481270749086812859368508014415946533998179988559857504293920595413628599013332707852112836961013011776404750782743497151814501642329380845514367461417507359700916038221141372806974373715120725996620987201981201862080819204231560333360358877312956996689255714004, 21202844801402136038352119446424092455866253014000697343341909479447787177544506118889262865075270094553150816063813837615235188182198685732866552127817888741380965273353384727056967274286013776231277876096221604495787339246750177700519027713707179193341543487649190348592716119360984416904534716054066108756810473683119207067372245169091581667640047925542085997810879619737460597398306694599394315094088911128453036238429364450159471783387648572993891718699530892286145856444346652085019036261083866394340634190681176058460660774753969697059554889932550675406172694862072350863146770051660593374837848143819391257778, 6389830608423643625454516327879640294979656037702609295809841732875648681221700358218124618620408917122654976585529755931605532377688719892471655322118127274129760486775640100749623946707073761225435800309040691497039223562524465877825209799142784083262087888933183344833121052467129790509997957459916752481359560418549141232810852694233755740185662147731119972307738072327959133883700892898243621611814891357440047465931674801531282222852477116554773492902059954409357142114375040107985942414762226924993101700126829938764498987141064182660362845605504710000129068279175716137758480210491545527316279500062476753366, 4521141175608997270154067455189713945676815318686545079148761488047981769208804758174261888239279708309205828485458650317746021051074214298317714178771588407094620088079227648555531806429506072785325363802181486333600444680193622786528938032096559365888874143356898074623781816428371952768365949735419551390292817000897717317508790568153354308998810693872644557751781104246206682939052330251023148213832705670617404989072186655833154202641570935229213448805084253704550592677663282782823073673705663205002292632421859224580660652376551085167692349639886056302426576578394409288176958888003801420557805403452683855320, 15647690245657011298210401807006970580456083914063968759592765606320364018599300313959239965595937612338196578302801680308797305624762469398989142141613452356442476818650874511879302153453699039217174675789857741268233075198046767842347143428272950554930266977887788935392262497492641547766540034798641948769051189342928101819226388401692679796610661794344063798901504351131180258814410279355531799858649467723999422277188100027728465115214450227158187000680148595634058397963108230625472835971787418323033619670035634061740941826784942067975557605518452657495875414860982135323640606847671300939980040097112705928989, 23433614843771357016381709927985576290351647438026234117730641376630088752810572693604128055000624301227067264019398401451650130117500498388964123176460377695411895581073996352745794480675520838675322787373444350790957407101625180381154480652626058836547009862308280635004708207909570171716160826989534054670491595937735395818003372719917854410888944718780123501864288706980465145468865300295400035040737961856397333777953684479106074973099483234627011932718047633598042532310746246618542151408314481321584543442724397027333310072920249411880199587622571137534094634225983896964191991205626627420952580226122437057772, 4708314618979803203692946904847162207492836265107184001979539861813316701228298205765248972708885737347463589230850828006461016568327947028344362539342154159948022980689438395094689830895065615036068596509836053090916490188353277762423098429251988308239298882151316156081393237580053696662664356353723249629187564650764103343620120936452516606643306709236055696517938065861902935315666052762019985421323559529546698156332651347774484936511717826466828762765259901785049775631059068855865971169193423707795617647657177858809423726047347533240572576631762081859949413055145780320338747299543439441667260654657536414834, 13067402761740335161364258055850271441888360895824272970778956723336359629158216080429514556849158958559034850403357268081705428381013969267864155642649463974762777459371189314211191371079777821559021831462324760486814757027129092326679487003072923192948087379742572312127195439163244663854156154399900695413906372193509565797851869152773484019225815811206481270749086812859368508014415946533998179988559857504293920595413628599013332707852112836961013011776404750782743497151814501642329380845514367461417507359700916038221141372806974373715120725996620987201981201862080819204231560333360358877312956996689255714004, 14366952524551465080777190431352141309028885653755273162078163904707811991715519095439875462669063825307551853893677013569627602417703605369760725221485620647314820166891494013115583225351387614037779148132728133545482681511960896013682089391161675716238603493017528125896550908000655936724722176990063489813278581335478378250549122708634129056672898411867742306602541403288969283281184122628557093424990183523804404074556307889678642864002382355658137479815570661790921677231617247896702130559775478520597264524817653027951857956102578140500818960987297413547661367302858012881506673924763114265066298290111521395807, 15797328485413319584910252307769002642195894485809757869799751009153371424217673230778156800964873122141122568931216861879838261389342761858270339016521736410732769811733567255764453049593369396392413530955946682195991231142698027771823541877253461494115257722889070027996381309775594798272595588425109040240369078903351711037016564584369038024416442093364971473201914371721313870855118992256211975378725848631994214696733993219223580372140205152934432508443567889518024585474385654627318632216280662141049938931876484788122214044198015713238794284395468246210606871620973038690406985389677883074345449433937143229983, 13067402761740335161364258055850271441888360895824272970778956723336359629158216080429514556849158958559034850403357268081705428381013969267864155642649463974762777459371189314211191371079777821559021831462324760486814757027129092326679487003072923192948087379742572312127195439163244663854156154399900695413906372193509565797851869152773484019225815811206481270749086812859368508014415946533998179988559857504293920595413628599013332707852112836961013011776404750782743497151814501642329380845514367461417507359700916038221141372806974373715120725996620987201981201862080819204231560333360358877312956996689255714004, 16500470912652282855972311680626054621875782495397433291078007324308049526625028078804041256074957478111712807698532540970592194794664604933467460280166566478734155002372631857221470481934544359332120565901965210820799903333727071675893620468642428750721248108347422801980681531677141664374592203184980071632682927174286514027509082034993139069296382591326069930333135749500701655069398387884267275674124545196257409972983519806680278022888739021636466435770065836374493442552036843596557646255271188206604928514319010639307239898378611822945291239992761886751837546511655617572154123854028386476210632902305719450511, 15797328485413319584910252307769002642195894485809757869799751009153371424217673230778156800964873122141122568931216861879838261389342761858270339016521736410732769811733567255764453049593369396392413530955946682195991231142698027771823541877253461494115257722889070027996381309775594798272595588425109040240369078903351711037016564584369038024416442093364971473201914371721313870855118992256211975378725848631994214696733993219223580372140205152934432508443567889518024585474385654627318632216280662141049938931876484788122214044198015713238794284395468246210606871620973038690406985389677883074345449433937143229983, 6389830608423643625454516327879640294979656037702609295809841732875648681221700358218124618620408917122654976585529755931605532377688719892471655322118127274129760486775640100749623946707073761225435800309040691497039223562524465877825209799142784083262087888933183344833121052467129790509997957459916752481359560418549141232810852694233755740185662147731119972307738072327959133883700892898243621611814891357440047465931674801531282222852477116554773492902059954409357142114375040107985942414762226924993101700126829938764498987141064182660362845605504710000129068279175716137758480210491545527316279500062476753366, 12353057889329692397652864117072844642193561369068553933205322405708023176639061621165812173193141524258143497885495837782902908333793102896145156943231582500888798054118785027183093137927706594156414685552991971468987658979992102110235362679667841353261214403908164904417581879709710479888618847072584482551577495531831881025462843394181256623684292413799385645785537699952416304437234388427199114992287153874674363529226122725771761101409914696175687698147261571549249756869412062081000265168203573499265800836519696415658320124635244813274498454331514075455059766591093115736673123551530324409090324845866576288908, 15797328485413319584910252307769002642195894485809757869799751009153371424217673230778156800964873122141122568931216861879838261389342761858270339016521736410732769811733567255764453049593369396392413530955946682195991231142698027771823541877253461494115257722889070027996381309775594798272595588425109040240369078903351711037016564584369038024416442093364971473201914371721313870855118992256211975378725848631994214696733993219223580372140205152934432508443567889518024585474385654627318632216280662141049938931876484788122214044198015713238794284395468246210606871620973038690406985389677883074345449433937143229983, 15797328485413319584910252307769002642195894485809757869799751009153371424217673230778156800964873122141122568931216861879838261389342761858270339016521736410732769811733567255764453049593369396392413530955946682195991231142698027771823541877253461494115257722889070027996381309775594798272595588425109040240369078903351711037016564584369038024416442093364971473201914371721313870855118992256211975378725848631994214696733993219223580372140205152934432508443567889518024585474385654627318632216280662141049938931876484788122214044198015713238794284395468246210606871620973038690406985389677883074345449433937143229983, 12353057889329692397652864117072844642193561369068553933205322405708023176639061621165812173193141524258143497885495837782902908333793102896145156943231582500888798054118785027183093137927706594156414685552991971468987658979992102110235362679667841353261214403908164904417581879709710479888618847072584482551577495531831881025462843394181256623684292413799385645785537699952416304437234388427199114992287153874674363529226122725771761101409914696175687698147261571549249756869412062081000265168203573499265800836519696415658320124635244813274498454331514075455059766591093115736673123551530324409090324845866576288908, 4521141175608997270154067455189713945676815318686545079148761488047981769208804758174261888239279708309205828485458650317746021051074214298317714178771588407094620088079227648555531806429506072785325363802181486333600444680193622786528938032096559365888874143356898074623781816428371952768365949735419551390292817000897717317508790568153354308998810693872644557751781104246206682939052330251023148213832705670617404989072186655833154202641570935229213448805084253704550592677663282782823073673705663205002292632421859224580660652376551085167692349639886056302426576578394409288176958888003801420557805403452683855320, 22630408637178910336078149804790772477162661003464143477659559809606569844082498279081572042697181913270227548993895930733573210670164393269934684457370200172712657178446265813181026408207044747600803345912045739737373606421384194066243289785559627934394033946505259608780697360035571807137605959935922987393195178081525069096404088909987240905526664847290937689115460320131778415594286052690575761890573259657360139843804042964145162030772686906270448637155647065522169261051099324730006171885035147264274213888846793867928111091875210570579302535048101327733041854435457334935472989211850928514343502939275848956503, 6389830608423643625454516327879640294979656037702609295809841732875648681221700358218124618620408917122654976585529755931605532377688719892471655322118127274129760486775640100749623946707073761225435800309040691497039223562524465877825209799142784083262087888933183344833121052467129790509997957459916752481359560418549141232810852694233755740185662147731119972307738072327959133883700892898243621611814891357440047465931674801531282222852477116554773492902059954409357142114375040107985942414762226924993101700126829938764498987141064182660362845605504710000129068279175716137758480210491545527316279500062476753366, 12353057889329692397652864117072844642193561369068553933205322405708023176639061621165812173193141524258143497885495837782902908333793102896145156943231582500888798054118785027183093137927706594156414685552991971468987658979992102110235362679667841353261214403908164904417581879709710479888618847072584482551577495531831881025462843394181256623684292413799385645785537699952416304437234388427199114992287153874674363529226122725771761101409914696175687698147261571549249756869412062081000265168203573499265800836519696415658320124635244813274498454331514075455059766591093115736673123551530324409090324845866576288908, 13067402761740335161364258055850271441888360895824272970778956723336359629158216080429514556849158958559034850403357268081705428381013969267864155642649463974762777459371189314211191371079777821559021831462324760486814757027129092326679487003072923192948087379742572312127195439163244663854156154399900695413906372193509565797851869152773484019225815811206481270749086812859368508014415946533998179988559857504293920595413628599013332707852112836961013011776404750782743497151814501642329380845514367461417507359700916038221141372806974373715120725996620987201981201862080819204231560333360358877312956996689255714004, 13902108401372766216435686598883166462718370176872457303041338686324209123022604352694633411033411256085431424523035978942475478113149476545757562794006461983197231978452707129801424571427371469164979150127110600942840192717687795435476669311636385256008047428779616962846931617334673004399578644426441286632936106317964414895618599381960160641405403200204491299642749179223586882308142262885370380050036905454892068356222587292973184542284106972777370287660320141068046198176619502994885957156490508948840970640416377486235597580339861436089376346914464779715963246380278987830069272275983795180195497192128027347890, 17317057967717984545064283267563817203387028191709873283270912919957585507598744507800246927766105186759352325860100372183470069476765795900096698516608948560181803614605354319676602881106207486809219687722999253251376507788795216520633953330852247928193324644059444727295370046757194341412859515560148931989361555355390962044231206436841318257407812638918839196725110832282636810979410933854574822356868833169290185966589301153945305960536975420542966877390167714257593780071533231426170207211561155364679000593476320155877229477814027247194012318769551522294835316833481123819187792108682444012748348314918528140528, 13384601026546351477019795149207461115670795122687330781933418209799509900998293615505721209788448962447897815099814933644923298269095812132347197816941204582403940277971333828667326233536228802577255143735456088279096942071695637488031239979151589534207592236600983294709682937424715755899827401126839784241615668071677222510933141991459749940470424458957271164081709995744390000567720823748559522269113592961207115755624489515777275550690557889868157604984872296442340631328678982041918583357359886580276858448625233986182504485247163226837998755616433762156968287131853436576386391257523855358949959132118545736050, 13902108401372766216435686598883166462718370176872457303041338686324209123022604352694633411033411256085431424523035978942475478113149476545757562794006461983197231978452707129801424571427371469164979150127110600942840192717687795435476669311636385256008047428779616962846931617334673004399578644426441286632936106317964414895618599381960160641405403200204491299642749179223586882308142262885370380050036905454892068356222587292973184542284106972777370287660320141068046198176619502994885957156490508948840970640416377486235597580339861436089376346914464779715963246380278987830069272275983795180195497192128027347890, 23544466341103303852177503583134973463548730859662793391453044498707054382665853932412902102396995106918934459819831093427541958859024039453426810225228429770923008373370320932143504651550024854891524316620741850574435705565262903643095492753382085090762433024595630432464018382806200767280894248465860232209177493870724839378746565344305298053029774418225283003000347959377028060514780732522302721901542334943957686780872371706590155161382511096128220788925901408172939652983902641086106837347212476767269941848738284258618180399522048906377716813577343801465045430753676492167535358054447170119969571037539502047549, 13384601026546351477019795149207461115670795122687330781933418209799509900998293615505721209788448962447897815099814933644923298269095812132347197816941204582403940277971333828667326233536228802577255143735456088279096942071695637488031239979151589534207592236600983294709682937424715755899827401126839784241615668071677222510933141991459749940470424458957271164081709995744390000567720823748559522269113592961207115755624489515777275550690557889868157604984872296442340631328678982041918583357359886580276858448625233986182504485247163226837998755616433762156968287131853436576386391257523855358949959132118545736050, 22201112645324547853169461183905708133914080041470208544887543077406617962513084437529137190249117329364052058261670352313282990405463301815851291221468044369980605899860512939424418039802745509609519868634161235791010994022727044687765205484273598066323664235840595551903252365882931261849309529658110569628026591435123492111453400467552330686305369402999097995213933078113144170053561372082272117496908609832672408376518371125927523558020103451776305591386126975988810451913023458049113695454143009493773719623387220940976588325436208338766716585345285137369381914559989289685270050442822693739806935248907109733819]

'''