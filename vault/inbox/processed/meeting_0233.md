---
alfred_tags:
- rami/meetings
- zoom-sessions
processed_at: '2026-02-26T20:09:04.973117+00:00'
status: processed
---

# Meeting: rami's Uploaded Recording | Aug 11, 2025 (Transcript)

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2025-08-11T07:21:47.037Z |
| **Title** | rami's Uploaded Recording | Aug 11, 2025 (Transcript) |
| **Classification** | N/A |
| **Category** | N/A |
| **Meeting Type** | N/A |
| **Source Document** | [https://docs.google.com/document/d/1L_tv3QtrlHLDtwselL76pnGe6SxYbKOLUJo8R81Rg9U/edit?usp=drivesdk](https://docs.google.com/document/d/1L_tv3QtrlHLDtwselL76pnGe6SxYbKOLUJo8R81Rg9U/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Rami Khouri | Meeting moderator / main presenter (AI agents, MCP, workflows) | 0.91 |
| Ahmad Massalha | Presenter (Asana vs Jira; project management tools/workflows) | 0.78 |
| Stav Zamir | Participant; prompt engineering + database/context tasks | 0.82 |
| Zahra | Participant (likely new/external); subscriptions/calculators/admin tasks | 0.65 |
| Rivi Idelman | Participant or referenced admin/coordinator; insufficient evidence | 0.35 |
| David | External technical collaborator (mentioned multiple times; may or may not be on the call) | 0.7 |
| Shachar Segev | VP R&D (mentioned; not confirmed as present) | 0.85 |


## 3. Key Topics

- AI agents and multi-agent systems
- MCP (Model Context Protocol) and how it fits into the AI workspace
- Asana vs Jira evaluation; project management workspace setup
- Workflow automation (n8n) and building fundamental workflows/nodes
- Prompt engineering tasks and prompt/database structuring
- Supabase and data/storage considerations
- Knowledge base vs memory concepts for AI systems
- Model/tool comparison (Claude vs ChatGPT vs Gemini; related subscriptions/costs)
- External platform/tooling referenced: Alfred / Alfred OS (built by David)


## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Unknown (32.82): Oi, 
Unknown (33.78):  como  você  está? 
Unknown (43.3):  Tudo  bem  com  vocês? 
Unknown (44.85):  Tudo  bem, 
Unknown (45.12):  e  você? 
Unknown (45.23):  Sim, 
Unknown (45.37):  estou  bem. 
Unknown (45.71):  Sim, 
Unknown (46.13):  aqui  está  o  Ram. 
Unknown (49.91):  Tudo  bem, 
Unknown (50.43):  eu  gostaria  de  te  conhecer  mais. 
Unknown (51.77):  Então, 
Unknown (51.9):  você  já  experimentou  isso  em  outra  reunião? 
Unknown (54.48):  Sim, 
Unknown (54.63):  sim. 
Unknown (54.76):  Então, 
Unknown (54.95):  só  com  mim  foi? 
Unknown (57.53):  Não  é  da... 
Unknown (61.52):  Não  é  da... 
Unknown (62.2):  Não  é  da... 
Unknown (64.26):  Não  é  da... 
Unknown (64.58):  Não  é  da... 
Unknown (66.46):  Não  é  da... 
Unknown (66.64):  Não 
Unknown (68.24):  é 
Unknown (72.97):  da... 
Unknown (73.25):  Não  é  da... 
Unknown (76.94):  Não  é 
Unknown (81.17):  da... 
Unknown (81.74):  Não  é 
Unknown (83.17):  da... 
Unknown (83.38):  Não  é  da... 
Unknown (84.72):  Não  é  da... 
Unknown (85.03):  Não  é  da... 
Unknown (85.36):  Não  é  da... 
Unknown (85.7):  Obrigada. 
Unknown (86.81):  No  início, 
Unknown (90.66):  falamos  sobre  o  processo  de  gestão  de  projetos, 
Unknown (95.74):  e 
Unknown (96.88):  o  que  é  o  Workspace, 
Unknown (98.1):  com  resumidos  automáticos  no  Reader, 
Unknown (106.25):  e  a  plataforma, 
Unknown (107.94):  a 
Unknown (109.39):  plataforma  da  IBM. 
Unknown (112.81):  Sim, 
Unknown (113.97):  sim. 
Unknown (114.43):  Então, 
Unknown (120.83):  quem  quer  começar? 
Unknown (123.14):  Como  vocês  prepararam  as  lembranças? 
Unknown (126.86):  Sim, 
Unknown (127.02):  muito  obrigada, 
Unknown (134.55):  Fih. 
Unknown (225.74):  A 
Unknown (251.47):  plataforma 
Unknown (253.61):  de  gestão  do  projeto. 
Unknown (257.5):  Eu  pesquisei  para  Jira  e  Sana. 
Unknown (261.19):  Jira  eu  conheço  um  pouco  da  minha  outra  empresa. 
Unknown (263.85):  Tentei  ver  quais  são  as  funções  que  tem  para  a  minha  outra  empresa. 
Unknown (269.31):  Tentei  abrir  uma  outra  empresa. 
Unknown (285.28):  Eu  fiz  um  task  entre  eles, 
Unknown (288.52):  algo  simples, 
Unknown (289.34):  para  ver  qual  criptograma  existe. 
Unknown (291.33):  O  que  sim, 
Unknown (292.85):  nós  fizemos  muito  mais  user-friendly. 
Unknown (295.92):  A  Jira  é  um  pouco  mais  confusa. 
Unknown (300.03):  Nós  oferecemos  coisas  que  não  nos  preocupamos 
Unknown (306.17):  em  uma  equipe  com  três  pessoas. 
Unknown (307.75):  Há  muitas  coisas  que  podemos  adicionar  no  código, 
Unknown (313.55):  inclusive  adicionar  um  calendário  e  um  drive. 
Unknown (318.51):  Há  algo  preparado  que  podemos  fazer  de  forma  sincronizada  e  também  podemos  utilizar  SQL. 
Unknown (329.23):  A  sana  é  muito  mais... 
Unknown (332.67):  Tudo  está  pronto  lá. 
Unknown (334.42):  Só  que  a  diferença  é  que  na  sana... 
Unknown (343.59):  Eu  não  entendo. 
Unknown (346.44):  Diga, 
Unknown (346.73):  eu  fiz  um  trabalho... 
Unknown (352.15):  Tipo, 
Unknown (355.37):  é... 
Unknown (355.6):  Você  pode  dar... 
Unknown (356.55):  Podemos  dar  a  ele  qualquer  nome  que  quisermos, 
Unknown (358.29):  mas  é  o  mesmo  plano, 
Unknown (359.93):  seja  em  reuniões  ou  em  testes. 
Unknown (362.4):  Nós  simplesmente  adicionamos  um  projeto  aqui, 
Unknown (366.9):  e  então  podemos  fazer  um  nome  que  seja  como  o 
Unknown (377.57):  nosso  encontro  de  semana. 
Unknown (380.1):  Então, 
Unknown (380.21):  o  que  é  legal  na  Asana, 
Unknown (380.62):  que  é  possível  dentro  do  encontro, 
Unknown (383.71):  No  Meetings, 
Unknown (384.47):  você  pode  conectar, 
Unknown (385.63):  primeiro  de  tudo, 
Unknown (387.43):  você  pode  conectar  para  o  Calender, 
Unknown (388.81):  mas  a  planilha  que  é  de  forma  própria  não  é  possível. 
Unknown (392.52):  Então, 
Unknown (393.29):  você  precisa 
Unknown (396.46):  fazer  10  dólares  por  mês, 
Unknown (398.97):  e  isso  nos  dará  a  opção  de  sincronização  para  o  Calender  e  a  opção  de  resumir  através  do  AI. 
Unknown (406.93):  e  nós  podemos  subir  a  temperatura  da  reunião. 
Unknown (413.14):  podem  fazer  um  resumo  com  a  AI  dentro  do  TASK  Pro  e  então  criar  um  arquivo  que  pode  ser  criado  e  que  pode  ser  escrito  e  abaixo  disso  pode  fazer  um 
Unknown (429.72):  subtasque  por  exemplo, 
Unknown (432.25):  na  reunião  de  conversa  eu  faço  assim  e  assim  e  o  staff  faz  assim  e  assim  então  podemos  abrir  arquivos 
Unknown (444.56):  e  também  pode  ter  um  par  de  fios  do  nosso  drive  direto  para  aqui, 
Unknown (449.52):  mas  também  não  é  possível  na  subscrição  e  dentro  do  subtask  é  possível  marcar, 
Unknown (464.44):  é  possível, 
Unknown (464.93):  como  em  qualquer  task, 
Unknown (466.61):  fazer  um  tag, 
Unknown (467.44):  por  exemplo, 
Unknown (467.97):  eu  vou  fazer  um  tag  list  tag  e  até 
Unknown (470.51):  Você  pode  adicionar  isso  ao  seu  calendário. 
Unknown (474.05):  Eu  não  posso. 
Unknown (475.13):  Você  vai  receber  um  link  para  o  email, 
Unknown (479.62):  e  na  próxima  hora  que  vocês  o  ativarem, 
Unknown (482.04):  ele  se  expande  para  o  calendário. 
Unknown (484.54):  E  então, 
Unknown (485.1):  aqui, 
Unknown (488.52):  para  cada  task  que  vocês  verão  aqui, 
Unknown (497.82):  task  1, 
Unknown (498.2):  você  pode  fazer... 
Unknown (499.55):  para  ver  se  alguém  pode  ver  isso, 
Unknown (501.33):  quem  pode  editar  isso  e  então  podemos  fazer  isso  como  se  tivéssemos  terminado  com  esse  trabalho  ou  terminamos  em  progresso  ou  coisas  assim  e  então, 
Unknown (510.38):  na  hora  que  eu  faço, 
Unknown (512.28):  digamos  que  nós  três  podemos  fazer  a  análise  desse  trabalho, 
Unknown (518.27):  então  também  podemos  responder  um  ao  outro  e  juntar  documentos  dentro  do  comentário 
Unknown (528.74):  Como  eu  queria  lhe  dizer, 
Unknown (531.1):  você  tem  o  link  para  o  código  de  AI  e  portais, 
Unknown (537.25):  então  nós  poderíamos  fazer  isso  aqui  e  a  Spilot  está  ligada  aqui. 
Unknown (540.99):  E  então  sempre  será  mais, 
Unknown (544.89):  digamos, 
Unknown (547.54):  Agora, 
Unknown (548.34):  essas  são  as  programas. 
Unknown (552.84):  Tem  o  Advanced  e  o  Enterprise, 
Unknown (554.75):  que  não  estão  ligados  a  nós, 
Unknown (556.67):  eu  acho. 
Unknown (557.39):  e  também 
Unknown (559.57):  com  as  propostas  avançadas  e  o  starter  é  de  11  dólares  por  mês  o  que  permite, 
Unknown (566.86):  principalmente, 
Unknown (570.74):  as  duas  funções  que  podemos  utilizar  muito  bem  são  as  condições  diretas  dentro  da  reunião  ou  a  condição  que  surgiu  depois, 
Unknown (583.9):  também  na  formação  automática 
Unknown (585.58):  e  ligar  o 
Unknown (586.74):  Google  e  o 
Unknown (589.43):  Skype.  Em  qual  época? 
Unknown (590.43):  Na  primeira, 
Unknown (591.63):  no  startup. 
Unknown (593.13):  Agora, 
Unknown (595.36):  sobre  a 
Unknown (597.6):  Jira.  Jira  é  muito... 
Unknown (599.55):  Eu  conheço... 
Unknown (600.73):  A  Jira, 
Unknown (600.93):  por  exemplo, 
Unknown (601.53):  no  Asana, 
Unknown (602.47):  é  o  mesmo  workflow, 
Unknown (604.83):  não  importa, 
Unknown (607.82):  como  reuniões, 
Unknown (613.22):  tarefas, 
Unknown (613.66):  não  importa  qual  é  a  questão, 
Unknown (615.06):  você  pode  usar  o  mesmo  workflow, 
Unknown (617.98):  abrir  um  trabalho, 
Unknown (619.04):  dar  o  nome  que  você  quiser, 
Unknown (619.67):  e  daí, 
Unknown (619.81):  as  coisas  que  você  pode  fazer  em  edit, 
Unknown (621.81):  são  as  mesmas  coisas. 
Unknown (623.22):  Gira, 
Unknown (623.59):  no  entanto, 
Unknown (624.68):  você  precisa  escolher, 
Unknown (626.25):  nós  precisamos  escolher  de  onde  começar  e  o  que  é. 
Unknown (630.33):  A  obra  sobre... 
Unknown (633.02):  Se  é  um  trabalho  de  projeto, 
Unknown (634.54):  e  um  projeto  de  gestão, 
Unknown (636.02):  então  é  um  flow  diferente. 
Unknown (637.56):  Se  é  um  encontro, 
Unknown (639.34):  é  um  flow  diferente, 
Unknown (641.34):  então  não  é  possível  fazer  um  sobre  o  outro. 
Unknown (644.27):  Não  é  possível, 
Unknown (645.18):  no  encontro, 
Unknown (646.21):  fazer  um  resumo  e  dizer  que  nesse  encontro  também  surgiram  essas  questões  e  essas  questões, 
Unknown (651.04):  e  fazer  uma  conversa. 
Unknown (652.46):  E, 
Unknown (652.55):  como  uma  experiência... 
Unknown (657.86):  Eu  acho  que  a  Jira  tem  muitas  melhorias, 
Unknown (661.78):  como  se  ela  fosse  conectada  ao  CRM  e  tal. 
Unknown (670.62):  Por  isso  eu  sou  um  tipo  de  criador. 
Unknown (672.14):  Nós  trabalhamos  com  isso. 
Unknown (674.43):  Eles  abrem  bugs  e  se  conectam  ao  Salesforce. 
Unknown (680.89):  E  então, 
Unknown (681.11):  mesmo 
Unknown (683.62):  na  situação  normal, 
Unknown (686.22):  ela... 
Unknown (687.33):  Embora  eu  conheça  isso, 
Unknown (688.11):  foi  um  pouco  difícil  para  mim. 
Unknown (689.07):  E, 
Unknown (689.11):  por  isso, 
Unknown (689.53):  fizemos  mais  do  que  um  pequeno, 
Unknown (691.29):  mais  do  que  um  detalhe, 
Unknown (692.65):  as  coisas  que  precisamos  nesse  bag  share. 
Unknown (700.38):  Agora, 
Unknown (700.98):  na  verdade, 
Unknown (702.07):  e  vocês  não  concordam  comigo, 
Unknown (704.04):  não  precisamos  de  algo  que  se  expanda  de  forma  dramática, 
Unknown (707.68):  como  o  Jira. 
Unknown (708.37):  E, 
Unknown (708.59):  na 
Unknown (709.88):  verdade, 
Unknown (710.73):  quando  fazemos  o  Startup  Tag, 
Unknown (712.57):  podemos  ver 
Unknown (715.76):  mais  lá. 
Unknown (716.89):  fora  do  fator  do  calendário, 
Unknown (719.95):  Google  e  Even, 
Unknown (721.99):  para  ver  os  dados, 
Unknown (723.07):  com  as  resumidas  do  AI, 
Unknown (724.73):  para  ver  quais  são  as  funções  mais  importantes. 
Unknown (726.66):  Isso  é  tudo. 
Unknown (735.26):  Ok. 
Unknown (740.08):  Zahra, 
Unknown (742.59):  antes  de  esquecer, 
Unknown (743.8):  sobre  todo  o  assunto  de  gestão... 
Unknown (747.29):  todas  as  descrições  que  eu  vou  usar, 
Unknown (752.57):  também 
Unknown (755.66):  o  nome, 
Unknown (756.52):  a  concentração  de  calculadores, 
Unknown (768.42):  a  minha  passagem, 
Unknown (769.92):  então  eu  quero  que  você  faça  isso, 
Unknown (775.12):  porque  os  calculadores  me  assustam, 
Unknown (775.96):  então... 
Unknown (776.24):  e  não  conseguimos  guardá-los  e  não  os  gastamos  no  tempo  Vou  passar  para  você  o  cartão  de  Shrive  O  nosso  valor  mensal  de  200  é  de 
Unknown (788.74):  1000  shk  Agora  fiz 
Unknown (794.6):  um  teste  no  Google  Ultra  que  custa  200  dólares  e  queria  tentar  o  novo  futuro  de  Gemini  chamado  DeepThink 
Unknown (805.66):  Eu  não  acho  que  isso  vale, 
Unknown (806.74):  então  eu  vou  acabar  com  isso. 
Unknown (809.22):  1.000  Shekels  para  o  que? 
Unknown (810.81):  Para  a  subscrição? 
Unknown (813.35):  Sim, 
Unknown (814.55):  sim. 
Unknown (814.97):  Nós  podemos  passar  por  isso, 
Unknown (816.79):  mas, 
Unknown (816.91):  ao  mesmo  tempo, 
Unknown (818.51):  vamos  dividir  como  nós  pagamos, 
Unknown (820.82):  que  sai  1.000  Shekels  por  mês, 
Unknown (822.89):  o  que  nós  já  pagamos  para  a  JGPT, 
Unknown (827.86):  Manus, 
Unknown (828.36):  acho  que  é  o  segundo  cartão  de  renda  que  o 
Unknown (832.13):  Vy  administra. 
Unknown (835.81):  Isso  não  é  o  que  pensamos  dentro  do  coração. 
Unknown (841.15):  E  então  decidimos  se  usar  ou  não. 
Unknown (844.43):  E  isso  é  o  que  precisamos. 
Unknown (848.33):  E  eu  vou  continuar  falando  sobre  o  tema  do  RAM  e  o  teste  de  calculadora. 
Unknown (860.1):  Ok. 
Unknown (860.46):  Só  uma  coisa, 
Unknown (861.15):  como  se  fosse  a  aplicação  que  podemos  adicionar, 
Unknown (864.29):  como  se  fossem  os  dois  em  uma  mesma  subscrição, 
Unknown (867.67):  é  o  que  eu  preciso  dizer. 
Unknown (868.31):  Nós  não  sabemos, 
Unknown (870.85):  a  aplicação, 
Unknown (872.23):  como  se  fossem  os  dois. 
Unknown (874.5):  O  que  você  está  perguntando? 
Unknown (876.79):  Não, 
Unknown (877.34):  não. 
Unknown (877.59):  Como  se  fosse  o  calendário, 
Unknown (880.71):  o  zoom, 
Unknown (881.6):  o  slide, 
Unknown (883.1):  o  tab, 
Unknown (883.38):  o  tab, 
Unknown (883.71):  o  tab, 
Unknown (883.87):  o  tab, 
Unknown (884.13):  o  tab. 
Unknown (884.35):  Em  grande, 
Unknown (887.66):  o  drive. 
Unknown (894.21):  E  aí  E  aí  E  aí  E  aí  E  aí  E  aí  E  aí  E  aí  E  aí  E  aí  E  aí  Obrigado. 
Unknown (900):  Eu  vou  explicar  agora  quais  são  os  elementos  básicos 
Unknown (905.48):  que  precisamos  utilizar  e  o  que  eu  quero  que  vocês  examinem  e  exibam. 
Unknown (911.55):  Então, 
Unknown (911.77):  em  grande, 
Unknown (912.2):  eu  concordo  que  a 
Unknown (914.73):  SANA  é  a  mais  importante  para  mim  e  também  oferece  integrações  para  muitos, 
Unknown (920.88):  e  eu  acho  que  nós  usamos  elas. 
Unknown (924.44):  Agora, 
Unknown (926.03):  antes  de  chegarmos  à  parte  de  Rastaf... 
Unknown (931.32):  em  quais  espaços  de  trabalho  estão  disponíveis  e  o  que  pode  interagir  bem  no  nosso  trabalho. 
Unknown (939.02):  Quero  destacar  que  para  que  nosso  trabalho  seja  dividido, 
Unknown (946.35):  precisamos  de  uma  plataforma  de  Project  Management, 
Unknown (951.42):  precisamos  de  uma  plataforma  de 
Unknown (954.58):  Calender  que  queremos  usar, 
Unknown (956.66):  de  e-mail. 
Unknown (961.94):  database  memory  agora  vou  explicar  o  que  é  diferente  e  a  plataforma  de  encontros  por  que  é  importante  que  todas  essas  plataformas 
Unknown (977.73):  tenham  integração  de  todas  as  horas  porque  no  final  precisamos  escolher  uma  estrutura  de  trabalho  de  uma  empresa 
Unknown (989.4):  que, 
Unknown (989.52):  na  verdade, 
Unknown (989.89):  seria  uma  área  de  trabalho  de  agentes  que  discutem  um  com  o  outro. 
Unknown (996.23):  O  que  isso  significa? 
Unknown (999.18):  Digamos  que  nós  gestionamos  as  nossas  tarefas  e  fazemos. 
Unknown (1005.24):  Agora  temos  a  reunião. 
Unknown (1007.24):  Precisamos  de  um  agente  que  receba  a  reunião  e 
Unknown (1012.88):  conclua. 
Unknown (1013.24):  E  então  ele  envia  isso  ao  agente  que... 
Unknown (1020.88):  que  divide  as  tarefas  ou  decide  quais  tarefas  vão  para  quem. 
Unknown (1025.49):  Agora, 
Unknown (1025.77):  o  agente  que  decide  onde  vão  as  tarefas, 
Unknown (1028.37):  e  depois  ele  vai  saber  como  fazer, 
Unknown (1030.48):  quem  é  responsável  por  cada  tarefa, 
Unknown (1034.72):  ele  precisa  ser  conectado 
Unknown (1039.29):  à  database. 
Unknown (1041.09):  Ele  precisa  saber  quem  é  o  testar, 
Unknown (1043.13):  quem  é  o  Ahmad, 
Unknown (1044.27):  o  que  fazemos, 
Unknown (1045.85):  o  que  fizemos, 
Unknown (1046.59):  o  que  queremos  fazer. 
Unknown (1049.16):  precisa  usar  o  seu  precisa  ter  um  tool  ou  função  para  ler  o  database  depois  que  ele  decidiu  precisa 
Unknown (1060.41):  ligar  à  plataforma  do  project  management  e  abrir  se  precisa  abrir  um  novo  project  abre  se  precisa  adicionar  tarefas  adicionar, 
Unknown (1072.02):  adicionar  tarefas  adicionar  fones, 
Unknown (1075.63):  tudo  o  que  nós  devemos  fazer 
Unknown (1078.91):  O  que  Ahmad  já  explicou  sobre  o  que  podemos  fazer  para  abrir  tasks, 
Unknown (1081.93):  subtasks, 
Unknown (1083.05):  e  também  um  resumo  automático  dentro  dessa  Asana, 
Unknown (1086.86):  nós  precisamos  definir  isso  dentro  da  área  de  trabalho  do  cliente. 
Unknown (1099.69):  Então, 
Unknown (1101.1):  dentro  da  Asana, 
Unknown (1102.1):  pode  ser  que... 
Unknown (1102.41):  dentro  da  Asana  existe  uma  área  de  trabalho  de  Agents. 
Unknown (1106.27):  A  Asana  pode  se  conectar  com  o  Canva, 
Unknown (1107.16):  mas... 
Unknown (1108.86):  No  entanto, 
Unknown (1110.16):  usamos  o  Asana  como  um  meio  de  gestão  de  projetos, 
Unknown (1113.64):  gestão  de  tarefas. 
Unknown (1114.52):  Ou  seja, 
Unknown (1115.47):  um  agente  que  decide  quais  são  as  tarefas, 
Unknown (1120.25):  ou  também  se  precisa  de  uma  reunião, 
Unknown (1122.59):  se  precisa  de  fazer  algo  no  calendário. 
Unknown (1126.56):  Você  está  falando  sobre  um  relacionamento  de  três, 
Unknown (1129.3):  um  relacionamento  de  três, 
Unknown (1133.42):  um  relacionamento  de  três. 
Unknown (1136.92):  Selan, 
Unknown (1137.23):  um  abraço. 
Unknown (1139.04):  Ele  se  equipa, 
Unknown (1143.0):  produz  coisas  dentro  do  calendário, 
Unknown (1148.85):  ele  também  envia  um  e-mail  para  a  gente, 
Unknown (1155.21):  então  temos  que  conectar  um  e-mail. 
Unknown (1162.9):  E  isso  é  o  que  precisamos  fazer  agora  para  transformar  a  nossa  trabalho  em  mais  coisas. 
Unknown (1168.97):  e  precisamos  de  agentes  que  façam  pesquisas  Eu  ensinei  uma  pesquisa  de  pesquisa  e  podemos  criar  um  tipo  de  agente  que  diz  a  nossa  pesquisa  que  precisamos  fazer  pesquisa  sobre  ferramentas  de  desenvolvimento  de  projetos  Ele  sabe  apenas  a  final  da  pesquisa  do  trabalho  que  precisa  fazer  então  ele  faz  uma  pesquisa  pode  ser  um  único  agente 
Unknown (1195.68):  o  cara  é  um  sacan, 
Unknown (1196.96):  ele  é  um  ser, 
Unknown (1197.69):  ele  é  um  ser  que  mostra. 
Unknown (1200.24):  você  a  insere  na  Asana, 
Unknown (1205.55):  pode  ser  assim, 
Unknown (1206.44):  e  também  se  nós  queremos  criar  páginas, 
Unknown (1216.42):  campos, 
Unknown (1219.35):  não  sei, 
Unknown (1219.85):  a  criação  de  um  texto, 
Unknown (1221.09):  uma  publicação  para  o  Facebook, 
Unknown (1223.8):  Instagram, 
Unknown (1225.19):  não  importa  o  que, 
Unknown (1226.84):  então... 
Unknown (1227.71):  Tudo  isso  precisa  se  conectar  ao  World  Space  da  X. 
Unknown (1236.15):  Agora, 
Unknown (1236.43):  eu  pedi  para  você  verificar 
Unknown (1241.62):  os  chatbots  que  existem  hoje 
Unknown (1244.74):  e  como  eles  podem  se  conectar. 
Unknown (1254.67):  Você  conseguiu  estudar? 
Unknown (1258.76):  Você  é  estudante  de 
Unknown (1262.28):  educação? 
Unknown (1262.98):  Sim, 
Unknown (1263.14):  eu  fiz. 
Unknown (1263.28):  Eu  sei  que... 
Unknown (1264.16):  eu  não  sei  se  você  sabe, 
Unknown (1267.47):  mas  eu  fiz. 
Unknown (1268.07):  Eu  me  encontrei, 
Unknown (1270.07):  me  encontrei  com  o  professor  e  fiz... 
Unknown (1272.61):  eu  escrevi  para  ele  uma  missão  que  fazia  com  que  ele  pudesse  estudar  em  uma  escola  de  educação. 
Unknown (1279.21):  E  eu  construí  como  um  estudante  de  educação 
Unknown (1284.56):  para  ver  como  ele  funciona. 
Unknown (1289.04):  Mas  em  outros  lugares, 
Unknown (1289.76):  como  em  Clóvis, 
Unknown (1290.32):  em  Plácio 
Unknown (1295.22):  de 
Unknown (1296.18):  Edad,  eu  não  fiz  isso. 
Unknown (1301.02):  Então, 
Unknown (1301.2):  nós  temos  um  cidadão, 
Unknown (1303.6):  como  os  GPTs, 
Unknown (1304.02):  no  chat, 
Unknown (1304.37):  e  ele, 
Unknown (1304.54):  o  que  eu  percebi, 
Unknown (1305.46):  é  que  ele  não  se  mantém  no  cidadão, 
Unknown (1306.52):  não  se  baseia  em  uma  palavra, 
Unknown (1307.81):  ele  pode  dizer 
Unknown (1309.59):  que  não  é  tão  relevante. 
Unknown (1312.28):  e  agora  eu  vou  te  chamar  primeiro, 
Unknown (1313.92):  porque  eu  quero  te  falar  sobre  o 
Unknown (1317.58):  que  é  o 
Unknown (1319.2):  FIMCO, 
Unknown (1320.87):  o 
Unknown (1321.44):  FIMCO  é  o  FIMCO  de  Abre, 
Unknown (1324.39):  o  FIMCO  é  o  FIMCO  de  Arte  e  Arte, 
Unknown (1326.33):  e  eu  vou  te  falar  sobre  o  que  é  o  FIMCO, 
Unknown (1328.63):  e  o  que  é  o  FIMCO  de  Arte. 
Unknown (1331.39):  Então, 
Unknown (1331.67):  eu  vou  te  chamar  primeiro, 
Unknown (1335.06):  porque  eu  quero  te  falar  sobre  o  que  é  o  FIMCO, 
Unknown (1341.07):  para  ver  se  eu  consegui  entender  o  que  ela  estava  dizendo. 
Unknown (1345.95):  E  não  sempre  é  possível  explicar  o  que  eu  estava  dizendo  na  primeira  vez  que  a  gente 
Unknown (1359.81):  se 
Unknown (1364.99):  encontrou. 
Unknown (1366.21):  Eu  não  vou  deixar  de  falar  o  que  eu  me  lembrei. 
Unknown (1369.12):  Para  quem  de  vocês  foi  ou  se  encontrou  com  o  termo  MCP, 
Unknown (1407.73):  Agora, 
Unknown (1407.87):  vamos  começar  a  ver  quais  são  os  fechados  que  existem. 
Unknown (1429.17):  Então, 
Unknown (1429.67):  em  termos 
Unknown (1433.15):  de  modelos  de  língua... 
Unknown (1437.5):  É  o  que  a  Gpt  oferece. 
Unknown (1438.9):  O  que  eu  quero  fazer  é  fazer  uma  apresentação 
Unknown (1450.27):  de  como  funciona  cada  modelo  e  quando  é 
Unknown (1459.82):  necessário 
Unknown (1462.96):  usar  cada  um. 
Unknown (1466.48):  E  isso  é  importante, 
Unknown (1468.22):  mais 
Unknown (1471.28):  ou 
Unknown (1472.46):  menos  será  menos  importante  quando  o  GPT-5  sair, 
Unknown (1476.84):  porque  então  ele  fará  a  escolha  para  o  presidente. 
Unknown (1480.44):  Mas  sim, 
Unknown (1480.86):  é  importante  entender  o  conceito  próprio  das  mudanças  entre  os  modos. 
Unknown (1489.08):  Agora, 
Unknown (1489.27):  aqui, 
Unknown (1489.61):  se  abrirmos, 
Unknown (1490.0):  então  temos  alguns 
Unknown (1494.5):  modos. 
Unknown (1496.56):  Canvas  é, 
Unknown (1497.52):  na  verdade, 
Unknown (1498.03):  um  aplicativo  que... 
Unknown (1500.17):  e  nos  permite  escrever  texto  se  tivermos  um  ponte, 
Unknown (1505.06):  digamos 
Unknown (1507.16):  vamos  dizer  não 
Unknown (1549.46):  E  então  podemos  fazer  Edit 
Unknown (1551.7):  E  aqui  nós  pedimos  que  ele  escolha  As  letras  da  letra 
Unknown (1560.36):  Mudar  o  tempo  do  texto 
Unknown (1562.92):  Mudar  a  altura  da  língua  Fazer  um  Polish  no  ponto  de 
Unknown (1570.8):  vista  do  projeto  Ou  adicionar  emojis, 
Unknown (1575.01):  se  isso  for  possível 
Unknown (1577.9):  post  no  facebook, 
Unknown (1578.94):  instagram, 
Unknown (1585.56):  websearch  é  quando  queremos  dizer  que  deve  usar  websearch, 
Unknown (1589.59):  não  é  que  seja  100  ou  300  ou  400  ou  300, 
Unknown (1596.43):  todos  usam  quando  necessário, 
Unknown (1598.24):  mas  é  uma  opção  que  acontece  study  and  learn  é  novo 
Unknown (1604.43):  plataforma, 
Unknown (1606.01):  é  um  modelo  que  o 
Unknown (1609.61):  artista  desenvolve  o  tempo 
Unknown (1616.92):  todo  e  ensina. 
Unknown (1617.9):  Então  ele  vai  perguntar, 
Unknown (1618.66):  por  exemplo, 
Unknown (1618.88):  se  eu  disser  que  ele  está  com  uma  experiência. 
Unknown (1643.8):  Então, 
Unknown (1644.14):  para  começar, 
Unknown (1644.72):  pergunte  a  ele  qual  é  o  Ramal  e  o  Ramal  vai  responder. 
Unknown (1650.15):  Então, 
Unknown (1650.63):  o  Ramal  vai  começar. 
Unknown (1669.86):  Ele  é  muito  interativo, 
Unknown (1671.38):  nós  também  podemos  lhe  dar  um  livro  e  ajudar  a  estudar, 
Unknown (1673.06):  perguntas, 
Unknown (1674.58):  quando  lhe  dão  uma  pergunta, 
Unknown (1676.62):  ele  não  lhe  dá  a  resposta, 
Unknown (1677.86):  mas  eles  lhe  dizem, 
Unknown (1679.24):  então  ele  tenta  nos  ensinar  durante  o  processo. 
Unknown (1686.26):  Ok, 
Unknown (1687.62):  o  Imagem  é... 
Unknown (1699.38):  Agora  vou 
Unknown (1702.37):  chegar  no  modo  Agents, 
Unknown (1705.81):  e  vou  clicar  em  Connectors. 
Unknown (1708.59):  Agora, 
Unknown (1710.18):  esse  é  o  MCP. 
Unknown (1711.24):  O  que  isso  significa? 
Unknown (1714.84):  Aqui, 
Unknown (1715.32):  quando  eu  digo  a  ele, 
Unknown (1721.44):  eu  posso 
Unknown (1723.47):  conectar  todos  os... 
Unknown (1725.85):  Então  aqui, 
Unknown (1726.33):  por  exemplo... 
Unknown (1728.41):  é  uma  ação  e  Cláudia  é  uma  melhoria  é  ok, 
Unknown (1737.58):  é  possível  fazer  um  procreate  e  então  nós  criamos  o  MCP  Server  e  também  precisamos  aprender  como  fazer  isso  porque  o  que  existe  aqui  é  muito  variado  então  é  muito  variado  o  drive  e  as  notificações  então  aqui  ele 
Unknown (1751.6):  é 
Unknown (1756.04):  variado 
Unknown (1767.0):  a  gente  vai  fazer  um  teste  de  o  que  é 
Unknown (1778.07):  que 
Unknown (1778.77):  é  o 
Unknown (1780.54):  que  é 
Unknown (1784.88):  Quando  abrir  o  cloud, 
Unknown (1785.94):  eu  vou  explicar  o  que  é  isso. 
Unknown (1787.44):  Tem  que  definir  o  que  é  o  MCP. 
Unknown (1788.81):  Se  eu  conectar  ele  ao  e-mail, 
Unknown (1790.85):  então, 
Unknown (1791.23):  se  eu  ler  o  e-mail, 
Unknown (1793.92):  escrever  o  e-mail, 
Unknown (1795.16):  rir, 
Unknown (1795.34):  não  vai 
Unknown (1797.16):  se  conectar  ao  e-mail. 
Unknown (1800.03):  E  se  eu  ativar  todas  as  funções, 
Unknown (1803.15):  ele  vai  se  transformar. 
Unknown (1806.83):  Então  todos  os  agentes  precisam  saber  exatamente  o  que  deve  fazer. 
Unknown (1810.92):  A  MCP  é  uma  forma  de  reduzir  a  construção  de  zero  dos  agentes  e  conectá-los. 
Unknown (1819.98):  É  uma  espécie  de  língua  na  qual  os  agentes  podem  conversar  com  os  outros. 
Unknown (1828.88):  Se  eu  tenho  um  agente  aqui, 
Unknown (1829.98):  que  eu  digo  para  ele, 
Unknown (1831.16):  vá  para  o  resumo, 
Unknown (1834.55):  envia  um  e-mail  e  leve  o  resumo  ao  Drive, 
Unknown (1838.49):  e  eu  o  ativo, 
Unknown (1839.73):  tenho  a  MCP  de  todos  esses, 
Unknown (1842.2):  não  precisa  dizer  o  que  isso  quer  dizer, 
Unknown (1848.84):  entre  no  e-mail, 
Unknown (1850.38):  escreva, 
Unknown (1852.72):  ele  sabe  fazer  isso. 
Unknown (1854.08):  Só  precisa  escrever. 
Unknown (1858.45):  e  isso  nos  leva  ao 
Unknown (1863.07):  Agent  Mode. 
Unknown (1864.87):  Agent  Mode  é  um  outro  mais  adicionado  do  Operator. 
Unknown (1869):  O 
Unknown (1869.86):  Operator  era  um 
Unknown (1872.16):  agente  que  atua  um  computador  local  e  faz  tarefas. 
Unknown (1876.48):  Ele  escreve, 
Unknown (1877.02):  tem 
Unknown (1878.3):  um 
Unknown (1880.2):  computador  e  uma  fonte  de  luz  e  faz  tarefas. 
Unknown (1882.47):  Mas  ele  não  era... 
Unknown (1898.26):  o 
Unknown (1908.8):  que 
Unknown (1909.85):  é 
Unknown (1918.14):  O  que  acontece  é  que  quando  o  agente  está  conectado  ao  MCP  através  do  Drive, 
Unknown (1924.61):  ele  não  precisa  fazer  essas  operações. 
Unknown (1926.5):  Ele  entra  através  do  API  no  Drive, 
Unknown (1929.71):  encontra  os  botões  e  os  envia. 
Unknown (1934.5):  Agora, 
Unknown (1935.63):  há  perigos  para 
Unknown (1940.19):  agentes  como  o  Operator, 
Unknown (1942.42):  que  são  os  computadores  abertos  e  os  monitoradores. 
Unknown (1946.86):  entre  um  agente  como  esse  se  eu  for  para  você  usar  o  Manos 
Unknown (1953.12):  eu  um  pouco  com  o  Manos, 
Unknown (1956.79):  se  eu  disser  para  ele  fazer  uma  pesquisa  ele  também  vai  abrir  vídeos  no  YouTube  e  vai  aprender  lá  que  é  legal, 
Unknown (1963.25):  é  bom  ele  pode  gravar  um  spot  tipo, 
Unknown (1967.08):  um  filme  ele  usa  screenshots 
Unknown (1975.55):  A  capacidade  de  analisar  os  vídeos  não  existe  hoje  em 
Unknown (1981.98):  OpenAI.  Quem  conclui  com  isso  é  o  Gemini. 
Unknown (1985.5):  Ele  pode  fazer 
Unknown (1990.09):  áudio, 
Unknown (1990.67):  vídeo, 
Unknown (1990.98):  não  sei  o  que, 
Unknown (1991.39):  ele  também  produz  vídeo  muito 
Unknown (1996.71):  bem. 
Unknown (1996.87):  Por  exemplo, 
Unknown (1997.36):  você  dá  um  vídeo  no  YouTube, 
Unknown (1999.08):  ele  pode  ouvir  o  que  tem. 
Unknown (2003.88):  Ou  isso  funciona... 
Unknown (2005.26):  LUL  é  uma  técnica  que  não  é  possível  usar  que  todos  podem  gravar  ouvir  digamos, 
Unknown (2013.48):  se  você  perguntar  ou  não, 
Unknown (2015.53):  é  uma  apresentação  para  entender  o  que  existe  nessa  apresentação  como  se  fosse  um  vídeo  Sim, 
Unknown (2024.96):  sim, 
Unknown (2025.26):  o 
Unknown (2027.04):  Gemini  pode  mas  é  importante 
Unknown (2037.5):  A 
Unknown (2040.24):  ideia  é  o  suporte  da  tonalidade. 
Unknown (2044.53):  Se  você  está  gravando  uma  apresentação, 
Unknown (2048.63):  não  é  necessário  entender  o  sentimento, 
Unknown (2052.91):  mas  existem  modelos  que  podem  te  ajudar. 
Unknown (2057.53):  Se  alguém  está  com  fome, 
Unknown (2060.41):  se  alguém  diz... 
Unknown (2061.47):  algo  em  um  tom  grudoso, 
Unknown (2063.59):  mas  o  conteúdo  é  positivo, 
Unknown (2065.59):  então  o  modelo  que  está  implementado  não  sabe  distinguir. 
Unknown (2072.74):  Isso  é  importante, 
Unknown (2076.45):  principalmente  quando  sim  vamos  para  um  tratamento  de  reunião  com  o  vídeo  e  tudo  isso, 
Unknown (2084.45):  então  existe, 
Unknown (2085.09):  existe  hoje  e  podemos  fazer  isso, 
Unknown (2088.44):  nós  simplesmente  não  pensamos  que... 
Unknown (2091.74):  Pelo  menos  na  nossa  prática  hoje, 
Unknown (2098.64):  isso  é  realmente... 
Unknown (2101.32):  Eu  pedi  para  você  ver  se  você  conseguia  entender, 
Unknown (2105.54):  aqui  nós  pegamos  uma  verificação  que  o  GPT  não  é  um  tipo  de  P, 
Unknown (2109.37):  não  é  um  P  de  Asana  e  não  é  um  G. 
Unknown (2112.91):  Agora  vamos  ver  se  a  Cloud... 
Unknown (2114.89):  Agora, 
Unknown (2115.06):  a  Cloud... 
Unknown (2115.76):  Tem 
Unknown (2118.62):  aqui... 
Unknown (2118.84):  Não. 
Unknown (2138.94):  O 
Unknown (2140.98):  que 
Unknown (2142.32):  é  relevante  para  nós  é  o  Sonic  4  e  o  Opus 
Unknown (2146.66):  4.1.  Isso  é  novo, 
Unknown (2148.81):  os  dois  são  novos. 
Unknown (2149.65):  O  Cloud  está  em  uma  nova  fase. 
Unknown (2154.8):  O  modelo  de  sua  pensão  é  bom. 
Unknown (2158.02):  Podemos  olhar  para  os  benchmarks. 
Unknown (2163.77):  que  fazem  o  mesmo  tempo  que  lançam  um  modelo  novo  eles  examinam  todos  os  tipos  de  benchmark  de  arquivo  perguntas  científicas  sobre  matemática  criação  de  código, 
Unknown (2175.62):  criação  de  código, 
Unknown (2176.3):  tudo  isso  ele  deve  ser 
Unknown (2179.61):  excelente  eu  não  sei  se  sua  capacidade  de  fazer  reasoning  é  longa  se  ela  é  igual  ao  3 
Unknown (2189.02):  Pro  ou  ao  novo  modelo  de 
Unknown (2191.19):  Google  o  Deep  Sync 
Unknown (2193.92):  Mas  isso  não  é  algo  que  precisamos  agora. 
Unknown (2196.0):  Quando  realmente  precisamos  de  um  modelo  assim? 
Unknown (2200.82):  Ou  Manos  pode  dar-lhe, 
Unknown (2202.56):  e 
Unknown (2204.04):  Manos  é  uma  empresa  muito  avançada  de  agentes  que  trabalham  juntos, 
Unknown (2213.11):  mas  pode-lhe  dar  100  quadros  e  dizer-lhe, 
Unknown (2216.89):  vá 
Unknown (2218.06):  para  todos  e  me  dê  algo. 
Unknown (2222.11):  Ele  vai  abrir  um  por 
Unknown (2225.29):  um, 
Unknown (2225.43):  realmente  vai  levar  tempo, 
Unknown (2226.55):  não  importa  o  quanto  é, 
Unknown (2228.8):  ele  vai  abrir  um  por  um  e  ele  vai  construir  para  si  mesmo  sempre  tarefas, 
Unknown (2233):  vai  aprimorar  elas. 
Unknown (2236.06):  Então, 
Unknown (2236.26):  digamos  que  eu  dê  uma  data  muito  grande  e  eu  quero  que  ele  faça  uma  estatística  e  escreva  e  dê  informações, 
Unknown (2241.81):  então  modelos  de  reasoning  e  compreensão  podem  ser  melhores  do  que, 
Unknown (2250.88):  digamos, 
Unknown (2251.62):  4-1, 
Unknown (2251.8):  opus. 
Unknown (2252.95):  Mas  em  tarefas  diárias, 
Unknown (2255.07):  ou  habilidades  de  agentes, 
Unknown (2258.25):  também  entender  outro  agente, 
Unknown (2260.35):  também  se  conectar  com  outro  agente, 
Unknown (2263.29):  então  é  bom. 
Unknown (2266.25):  Aqui  também  tem  a 
Unknown (2268.98):  pesquisa, 
Unknown (2269.85):  e  tem  aqui 
Unknown (2272.71):  integrações 
Unknown (2274.82):  Drive,  Gmail  e  Calendar. 
Unknown (2276.32):  É  possível  aplicar  o  Extended  Thinking. 
Unknown (2280.65):  E  também  podemos  dizer  como  fazer  custom  style. 
Unknown (2285.87):  No  final, 
Unknown (2287.0):  quando  fiz  isso, 
Unknown (2291.03):  tentei  entender  o  que  era  o  seu  trabalho. 
Unknown (2294.26):  E  então, 
Unknown (2295.57):  agora, 
Unknown (2295.93):  eu  pensei  apenas  nas  provas  que  havia  até  agora. 
Unknown (2298.05):  Como  se  eu  tivesse  um  aluno  que  não  sabia. 
Unknown (2300.94):  Eu  preciso  de  um  aluno  que  não  tenha  um  grande  respeito 
Unknown (2313.98):  o 
Unknown (2315.84):  que  é  isso? 
Unknown (2316.88):  o  que  é  isso? 
Unknown (2317.32):  o  que  é  isso? 
Unknown (2317.93):  no  final  não  se  trata 
Unknown (2320.8):  de  um  modelo  para  saber  quando  usar  todo  o  modelo  todo  o  modelo  precisa  saber  o  que  é  agora  aqui  eu  posso  adicionar  um  elemento  vejam  aqui  eu  adicionei  de  forma  jurídica  o  Zapier 
Unknown (2338.58):  Zapier 
Unknown (2340.5):  é  adicionar  mais  uma  linha  de  formação  para  o  MCP  porque  ele  é  na  própria  plataforma  de  automação  ou  seja, 
Unknown (2351.39):  através  do  Zapier  eu  posso  adicionar  tudo  o  que  se  conecta  ao  Zapier  eu  posso  adicioná-lo  aqui  e  não, 
Unknown (2357.12):  por  exemplo, 
Unknown (2358.09):  se  eu  quiser  trocar  os  dados  do  TimeOS  eu  não  sei  se  ele  se  conecta  ao  Zapier 
Unknown (2368.39):  Se  eu  não  tenho  um  server  de  MCP  para  TimeOS, 
Unknown (2371.59):  mas  ele  se  conecta  ao  Zapier, 
Unknown (2374.09):  então  eu  posso  se  conectar  aqui. 
Unknown (2376.11):  Isso  não  é  verdade  sobre... 
Unknown (2380.82):  OpenAI, 
Unknown (2381.14):  olhem, 
Unknown (2381.4):  eu  tentei  conectar  ao  Zapier, 
Unknown (2383.68):  eles  são  mais  amplios. 
Unknown (2387.27):  E  o  que  ele  me  diz... 
Unknown (2399.05):  Seu  Pai, 
Unknown (2399.43):  eu  te  ab 
Unknown (2400.36):  porque  as  tarefas  não  podem  ser  usadas  como  informações  de  pesquisa  ou  digamos  que  não  são  realmente  necessárias 
Unknown (2416.93):  eles 
Unknown (2417.35):  se  definem  a  si  mesmos  no  que  os  servidores  usam 
Unknown (2421.53):  aqui  temos  a  Asana  temos  o  DR 
Unknown (2428.54):  tem  também  o  PayPal, 
Unknown (2429.92):  podemos  dizer  o  quanto  custa  tem  o 
Unknown (2438.27):  Notion,  se  decidimos  usar  ele  para  database  ou  para  memória 
Unknown (2451.9):  e  eles  aqui, 
Unknown (2453.74):  algo  de  database  que... 
Unknown (2458.73):  Agora, 
Unknown (2460.09):  todas 
Unknown (2462.96):  as  plataformas 
Unknown (2468.93):  que  estão  no  final  não  são  ideais  para  nós. 
Unknown (2472.68):  Precisamos  de  mais  facilidade. 
Unknown (2475.82):  Por  isso, 
Unknown (2477.09):  é  importante  lembrarmos  do  que  existe  aqui, 
Unknown (2478.78):  que  vocês  também  vão  usar. 
Unknown (2480.17):  Por  exemplo, 
Unknown (2481.17):  no  meu  caso, 
Unknown (2481.9):  entregaram  o  Drive, 
Unknown (2483.23):  o  Gmail, 
Unknown (2484.47):  o  Zapier, 
Unknown (2485.0):  e  também  tentaram  usar  o  próprio, 
Unknown (2486.76):  para  entender  como  funciona. 
Unknown (2490.65):  e  também  a  sua  própria  área  de  trabalho. 
Unknown (2494.45):  Digamos  que  aqui  tem  o  projeto. 
Unknown (2497.6):  Então  eu  faço  um  projeto, 
Unknown (2500.04):  coloco  os  meus  pontos  dentro  do  projeto, 
Unknown (2503.16):  então  aqui  eu  defino  o  que  fazer, 
Unknown (2507.18):  onde? 
Unknown (2510.57):  defino  o  que  fazer, 
Unknown (2512.65):  e  então  adiciono  o  conhecimento. 
Unknown (2515.95):  Toda  vez  que  eu  trabalho  sobre  o  projeto, 
Unknown (2518.4):  ele  também... 
Unknown (2521.18):  que  lhe  ocorre  o  conhecimento  é  a  mesma  coisa  no  projeto 
Unknown (2526.16):  de  OpenAI  Agora, 
Unknown (2530.66):  a  partir  da  ideia  de  uma  obra  contínua  há  dois  conceitos  importantes  para  entender  há  o  conceito  de  base  de  conhecimento  ou  database  que  eu  uso  como  referência  e 
Unknown (2546.84):  há 
Unknown (2547.23):  o  conceito  de  memória 
Unknown (2551.4):  Knowledge  base  é  algo  que  eu  consigo... 
Unknown (2555.98):  que  é  constante, 
Unknown (2557.07):  na  verdade. 
Unknown (2559.26):  Eu  entro  sempre, 
Unknown (2560.95):  mas  não  o  lembro, 
Unknown (2562.81):  não  o  reajudo. 
Unknown (2564.28):  Memorial  é 
Unknown (2567.19):  algo  diferente, 
Unknown (2568.04):  certo? 
Unknown (2568.47):  E  é  algo  que... 
Unknown (2569.26):  que  é  como  se  fosse  adicionado  ao  meu  database  as  coisas  que  eu  fiz  durante  as  conversas  que  eu  fiz... 
Unknown (2583.68):  O  memory  é  sempre  ligado  ao  chat, 
Unknown (2585.84):  ou 
Unknown (2588.41):  seja, 
Unknown (2590.75):  é  o  conteúdo  do  chat. 
Unknown (2593.34):  Databases  são  coisas  que  eu  insiro  de  fora. 
Unknown (2595.25):  Como  isso  se  conecta? 
Unknown (2612.49):  Em  nosso  ambiente  de  trabalho  ideal, 
Unknown (2616.83):  deve  haver  um  chat 
Unknown (2621.14):  que  usamos  como  serviço  pessoal, 
Unknown (2627.61):  que  usamos  para  questões  de  trabalho, 
Unknown (2631.89):  para  pesquisa. 
Unknown (2640.57):  e  não  sei, 
Unknown (2640.73):  todos  os  tipos  de  tarefas. 
Unknown (2643.95):  Precisa  ser  conectado  ao  project  management  tool, 
Unknown (2646.8):  ao  calendar, 
Unknown (2648.3):  ao  database  e  ao 
Unknown (2650.67):  memory  tool, 
Unknown (2652.07):  ao  e-mail  e  ao  matrix. 
Unknown (2654.13):  Desses  recursos, 
Unknown (2658.53):  nós  criamos  a  agent. 
Unknown (2660.78):  A 
Unknown (2662.4):  definição  de  agent, 
Unknown (2664.23):  quando  definimos  agent, 
Unknown (2665.35):  então  definimos  no  início, 
Unknown (2666.56):  a  instrução  do  sistema, 
Unknown (2672.02):  quais  são  os  ferramentas  que  queremos  utilizar  e  na  instrução, 
Unknown (2676.28):  como  usarmos  isso 
Unknown (2678.62):  o  modelo, 
Unknown (2679.74):  os  parâmetros  e  a  ligação  com  outros  agentes  hoje, 
Unknown (2683.91):  é  possível, 
Unknown (2686.86):  sem  problemas, 
Unknown (2694.11):  fazer  uma  operação  de  agentes  conectar  entre  eles 
Unknown (2703.33):  Vamos  dizer, 
Unknown (2704.33):  eu  sim, 
Unknown (2706.15):  como  o  Ahmad  vai  trabalhar  sobre  o  MNTM, 
Unknown (2708.03):  talvez  Ahmad  na  próxima  apresentação, 
Unknown (2713.71):  você  crie  um  workflow  fundamental, 
Unknown (2715.73):  você  o  apresente  para  que  também  o  Stavi... 
Unknown (2718.65):  Para  o  MNTM? 
Unknown (2719.47):  Sim, 
Unknown (2719.62):  para  que  ele  entenda  o  que  é  um 
Unknown (2723.97):  Node,  o  que  é  um 
Unknown (2725.83):  workflow, 
Unknown (2726.61):  como  funciona. 
Unknown (2729.92):  um  pouco  sobre  API  e  Web  Work 
Unknown (2732.78):  Night,  entre  eles, 
Unknown (2735.32):  e  também  sobre  sistemas. 
Unknown (2735.78):  Sim, 
Unknown (2735.86):  vamos  dizer  que  nós  não  precisaremos  fazer  ou  construir  essas  coisas  de  zero, 
Unknown (2744.27):  porque 
Unknown (2746.39):  David,  aquele  cara  que  nos  deu  os  dados, 
Unknown (2749.4):  construiu  uma 
Unknown (2752.64):  plataforma  chamada 
Unknown (2757.92):  Alfred. 
Unknown (2760.12):  Alfred  OS  e  lá 
Unknown (2764.36):  tem  conectados  um 
Unknown (2767.28):  calendário, 
Unknown (2767.98):  um  e-mail  tipo  um  botão  que  sabe  conectar  qualquer  calendário  que  você  quiser 
Unknown (2774.46):  um  e-mail  uma 
Unknown (2776.89):  plataforma  de  publicações  tem  lá  na  área  da  plataforma 
Unknown (2783.6):  também  a  possibilidade  de  construir  agentes  e  conectá-los  juntos 
Unknown (2788.34):  que  funciona  tanto  na  NA10  quanto 
Unknown (2794.5):  em  outra  plataforma  chamada  Ghost  que  eu  ainda  não  me  conectei  com  o  software  mas  é  algo  que  deve  ser  útil  para  tudo  o  que  estamos  procurando  que 
Unknown (2809.39):  pode 
Unknown (2809.66):  ajudar  a  gente, 
Unknown (2810.24):  mas  eu  quero  que  a  gente  controlasse  muito  bem  na  NA10 
Unknown (2820.11):  Você  pode  dizer  que  David 
Unknown (2823.03):  tem  coisas  que  eu  não  entendo  da  NITM? 
Unknown (2828.18):  David, 
Unknown (2828.86):  entre  as  reuniões, 
Unknown (2830.06):  você  pode  falar  com 
Unknown (2834.54):  ele, 
Unknown (2835.2):  mas  as  suas  palavras  não  são  apenas  a  hora  da  reunião. 
Unknown (2843.37):  NITM, 
Unknown (2847.57):  sucesso. 
Unknown (2849.83):  E  para  usar 
Unknown (2854.25):  o 
Unknown (2854.84):  Memory, 
Unknown (2857.34):  esqueci  de  dizer  que  tem  outra  plataforma  que  se  conecta  com  o  Superbase, 
Unknown (2861.32):  que  é  o  Chat 
Unknown (2863.02):  Memory. 
Unknown (2865.88):  Você  vai  ver, 
Unknown (2867.23):  eu  vou  escrever  no  YouTube, 
Unknown (2868.91):  no  Superbase, 
Unknown (2870.51):  o  Chat  Memory, 
Unknown (2870.99):  você  vai  ver. 
Unknown (2871.99):  O 
Unknown (2875.21):  conceito  do  MCP. 
Unknown (2878.3):  Vamos  investigar  isso. 
Unknown (2889.72):  E... 
Unknown (2889.82):  É  isso. 
Unknown (2892.34):  Você  está  falando. 
Unknown (2893.0):  Agora  estou 
Unknown (2898.2):  falando. 
Unknown (2898.53):  Ok. 
Unknown (2898.61):  Nós  revelamos  algumas  coisas  que  queríamos  apresentar. 
Unknown (2902.37):  Então, 
Unknown (2903.04):  eu  vou  sair  daqui, 
Unknown (2904.62):  da  parte  de  Management  de  Lógica  e  Routes  de  IBI. 
Unknown (2907.92):  Para  o  Zerami, 
Unknown (2910.9):  para  o  e-learning, 
Unknown (2914.34):  eu  vou  mais  para  a  próxima  apresentação, 
Unknown (2921.11):  que  ainda  não  me  avancei  muito  na  próxima  apresentação, 
Unknown (2930.18):  mas  é  algo  inicial  que  olhamos  juntos  e  por  causa... 
Unknown (2934.81):  que  vocês  sejam  mais  no  seu  campo, 
Unknown (2936.38):  então  podemos  adicionar  ou  dar  informações  sobre 
Unknown (2941.18):  isso. 
Unknown (2942.26):  Agora, 
Unknown (2942.82):  e... 
Unknown (2942.84):  Ah, 
Unknown (2942.9):  peraí. 
Unknown (2944.4):  Tem  uma  pergunta, 
Unknown (2945.18):  talvez  venhamos  a  isso  em  seguida. 
Unknown (2948.55):  As  prompters  que  o  Stav  está  trabalhando, 
Unknown (2951.88):  já  existe 
Unknown (2955.45):  a  database  que  ele  solicitou  na  prompter, 
Unknown (2958.06):  e  eu  queria  perguntar, 
Unknown (2962.14):  eu  quero  expor... 
Unknown (2964.06):  Então, 
Unknown (2964.49):  se  você  verificar, 
Unknown (2965.69):  eu  gostaria  de  perguntar  se  você  tem  a  opção  de  fazer  uma  comparação  entre  eles, 
Unknown (2969.91):  ou  modelos  que  não  se  relacionam. 
Unknown (2972.68):  Eu  imagino  que  você  tenha  3,5, 
Unknown (2977.24):  4, 
Unknown (2977.74):  ou 
Unknown (2978.66):  4,1,  ou  2, 
Unknown (2982.11):  como  você  quer  que  sejam. 
Unknown (2983.54):  Eu  não  dou  a  resposta, 
Unknown (2984.34):  porque  é  o  que  você 
Unknown (2986.81):  vai  fazer. 
Unknown (2993.31):  e  a  gente  vai  estudar  cada  um  de  nós. 
Unknown (2996.26):  E  também  tentaremos  reforçar  o  nosso  processo. 
Unknown (2998.94):  Os  concursos  são  muito  bons. 
Unknown (3031.58):  Você  também  precisa  comprovar  os  modelos  de  OpenAI, 
Unknown (3034.74):  de 
Unknown (3036.22):  Cloud  e  de  Google. 
Unknown (3038.57):  Agora, 
Unknown (3039.55):  eu  lhe  digo, 
Unknown (3040.11):  entre  no  manus, 
Unknown (3041.71):  escreva-lhe 
Unknown (3044.67):  a  tarefa  e  apresente  a  sua  resultado. 
Unknown (3048.6):  Como, 
Unknown (3048.81):  escreva  isso, 
Unknown (3051.5):  prepare-se, 
Unknown (3051.99):  mas  você  não  precisa  fazer  nada. 
Unknown (3054.16):  Então, 
Unknown (3054.27):  isso  é  o  que  eu  estou  fazendo. 
Unknown (3062.16):  Mas  sim, 
Unknown (3063.42):  mas  o  que? 
Unknown (3063.77):  É  preciso  que  você  se  acostumar  a  usar  os  mecanismos  do  Researcher, 
Unknown (3067.61):  que  é  o  mais  inteligente. 
Unknown (3069.21):  Sim, 
Unknown (3069.31):  é  o  que  fiz  agora  com  os  agentes, 
Unknown (3072.39):  mas 
Unknown (3074.24):  me  parece 
Unknown (3076.53):  que  havia  muito  pouco, 
Unknown (3078.29):  porque  ele  me  deu  uma  tabela, 
Unknown (3080.46):  mas  não  no  uso  físico, 
Unknown (3081.46):  mas  no  físico. 
Unknown (3082.78):  Isso  é  também  uma  das  coisas  que  eu  gostaria  de  saber, 
Unknown (3089.95):  como  orientá-los. 
Unknown (3091.38):  Eu  sempre  pergunto  a  você  sobre  cada  clica  de  pre-search. 
Unknown (3094.71):  Sim, 
Unknown (3105.44):  eu  sempre  pergunto 
Unknown (3126.21):  E  agora, 
Unknown (3128.27):  sobre  os  resultados  automáticos, 
Unknown (3131.78):  o  grader, 
Unknown (3133.04):  todo  o  projeto  da  clínica, 
Unknown (3139.06):  você  precisaria  fazer  algo  sobre 
Unknown (3144.98):  isso? 
Unknown (3151.13):  Eu  lembro  que  eu  te  dei  um  sinal  no  ano  passado, 
Unknown (3154.09):  mas  em  um  segundo  eu  me  apercebi  com  essa  ideia, 
Unknown (3156.93):  me  ajudaram  a  trabalhar, 
Unknown (3158.07):  e  eu  tive  que  definir  o  projeto. 
Unknown (3159.53):  E  é  por  isso  que  eu  disse  isso. 
Unknown (3164.36):  Sim, 
Unknown (3164.55):  eu  também. 
Unknown (3165.54):  Os  trabalhos  são  fáceis, 
Unknown (3169.71):  como  o  chatbot  e  o 
Unknown (3174.98):  platform  de  educação  de  projetos. 
Unknown (3201.82):  Não, 
Unknown (3202.22):  na  verdade, 
Unknown (3204.6):  há  dois. 
Unknown (3206.16):  Eu  também  fiz, 
Unknown (3207.18):  mas  agora... 
Unknown (3208.92):  Vamos  dizer, 
Unknown (3209.2):  temos  que  começar  agora, 
Unknown (3210.17):  quando  temos  a... 
Unknown (3210.83):  Decidimos  que  estamos  falando  sobre  a  SANA, 
Unknown (3214.05):  certo? 
Unknown (3214.27):  Então, 
Unknown (3214.37):  temos  que  começar  a  usá-la. 
Unknown (3215.39):  E... 
Unknown (3215.51):  Nós  definimos  os  projetos  na  semana  passada. 
Unknown (3219.64):  Sim, 
Unknown (3223.7):  e  talvez  você  tenha  decidido, 
Unknown (3228.38):  no  seu... 
Unknown (3228.58):  No  seu... 
Unknown (3228.78):  No  seu... 
Unknown (3228.97):  Como... 
Unknown (3229.27):  Como... 
Unknown (3243.11):  Primeiramente, 
Unknown (3244.91):  para  caracterizar  o  projeto  de 
Unknown (3248.69):  tudo  o  que  temos, 
Unknown (3254.32):  entre  todos, 
Unknown (3255.51):  eu  vou  dar  a  você  a  liberdade  de  definir, 
Unknown (3257.76):  mas, 
Unknown (3257.88):  em  grande, 
Unknown (3259.43):  o  que  precisamos  é  o  que  esse  projeto  quer. 
Unknown (3267.89):  o  que  é  o  input  e  o  output, 
Unknown (3272.09):  e 
Unknown (3273.49):  precisamos 
Unknown (3279.43):  de  todas  as  exemplos  verdadeiros, 
Unknown (3282.16):  evaluadores  para  todos, 
Unknown (3284.04):  e  os  feedbacks  e  o  que  queremos. 
Unknown (3289.65):  Porque  eu  quero  que  em  alguns  meses... 
Unknown (3295.69):  Vamos  chegar  ao  ponto  com  todo  o  que... 
Unknown (3300.03):  que  temos  uma  sistema  automático  que  analisa  as  análises, 
Unknown (3302.53):  o  que  você  faz  se  tem  feedbacks  da  equipe  ou  se, 
Unknown (3304.05):  por  exemplo, 
Unknown (3304.69):  Vamos  construir  um  sistema  de  perguntas  que  é  enviado  a  cada  semana, 
Unknown (3310.76):  mês, 
Unknown (3311.26):  e  vamos  fazer  uma  avaliação  mensal  para  cada  pessoa. 
Unknown (3323.59):  Agora, 
Unknown (3325.23):  nós  não  vamos  encontrar... 
Unknown (3330.42):  A  agenda  da  psiquiatra  deve  ser  algo  mais, 
Unknown (3335.15):  da  administrativa, 
Unknown (3335.95):  porque  ainda  é  uma  área  inicial, 
Unknown (3336.79):  todo  o  campo  dos  filhos  não  foi  realmente... 
Unknown (3342.89):  não  fizemos  alguma  otimização, 
Unknown (3345.32):  dissemos  que  no  raciocínio  da  psiquiatra  queremos  separar  o  status  só, 
Unknown (3353.24):  e 
Unknown (3354.64):  que  se  tivermos  dois  prontos, 
Unknown (3356.36):  um  só  passará  pela  avaliação, 
Unknown (3358.56):  Eu  espero  que  isso  também  vá  para  o  projeto. 
Unknown (3364.77):  Havia  muitas  coisas  sobre  as  quais  falamos  nos  projetos, 
Unknown (3367.39):  mas 
Unknown (3369.51):  vamos  chegar  e... 
Unknown (3370.61):  Vamos  encerrar  tudo. 
Unknown (3374.1):  Tem  que  começar  com... 
Unknown (3375.38):  De  fato, 
Unknown (3376.61):  é  um  papel  de  definição  de 
Unknown (3381.13):  cada  projeto, 
Unknown (3383.61):  no  conceito  de  gestão  de  projetos. 
Unknown (3388.51):  para  poder  afetar  também  a  doença. 
Unknown (3393.31):  Sim. 
Unknown (3393.37):  Enquanto  isso, 
Unknown (3393.63):  posso  mostrar  para  vocês  uma  foto  de  um  prontocard, 
Unknown (3396.55):  de  toda  a  sua  pele. 
Unknown (3398.06):  O  que  você  poderia  melhorar, 
Unknown (3399.44):  que  o  chat  fez, 
Unknown (3399.82):  de  acordo  com  as  dicas  da  Adriana, 
Unknown (3401.78):  e  os  exemplos  da  sua  avó, 
Unknown (3403.16):  que  ela  não  tinha  mais  a  ver 
Unknown (3414.84):  com  a  doença. 
Unknown (3420.94):  Então, 
Unknown (3424.63):  há  uma  ideia  de  que  a  gente  tem  que  ter  gênero, 
Unknown (3425.69):  mas  isso 
Unknown (3428.29):  é  o  que  o  homem  diz  para  mim. 
Unknown (3431.13):  É  antes  de  entender  o  que... 
Unknown (3434.3):  porque  isso  é  o  que  o  homem  diz  para  mim. 
Unknown (3435.03):  Nós  precisamos, 
Unknown (3435.39):  mas, 
Unknown (3436.34):  por  favor, 
Unknown (3436.59):  fazer  um  filme  de  que  nós  precisamos  ver  mais. 
Unknown (3438.62):  Vamos  dizer  que, 
Unknown (3438.94):  no  final, 
Unknown (3439.14):  precisamos  chegar  a  algum  modelo  de 
Unknown (3442.25):  estrutura  dentro  da  casa. 
Unknown (3444.51):  Eu  sugiro  que  comece  a  usar  isso, 
Unknown (3447.53):  entenda  o  modelo. 
Unknown (3448.85):  Se  eu  não  me  engano, 
Unknown (3450.57):  há  diferenças  entre  scopes, 
Unknown (3456.14):  Workspace, 
Unknown (3456.98):  Project, 
Unknown (3457.62):  Task, 
Unknown (3458.62):  então  comece  a  entender  o  que  cada  um... 
Unknown (3462.01):  Você  precisa  construir  sua  hierarquia  e  dividir 
Unknown (3468.84):  bem. 
Unknown (3469.84):  Você  sabe  onde... 
Unknown (3474.73):  e  aí  a  gente  vai  fazer  um  projeto  e  depois  para  cada  um  nós  vamos  construir  um  database  o  database  vai  explicar  o  que  é  esse  prompt  pode  ser  um  contexto  geral  do  que  estamos  fazendo  e  então  para  cada  um  tem  um  contexto 
Unknown (3491.9):  sobre  ele, 
Unknown (3492.95):  por  exemplo, 
Unknown (3493.59):  esse  prompt  ele  toma  um  resumo  psiquiátrico 
Unknown (3502.11):  Se  temos  alguma  compreensão  sobre  o  que  nós  fizemos  com  os  dados, 
Unknown (3507.43):  nós  adicionamos  isso  para  a  sua  data. 
Unknown (3508.78):  Agora, 
Unknown (3509.03):  comece  com  os  dados  básicos. 
Unknown (3513.06):  Você  pode  abrir  um  código  básico  para  cada  projeto. 
Unknown (3516.73):  Vamos  dizer, 
Unknown (3517.53):  um  código  de  contexto  global, 
Unknown (3520.76):  e  então, 
Unknown (3522.47):  códigos  para  cada  um, 
Unknown (3523.89):  para  cada  um  deles, 
Unknown (3525.59):  também  que  tenha  contexto, 
Unknown (3527.55):  esboço. 
Unknown (3528.38):  Eu  acho  que  você  também  tem  coisas  boas... 
Unknown (3531.66):  e  os  alunos  aqui  e  lá. 
Unknown (3532.75):  E  mais  algo... 
Unknown (3536.87):  Vou  fazer  uma  subscrição  para  a  Asana. 
Unknown (3557.75):  Se  isso  nos  ajuda  ou  se  é  melhor 
Unknown (3563.59):  trabalhar  assim? 
Unknown (3565.84):  Não, 
Unknown (3565.95):  se  antes  de  tudo, 
Unknown (3569.21):  se  precisar. 
Unknown (3570.3):  Não, 
Unknown (3570.8):  se  é  mais  fácil, 
Unknown (3571.28):  sim. 
Unknown (3571.48):  Se  há  um  som, 
Unknown (3571.82):  se  é  possível  trabalhar  sem  o  navio. 
Unknown (3575.32):  Aqui 
Unknown (3578.76):  eu  uso  isso  para  escrever  explicações. 
Unknown (3584.35):  mas  tem  aqui  no  chat, 
Unknown (3586.11):  no  Playground  um  tipo  de  que  eu 
Unknown (3592.5):  coloquei  no  VectorStore  que  tem  resumidos  para  todas  as  reuniões  que  eu 
Unknown (3600.09):  Eu  me  envolvi  com  isso, 
Unknown (3602.93):  desde  a  época  em  que... 
Unknown (3604.37):  Agora, 
Unknown (3605.29):  qualquer  contexto  que  nós  queiramos  construir, 
Unknown (3610.3):  podemos  fazer  isso  daqui. 
Unknown (3612.36):  Vocês  podem  entrar, 
Unknown (3616.81):  eu 
Unknown (3618.17):  coloquei  aqui  para  mim, 
Unknown (3620.59):  digamos, 
Unknown (3620.95):  o  meu  contexto  global, 
Unknown (3622.68):  sobre  o  que  eu  faço, 
Unknown (3624.18):  onde  eu  trabalho, 
Unknown (3625.57):  etc. 
Unknown (3625.97):  E  como  ele  deveria  escrever. 
Unknown (3629.07):  Depois... 
Unknown (3630.39):  que  eu  não  sabia  que  ele  ia 
Unknown (3634.34):  escrever  para  mim, 
Unknown (3636.68):  você  pode  fazer 
Unknown (3648.16):  isso? 
Unknown (3704.44):  Também  aqui  é  possível  adicionar... 
Unknown (3708.94):  Para  que  vocês 
Unknown (3719.15):  saibam 
Unknown (3727.6):  como... 
Unknown (3727.93):  Eu  tenho  aqui  o  VectorStore... 
Unknown (3730.76):  ou  3  corpos  se  vocês  precisarem  de  algo  mais  legal  podemos  colocar  aqui  e  vamos  lá  vamos  lá 
Unknown (3791.96):  Agora  aqui  não  tem... 
Unknown (3793.78):  eu  não  coloquei  a  quantidade  de  prompt, 
Unknown (3795.44):  não  coloquei  a  quantidade  de  código  que  fizemos, 
Unknown (3797.8):  até  que  ele  tenha  um  workflow. 
Unknown (3799.05):  Aqui  é  um  exemplo  de  se... 
Unknown (3800.14):  se  nós  já  mencionamos  isso  em  perguntas, 
Unknown (3804.93):  então... 
Unknown (3805.39):  é  bom  para  o  contexto  global, 
Unknown (3809.94):  vocês  podem  adicionar... 
Unknown (3812.06):  eu  quero  dizer, 
Unknown (3813.03):  adicionar  todos  os  prompt, 
Unknown (3815.74):  e  assim  por  diante. 
Unknown (3816.84):  E  é  possível  fazer  com  o  gpt, 
Unknown (3819.27):  quando  conectamos  ele  ao  drive... 
Unknown (3822.34):  Se  tem  os  blocos  lá, 
Unknown (3823.48):  pode  dizer  para  ele, 
Unknown (3825.98):  conclua-me, 
Unknown (3826.58):  escreva-me  dentro  disso. 
Unknown (3828.57):  Também  pode  fazer  uma  pesquisa  profunda 
Unknown (3839.55):  para  indicar  que  vai  usar  o  botão. 
Unknown (3846.52):  Então, 
Unknown (3846.66):  é  mais  claro  o  que  você  quer  fazer? 
Unknown (3848.32):  Sim. 
Unknown (3848.66):  Quer  dizer, 
Unknown (3849.16):  nós  dividimos  isso  em  projetos  ativos  e  futuros. 
Unknown (3851.8):  Existem  alguns  projetos  que  pensei  em... 
Unknown (3856.02):  que 
Unknown (3859.61):  eu  quero  que  eles  sejam  inscritos  no  programa  de  trabalho  para  o  futuro  próximo, 
Unknown (3866.45):  relativamente. 
Unknown (3867.17):  Eu  quero  que  cada  tratador  receba... 
Unknown (3892.67):  Mas... 
Unknown (3926.29):  é  uma  chave  também 
Unknown (3933.57):  é  que  a  pele  e  também  se  foi  a  nossa  que  vai 
Unknown (3940.14):  passar 
Unknown (3940.68):  pelos  dois  lados  e  dar  uma  olhada  em  relação  ao 
Unknown (3951.26):  tempo. 
Unknown (3953.19):  sobre  o  que  o  treinador  conseguiu  fazer, 
Unknown (3956.49):  coisas  que  ele  fez  bem, 
Unknown (3957.63):  coisas  que  ele  fez  mal, 
Unknown (3960.14):  perguntar  as  perguntas  que  precisava, 
Unknown (3963.22):  ter  empatia, 
Unknown (3965.92):  todas  essas  coisas  que  nós  queremos, 
Unknown (3967.34):  que  são  tarefas  que  queremos  lidar  com, 
Unknown (3972.0):  nós  enviamos  isso  para  um  treinador  com  recomendações  sobre  o  que  deve  ser  melhor. 
Unknown (3983.5):  E  eu  quero  dizer  que  nós  tentamos 
Unknown (3992.07):  fazer  uma  pesquisa  psiquiátrica  e  foi  muito  random. 
Unknown (3997.63):  O  que  eu  quero  é  entender  quando  o  tratador  começa  a  fazer  a  pesquisa  sozinho. 
Unknown (4011.52):  Ou  seja, 
Unknown (4011.64):  se  o  índice  do  operador  de  pacientes  hoje  é  de  cerca  de  meia  semana, 
Unknown (4018.81):  mas  há  operadores  de  pacientes  que  são  bastante  ativos  e  terminam  o  índice  em  20  minutos  e  tomam  um  descanso  em  10  minutos. 
Unknown (4035.8):  Então, 
Unknown (4035.95):  eu  saio  de  forma  passiva, 
Unknown (4036.39):  sem... 
Unknown (4036.51):  é  realmente... 
Unknown (4037.07):  sempre  escrever  e  perceber  quando  alguém  consegue  fechar  a  reunião  e  manter  a  facilidade, 
Unknown (4045.25):  a  qualidade  da  reunião, 
Unknown (4049.34):  vir  e  oferecer  a  ele  que 
Unknown (4053.21):  a  organização  me  oferece, 
Unknown (4055.38):  que  eu 
Unknown (4058.43):  tenho  uma  ideia  e... 
Unknown (4065.92):  Então, 
Unknown (4066.62):  quando  a 
Unknown (4068.87):  maioria  dos  trabalhadores  recebe  mais  renda, 
Unknown (4074.19):  eu  sugiro  que  eles  reduzam  a  renda  e  adicionem  mais  dinheiro  por  hora, 
Unknown (4081.62):  que  eles  também  ganham  e  eu  também  obtenho  mais  renda. 
Unknown (4093.82):  O  que  eu  quero  dizer  é  que  não  será  random, 
Unknown (4095.3):  mas  que  eu  vou  para  o  tipo  e  vou  perguntar  para  ele. 
Unknown (4098.66):  Eu  acho  que  isso  é  baseado  em  algo  que  acontece  no  mundo. 
Unknown (4103.18):  Então, 
Unknown (4103.52):  são  duas  coisas  que  eu  pensei  que  eu  quero  adicionar  para  a  nossa  jornada. 
Unknown (4108.1):  Ainda  não  tem  o  que  fazer  com  isso. 
Unknown (4112.54):  Eu  vou  lembrar  disso  que  vai  acontecer  e  dar  uma  dica  para  o  futuro. 
Unknown (4127.11):  Então, 
Unknown (4127.64):  o  que  eu  perciso  é, 
Unknown (4129.8):  talvez  não  façamos  isso  hoje, 
Unknown (4132.16):  mas  sim, 
Unknown (4132.42):  alguma  lista  de  tarefas  que  vocês  querem  perguntar  ao  David. 
Unknown (4139.35):  Eu  não  acho  que  eu  gostaria  do  que  vocês  fizeram  na  semana. 
Unknown (4142.54):  E  vocês  realmente  têm  uma  pergunta. 
Unknown (4146.76):  Quando  nós  começarmos  a  nos  encaixar  nos  meios  de  AI, 
Unknown (4151.19):  em  automação... 
Unknown (4154.99):  como  vai  ser  a  ideia 
Unknown (4157.53):  de  pensar  o  que  vocês  fariam, 
Unknown (4160.69):  das  tarefas  que  vocês  fariam, 
Unknown (4162.68):  o  que  vocês  queriam  adicionar  à  automação, 
Unknown (4165.2):  e  então  poderíamos  chegar  a  eles  com  a 
Unknown (4170.3):  capacidade 
Unknown (4172.62):  de... 
Unknown (4175.45):  Sim. 
Unknown (4175.84):  Muito  bem. 
Unknown (4176.97):  Agora, 
Unknown (4177.39):  Estav, 
Unknown (4178.36):  eu  vou  enviar  para  você  a... 
Unknown (4179.75):  Eu 
Unknown (4182.34):  vou  escrever  a  frase. 
Unknown (4183.45):  E... 
Unknown (4183.61):  Você  está  na  sua  equipe, 
Unknown (4184.73):  as  equipes  relevantes 
Unknown (4190.1):  que  fazem  com  que  haja  problemas  e  problemas, 
Unknown (4194.24):  então  pense  nisso. 
Unknown (4195.64):  E  se  há  algo  que  precisa  de  tratamento, 
Unknown (4199.35):  também  para  mim. 
Unknown (4204.54):  Se 
Unknown (4211.05):  alguém 
Unknown (4213.81):  quiser 
Unknown (4226.08):  que 
Unknown (4228.17):  eu... 
Unknown (4230.42):  Falamos  fora  da  atividade, 
Unknown (4232.15):  isso  pode  ser  algo  técnico, 
Unknown (4233.61):  digamos, 
Unknown (4234.21):  coisas  que  eu  não  sei, 
Unknown (4237.19):  que  eu  aprendo  sem  entender, 
Unknown (4238.39):  que  eu  não  entendo  bem, 
Unknown (4240.43):  digamos, 
Unknown (4240.88):  como  faz. 
Unknown (4241.49):  Quando  ele  te  apresentar  e  te  conhecer, 
Unknown (4245.7):  você  terá  dificuldades. 
Unknown (4248.28):  Sim, 
Unknown (4248.77):  sim. 
Unknown (4249.06):  Então, 
Unknown (4256.92):  ok. 
Unknown (4257.25):  Eu  acho  que  esse  é  o  passo  mais  importante. 
Unknown (4261.48):  e 
Unknown (4263.46):  a  importância  do  projeto. 
Unknown (4264.5):  Eu  pedi  para  o  Shachar  o  resumo  do  diretor  do  TIC, 
Unknown (4268.66):  do  A-TECH, 
Unknown (4269.22):  que  vai  chegar  ao  GEM  em  dois  e  meio  minutos. 
Unknown (4271.32):  Então, 
Unknown (4273.5):  verifique  se  ele  já  fez  isso. 
Unknown (4275.83):  E  também  pedi  para  ele  fazer  uma  tela  de  encontro  do  horário  de  entrada  de  cada  um  dos  alunos. 
Unknown (4287.7):  e  também  a  gente  vai  ter  que  fazer  uma  análise  de  como  a  gente  vai  fazer  a  reação. 
Unknown (4319.65):  É  um  dos  projetos. 
Unknown (4320.13):  Depois  falamos  sobre  isso. 
Unknown (4320.69):  Eu  disse  que  você  poderia  fazer  a  discussão  entre  nós. 
Unknown (4322.99):  Tudo  bem. 
Unknown (4323.92):  Não  faça  isso. 
Unknown (4324.22):  Ok. 
Unknown (4324.28):  E  no  início  do  projeto, 
Unknown (4324.84):  eu  tento... 
Unknown (4325.2):  Eu  não  consigo  fazer  uma  pesquisa. 
Unknown (4327.84):  Então, 
Unknown (4328.0):  eu  não  tento  fazer  uma  pesquisa. 
Unknown (4329.22):  Como  se  fosse  uma  pesquisa  sobre  a  história. 
Unknown (4332.54):  O 
Unknown (4335.96):  que  eu 
Unknown (4337.46):  posso  fazer? 
Unknown (4349.35):  É  possível  tentar, 
Unknown (4350.37):  se  possível, 
Unknown (4350.95):  colocar  um  direito. 
Unknown (4352.46):  É  melhor  também, 
Unknown (4353.26):  é  melhor  conhecer  todo  o  espelho  que  existe. 
Unknown (4362.34):  Não  é  necessário  fazer  isso  na  minha  e-mail? 
Unknown (4367.94):  Não, 
Unknown (4368.17):  é  melhor  que  o  Estado  faça  isso  para  que  você  receba  os  resultados. 
Unknown (4376.35):  Então, 
Unknown (4376.71):  a  staff 
Unknown (4381.05):  de  TLSC, 
Unknown (4384.01):  ela  pode  fazer  e  nos  convidar  para  a  e-mail, 
Unknown (4385.87):  não  precisamos  nos  conectar  com  o  nome  do  usuário  dela. 
Unknown (4397.23):  Ah, 
Unknown (4397.44):  com  a  adição  da  conta. 
Unknown (4399.75):  Com  o  nome  da  inovação, 
Unknown (4401.08):  digamos, 
Unknown (4401.27):  que  já  nos  ajudou. 
Unknown (4402.22):  Não, 
Unknown (4402.36):  eu  vejo  a  sua  e-mail  e  então... 
Unknown (4402.94):  Sim, 
Unknown (4403.02):  que  seja  a  e-mail  dela. 
Unknown (4403.53):  Ah. 
Unknown (4408.92):  O  que  você  disse? 
Unknown (4413.76):  Isso, 
Unknown (4413.96):  bom, 
Unknown (4414.14):  vamos  abrir  uma  e-mail. 
Unknown (4416.05):  E  agora? 
Unknown (4416.51):  Vamos  ver  se  ele  vai  nos  abrir  uma  e-mail. 
Unknown (4419.39):  Inovacion 
Unknown (4420.43):  Studio.  Então, 
Unknown (4421.51):  vamos  lá. 
Unknown (4430.45):  E  agora, 
Unknown (4431.14):  vamos  ver  se  ele  vai  nos  abrir  uma  e-mail. 
Unknown (4468.9):  Seu  amor  é  a  palavra  que  nos  envolve  em  todo  momento. 
Unknown (4472.76):  Então, 
Unknown (4473.24):  eu  vou  te  pedir. 
Unknown (4475.12):  Quando? 
Unknown (4475.28):  Na  próxima  quarta-feira? 
Unknown (4479.55):  Na  próxima  quarta-feira, 
Unknown (4481.96):  em  1  de  dezembro. 
Unknown (4482.74):  Ah, 
Unknown (4482.87):  sim. 
Unknown (4483.01):  Sim. 
Unknown (4483.14):  Sim. 
Unknown (4483.21):  Rami, 
Unknown (4484.09):  me  desculpe, 
Unknown (4484.81):  Rami. 
Unknown (4484.98):  Na  próxima  quarta-feira... 
Unknown (4500.49):  Eu  vou  para  a  próxima  quinta-feira. 
Unknown (4503.63):  Sim, 
Unknown (4506.56):  eu  vou  para  a  próxima  quinta-feira. 
Unknown (4515.51):  Mas  amanhã, 
Unknown (4515.8):  Rami, 
Unknown (4515.89):  no  rádio, 
Unknown (4516.11):  me  lembre. 
Unknown (4516.33):  Eu  não  sei. 
Unknown (4517.18):  Esperem 
Unknown (4519.65):  algo  que  vocês  gostem. 
Unknown (4520.79):  E  eu  vou  entrar. 
Unknown (4522.23):  Eu  tento  fazer  as  primeiras  fotos. 
Unknown (4525.47):  E  então  eu  vou  me  juntar. 
Unknown (4529.5):  Por  que  isso  mudou  para  o  primeiro  ou  para  o  quinto? 
Unknown (4532.2):  O  primeiro  foi  no  evento  culinário, 
Unknown (4536.93):  eu  já  falei  para  vocês, 
Unknown (4538.79):  mas  nós  começamos  a  fazer  o  evento  culinário  no  chef  de  Iapu. 
Unknown (4545.3):  O  primeiro  e  o  quinto  é  a  fotografia. 
Unknown (4553.02):  Então, 
Unknown (4553.41):  você  me  deu  a  foto  e  a  minha  luz  não  importa. 
Unknown (4558.87):  Eu 
Unknown (4562.71):  não  sei  o  que  eu  vou 
Unknown (4565.31):  dizer, 
Unknown (4565.43):  mas  eu  não  sei  o  que  eu  vou  dizer. 
Unknown (4566.29):  Eu  não  sei  o  que  eu  vou  dizer. 
Unknown (4567.79):  Eu  não  sei  o  que 
Unknown (4583.61):  eu 
Unknown (4583.73):  vou  dizer. 
Unknown (4583.91):  Você  pode  me  perguntar. 
Unknown (4597.89):  Você 
Unknown (4605.61):  nos  lembra 
Unknown (4612.39):  de... ... ... ... ... ... ... ... ... ... ... ... ... ... 
Unknown (4617.09):  Então  talvez  na  próxima  reunião  falaremos  sobre... 
Unknown (4620.39):  Vou  deixar  para  vocês  terminar. 
Unknown (4625.51):  ...bídeo, 
Unknown (4625.96):  que  há  dois  meses  não  falamos. 
Unknown (4627.24):  Bom, 
Unknown (4627.38):  amigos. 
Unknown (4627.5):  Tchau. 
Unknown (4630.24):  Tchau.
```