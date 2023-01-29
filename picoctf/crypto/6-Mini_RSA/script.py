import gmpy2

n = 1615765684321463054078226051959887884233678317734892901740763321135213636796075462401950274602405095138589898087428337758445013281488966866073355710771864671726991918706558071231266976427184673800225254531695928541272546385146495736420261815693810544589811104967829354461491178200126099661909654163542661541699404839644035177445092988952614918424317082380174383819025585076206641993479326576180793544321194357018916215113009742654408597083724508169216182008449693917227497813165444372201517541788989925461711067825681947947471001390843774746442699739386923285801022685451221261010798837646928092277556198145662924691803032880040492762442561497760689933601781401617086600593482127465655390841361154025890679757514060456103104199255917164678161972735858939464790960448345988941481499050248673128656508055285037090026439683847266536283160142071643015434813473463469733112182328678706702116054036618277506997666534567846763938692335069955755244438415377933440029498378955355877502743215305768814857864433151287
e = 3
c = 1220012318588871886132524757898884422174534558055593713309088304910273991073554732659977133980685370899257850121970812405700793710546674062154237544840177616746805668666317481140872605653768484867292138139949076102907399831998827567645230986345455915692863094364797526497302082734955903755050638155202890599808146919581675891411119628108546342758721287307471723093546788074479139848242227243523617899178070097350912870635303707113283010669418774091018728233471491573736725568575532635111164176010070788796616348740261987121152288917179932230769893513971774137615028741237163693178359120276497700812698199245070488892892209716639870702721110338285426338729911942926177029934906215716407021792856449586278849142522957603215285531263079546937443583905937777298337318454706096366106704204777777913076793265584075700215822263709126228246232640662350759018119501368721990988895700497330256765579153834824063344973587990533626156498797388821484630786016515988383280196865544019939739447062641481267899176504155482

if_true = False

# c = m**e (mod n)
# m**e = i*n + c

# e is small
# m**e is just a bit larger then n
#5**3 is just a little larger than 119

for i in range(10000):
	m,if_true = gmpy2.iroot((i*n)+c,e)
	if if_true:
		print(f"i is: {i}")
		print(f"Value of m is: {m}")
		data = hex(m)[2:]
		flag = bytes.fromhex(data).decode()
		print(f"FLag is: {flag}")
		break