export const ELECTION_INAUGURATION_GUIDE = {
  en: {
    all: "All phases",
    nominate: "Nomination",
    vote: "Election Day",
    certify: "Certification",
    inaugurate: "Inauguration",
    filterLabel: "Filter election-to-inauguration phases",
    note: "This guide walks from primaries through inauguration day, showing where the constitutional guardrails are at each step and what happens when someone tries to break the chain.",
    sections: [
      {
        key: "nominate",
        label: "Nomination phase",
        summary: "The Electoral Commission sets the rules before the race begins. Candidates must meet constitutional eligibility requirements; party primaries operate under EC-administered timetables.",
        steps: [
          {
            title: "EC sets primary dates and ballot-access rules",
            meta: "Art. I §4 / Art. XII §2.1",
            text: "The Electoral Commission, not Congress or any party, establishes the federal election calendar and minimum ballot-access standards. States may hold their own primaries but cannot set rules that block eligible candidates from the general election.",
          },
          {
            title: "Eligibility is confirmed before the ballot is set",
            meta: "Art. III §2.1",
            text: "Candidates for President and Vice President must satisfy constitutional age, citizenship, and residency requirements. The EC confirms eligibility before a candidate appears on the general-election ballot.",
          },
          {
            title: "Public campaign financing is activated",
            meta: "Art. I §7",
            text: "Once a candidate qualifies for the general election ballot, the public campaign finance system activates. Contribution limits and disclosure rules apply regardless of party affiliation or outside spending.",
          },
          {
            title: "Debate access rules prevent exclusion",
            meta: "Art. I §5 / Art. XII §2.2",
            text: "Federally administered debate access rules prevent any private party from excluding ballot-qualified candidates from major public forums. The EC may set objective polling or signature thresholds but cannot discriminate by party.",
          },
        ],
      },
      {
        key: "vote",
        label: "Election Day",
        summary: "Voting is administered by an independent constitutional organ — not by sitting officials who have a stake in the outcome. Emergency powers cannot be used to suppress access or delay counting.",
        steps: [
          {
            title: "Multi-day polling and 15 days of early voting",
            meta: "Art. I §3.2",
            text: "Federal elections span at least three days, with a minimum of fifteen days of early voting before election day. This prevents a single disruption from disenfranchising large populations.",
          },
          {
            title: "The Electoral Commission administers polling, not partisan officials",
            meta: "Art. I §10.1 / Art. XII §2",
            text: "All federal polling places operate under EC authority. No sitting president, governor, or elected official controls ballot tabulation or reporting for a federal race in which they appear.",
          },
          {
            title: "Emergency declarations cannot suppress voting",
            meta: "Art. I §3.4",
            text: "A late emergency declaration cannot be used to close polling places, shorten voting hours, or delay certification without a specific order from a federal court with jurisdiction — issued before the polls open.",
          },
          {
            title: "Ranked-choice voting for House races",
            meta: "Art. I §2",
            text: "House elections use ranked-choice voting in multi-member districts. Voters rank candidates in order of preference; if no candidate reaches quota, lower preferences redistribute until all seats are filled.",
          },
          {
            title: "Preliminary results are published in real time",
            meta: "Art. XII §2.3",
            text: "The EC publishes precinct-level results as they are reported. Unofficial tallies must be clearly labeled as unofficial. Any attempt to suppress or delay publication is a constitutional violation.",
          },
        ],
      },
      {
        key: "certify",
        label: "Certification",
        summary: "Certification is mandatory and time-bound. Courts can pause it for genuine legal disputes, but not indefinitely — and frivolous delay is itself sanctionable.",
        steps: [
          {
            title: "States certify their results within 21 days",
            meta: "Art. I §6.2",
            text: "Each state must certify its federal election results within 21 days of election day. Late certification without a judicial hold triggers automatic escalation to the EC.",
          },
          {
            title: "The EC reviews state certifications for constitutional compliance",
            meta: "Art. XII §2.2",
            text: "The Electoral Commission reviews each state certification against constitutional standards — voter eligibility, proper tabulation procedure, no suppression — before accepting it into the national count.",
          },
          {
            title: "The ACC investigates fraud allegations in parallel",
            meta: "Arts. VIII, XII §3",
            text: "If the EC refers credible evidence of electoral fraud or interference, the Accountability Commission opens an investigation immediately. The investigation runs in parallel with certification; it does not pause the timeline.",
          },
          {
            title: "Presidential results certified within 30 days",
            meta: "Art. I §6.3",
            text: "The EC must certify the presidential election no later than 30 days after election day. If a court has not issued a specific stay before that deadline, certification proceeds automatically.",
          },
          {
            title: "Congressional certification is ministerial",
            meta: "Art. II §3",
            text: "Congress counts and records the certified electoral votes. Individual members may note a formal objection for the record, but no chamber has the power to reject a constitutionally certified result on policy or partisan grounds.",
          },
        ],
      },
      {
        key: "inaugurate",
        label: "Inauguration",
        summary: "From the day after certification, both the outgoing and incoming administrations have affirmative constitutional duties. The transfer is not optional.",
        steps: [
          {
            title: "Transition cooperation begins the day after certification",
            meta: "Art. III §13.2",
            text: "The outgoing President must cooperate with the President-elect beginning the day after EC certification: security briefings, agency access, office space, and key personnel introductions.",
          },
          {
            title: "Federal agencies support transition planning",
            meta: "Art. III §13.3 / Art. XIX §6.2",
            text: "Cabinet departments and independent agencies must provide incoming transition teams with the information necessary to assume responsibility. Congress must fund and support the process.",
          },
          {
            title: "Outgoing officials cannot obstruct or hollow out the state",
            meta: "Art. III §13.4 / Art. XIX §6.1–§6.5",
            text: "The departing administration may not destroy records, rescind prior acts for spite, make last-minute appointments designed to bind the incoming administration, or use expiring authority to sabotage the transition.",
          },
          {
            title: "Oath of office completes the transfer",
            meta: "Art. III §1.2",
            text: "The President-elect takes the constitutional oath before assuming any presidential powers. The Vice President-elect takes the oath at the same ceremony. Both are administered by the Chief Justice.",
          },
          {
            title: "Anti-subversion rules remain active after the handover",
            meta: "Art. III §13.6 / Art. XIX §6.3",
            text: "Former officials who obstruct the lawful transition — before or after inauguration — face removal, disqualification from future office, and potential prosecution. The ACC's jurisdiction does not end when the keys are handed over.",
          },
        ],
      },
    ],
  },
  es: {
    all: "Todas las fases",
    nominate: "Nominación",
    vote: "Día de elección",
    certify: "Certificación",
    inaugurate: "Inauguración",
    filterLabel: "Filtrar fases de la elección a la inauguración",
    note: "Esta guía recorre el proceso desde las primarias hasta el día de la inauguración, mostrando dónde están los resguardos constitucionales en cada paso y qué sucede cuando alguien intenta romper la cadena.",
    sections: [
      {
        key: "nominate",
        label: "Fase de nominación",
        summary: "La Comisión Electoral establece las reglas antes de que comience la carrera. Los candidatos deben cumplir los requisitos de elegibilidad constitucional; las primarias partidistas operan bajo calendarios administrados por la CE.",
        steps: [
          {
            title: "La CE establece las fechas de las primarias y las reglas de acceso a la boleta",
            meta: "Art. I §4 / Art. XII §2.1",
            text: "La Comisión Electoral, no el Congreso ni ningún partido, establece el calendario electoral federal y los estándares mínimos de acceso a la boleta. Los estados pueden celebrar sus propias primarias, pero no pueden establecer reglas que bloqueen a candidatos elegibles en las elecciones generales.",
          },
          {
            title: "La elegibilidad se confirma antes de fijar la boleta",
            meta: "Art. III §2.1",
            text: "Los candidatos a Presidente y Vicepresidente deben cumplir con los requisitos constitucionales de edad, ciudadanía y residencia. La CE confirma la elegibilidad antes de que un candidato aparezca en la boleta de las elecciones generales.",
          },
          {
            title: "Se activa el financiamiento público de campaña",
            meta: "Art. I §7",
            text: "Una vez que un candidato califica para la boleta de las elecciones generales, se activa el sistema de financiamiento público de campaña. Los límites de contribución y las reglas de divulgación se aplican independientemente de la afiliación partidista o el gasto externo.",
          },
          {
            title: "Las reglas de acceso a debates impiden la exclusión",
            meta: "Art. I §5 / Art. XII §2.2",
            text: "Las reglas de acceso a debates administradas federalmente impiden que cualquier entidad privada excluya a candidatos cualificados en la boleta de los principales foros públicos. La CE puede establecer umbrales objetivos de encuestas o firmas, pero no puede discriminar por partido.",
          },
        ],
      },
      {
        key: "vote",
        label: "Día de elección",
        summary: "La votación es administrada por un órgano constitucional independiente, no por funcionarios en ejercicio que tienen interés en el resultado. Los poderes de emergencia no pueden usarse para suprimir el acceso o retrasar el conteo.",
        steps: [
          {
            title: "Votación de varios días y 15 días de votación anticipada",
            meta: "Art. I §3.2",
            text: "Las elecciones federales abarcan al menos tres días, con un mínimo de quince días de votación anticipada antes del día electoral. Esto evita que una sola perturbación prive del derecho al voto a grandes poblaciones.",
          },
          {
            title: "La Comisión Electoral administra las urnas, no funcionarios partidistas",
            meta: "Art. I §10.1 / Art. XII §2",
            text: "Todos los centros de votación federales operan bajo la autoridad de la CE. Ningún presidente, gobernador ni funcionario electo en ejercicio controla la tabulación de boletas ni los informes para una elección federal en la que aparezca como candidato.",
          },
          {
            title: "Las declaraciones de emergencia no pueden suprimir la votación",
            meta: "Art. I §3.4",
            text: "Una declaración de emergencia tardía no puede usarse para cerrar centros de votación, acortar el horario de votación ni retrasar la certificación sin una orden específica de un tribunal federal con jurisdicción, emitida antes de que abran las urnas.",
          },
          {
            title: "Votación por orden de preferencia para escaños de la Cámara",
            meta: "Art. I §2",
            text: "Las elecciones a la Cámara utilizan votación por orden de preferencia en distritos plurinominales. Los votantes clasifican a los candidatos en orden de preferencia; si ningún candidato alcanza el cuórum, las preferencias inferiores se redistribuyen hasta que se cubren todos los escaños.",
          },
          {
            title: "Los resultados preliminares se publican en tiempo real",
            meta: "Art. XII §2.3",
            text: "La CE publica los resultados a nivel de circunscripción a medida que se reportan. Los recuentos no oficiales deben etiquetarse claramente como tal. Cualquier intento de suprimir o retrasar la publicación es una violación constitucional.",
          },
        ],
      },
      {
        key: "certify",
        label: "Certificación",
        summary: "La certificación es obligatoria y tiene plazos fijos. Los tribunales pueden pausarla por disputas legales genuinas, pero no indefinidamente — y el retraso frívolo es en sí mismo sancionable.",
        steps: [
          {
            title: "Los estados certifican sus resultados en 21 días",
            meta: "Art. I §6.2",
            text: "Cada estado debe certificar sus resultados electorales federales dentro de los 21 días posteriores al día electoral. La certificación tardía sin una orden judicial desencadena una escalada automática a la CE.",
          },
          {
            title: "La CE revisa las certificaciones estatales para verificar el cumplimiento constitucional",
            meta: "Art. XII §2.2",
            text: "La Comisión Electoral revisa cada certificación estatal según los estándares constitucionales — elegibilidad de los votantes, procedimiento de tabulación adecuado, ausencia de supresión — antes de aceptarla en el conteo nacional.",
          },
          {
            title: "La CRC investiga en paralelo las denuncias de fraude",
            meta: "Arts. VIII, XII §3",
            text: "Si la CE remite evidencia creíble de fraude o interferencia electoral, la Comisión de Rendición de Cuentas abre una investigación de inmediato. La investigación corre en paralelo con la certificación; no pausa el cronograma.",
          },
          {
            title: "Los resultados presidenciales se certifican en 30 días",
            meta: "Art. I §6.3",
            text: "La CE debe certificar la elección presidencial a más tardar 30 días después del día electoral. Si un tribunal no ha emitido una suspensión específica antes de ese plazo, la certificación avanza automáticamente.",
          },
          {
            title: "La certificación del Congreso es ministerial",
            meta: "Art. II §3",
            text: "El Congreso cuenta y registra los votos electorales certificados. Los miembros individuales pueden anotar una objeción formal para el registro, pero ninguna cámara tiene el poder de rechazar un resultado constitucionalmente certificado por razones políticas o partidistas.",
          },
        ],
      },
      {
        key: "inaugurate",
        label: "Inauguración",
        summary: "A partir del día después de la certificación, tanto la administración saliente como la entrante tienen deberes constitucionales afirmativos. La transferencia no es opcional.",
        steps: [
          {
            title: "La cooperación de transición comienza al día siguiente de la certificación",
            meta: "Art. III §13.2",
            text: "El Presidente saliente debe cooperar con el Presidente electo a partir del día siguiente de la certificación de la CE: sesiones de seguridad, acceso a agencias, espacio de oficina e introducción al personal clave.",
          },
          {
            title: "Las agencias federales apoyan la planificación de la transición",
            meta: "Art. III §13.3 / Art. XIX §6.2",
            text: "Los ministerios y las agencias independientes deben proporcionar a los equipos de transición entrantes la información necesaria para asumir la responsabilidad. El Congreso debe financiar y apoyar el proceso.",
          },
          {
            title: "Los funcionarios salientes no pueden obstruir ni vaciar el Estado",
            meta: "Art. III §13.4 / Art. XIX §6.1–§6.5",
            text: "La administración saliente no puede destruir registros, revocar actos anteriores por despecho, hacer nombramientos de última hora diseñados para vincular a la administración entrante, ni usar autoridades que expiran para sabotear la transición.",
          },
          {
            title: "El juramento de cargo completa la transferencia",
            meta: "Art. III §1.2",
            text: "El Presidente electo presta el juramento constitucional antes de asumir cualquier poder presidencial. El Vicepresidente electo presta el juramento en la misma ceremonia. Ambos son administrados por el Presidente del Tribunal Supremo.",
          },
          {
            title: "Las reglas antisubversivas permanecen activas después del traspaso",
            meta: "Art. III §13.6 / Art. XIX §6.3",
            text: "Los ex funcionarios que obstruyan la transición legal — antes o después de la inauguración — enfrentan destitución, inhabilitación para cargos futuros y posible procesamiento. La jurisdicción de la CRC no termina cuando se entregan las llaves.",
          },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部阶段",
    nominate: "提名",
    vote: "选举日",
    certify: "认证",
    inaugurate: "就职",
    filterLabel: "筛选从选举到就职的阶段",
    note: "本指南从初选到就职日逐步梳理，展示每个环节的宪法护栏，以及当有人试图打断这条链条时会发生什么。",
    sections: [
      {
        key: "nominate",
        label: "提名阶段",
        summary: "选举委员会在选举开始前制定规则。候选人须满足宪法规定的资格要求；党内初选按照选举委员会管理的时间表进行。",
        steps: [
          {
            title: "选举委员会制定初选日期和上票规则",
            meta: "第一条 §4 / 第十二条 §2.1",
            text: "联邦选举日历和最低上票标准由选举委员会制定，而非国会或任何政党。各州可举行自己的初选，但不得制定阻止合格候选人参加普选的规则。",
          },
          {
            title: "确定选票前先核实资格",
            meta: "第三条 §2.1",
            text: "总统和副总统候选人必须符合宪法规定的年龄、公民身份和居住要求。选举委员会在候选人出现在普选选票上之前确认其资格。",
          },
          {
            title: "启动公共竞选融资",
            meta: "第一条 §7",
            text: "候选人一旦取得普选资格，公共竞选融资系统即告启动。捐款上限和信息披露规则适用于所有党派归属或外部支出。",
          },
          {
            title: "辩论准入规则防止排斥",
            meta: "第一条 §5 / 第十二条 §2.2",
            text: "联邦管理的辩论准入规则禁止任何私营机构将合格候选人排除在主要公共论坛之外。选举委员会可设定客观的民调或签名门槛，但不得按党派歧视。",
          },
        ],
      },
      {
        key: "vote",
        label: "选举日",
        summary: "投票由独立的宪法机关管理，而非对结果有利害关系的在任官员。紧急权力不能用于压制投票渠道或拖延计票。",
        steps: [
          {
            title: "多日投票与15天提前投票",
            meta: "第一条 §3.2",
            text: "联邦选举至少持续三天，选举日前至少提供十五天的提前投票。这防止单一事件使大量选民无法行使投票权。",
          },
          {
            title: "由选举委员会管理投票站，而非党派官员",
            meta: "第一条 §10.1 / 第十二条 §2",
            text: "所有联邦投票站在选举委员会授权下运作。任何在任总统、州长或民选官员不得控制其参选的联邦选举的计票或报告工作。",
          },
          {
            title: "紧急状态宣布不得压制投票",
            meta: "第一条 §3.4",
            text: "紧急状态宣布不得用于关闭投票站、缩短投票时间或拖延认证，除非有管辖权的联邦法院在投票站开放前发出具体命令。",
          },
          {
            title: "众议院选举采用优先顺序投票制",
            meta: "第一条 §2",
            text: "众议院选举在多席位选区使用优先顺序投票制。选民按偏好顺序对候选人排序；如无候选人达到配额，低优先顺序偏好重新分配，直至所有席位填满。",
          },
          {
            title: "初步结果实时公布",
            meta: "第十二条 §2.3",
            text: "选举委员会在结果报告后即时公布辖区级结果。非官方计票必须明确标注为非官方。任何压制或延迟公布的行为均属宪法违规。",
          },
        ],
      },
      {
        key: "certify",
        label: "认证阶段",
        summary: "认证具有强制性且有时限。法院可因真实法律争议暂停认证，但不能无限期暂停——无故拖延本身也可受到制裁。",
        steps: [
          {
            title: "各州须在21天内认证其选举结果",
            meta: "第一条 §6.2",
            text: "每个州必须在选举日后21天内认证其联邦选举结果。在没有司法命令的情况下逾期认证，将自动上报至选举委员会。",
          },
          {
            title: "选举委员会审查各州认证是否符合宪法",
            meta: "第十二条 §2.2",
            text: "选举委员会按宪法标准审查每项州级认证——选民资格、计票程序是否正当、是否存在压制——然后才将其纳入全国计票。",
          },
          {
            title: "问责委员会同步调查舞弊指控",
            meta: "第八条、第十二条 §3",
            text: "若选举委员会转交可信的选举舞弊或干预证据，问责委员会立即启动调查。调查与认证程序并行运行，不暂停时间表。",
          },
          {
            title: "总统选举结果须在30天内认证",
            meta: "第一条 §6.3",
            text: "选举委员会必须在选举日后不超过30天认证总统选举结果。若法院未在截止日前发出具体中止令，认证自动进行。",
          },
          {
            title: "国会认证属于行政事务",
            meta: "第二条 §3",
            text: "国会清点并记录经认证的选举人票。个别议员可在记录上提出正式异议，但任何议院都无权以政策或党派理由否决经宪法认证的结果。",
          },
        ],
      },
      {
        key: "inaugurate",
        label: "就职阶段",
        summary: "从认证后的次日起，离任和新任政府均有积极的宪法义务。权力交接不是可选项。",
        steps: [
          {
            title: "认证后的次日开始交接合作",
            meta: "第三条 §13.2",
            text: "离任总统必须从选举委员会认证后的次日起与当选总统合作：安全简报、机构访问权、办公空间和核心人员介绍。",
          },
          {
            title: "联邦机构支持交接筹备",
            meta: "第三条 §13.3 / 第十九条 §6.2",
            text: "各内阁部门和独立机构必须向接任过渡团队提供履职所需信息。国会必须为过渡程序提供资金和支持。",
          },
          {
            title: "离任官员不得阻挠或掏空国家机器",
            meta: "第三条 §13.4 / 第十九条 §6.1–§6.5",
            text: "离任政府不得销毁记录、出于报复撤销此前行为、做出旨在约束新政府的最后时刻任命，或利用即将失效的权力破坏交接。",
          },
          {
            title: "宣誓就职完成权力交接",
            meta: "第三条 §1.2",
            text: "当选总统在承担任何总统权力之前须宣读宪法誓词。当选副总统在同一仪式上宣誓。两者均由首席大法官主持。",
          },
          {
            title: "反颠覆规则在交接后仍持续有效",
            meta: "第三条 §13.6 / 第十九条 §6.3",
            text: "阻挠合法交接的前官员——无论在就职典礼前后——均面临免职、取消未来参选资格和潜在起诉。问责委员会的管辖权不会因为钥匙已经移交而终止。",
          },
        ],
      },
    ],
  },
};

export function electionInaugurationDataForLocale(locale) {
  return ELECTION_INAUGURATION_GUIDE[locale] || ELECTION_INAUGURATION_GUIDE.en;
}

export const ORGANS_GUIDE = {
  en: {
    all: "All",
    filterLabel: "Filter by organ",
    note: "The constitutional organs — Electoral Commission, Accountability Commission, courts, and the Judicial Conduct Board — each have a defined mandate and cannot direct each other. This guide shows what each does and how they check one another.",
    categories: [
      {
        key: "electoral",
        label: "Electoral Commission",
        summary: "The EC runs federal elections, certifies results, and refers violations. No sitting elected official controls it.",
        items: [
          {
            title: "Runs and certifies all federal elections",
            article: "Art. XII §2",
            text: "The Electoral Commission administers federal polling, sets ballot-access rules, and certifies results from states. It is a constitutional organ — not an executive agency that the President can direct.",
          },
          {
            title: "Refers electoral fraud to the ACC",
            article: "Arts. VI, XII",
            text: "When the EC identifies credible evidence of electoral interference, fraud, or subversion, it refers the matter to the Accountability Commission. The ACC then opens an independent investigation without needing executive approval.",
          },
          {
            title: "Budget floor protects it from defunding",
            article: "Art. XII §2.4",
            text: "A minimum operating budget for the EC is constitutionally established. Congress may increase it but cannot reduce it below the floor as a tool of political pressure.",
          },
          {
            title: "Reports to Congress annually — not to the President",
            article: "Art. XII §2.5",
            text: "The EC submits an annual report to Congress on election administration, budget, and any interference encountered. The report is public. The EC is not accountable to the executive branch.",
          },
          {
            title: "Members can only be removed by Regional Assembly",
            article: "Art. XII §2.6",
            text: "EC members serve fixed terms and can only be removed through the constitutional impeachment process — not by presidential order or a simple legislative vote.",
          },
        ],
      },
      {
        key: "accountability",
        label: "Accountability Commission",
        summary: "The ACC investigates corruption and abuse of power across all branches, prosecutes independently, and cannot be shut down by the official it is investigating.",
        items: [
          {
            title: "Investigates across all three branches",
            article: "Arts. VIII, XII §3",
            text: "The ACC's jurisdiction covers bribery, corruption, anti-subversion conduct, and electoral fraud — wherever it occurs. No official is exempt because of their branch or rank.",
          },
          {
            title: "Receives referrals from the Electoral Commission",
            article: "Arts. VI, XII",
            text: "Electoral fraud referrals from the EC trigger an automatic ACC investigation. The ACC does not need a congressional vote or presidential approval to open the case.",
          },
          {
            title: "Refers judicial misconduct evidence to the JCB",
            article: "Arts. IV, XII",
            text: "If the ACC uncovers evidence of judicial misconduct during an investigation, it refers that evidence to the Judicial Conduct Board. The JCB handles discipline; the ACC does not discipline judges directly.",
          },
          {
            title: "Protected from presidential removal",
            article: "Art. XII §3.4",
            text: "ACC members cannot be fired by the President. Removal requires impeachment by the House and conviction by a two-thirds vote of the Regional Assembly — the same process as removing a federal judge.",
          },
          {
            title: "Actions remain reviewable by courts",
            article: "Arts. IV, XII",
            text: "The ACC is independent from the executive branch, but it is not above the law. Any target of an ACC prosecution can challenge the action in federal court, and the courts review ACC conduct for constitutional compliance.",
          },
        ],
      },
      {
        key: "judicial",
        label: "Courts and Judicial Conduct Board",
        summary: "Federal courts review all branch actions for constitutionality. The JCB handles internal judicial discipline without congressional micromanagement.",
        items: [
          {
            title: "Courts review ACC and EC actions for constitutionality",
            article: "Art. IV",
            text: "Federal courts remain the final arbiter of whether any constitutional organ has acted within its authority. EC certification rules, ACC prosecutions, and JCB referrals are all subject to judicial review.",
          },
          {
            title: "Judicial Conduct Board handles misconduct complaints",
            article: "Art. IV §7",
            text: "The JCB receives, investigates, and decides complaints about federal judges. It can censure, require recusal, mandate training, or refer a judge for impeachment — without waiting for Congress to act.",
          },
          {
            title: "JCB can refer judges for congressional impeachment",
            article: "Art. IV §8.1",
            text: "When the JCB finds grounds that warrant removal, it refers the judge to the House for impeachment proceedings. The referral does not bind Congress, but it establishes the formal factual record.",
          },
          {
            title: "Supreme Court resolves organ boundary disputes",
            article: "Art. IV §3",
            text: "When two constitutional organs disagree about the scope of their respective authority, the Supreme Court has original jurisdiction to resolve the dispute. This prevents organs from silently expanding into each other's mandates.",
          },
          {
            title: "Expedited review for electoral and rights cases",
            article: "Art. IV §5",
            text: "Courts are required to resolve electoral certification challenges and fundamental rights claims on an expedited timetable. Delay cannot be used as a substitute for ruling.",
          },
        ],
      },
      {
        key: "interactions",
        label: "Cross-organ checks",
        summary: "No single actor can capture the constitutional order by controlling one organ, because each organ is a check on the others.",
        items: [
          {
            title: "No organ can direct another",
            article: "Arts. XII, XIX",
            text: "Each constitutional organ derives its authority from the constitution, not from any other branch or organ. The President cannot instruct the ACC. Congress cannot direct the EC's day-to-day administration. The ACC cannot override a court.",
          },
          {
            title: "Appointment paths are deliberately separated",
            article: "Art. XII",
            text: "EC and ACC members are appointed through different institutional paths — different nominating bodies, different confirmation procedures. This makes simultaneous capture of all organs structurally difficult.",
          },
          {
            title: "Congress can impeach organ members but not direct their work",
            article: "Art. XII §2.6, §3.6",
            text: "The House may bring impeachment articles against EC or ACC members for serious misconduct. But Congress cannot issue binding directives about how either body handles a specific investigation or election.",
          },
          {
            title: "Institutional sabotage is itself a constitutional offense",
            article: "Arts. VI, XII, XIX",
            text: "Destroying records, disabling operations, blocking lawful proceedings, or using emergency powers to suppress a constitutional organ all constitute anti-subversion conduct — triggering ACC investigation and potential prosecution regardless of who ordered it.",
          },
          {
            title: "Annual public reports create accountability without subordination",
            article: "Art. XII",
            text: "Each constitutional organ publishes an annual public report. The reports go to Congress and are available to the public. Transparency and accountability do not require subordination to any single political actor.",
          },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar por órgano",
    note: "Los órganos constitucionales — la Comisión Electoral, la Comisión de Rendición de Cuentas, los tribunales y el Consejo de Conducta Judicial — tienen cada uno un mandato definido y no pueden dirigirse mutuamente. Esta guía muestra qué hace cada uno y cómo se controlan entre sí.",
    categories: [
      {
        key: "electoral",
        label: "Comisión Electoral",
        summary: "La CE administra las elecciones federales, certifica resultados y remite infracciones. Ningún funcionario electo en ejercicio la controla.",
        items: [
          { title: "Dirige y certifica todas las elecciones federales", article: "Art. XII §2", text: "La Comisión Electoral administra las urnas federales, establece las reglas de acceso a la boleta y certifica los resultados de los estados. Es un órgano constitucional, no una agencia ejecutiva que el Presidente pueda dirigir." },
          { title: "Remite el fraude electoral a la CRC", article: "Arts. VI, XII", text: "Cuando la CE identifica evidencia creíble de interferencia, fraude o subversión electoral, remite el asunto a la Comisión de Rendición de Cuentas, que abre una investigación independiente sin necesidad de aprobación ejecutiva." },
          { title: "El piso presupuestario la protege de la desfinanciación", article: "Art. XII §2.4", text: "La constitución establece un presupuesto operativo mínimo para la CE. El Congreso puede aumentarlo, pero no reducirlo por debajo del piso como herramienta de presión política." },
          { title: "Reporta al Congreso anualmente, no al Presidente", article: "Art. XII §2.5", text: "La CE presenta un informe anual al Congreso sobre la administración electoral, el presupuesto y cualquier interferencia encontrada. El informe es público. La CE no responde ante el poder ejecutivo." },
          { title: "Los miembros solo pueden ser removidos por la Asamblea Regional", article: "Art. XII §2.6", text: "Los miembros de la CE tienen mandatos fijos y solo pueden ser removidos mediante el proceso constitucional de destitución, no por orden presidencial ni por un voto legislativo simple." },
        ],
      },
      {
        key: "accountability",
        label: "Comisión de Rendición de Cuentas",
        summary: "La CRC investiga la corrupción y el abuso de poder en todos los poderes, acusa de manera independiente y no puede ser clausurada por el funcionario que investiga.",
        items: [
          { title: "Investiga en los tres poderes", article: "Arts. VIII, XII §3", text: "La jurisdicción de la CRC abarca el soborno, la corrupción, la conducta antisubversiva y el fraude electoral, dondequiera que ocurra. Ningún funcionario está exento por su poder o rango." },
          { title: "Recibe remisiones de la Comisión Electoral", article: "Arts. VI, XII", text: "Las remisiones de fraude electoral de la CE activan automáticamente una investigación de la CRC. La CRC no necesita un voto del Congreso ni aprobación presidencial para abrir el caso." },
          { title: "Remite evidencia de mala conducta judicial al CCJ", article: "Arts. IV, XII", text: "Si la CRC descubre evidencia de mala conducta judicial durante una investigación, remite esa evidencia al Consejo de Conducta Judicial. El CCJ maneja la disciplina; la CRC no disciplina a los jueces directamente." },
          { title: "Protegida de la remoción presidencial", article: "Art. XII §3.4", text: "Los miembros de la CRC no pueden ser despedidos por el Presidente. La remoción requiere un juicio político por la Cámara y una condena con dos tercios de votos de la Asamblea Regional, el mismo proceso que para remover a un juez federal." },
          { title: "Sus acciones siguen siendo revisables por los tribunales", article: "Arts. IV, XII", text: "La CRC es independiente del poder ejecutivo, pero no está por encima de la ley. Cualquier objetivo de un proceso de la CRC puede impugnarlo ante un tribunal federal, y los tribunales revisan la conducta de la CRC para verificar el cumplimiento constitucional." },
        ],
      },
      {
        key: "judicial",
        label: "Tribunales y Consejo de Conducta Judicial",
        summary: "Los tribunales federales revisan la constitucionalidad de las acciones de todos los poderes. El CCJ maneja la disciplina judicial interna sin microgestión del Congreso.",
        items: [
          { title: "Los tribunales revisan las acciones de la CRC y la CE", article: "Art. IV", text: "Los tribunales federales siguen siendo el árbitro final de si un órgano constitucional ha actuado dentro de sus competencias. Las reglas de certificación de la CE, los procesos de la CRC y las remisiones del CCJ están todos sujetos a revisión judicial." },
          { title: "El Consejo de Conducta Judicial gestiona las quejas por mala conducta", article: "Art. IV §7", text: "El CCJ recibe, investiga y decide quejas sobre jueces federales. Puede censurar, exigir inhibición, ordenar formación o remitir a un juez para un juicio político, sin esperar a que actúe el Congreso." },
          { title: "El CCJ puede remitir jueces para un juicio político del Congreso", article: "Art. IV §8.1", text: "Cuando el CCJ encuentra motivos que justifiquen la remoción, remite al juez a la Cámara para iniciar el proceso de destitución. La remisión no vincula al Congreso, pero establece el registro fáctico formal." },
          { title: "El Tribunal Supremo resuelve disputas de competencia entre órganos", article: "Art. IV §3", text: "Cuando dos órganos constitucionales no están de acuerdo sobre el alcance de su autoridad respectiva, el Tribunal Supremo tiene jurisdicción original para resolver la disputa." },
          { title: "Revisión acelerada para casos electorales y de derechos", article: "Art. IV §5", text: "Los tribunales deben resolver en plazos acelerados las impugnaciones de certificación electoral y las reclamaciones de derechos fundamentales. El retraso no puede usarse como sustituto de una resolución." },
        ],
      },
      {
        key: "interactions",
        label: "Controles inter-órganos",
        summary: "Ningún actor puede capturar el orden constitucional controlando un solo órgano, porque cada órgano frena a los demás.",
        items: [
          { title: "Ningún órgano puede dirigir a otro", article: "Arts. XII, XIX", text: "Cada órgano constitucional deriva su autoridad de la constitución, no de ningún otro poder u órgano. El Presidente no puede instruir a la CRC. El Congreso no puede dirigir la administración diaria de la CE. La CRC no puede anular un tribunal." },
          { title: "Las vías de nombramiento están deliberadamente separadas", article: "Art. XII", text: "Los miembros de la CE y la CRC son nombrados mediante vías institucionales distintas, con diferentes organismos nominadores y procedimientos de confirmación. Esto hace que la captura simultánea de todos los órganos sea estructuralmente difícil." },
          { title: "El Congreso puede destituir a miembros de órganos, pero no dirigir su trabajo", article: "Art. XII §2.6, §3.6", text: "La Cámara puede presentar artículos de acusación contra miembros de la CE o la CRC por conducta indebida grave. Pero el Congreso no puede emitir directivas vinculantes sobre cómo cualquiera de los dos cuerpos maneja una investigación o elección específica." },
          { title: "El sabotaje institucional es un delito constitucional", article: "Arts. VI, XII, XIX", text: "Destruir registros, desactivar operaciones, bloquear procedimientos legales o usar poderes de emergencia para suprimir un órgano constitucional constituyen conducta antisubversiva, desencadenando una investigación de la CRC y posible procesamiento." },
          { title: "Los informes públicos anuales crean rendición de cuentas sin subordinación", article: "Art. XII", text: "Cada órgano constitucional publica un informe público anual que va al Congreso y está disponible para el público. La transparencia y la responsabilidad no requieren subordinación a ningún actor político único." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "按机关筛选",
    note: "宪法机关——选举委员会、问责委员会、法院和司法行为委员会——各有明确授权，互不指挥。本指南展示各机关的职能及其相互制约机制。",
    categories: [
      {
        key: "electoral",
        label: "选举委员会",
        summary: "选举委员会负责联邦选举、认证结果并转介违规行为。没有任何在任民选官员能控制它。",
        items: [
          { title: "主持并认证所有联邦选举", article: "第十二条 §2", text: "选举委员会管理联邦投票，制定上票规则，认证各州结果。它是宪法机关，而非总统可以指挥的行政机构。" },
          { title: "将选举舞弊转介给问责委员会", article: "第六条、第十二条", text: "当选举委员会发现可信的选举干预、舞弊或颠覆证据时，将此事转介给问责委员会，后者无需行政部门批准即可启动独立调查。" },
          { title: "预算底线防止断资", article: "第十二条 §2.4", text: "宪法确立了选举委员会的最低运营预算。国会可以增加，但不得以政治压力为由将其削减至底线以下。" },
          { title: "向国会报告，而非向总统报告", article: "第十二条 §2.5", text: "选举委员会每年向国会提交关于选举管理、预算和所遇干预的年度报告，报告公开。选举委员会对行政部门不负责。" },
          { title: "成员只能由区域议会罢免", article: "第十二条 §2.6", text: "选举委员会成员任期固定，只能通过宪法弹劾程序免职，不能由总统命令或简单立法投票罢免。" },
        ],
      },
      {
        key: "accountability",
        label: "问责委员会",
        summary: "问责委员会跨越三大机构调查腐败与权力滥用，独立起诉，且不能被被调查对象关闭。",
        items: [
          { title: "跨越三大机构展开调查", article: "第八条、第十二条 §3", text: "问责委员会的管辖权涵盖贿赂、腐败、反颠覆行为和选举舞弊，无论发生在何处。没有官员因其所在机构或职级而获豁免。" },
          { title: "接受选举委员会的转介", article: "第六条、第十二条", text: "选举委员会的选举舞弊转介自动触发问责委员会调查。问责委员会无需国会投票或总统批准即可立案。" },
          { title: "将司法不当行为证据转介给司法行为委员会", article: "第四条、第十二条", text: "若问责委员会在调查中发现司法不当行为证据，将该证据转介给司法行为委员会。由司法行为委员会处理纪律问题；问责委员会不直接约束法官。" },
          { title: "受到保护，不受总统免职", article: "第十二条 §3.4", text: "问责委员会成员不能被总统解职。免职须经众议院弹劾，并由区域议会三分之二投票定罪——与罢免联邦法官程序相同。" },
          { title: "其行为仍受法院审查", article: "第四条、第十二条", text: "问责委员会独立于行政部门，但并不凌驾于法律之上。问责委员会起诉的任何对象均可在联邦法院提出质疑，法院审查问责委员会的行为是否符合宪法。" },
        ],
      },
      {
        key: "judicial",
        label: "法院与司法行为委员会",
        summary: "联邦法院审查所有机构行为的合宪性。司法行为委员会处理内部司法纪律，无需国会微观管理。",
        items: [
          { title: "法院审查问责委员会和选举委员会行为的合宪性", article: "第四条", text: "联邦法院仍是裁定任何宪法机关是否在其权限范围内行事的最终仲裁者。选举委员会的认证规则、问责委员会的起诉和司法行为委员会的转介均受司法审查。" },
          { title: "司法行为委员会处理不当行为投诉", article: "第四条 §7", text: "司法行为委员会接收、调查并裁定有关联邦法官的投诉。它可以谴责、要求回避、命令培训或将法官转介弹劾，无需等待国会行动。" },
          { title: "司法行为委员会可将法官转介国会弹劾", article: "第四条 §8.1", text: "司法行为委员会认定存在足够罢免理由时，将法官转介众议院启动弹劾程序。转介不约束国会，但确立了正式的事实记录。" },
          { title: "最高法院解决机关间管辖权争议", article: "第四条 §3", text: "当两个宪法机关对各自权力范围存在分歧时，最高法院拥有初审管辖权来解决争议，防止各机关悄然扩张到彼此的授权领域。" },
          { title: "选举和权利案件适用加速审查", article: "第四条 §5", text: "法院须按加速时间表解决选举认证质疑和基本权利主张。拖延不能代替裁决。" },
        ],
      },
      {
        key: "interactions",
        label: "跨机关制衡",
        summary: "没有任何单一行为者能通过控制一个机关来俘获宪法秩序，因为每个机关都是对其他机关的制衡。",
        items: [
          { title: "任何机关不得指挥另一机关", article: "第十二条、第十九条", text: "每个宪法机关的权威来自宪法，而非任何其他机构或机关。总统不能指挥问责委员会。国会不能指挥选举委员会的日常行政。问责委员会不能推翻法院判决。" },
          { title: "任命路径刻意分离", article: "第十二条", text: "选举委员会和问责委员会成员通过不同的制度路径任命——不同的提名机构、不同的确认程序。这使得同时俘获所有机关在结构上极为困难。" },
          { title: "国会可弹劾机关成员，但不能指挥其工作", article: "第十二条 §2.6, §3.6", text: "众议院可对选举委员会或问责委员会成员提出严重不当行为弹劾条款。但国会不能就任何一方如何处理具体调查或选举发出具有约束力的指令。" },
          { title: "制度性破坏本身属于宪法罪行", article: "第六条、第十二条、第十九条", text: "销毁记录、瘫痪运作、阻断合法程序或利用紧急权力压制宪法机关，均构成反颠覆行为，无论谁发出命令，均触发问责委员会调查和潜在起诉。" },
          { title: "年度公开报告创造问责而不形成从属关系", article: "第十二条", text: "每个宪法机关发布年度公开报告，提交国会并向公众开放。透明度和问责制不要求从属于任何单一政治行为者。" },
        ],
      },
    ],
  },
};

export function organsDataForLocale(locale) {
  return ORGANS_GUIDE[locale] || ORGANS_GUIDE.en;
}
