export const CONGRESS_COMPARISON = {
  en: {
    all: "All",
    filterLabel: "Filter comparison categories",
    note: "Each row compares one feature of the current U.S. Congress with the same feature in this draft. Use the category buttons to focus on one area.",
    categories: [
      {
        key: "composition",
        label: "Composition",
        rows: [
          {
            feature: "Lower chamber",
            current: "House of Representatives — 435 members",
            draft: "House of Representatives — 500 members",
            note: "Larger House improves district size and proportionality.",
          },
          {
            feature: "Upper chamber",
            current: "Senate — 100 members, 2 per state regardless of population",
            draft: "Regional Assembly — ~100 members, proportional within 8 geographic regions, minimum 1 seat per state",
            note: "Replaces equal-per-state allocation with regional proportional representation while keeping geographic balance.",
          },
          {
            feature: "Total members",
            current: "535",
            draft: "~600",
            note: "",
          },
        ],
      },
      {
        key: "terms",
        label: "Terms and elections",
        rows: [
          {
            feature: "House term length",
            current: "2 years — entire chamber elected every 2 years",
            draft: "4 years — chamber staggered into two groups, half elected every 2 years",
            note: "Longer terms reduce permanent campaign pressure. Staggering preserves continuity.",
          },
          {
            feature: "Upper chamber term length",
            current: "Senate — 6 years, staggered thirds",
            draft: "Regional Assembly — 6 years, staggered thirds",
            note: "Same structure retained.",
          },
          {
            feature: "Recall",
            current: "None — members cannot be recalled by voters",
            draft: "Both chambers subject to constituent-initiated recall (Article I §13)",
            note: "Recall is a new accountability mechanism not present in the current system.",
          },
          {
            feature: "House age requirement",
            current: "25 years old, 7-year citizen",
            draft: "21 years old, 5-year citizen",
            note: "Lower threshold to broaden eligibility.",
          },
          {
            feature: "Upper chamber age requirement",
            current: "Senate — 30 years old, 9-year citizen",
            draft: "Regional Assembly — 25 years old, 7-year citizen",
            note: "Lower threshold to broaden eligibility.",
          },
        ],
      },
      {
        key: "powers",
        label: "Exclusive powers",
        rows: [
          {
            feature: "Originate revenue bills",
            current: "House only",
            draft: "House only",
            note: "Unchanged.",
          },
          {
            feature: "Impeach officers",
            current: "House only (simple majority)",
            draft: "House only (simple majority)",
            note: "Unchanged.",
          },
          {
            feature: "Try impeachments",
            current: "Senate (2/3 to convict)",
            draft: "Regional Assembly (2/3 to convict)",
            note: "Same structure, different chamber.",
          },
          {
            feature: "Confirm presidential nominees",
            current: "Senate (simple majority; no time limit)",
            draft: "Regional Assembly (simple majority; auto-confirmed after 90 days of inaction)",
            note: "90-day default confirmation eliminates indefinite blockades of nominees.",
          },
          {
            feature: "Ratify treaties",
            current: "Senate (2/3)",
            draft: "Regional Assembly (2/3)",
            note: "Same threshold, different chamber.",
          },
          {
            feature: "Approve emergency declarations",
            current: "No constitutional requirement",
            draft: "Regional Assembly must approve within 30 days or declaration lapses automatically",
            note: "New structural constraint on emergency power.",
          },
        ],
      },
      {
        key: "procedure",
        label: "Procedural rules",
        rows: [
          {
            feature: "Filibuster",
            current: "Senate — unlimited debate unless 60 senators vote for cloture",
            draft: "None — no filibuster mechanism; legislation decided by simple majority",
            note: "The filibuster is a Senate rule, not a constitutional requirement. This draft removes it structurally.",
          },
          {
            feature: "Veto override",
            current: "2/3 of both chambers",
            draft: "2/3 of both chambers",
            note: "Unchanged.",
          },
          {
            feature: "Deadlock resolution",
            current: "None — bills can die indefinitely in the other chamber",
            draft: "House may request floor vote if Regional Assembly has not acted; original House version goes to final Regional Assembly vote after 60-day conference failure",
            note: "New mechanism prevents indefinite legislative paralysis.",
          },
          {
            feature: "Suspension of member",
            current: "No automatic suspension under indictment",
            draft: "Member under felony indictment for official-duty offenses suspended from voting pending outcome",
            note: "New accountability rule.",
          },
          {
            feature: "Automatic removal",
            current: "Conviction of a felony does not automatically remove a member",
            draft: "Category 1 offenses (corruption, bribery, electoral subversion) trigger automatic removal on final conviction",
            note: "New bright-line rule for the most serious misconduct.",
          },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar categorías de comparación",
    note: "Cada fila compara una característica del Congreso actual de EE. UU. con la misma en este borrador.",
    categories: [
      {
        key: "composition",
        label: "Composición",
        rows: [
          { feature: "Cámara baja", current: "Cámara de Representantes — 435 miembros", draft: "Cámara de Representantes — 500 miembros", note: "Una cámara más grande mejora el tamaño de los distritos y la proporcionalidad." },
          { feature: "Cámara alta", current: "Senado — 100 miembros, 2 por estado sin importar la población", draft: "Asamblea Regional — ~100 miembros, proporcional dentro de 8 regiones geográficas, mínimo 1 escaño por estado", note: "Reemplaza la asignación igualitaria por estado con representación regional proporcional manteniendo el equilibrio geográfico." },
          { feature: "Total de miembros", current: "535", draft: "~600", note: "" },
        ],
      },
      {
        key: "terms",
        label: "Mandatos y elecciones",
        rows: [
          { feature: "Duración del mandato en la cámara baja", current: "2 años — toda la cámara elegida cada 2 años", draft: "4 años — cámara escalonada en dos grupos, la mitad elegida cada 2 años", note: "Mandatos más largos reducen la presión de la campaña permanente." },
          { feature: "Duración del mandato en la cámara alta", current: "Senado — 6 años, tercios escalonados", draft: "Asamblea Regional — 6 años, tercios escalonados", note: "Misma estructura mantenida." },
          { feature: "Revocación", current: "Ninguna — los miembros no pueden ser revocados por los votantes", draft: "Ambas cámaras sujetas a revocación iniciada por electores (Artículo I §13)", note: "La revocación es un nuevo mecanismo de rendición de cuentas." },
          { feature: "Requisito de edad para la cámara baja", current: "25 años, ciudadano por 7 años", draft: "21 años, ciudadano por 5 años", note: "Umbral más bajo para ampliar la elegibilidad." },
          { feature: "Requisito de edad para la cámara alta", current: "Senado — 30 años, ciudadano por 9 años", draft: "Asamblea Regional — 25 años, ciudadano por 7 años", note: "Umbral más bajo para ampliar la elegibilidad." },
        ],
      },
      {
        key: "powers",
        label: "Poderes exclusivos",
        rows: [
          { feature: "Originar proyectos de ingresos", current: "Solo la Cámara", draft: "Solo la Cámara", note: "Sin cambios." },
          { feature: "Someter a juicio político", current: "Solo la Cámara (mayoría simple)", draft: "Solo la Cámara (mayoría simple)", note: "Sin cambios." },
          { feature: "Juzgar el juicio político", current: "Senado (2/3 para condenar)", draft: "Asamblea Regional (2/3 para condenar)", note: "Misma estructura, diferente cámara." },
          { feature: "Confirmar nominados presidenciales", current: "Senado (mayoría simple; sin límite de tiempo)", draft: "Asamblea Regional (mayoría simple; confirmación automática tras 90 días de inacción)", note: "La confirmación automática elimina bloqueos indefinidos de nominados." },
          { feature: "Ratificar tratados", current: "Senado (2/3)", draft: "Asamblea Regional (2/3)", note: "Mismo umbral, diferente cámara." },
          { feature: "Aprobar declaraciones de emergencia", current: "Sin requisito constitucional", draft: "La Asamblea Regional debe aprobar en 30 días o la declaración caduca automáticamente", note: "Nueva restricción estructural sobre el poder de emergencia." },
        ],
      },
      {
        key: "procedure",
        label: "Reglas de procedimiento",
        rows: [
          { feature: "Obstruccionismo parlamentario", current: "Senado — debate ilimitado salvo que 60 senadores voten para cerrar el debate", draft: "Ninguno — no hay mecanismo de obstruccionismo; la legislación se decide por mayoría simple", note: "El obstruccionismo es una regla del Senado, no un requisito constitucional. Este borrador lo elimina estructuralmente." },
          { feature: "Anular el veto", current: "2/3 de ambas cámaras", draft: "2/3 de ambas cámaras", note: "Sin cambios." },
          { feature: "Resolución de bloqueos", current: "Ninguna — los proyectos pueden morir indefinidamente en la otra cámara", draft: "La Cámara puede solicitar una votación en plenario si la Asamblea Regional no ha actuado; la versión original de la Cámara se somete a votación final tras 60 días de fracaso en conferencia", note: "Nuevo mecanismo para prevenir la parálisis legislativa indefinida." },
          { feature: "Remoción automática", current: "La condena por un delito grave no remueve automáticamente a un miembro", draft: "Los delitos de categoría 1 (corrupción, soborno, subversión electoral) desencadenan remoción automática con la condena final", note: "Nueva regla clara para las conductas más graves." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "筛选对比类别",
    note: "每行对比当前美国国会与本草案在同一特征上的差异。",
    categories: [
      {
        key: "composition",
        label: "构成",
        rows: [
          { feature: "下议院", current: "众议院 — 435名成员", draft: "众议院 — 500名成员", note: "更大的众议院提升选区规模与比例代表性。" },
          { feature: "上议院", current: "参议院 — 100名成员，每州2名，不论人口多少", draft: "地区议会 — 约100名成员，在8个地理区域内按人口比例分配，每州至少1席", note: "以区域比例代表制取代各州等额分配，同时保持地理平衡。" },
          { feature: "成员总数", current: "535", draft: "约600", note: "" },
        ],
      },
      {
        key: "terms",
        label: "任期与选举",
        rows: [
          { feature: "下议院任期", current: "2年 — 整个议院每2年全部改选", draft: "4年 — 议院分为两组交错选举，每2年改选一半", note: "较长任期减少持续竞选压力；交错制保持连续性。" },
          { feature: "上议院任期", current: "参议院 — 6年，三分之一交错改选", draft: "地区议会 — 6年，三分之一交错改选", note: "结构不变。" },
          { feature: "罢免", current: "无 — 选民无法罢免成员", draft: "两院均适用选民发起的罢免制度（第一条第13节）", note: "罢免是现行制度中没有的新问责机制。" },
          { feature: "下议院年龄要求", current: "25岁，公民资格满7年", draft: "21岁，公民资格满5年", note: "降低门槛以扩大资格范围。" },
          { feature: "上议院年龄要求", current: "参议院 — 30岁，公民资格满9年", draft: "地区议会 — 25岁，公民资格满7年", note: "降低门槛以扩大资格范围。" },
        ],
      },
      {
        key: "powers",
        label: "专属权力",
        rows: [
          { feature: "发起税收法案", current: "仅众议院", draft: "仅众议院", note: "未变。" },
          { feature: "提出弹劾", current: "仅众议院（简单多数）", draft: "仅众议院（简单多数）", note: "未变。" },
          { feature: "审判弹劾", current: "参议院（2/3多数定罪）", draft: "地区议会（2/3多数定罪）", note: "结构相同，换了议院。" },
          { feature: "确认总统提名", current: "参议院（简单多数；无时间限制）", draft: "地区议会（简单多数；90天不作为则自动确认）", note: "90天默认确认规则消除了对提名人的无限期阻挠。" },
          { feature: "批准条约", current: "参议院（2/3多数）", draft: "地区议会（2/3多数）", note: "门槛不变，换了议院。" },
          { feature: "批准紧急状态宣言", current: "无宪法要求", draft: "地区议会须在30天内批准，否则宣言自动失效", note: "对紧急权力的新结构性约束。" },
        ],
      },
      {
        key: "procedure",
        label: "程序规则",
        rows: [
          { feature: "冗长辩论阻挠", current: "参议院 — 无限辩论，除非60名参议员投票结束辩论", draft: "无 — 没有阻挠机制；立法由简单多数决定", note: "冗长辩论是参议院规则，非宪法要求。本草案从结构上予以取消。" },
          { feature: "推翻总统否决", current: "两院各2/3多数", draft: "两院各2/3多数", note: "未变。" },
          { feature: "僵局解决", current: "无 — 法案可无限期搁置于另一议院", draft: "若地区议会未采取行动，众议院可要求全体投票；60天协商委员会失败后，众议院原版本提交地区议会最终表决", note: "新机制防止立法陷入无限期瘫痪。" },
          { feature: "自动罢免", current: "定罪重罪不自动罢免成员", draft: "第一类罪行（腐败、贿赂、选举颠覆）在最终定罪后触发自动罢免", note: "对最严重不当行为设立新的明确规则。" },
        ],
      },
    ],
  },
};

export function congressDataForLocale(locale) {
  return CONGRESS_COMPARISON[locale] || CONGRESS_COMPARISON.en;
}

export const AMENDMENT_GUIDE = {
  en: {
    all: "All",
    filterLabel: "Filter amendment process categories",
    note: "Track 1 covers structural amendments. Track 2 covers rights-expanding amendments. The unamendable core sits outside both paths.",
    featureLabel: "Feature",
    track1Label: "Track 1",
    track2Label: "Track 2",
    whyLabel: "Why it matters",
    categories: [
      {
        key: "tracks",
        label: "Two amendment tracks",
        rows: [
          {
            feature: "Purpose",
            current: "Structural or institutional amendment",
            draft: "Rights-expanding amendment only",
            note: "The draft separates ordinary redesign from rights expansion so the easier path cannot be used to narrow the democratic floor.",
          },
          {
            feature: "Congressional trigger",
            current: "2/3 of both chambers",
            draft: "3/5 of both chambers",
            note: "Track 2 is easier to initiate because it can only expand rights rather than weaken them.",
          },
          {
            feature: "Judicial pre-clearance",
            current: "Required before ratification",
            draft: "Required before ratification",
            note: "The Supreme Court must certify that the proposal fits the correct track and does not violate the unamendable core.",
          },
          {
            feature: "Ratification by states",
            current: "3/4 of the states",
            draft: "2/3 of the states",
            note: "Track 2 still needs broad federal buy-in, but not the higher threshold used for structural redesign.",
          },
          {
            feature: "National referendum",
            current: "Not required",
            draft: "Required",
            note: "Track 2 adds direct democratic approval before rights expansion becomes law.",
          },
        ],
      },
      {
        key: "preclearance",
        label: "Pre-clearance and gatekeeping",
        rows: [
          {
            feature: "Wrong-track proposal",
            current: "Rejected before ratification",
            draft: "Rejected before ratification",
            note: "A proposal cannot use Track 2 if it really narrows rights or restructures power.",
          },
          {
            feature: "Unamendable-core conflict",
            current: "Rejected before ratification",
            draft: "Rejected before ratification",
            note: "No amendment may repeal, suspend, or evade the democratic core listed in Article XI.",
          },
          {
            feature: "Effect of denial",
            current: "Proposal stops",
            draft: "Proposal stops",
            note: "Denied proposals never reach ratification, preventing a political campaign around an unconstitutional amendment path.",
          },
        ],
      },
      {
        key: "core",
        label: "Unamendable core",
        rows: [
          {
            feature: "What is locked",
            current: "Republican form of government only, indirectly",
            draft: "Democracy, equal citizenship, regular elections, judicial review, rights floor, civilian control, and more",
            note: "The draft makes the permanently protected core express rather than leaving it mostly implicit.",
          },
          {
            feature: "How many provisions",
            current: "No explicit locked list beyond equal suffrage in the Senate without state consent",
            draft: "Eleven permanently locked commitments",
            note: "The point is to prevent legal self-destruction by temporary majorities.",
          },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar categorías del proceso de enmienda",
    note: "La Vía 1 cubre enmiendas estructurales. La Vía 2 cubre enmiendas que amplían derechos. El núcleo no enmendable queda fuera de ambas rutas.",
    featureLabel: "Elemento",
    track1Label: "Vía 1",
    track2Label: "Vía 2",
    whyLabel: "Por qué importa",
    categories: [
      {
        key: "tracks",
        label: "Dos vías de enmienda",
        rows: [
          { feature: "Propósito", current: "Enmienda estructural o institucional", draft: "Solo enmienda que amplía derechos", note: "El borrador separa el rediseño ordinario de la expansión de derechos para que la vía más fácil no pueda usarse para debilitar el piso democrático." },
          { feature: "Activación en el Congreso", current: "2/3 de ambas cámaras", draft: "3/5 de ambas cámaras", note: "La Vía 2 es más fácil de iniciar porque solo puede ampliar derechos y no reducirlos." },
          { feature: "Preautorización judicial", current: "Requerida antes de la ratificación", draft: "Requerida antes de la ratificación", note: "El Tribunal Supremo debe certificar que la propuesta encaja en la vía correcta y no viola el núcleo no enmendable." },
          { feature: "Ratificación por los estados", current: "3/4 de los estados", draft: "2/3 de los estados", note: "La Vía 2 sigue requiriendo amplio respaldo federal, pero no el umbral más alto usado para rediseños estructurales." },
          { feature: "Referéndum nacional", current: "No requerido", draft: "Requerido", note: "La Vía 2 añade aprobación democrática directa antes de que la expansión de derechos entre en vigor." },
        ],
      },
      {
        key: "preclearance",
        label: "Preautorización y control de entrada",
        rows: [
          { feature: "Propuesta en vía incorrecta", current: "Rechazada antes de la ratificación", draft: "Rechazada antes de la ratificación", note: "Una propuesta no puede usar la Vía 2 si en realidad reduce derechos o reestructura el poder." },
          { feature: "Conflicto con el núcleo no enmendable", current: "Rechazada antes de la ratificación", draft: "Rechazada antes de la ratificación", note: "Ninguna enmienda puede derogar, suspender o eludir el núcleo democrático enumerado en el Artículo XI." },
          { feature: "Efecto de la denegación", current: "La propuesta se detiene", draft: "La propuesta se detiene", note: "Las propuestas denegadas nunca llegan a la ratificación, lo que evita campañas políticas sobre una vía inconstitucional." },
        ],
      },
      {
        key: "core",
        label: "Núcleo no enmendable",
        rows: [
          { feature: "Qué queda bloqueado", current: "Solo la forma republicana de gobierno, indirectamente", draft: "Democracia, ciudadanía igualitaria, elecciones periódicas, control judicial, piso de derechos, control civil y más", note: "El borrador hace expreso el núcleo permanentemente protegido en lugar de dejarlo mayormente implícito." },
          { feature: "Cuántas disposiciones", current: "No hay lista explícita bloqueada salvo la igualdad de sufragio en el Senado sin consentimiento estatal", draft: "Once compromisos permanentemente bloqueados", note: "El objetivo es impedir la autodestrucción legal por mayorías temporales." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "筛选修宪流程类别",
    note: "路径一用于结构性修宪。路径二仅用于扩大权利。不可修宪核心位于两条路径之外。",
    featureLabel: "项目",
    track1Label: "路径一",
    track2Label: "路径二",
    whyLabel: "意义",
    categories: [
      {
        key: "tracks",
        label: "两条修宪路径",
        rows: [
          { feature: "用途", current: "结构性或制度性修宪", draft: "仅限扩大权利的修宪", note: "草案将普通制度重构与权利扩张分开，防止较容易的路径被用来削弱民主底线。" },
          { feature: "国会启动门槛", current: "两院各2/3", draft: "两院各3/5", note: "路径二更容易启动，因为它只能扩大权利，不能缩减权利。" },
          { feature: "司法预审", current: "批准前必须完成", draft: "批准前必须完成", note: "最高法院必须确认提案适用正确路径，且不违反不可修宪核心。" },
          { feature: "州批准门槛", current: "3/4州同意", draft: "2/3州同意", note: "路径二仍需要广泛联邦支持，但门槛低于结构性重构所适用的标准。" },
          { feature: "全国公投", current: "不要求", draft: "要求", note: "路径二在权利扩张生效前增加全国直接民主批准。" },
        ],
      },
      {
        key: "preclearance",
        label: "预审与入口控制",
        rows: [
          { feature: "使用错误路径的提案", current: "在批准前被否决", draft: "在批准前被否决", note: "如果提案实际上缩减权利或重构权力，就不能使用路径二。" },
          { feature: "与不可修宪核心冲突", current: "在批准前被否决", draft: "在批准前被否决", note: "任何修宪都不得废除、暂停或规避第十一条列出的民主核心。" },
          { feature: "否决后的效果", current: "提案终止", draft: "提案终止", note: "被否决的提案不会进入批准阶段，从而避免围绕违宪修宪路径发动政治运动。" },
        ],
      },
      {
        key: "core",
        label: "不可修宪核心",
        rows: [
          { feature: "锁定内容", current: "仅间接保护共和政体", draft: "民主、平等公民资格、定期选举、司法审查、权利底线、文官控制等", note: "草案将永久受保护的核心明确写出，而不是主要依赖隐含原则。" },
          { feature: "条目数量", current: "除未经州同意不得剥夺参议院平等席位外，没有明确锁定清单", draft: "十一项永久锁定承诺", note: "目的是防止短暂多数通过法律形式自我毁灭。" },
        ],
      },
    ],
  },
};

export function amendmentDataForLocale(locale) {
  return AMENDMENT_GUIDE[locale] || AMENDMENT_GUIDE.en;
}

export const ELECTIONS_GUIDE = {
  en: {
    all: "All",
    filterLabel: "Filter elections categories",
    note: "Each card explains one feature of the electoral system. Use the buttons to focus on voting methods, access, integrity protections, or recall.",
    categories: [
      {
        key: "voting",
        label: "Voting methods",
        summary: "How votes are cast and counted for the House and Regional Assembly.",
        items: [
          { title: "House: ranked-choice in multi-member districts", article: "Art. I §4.1–4.2", text: "Voters rank candidates in order of preference. Districts return 3–7 members. Seats fill using the Droop quota: votes flow from elected candidates' surpluses and eliminated candidates to voters' next choices until all seats are filled. Produces proportional results." },
          { title: "Regional Assembly: instant runoff", article: "Art. I §5.1", text: "Voters rank candidates for their state's Regional Assembly seats. If no one has a majority, the last-place candidate is eliminated and their voters' next choices are counted. Repeats until one candidate reaches a majority." },
          { title: "Districts return 3–7 members, not 1", article: "Art. I §4.2", text: "No House district elects a single representative. Every district returns between 3 and 7 members in proportion to population. Minority communities can elect representation without needing to be a majority of a district." },
          { title: "No party primary requirement", article: "Art. I §9.1–9.3", text: "The constitution does not mandate party primaries. Independent candidates can run without party affiliation. Parties qualify for the ballot by collecting 0.1% of registered voters' signatures across 20+ states within 12 months." },
        ],
      },
      {
        key: "access",
        label: "Access and registration",
        summary: "How citizens are registered and how voting access is protected.",
        items: [
          { title: "Automatic registration at 18 or upon citizenship", article: "Art. I §2.1", text: "Every citizen is registered automatically when they turn 18 or become a citizen. No application required. Federal and state agency records are used. New citizens are registered through the naturalization process itself." },
          { title: "Registration cannot be removed arbitrarily", article: "Art. I §2.3", text: "A citizen's registration can only be removed by death, written request, or a judicial finding of ineligibility. Any other removal is unconstitutional." },
          { title: "Minimum 3-day voting window + 15 days early voting", article: "Art. I §3.2", text: "Federal elections must be held over at least 3 days ending on Election Day. Early voting must be available for at least 15 days before the election." },
          { title: "Election Day is a federal holiday", article: "Art. I §3.3", text: "Election Day is a mandatory federal public holiday. No employer may penalize an employee for taking time to vote." },
        ],
      },
      {
        key: "integrity",
        label: "Integrity protections",
        summary: "Constitutional rules that prevent the electoral system from being manipulated.",
        items: [
          { title: "Election date cannot be moved by executive order", article: "Art. I §3.1", text: "The election date is fixed by the constitution. No executive order or emergency declaration alone can move it. A date change requires a 2/3 vote of both chambers, a presidential declaration of catastrophic emergency, AND a Supreme Court finding that a fair election on the original date is impossible — all three simultaneously." },
          { title: "Only three specific disasters can delay an election", article: "Art. I §3.2", text: "Armed conflict on U.S. soil, a pandemic killing 10,000+ per week (CDC certified), or a natural disaster destroying critical infrastructure in 3+ states (FEMA certified). Any delay must land within 60 days of the original date." },
          { title: "No emergency manipulation near election day", article: "Art. I §3.4", text: "No emergency declaration within 60 days of a scheduled election may restrict polling access, reduce early voting, or delay certification — unless a federal court finds a direct, imminent, unavoidable threat to public safety under strict scrutiny. Courts must rule within 72 hours." },
          { title: "Independent redistricting with anti-gerrymandering rules", article: "Art. I §8.1–8.6", text: "An Independent Redistricting Commission draws all House district maps using open, publicly auditable algorithmic methods. Maps must keep the efficiency gap ≤7% and mean-median difference ≤5%. No systematic partisan advantage is allowed. If the Commission deadlocks, three randomly selected federal circuit judges choose between the competing maps." },
        ],
      },
      {
        key: "recall",
        label: "Recall",
        summary: "How voters can remove a sitting member of Congress between elections.",
        items: [
          { title: "Voters can remove any member of Congress", article: "Art. I §13.1", text: "House members can be recalled by their district voters. Regional Assembly members can be recalled by their state voters. Recall requires no finding of misconduct — it reflects a loss of constituent confidence." },
          { title: "Petition: 20% of prior-election votes in 120 days", article: "Art. I §13.3", text: "A recall petition must be signed by voters equal to 20% of votes cast in the official's prior election, collected within 120 consecutive days, and verified by the Electoral Commission within 30 days. Only one attempt allowed per term." },
          { title: "Recall election: majority + 40% turnout required", article: "Art. I §13.4", text: "Removal requires a majority of votes cast, with at least 40% of registered voters participating. The official is not suspended from duties while the recall election is pending and may campaign against removal." },
          { title: "Recall cannot target votes, speeches, or positions", article: "Art. I §13.5", text: "A petition cannot cite the official's votes, speeches, or legislative positions as the sole basis for recall. The Electoral Commission rejects petitions that are pretextual targeting of protected legislative conduct." },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar categorías electorales",
    note: "Cada tarjeta explica una característica del sistema electoral. Usa los botones para centrarte en métodos de votación, acceso, protecciones de integridad o revocación.",
    categories: [
      {
        key: "voting",
        label: "Métodos de votación",
        summary: "Cómo se emiten y cuentan los votos para la Cámara y la Asamblea Regional.",
        items: [
          { title: "Cámara: voto preferencial en distritos plurinominales", article: "Art. I §4.1–4.2", text: "Los votantes clasifican candidatos en orden de preferencia. Los distritos eligen 3–7 miembros. Los escaños se llenan mediante la cuota Droop: los votos fluyen de los excedentes de candidatos elegidos y candidatos eliminados hasta cubrir todos los escaños. Produce resultados proporcionales." },
          { title: "Asamblea Regional: segunda vuelta instantánea", article: "Art. I §5.1", text: "Los votantes clasifican candidatos para los escaños de la Asamblea Regional. Si nadie tiene mayoría, se elimina al último y sus votos pasan a la siguiente preferencia. Se repite hasta que un candidato alcanza la mayoría." },
          { title: "Los distritos eligen 3–7 miembros, no 1", article: "Art. I §4.2", text: "Ningún distrito de la Cámara elige un solo representante. Cada distrito elige entre 3 y 7 miembros proporcionalmente. Las comunidades minoritarias pueden elegir representación sin necesitar ser mayoría del distrito." },
          { title: "Sin requisito de primarias partidistas", article: "Art. I §9.1–9.3", text: "La constitución no exige primarias partidistas. Los candidatos independientes pueden presentarse sin afiliación. Los partidos acceden a la boleta recogiendo firmas del 0,1% de los votantes registrados en 20+ estados en 12 meses." },
        ],
      },
      {
        key: "access",
        label: "Acceso y registro",
        summary: "Cómo se registran los ciudadanos y cómo se protege el acceso al voto.",
        items: [
          { title: "Registro automático al cumplir 18 años o al naturalizarse", article: "Art. I §2.1", text: "Todo ciudadano queda registrado automáticamente al cumplir 18 años o al naturalizarse. No se requiere solicitud. Se usan registros de agencias federales y estatales. Los nuevos ciudadanos se registran a través del propio proceso de naturalización." },
          { title: "El registro no puede eliminarse arbitrariamente", article: "Art. I §2.3", text: "El registro de un ciudadano solo puede eliminarse por fallecimiento, solicitud escrita o resolución judicial de inelegibilidad. Cualquier otra eliminación es inconstitucional." },
          { title: "Mínimo 3 días de votación + 15 días de voto anticipado", article: "Art. I §3.2", text: "Las elecciones federales deben celebrarse durante al menos 3 días. El voto anticipado debe estar disponible al menos 15 días antes de la elección." },
          { title: "El día de elecciones es feriado federal", article: "Art. I §3.3", text: "El día de elecciones es un feriado federal obligatorio." },
        ],
      },
      {
        key: "integrity",
        label: "Protecciones de integridad",
        summary: "Normas constitucionales que impiden la manipulación del sistema electoral.",
        items: [
          { title: "La fecha electoral no puede cambiarse por decreto ejecutivo", article: "Art. I §3.1", text: "La fecha está fijada por la constitución. Cambiarla requiere 2/3 de ambas cámaras, declaración presidencial de emergencia catastrófica Y resolución del Tribunal Supremo de que una elección justa es imposible en la fecha original — los tres simultáneamente." },
          { title: "Solo tres catástrofes específicas pueden retrasar las elecciones", article: "Art. I §3.2", text: "Conflicto armado en suelo de EE. UU., pandemia con 10.000+ muertes semanales (certificado por los CDC), o desastre natural que destruya infraestructura crítica en 3+ estados (certificado por FEMA). El retraso debe quedar dentro de 60 días de la fecha original." },
          { title: "Sin manipulación de emergencia cerca del día de elecciones", article: "Art. I §3.4", text: "Ninguna declaración de emergencia en los 60 días previos a la elección puede restringir el acceso a las urnas, reducir el voto anticipado o retrasar la certificación, salvo que un tribunal federal encuentre una amenaza directa e inmediata bajo escrutinio estricto." },
          { title: "Redistritación independiente con reglas antigerrymandering", article: "Art. I §8.1–8.6", text: "Una Comisión de Redistritación Independiente dibuja todos los mapas distritales con métodos algorítmicos auditables. Las brechas de eficiencia deben ser ≤7% y la diferencia media-mediana ≤5%. No se permite ninguna ventaja partisan sistemática." },
        ],
      },
      {
        key: "recall",
        label: "Revocación de mandato",
        summary: "Cómo los votantes pueden destituir a un miembro del Congreso entre elecciones.",
        items: [
          { title: "Los votantes pueden destituir a cualquier miembro del Congreso", article: "Art. I §13.1", text: "Los miembros de la Cámara pueden ser revocados por su distrito. Los miembros de la Asamblea Regional por su estado. La revocación no requiere hallazgo de mala conducta — refleja pérdida de confianza del electorado." },
          { title: "Petición: 20% de votos de la elección anterior en 120 días", article: "Art. I §13.3", text: "La petición debe ser firmada por votantes equivalentes al 20% de los votos de la elección anterior del funcionario, recogida en 120 días consecutivos y verificada en 30 días. Solo un intento por mandato." },
          { title: "Elección de revocación: mayoría + 40% de participación", article: "Art. I §13.4", text: "La destitución requiere mayoría de votos emitidos, con al menos 40% de participación. El funcionario no es suspendido de sus funciones mientras esté pendiente la elección de revocación." },
          { title: "La revocación no puede dirigirse contra votos o discursos", article: "Art. I §13.5", text: "Una petición no puede citar los votos, discursos o posiciones legislativas del funcionario como único fundamento. La Comisión Electoral rechaza peticiones que sean un pretexto para atacar conducta legislativa protegida." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "筛选选举类别",
    note: "每张卡片解释选举制度的一个特征。使用按钮聚焦于投票方式、投票渠道、诚信保护或罢免机制。",
    categories: [
      {
        key: "voting",
        label: "投票方式",
        summary: "众议院和地区议会如何投票与计票。",
        items: [
          { title: "众议院：多议席选区排序投票", article: "第一条 §4.1–4.2", text: "选民按偏好顺序对候选人排序。每个选区产生3至7名议员。采用得票比例（Droop）公式：当选候选人的多余票数和被淘汰候选人的票数依次转移至选民下一偏好，直到所有席位填满。结果具有比例代表性。" },
          { title: "地区议会：即时决选投票", article: "第一条 §5.1", text: "选民对本州地区议会候选人排序。若无人过半数，末位候选人被淘汰，其票数转移至选民下一偏好。反复进行直至某候选人过半数。" },
          { title: "选区产生3至7名议员，而非1名", article: "第一条 §4.2", text: "没有任何众议院选区只选出一名代表。每个选区按人口比例产生3至7名议员。少数族裔社区无需在选区内占多数，也能选出代表。" },
          { title: "无党内初选要求", article: "第一条 §9.1–9.3", text: "宪法不要求政党举行初选。无党派候选人可自由参选。政党通过在12个月内收集20个以上州各0.1%登记选民签名来获得候选资格。" },
        ],
      },
      {
        key: "access",
        label: "投票渠道与选民登记",
        summary: "公民如何登记以及投票渠道如何受到保护。",
        items: [
          { title: "满18岁或入籍即自动登记", article: "第一条 §2.1", text: "每位公民在年满18岁或取得公民身份时自动完成选民登记。无需申请。利用联邦和州机构现有记录。新公民通过入籍程序本身完成登记。" },
          { title: "选民登记不得任意撤销", article: "第一条 §2.3", text: "公民的选民登记只能因其死亡、书面申请或司法裁定不具资格而被撤销。任何其他理由撤销均违宪。" },
          { title: "最少3天投票期 + 15天提前投票", article: "第一条 §3.2", text: "联邦选举必须在至少3天内进行。提前投票必须在选举日前至少15天开放。" },
          { title: "选举日为联邦公共假日", article: "第一条 §3.3", text: "选举日是法定联邦公共假日。" },
        ],
      },
      {
        key: "integrity",
        label: "诚信保护",
        summary: "防止选举制度被操控的宪法规则。",
        items: [
          { title: "选举日期不得通过行政命令更改", article: "第一条 §3.1", text: "选举日期由宪法固定。单凭行政命令或紧急状态宣言无法更改。更改日期需要两院各2/3多数投票、总统宣布灾难性紧急状态，以及最高法院认定原定日期无法举行公正选举——三者须同时具备。" },
          { title: "只有三类特定灾难可推迟选举", article: "第一条 §3.2", text: "美国本土发生武装冲突、每周死亡逾1万人的疫情（CDC认证）或摧毁3个以上州关键基础设施的自然灾害（FEMA认证）。推迟后的日期必须在原定日期60天以内。" },
          { title: "选举日前60天禁止利用紧急权力干预", article: "第一条 §3.4", text: "选举日前60天内，任何紧急状态宣言均不得限制投票站出入、减少提前投票或推迟认证结果——除非联邦法院在严格审查下认定存在直接、迫在眉睫且不可避免的公共安全威胁。法院须在72小时内裁决。" },
          { title: "独立划定选区，附反操纵规则", article: "第一条 §8.1–8.6", text: "独立选区重划委员会采用公开、可审计的算法方法划定所有众议院选区地图。效率差距须≤7%，均值-中位数差须≤5%。不允许任何系统性党派优势。若委员会陷入僵局，三名随机选取的联邦巡回法官从竞争方案中选取一个。" },
        ],
      },
      {
        key: "recall",
        label: "罢免",
        summary: "选民如何在两次选举之间罢免在任国会议员。",
        items: [
          { title: "选民可罢免任何国会议员", article: "第一条 §13.1", text: "众议员可由其选区选民罢免。地区议会议员可由其州选民罢免。罢免不需要认定存在不当行为——它反映的是选民信任的丧失。" },
          { title: "联署：上次选举得票的20%，120天内收集", article: "第一条 §13.3", text: "罢免请愿书须由等同于该官员上次选举得票20%的选民签署，在120天内收集完毕，并由选举委员会在30天内核实。每任期内只允许发起一次。" },
          { title: "罢免选举：过半数票 + 40%投票率", article: "第一条 §13.4", text: "罢免需要有效票过半，且至少40%的登记选民参与。罢免选举期间官员不停职，可参与竞选反对罢免。" },
          { title: "罢免不得针对议员的投票或言论", article: "第一条 §13.5", text: "请愿书不得仅以官员的投票、演讲或立法立场为由。选举委员会驳回以攻击受保护立法行为为借口的请愿书。" },
        ],
      },
    ],
  },
};

export function electionsDataForLocale(locale) {
  return ELECTIONS_GUIDE[locale] || ELECTIONS_GUIDE.en;
}

export const BILL_TO_LAW_GUIDE = {
  en: {
    all: "All paths",
    ordinary: "Ordinary path",
    vetoed: "Vetoed path",
    deadlocked: "Deadlock path",
    filterLabel: "Filter bill-to-law paths",
    note: "This guide shows the ordinary legislative route, what happens after a veto, and how the constitution resolves inter-chamber deadlock.",
    sections: [
      {
        key: "ordinary",
        label: "Ordinary legislative path",
        summary: "Bills become law only after bicameral passage in identical form and presidential action or inaction within a fixed deadline.",
        steps: [
          { title: "House or Regional Assembly passes a bill", meta: "Art. II §10", text: "A bill must clear the chamber where it is introduced before moving to the other chamber." },
          { title: "Both chambers pass the same text", meta: "Art. II §10.5", text: "A bill must pass both chambers in identical form before it can go to the President." },
          { title: "Conference committee if versions differ", meta: "Art. II §10.5", text: "If the chambers pass different versions, a conference committee attempts to reconcile them." },
          { title: "Optional pre-enactment single-subject review", meta: "Art. II §10.7A", text: "Any member of either chamber may seek Supreme Court review before presidential action. The President's 15-day clock pauses during that review." },
          { title: "President signs or does nothing", meta: "Art. II §10.6", text: "The President has 15 days to sign or veto. If the President does nothing, the bill becomes law automatically." },
        ],
      },
      {
        key: "vetoed",
        label: "Veto and override path",
        summary: "The President keeps a veto, but the path after veto is straightforward and constitutionally timed.",
        steps: [
          { title: "President vetoes the bill", meta: "Art. II §10.6", text: "The bill returns with objections instead of becoming law." },
          { title: "Congress may reconsider", meta: "Art. II §14.2(b)", text: "Both chambers may vote again on the vetoed bill." },
          { title: "Two-thirds in both chambers overrides", meta: "Art. II §14.2(b)", text: "If both chambers reach a 2/3 vote, the bill becomes law over the veto." },
          { title: "No pocket veto", meta: "Art. II §10.6", text: "A bill presented during recess still becomes law after 15 days if unsigned. Recess cannot quietly kill legislation." },
        ],
      },
      {
        key: "deadlocked",
        label: "Deadlock-resolution path",
        summary: "The draft adds constitutional anti-paralysis rules when the Regional Assembly stalls or conference collapses.",
        steps: [
          { title: "House-passed bill stalls in the Regional Assembly", meta: "Art. II §11.2", text: "If the Regional Assembly fails to act within the period established by law or rule, the House may declare the bill delayed and request an immediate floor vote." },
          { title: "Assembly amends or rejects", meta: "Art. II §11.1", text: "If the Regional Assembly changes the bill, the House may accept the changes, reject them, or request conference." },
          { title: "Conference committee gets 60 days", meta: "Art. II §11.1(b)", text: "If conference fails to produce agreement within 60 days, the original House-passed version goes to a final vote of the full Regional Assembly." },
          { title: "Final Assembly vote on the House version", meta: "Art. II §11.1(b)", text: "The Assembly must take a final position rather than holding the bill indefinitely in procedural limbo." },
        ],
      },
    ],
  },
  es: {
    all: "Todas las rutas",
    ordinary: "Ruta ordinaria",
    vetoed: "Ruta con veto",
    deadlocked: "Ruta de bloqueo",
    filterLabel: "Filtrar rutas legislativas",
    note: "Esta guía muestra la ruta legislativa ordinaria, qué ocurre tras un veto y cómo la constitución resuelve el bloqueo entre cámaras.",
    sections: [
      {
        key: "ordinary",
        label: "Ruta legislativa ordinaria",
        summary: "Un proyecto solo se convierte en ley tras aprobación bicameral en texto idéntico y acción o inacción presidencial dentro de un plazo fijo.",
        steps: [
          { title: "La Cámara o la Asamblea Regional aprueba un proyecto", meta: "Art. II §10", text: "Un proyecto debe superar la cámara en la que se presenta antes de pasar a la otra." },
          { title: "Ambas cámaras aprueban el mismo texto", meta: "Art. II §10.5", text: "El proyecto debe ser aprobado en forma idéntica por ambas cámaras antes de llegar al Presidente." },
          { title: "Comisión de conferencia si los textos difieren", meta: "Art. II §10.5", text: "Si ambas cámaras aprueban versiones distintas, una comisión de conferencia intenta conciliarlas." },
          { title: "Revisión previa opcional por regla de materia única", meta: "Art. II §10.7A", text: "Cualquier miembro de cualquiera de las cámaras puede pedir revisión ante el Tribunal Supremo antes de la acción presidencial. El plazo presidencial de 15 días se suspende durante esa revisión." },
          { title: "El Presidente firma o no actúa", meta: "Art. II §10.6", text: "El Presidente dispone de 15 días para firmar o vetar. Si no actúa, el proyecto se convierte automáticamente en ley." },
        ],
      },
      {
        key: "vetoed",
        label: "Ruta de veto y anulación",
        summary: "El Presidente conserva el veto, pero la ruta posterior es directa y constitucionalmente definida.",
        steps: [
          { title: "El Presidente veta el proyecto", meta: "Art. II §10.6", text: "El proyecto se devuelve con objeciones en lugar de convertirse en ley." },
          { title: "El Congreso puede reconsiderarlo", meta: "Art. II §14.2(b)", text: "Ambas cámaras pueden volver a votar sobre el proyecto vetado." },
          { title: "Dos tercios en ambas cámaras anulan el veto", meta: "Art. II §14.2(b)", text: "Si ambas cámaras alcanzan 2/3, el proyecto se convierte en ley pese al veto." },
          { title: "No existe veto de bolsillo", meta: "Art. II §10.6", text: "Un proyecto presentado durante el receso se convierte igualmente en ley tras 15 días si no se firma. El receso no puede matar silenciosamente la legislación." },
        ],
      },
      {
        key: "deadlocked",
        label: "Ruta de resolución del bloqueo",
        summary: "El borrador añade reglas constitucionales contra la parálisis cuando la Asamblea Regional se estanca o fracasa la conferencia.",
        steps: [
          { title: "Un proyecto aprobado por la Cámara se estanca en la Asamblea Regional", meta: "Art. II §11.2", text: "Si la Asamblea Regional no actúa dentro del plazo fijado por ley o reglamento, la Cámara puede declararlo retrasado y solicitar una votación inmediata en el pleno." },
          { title: "La Asamblea modifica o rechaza", meta: "Art. II §11.1", text: "Si la Asamblea Regional modifica el proyecto, la Cámara puede aceptar los cambios, rechazarlos o pedir conferencia." },
          { title: "La comisión de conferencia tiene 60 días", meta: "Art. II §11.1(b)", text: "Si la conferencia no logra acuerdo en 60 días, la versión original aprobada por la Cámara pasa a votación final en el pleno de la Asamblea Regional." },
          { title: "Votación final de la Asamblea sobre la versión de la Cámara", meta: "Art. II §11.1(b)", text: "La Asamblea debe adoptar una posición final en lugar de retener indefinidamente el proyecto en un limbo procedimental." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部路径",
    ordinary: "通常路径",
    vetoed: "否决路径",
    deadlocked: "僵局路径",
    filterLabel: "筛选法案成法路径",
    note: "本指南展示普通立法路径、被否决后会发生什么，以及宪法如何解决众议院与地区议会之间的僵局。",
    sections: [
      {
        key: "ordinary",
        label: "通常立法路径",
        summary: "法案只有在两院以相同文本通过，并在固定期限内由总统签署或因不作为而生效后，才成为法律。",
        steps: [
          { title: "众议院或地区议会通过法案", meta: "第二条 §10", text: "法案必须先在提出它的议院获得通过，然后才能送往另一议院。" },
          { title: "两院通过相同文本", meta: "第二条 §10.5", text: "法案必须以完全相同的文本通过两院，之后才能送交总统。" },
          { title: "若版本不同则进入协商委员会", meta: "第二条 §10.5", text: "如果两院通过的是不同版本，协商委员会将尝试统一文本。" },
          { title: "可选的单一主题预审", meta: "第二条 §10.7A", text: "任一议员都可在总统采取行动前请求最高法院审查。审查期间，总统的15天时钟暂停。" },
          { title: "总统签署或不作为", meta: "第二条 §10.6", text: "总统有15天时间签署或否决。若不采取行动，法案自动成为法律。" },
        ],
      },
      {
        key: "vetoed",
        label: "否决与推翻路径",
        summary: "总统保留否决权，但否决后的路径直接且有明确宪法规则。",
        steps: [
          { title: "总统否决法案", meta: "第二条 §10.6", text: "法案将附带异议退回，而不是成为法律。" },
          { title: "国会可重新审议", meta: "第二条 §14.2(b)", text: "两院都可以再次对被否决的法案投票。" },
          { title: "两院各2/3即可推翻否决", meta: "第二条 §14.2(b)", text: "若两院都达到2/3多数，法案即使在总统反对下也成为法律。" },
          { title: "不存在口袋否决", meta: "第二条 §10.6", text: "休会期间送交总统的法案，如15天内未签署，仍然生效。休会不能悄悄杀死法案。" },
        ],
      },
      {
        key: "deadlocked",
        label: "僵局解决路径",
        summary: "本草案在地区议会拖延或协商失败时加入了反瘫痪的宪法规则。",
        steps: [
          { title: "众议院通过的法案在地区议会被拖延", meta: "第二条 §11.2", text: "若地区议会在法律或议事规则规定期限内不采取行动，众议院可宣布该法案被拖延，并要求立即进行全院表决。" },
          { title: "地区议会修改或拒绝", meta: "第二条 §11.1", text: "如果地区议会修改法案，众议院可接受修改、拒绝修改，或要求进入协商委员会。" },
          { title: "协商委员会有60天时间", meta: "第二条 §11.1(b)", text: "若协商在60天内未达成一致，众议院原始版本将提交地区议会全院作最终表决。" },
          { title: "地区议会必须对众议院版本作最终决定", meta: "第二条 §11.1(b)", text: "地区议会必须作出最终立场，而不能将法案无限期困在程序性僵局中。" },
        ],
      },
    ],
  },
};

export function billToLawDataForLocale(locale) {
  return BILL_TO_LAW_GUIDE[locale] || BILL_TO_LAW_GUIDE.en;
}

export const UNAMENDABLE_CORE_GUIDE = {
  en: {
    all: "All",
    filterLabel: "Filter unamendable core categories",
    note: "This guide separates the permanently protected democratic core into functional groups so readers can see what the Constitution puts beyond amendment, repeal, or suspension.",
    categories: [
      {
        key: "democracy",
        label: "Democratic structure",
        summary: "The Constitution permanently protects the basic machinery of lawful democratic rule.",
        items: [
          { title: "Universal equal suffrage in federal elections", article: "Art. XI §3.1(1)", text: "No amendment may repeal or hollow out the equal right of adult citizens to vote in federal elections." },
          { title: "Integrity of election administration and certification", article: "Art. XI §3.1(2)", text: "No amendment may destroy the constitutional requirements that elections be lawfully administered, counted, and certified." },
          { title: "Regular democratic renewal", article: "Art. XI §3.1(3)", text: "Periodic elections, fixed constitutional turnover, and a continuing democratic chain cannot be abolished by amendment." },
        ],
      },
      {
        key: "membership",
        label: "Equal citizenship and rights floor",
        summary: "The draft forbids amendments that would turn the polity into a hierarchy of belonging or erase the basic rights floor.",
        items: [
          { title: "Equal citizenship", article: "Art. XI §3.1(4)", text: "No amendment may create castes of political membership or authorize second-class citizenship." },
          { title: "Core rights floor", article: "Art. XI §3.1(8)", text: "The basic rights structure cannot be repealed or suspended as a way to keep formal institutions while destroying meaningful liberty." },
          { title: "Substance-over-label protection", article: "Art. XI §3.1", text: "An amendment cannot evade these locks by renaming terms while narrowing the real substance of the protected right." },
        ],
      },
      {
        key: "institutions",
        label: "Guardrail institutions",
        summary: "Some institutions are protected because without them the democratic order could be dismantled from inside.",
        items: [
          { title: "Judicial review", article: "Art. XI §3.1(7)", text: "No amendment may abolish the constitutional power of courts to review and block unconstitutional action." },
          { title: "Electoral Commission independence", article: "Art. XI §3.1(5)", text: "The independence and protected mandate of the Electoral Commission cannot be amended away." },
          { title: "Accountability Commission independence", article: "Art. XI §3.1(6)", text: "The Accountability Commission cannot be stripped of its independent role as a constitutional anti-capture safeguard." },
        ],
      },
      {
        key: "order",
        label: "Constitutional order and civilian rule",
        summary: "The draft locks the principles that keep armed force, emergency politics, and constitutional change itself inside a lawful democratic order.",
        items: [
          { title: "Civilian control of the military", article: "Art. XI §3.1(9)", text: "No amendment may legalize military rule or place the armed forces above elected constitutional authority." },
          { title: "Peaceful transfer of power", article: "Art. XI §3.1(10)", text: "No amendment may abolish the constitutional obligation to carry out lawful transfer after elections and constitutional succession." },
          { title: "The amendment power stays limited", article: "Art. XI §3.1(11)", text: "The democratic core itself cannot be made amendable by ordinary amendment. The lock protects itself." },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar categorías del núcleo irreformable",
    note: "Esta guía separa el núcleo democrático protegido permanentemente en grupos funcionales para que el lector vea qué coloca la Constitución más allá de la reforma, derogación o suspensión.",
    categories: [
      {
        key: "democracy",
        label: "Estructura democrática",
        summary: "La Constitución protege de forma permanente la maquinaria básica del gobierno democrático legítimo.",
        items: [
          { title: "Sufragio universal e igual en elecciones federales", article: "Art. XI §3.1(1)", text: "Ninguna enmienda puede derogar o vaciar el derecho igual de los ciudadanos adultos a votar en elecciones federales." },
          { title: "Integridad de la administración y certificación electoral", article: "Art. XI §3.1(2)", text: "Ninguna enmienda puede destruir los requisitos constitucionales de administración, conteo y certificación legal de las elecciones." },
          { title: "Renovación democrática periódica", article: "Art. XI §3.1(3)", text: "Las elecciones periódicas, la alternancia constitucional fija y la continuidad democrática no pueden abolirse por enmienda." },
        ],
      },
      {
        key: "membership",
        label: "Ciudadanía igualitaria y piso de derechos",
        summary: "El borrador prohíbe enmiendas que conviertan la comunidad política en una jerarquía de pertenencia o borren el piso básico de derechos.",
        items: [
          { title: "Ciudadanía igualitaria", article: "Art. XI §3.1(4)", text: "Ninguna enmienda puede crear castas de pertenencia política ni autorizar ciudadanía de segunda clase." },
          { title: "Piso básico de derechos", article: "Art. XI §3.1(8)", text: "La estructura básica de derechos no puede derogarse o suspenderse como forma de conservar instituciones formales mientras se destruye la libertad real." },
          { title: "Protección de sustancia sobre etiqueta", article: "Art. XI §3.1", text: "Una enmienda no puede eludir estos bloqueos simplemente renombrando conceptos mientras reduce la sustancia real del derecho protegido." },
        ],
      },
      {
        key: "institutions",
        label: "Instituciones de resguardo",
        summary: "Algunas instituciones se protegen porque sin ellas el orden democrático podría ser desmantelado desde dentro.",
        items: [
          { title: "Control judicial de constitucionalidad", article: "Art. XI §3.1(7)", text: "Ninguna enmienda puede abolir el poder constitucional de los tribunales para revisar y bloquear actos inconstitucionales." },
          { title: "Independencia de la Comisión Electoral", article: "Art. XI §3.1(5)", text: "La independencia y el mandato protegido de la Comisión Electoral no pueden eliminarse mediante enmienda." },
          { title: "Independencia de la Comisión de Rendición de Cuentas", article: "Art. XI §3.1(6)", text: "La Comisión de Rendición de Cuentas no puede ser despojada de su papel independiente como salvaguarda constitucional contra la captura." },
        ],
      },
      {
        key: "order",
        label: "Orden constitucional y control civil",
        summary: "El borrador blinda los principios que mantienen la fuerza armada, la política de emergencia y el propio cambio constitucional dentro de un orden democrático legal.",
        items: [
          { title: "Control civil de las fuerzas armadas", article: "Art. XI §3.1(9)", text: "Ninguna enmienda puede legalizar el gobierno militar ni situar a las fuerzas armadas por encima de la autoridad constitucional electa." },
          { title: "Transferencia pacífica del poder", article: "Art. XI §3.1(10)", text: "Ninguna enmienda puede abolir la obligación constitucional de realizar una transferencia legal del poder tras elecciones o sucesión constitucional." },
          { title: "El poder de reforma sigue limitado", article: "Art. XI §3.1(11)", text: "El propio núcleo democrático no puede volverse reformable por enmienda ordinaria. El bloqueo se protege a sí mismo." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "筛选不可修宪核心类别",
    note: "本指南将受到永久保护的民主核心分成功能类别，帮助读者看清哪些内容被宪法置于修宪、废除或暂停之外。",
    categories: [
      {
        key: "democracy",
        label: "民主结构",
        summary: "宪法永久保护合法民主统治的基本运作机制。",
        items: [
          { title: "联邦选举中的普遍平等选举权", article: "第十一条 §3.1(1)", text: "任何修宪都不得废除或掏空成年公民在联邦选举中的平等投票权。" },
          { title: "选举管理与认证的完整性", article: "第十一条 §3.1(2)", text: "任何修宪都不得摧毁有关选举必须依法管理、计票并认证的宪法要求。" },
          { title: "定期的民主更新", article: "第十一条 §3.1(3)", text: "定期选举、固定的宪法更替以及持续的民主链条，不能通过修宪废除。" },
        ],
      },
      {
        key: "membership",
        label: "平等公民资格与权利底线",
        summary: "本草案禁止把共同体变成等级化归属结构，或抹去基本权利底线的修宪。",
        items: [
          { title: "平等公民资格", article: "第十一条 §3.1(4)", text: "任何修宪都不得制造政治成员资格等级或授权二等公民地位。" },
          { title: "核心权利底线", article: "第十一条 §3.1(8)", text: "不得通过保留形式机构而毁掉实质自由的方式，废除或暂停基本权利结构。" },
          { title: "重实质不重标签的保护", article: "第十一条 §3.1", text: "修宪不能靠更改名称来规避这些锁定，同时实质性缩减受保护权利。" },
        ],
      },
      {
        key: "institutions",
        label: "护栏机构",
        summary: "某些机构之所以被锁定，是因为没有它们，民主秩序可能被从内部拆毁。",
        items: [
          { title: "司法审查", article: "第十一条 §3.1(7)", text: "任何修宪都不得废除法院审查并阻止违宪行为的宪法权力。" },
          { title: "选举委员会独立性", article: "第十一条 §3.1(5)", text: "选举委员会的独立性和受保护职责不能被修宪消除。" },
          { title: "问责委员会独立性", article: "第十一条 §3.1(6)", text: "问责委员会作为防俘获宪法保障的独立角色，不能被修宪剥夺。" },
        ],
      },
      {
        key: "order",
        label: "宪法秩序与文官统治",
        summary: "本草案锁定那些使武装力量、紧急政治和宪法变更本身都留在合法民主秩序中的原则。",
        items: [
          { title: "军队的文官控制", article: "第十一条 §3.1(9)", text: "任何修宪都不得使军事统治合法化，或让武装力量凌驾于民选宪法权威之上。" },
          { title: "和平移交权力", article: "第十一条 §3.1(10)", text: "任何修宪都不得废除在选举和宪法继任后进行合法权力移交的宪法义务。" },
          { title: "修宪权本身仍受限制", article: "第十一条 §3.1(11)", text: "民主核心本身不能通过普通修宪变得可修。锁定机制保护其自身。" },
        ],
      },
    ],
  },
};

export function unamendableCoreDataForLocale(locale) {
  return UNAMENDABLE_CORE_GUIDE[locale] || UNAMENDABLE_CORE_GUIDE.en;
}
