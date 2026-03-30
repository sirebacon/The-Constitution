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

export const ACCOUNTABILITY_GUIDE = {
  en: {
    all: "All",
    filterLabel: "Filter Accountability Commission categories",
    note: "This guide separates the Commission's composition, powers, limits, and anti-capture protections so readers can see both what it can do and what it cannot become.",
    categories: [
      {
        key: "composition",
        label: "Composition and appointment",
        summary: "How the Commission is staffed and insulated from one-person control.",
        items: [
          { title: "Multi-member body", article: "Art. XII", text: "The Commission is not a single prosecutor. It is a constitutional organ with fixed terms, multi-member structure, and appointment rules that prevent personal control." },
          { title: "Split appointment path", article: "Art. XII", text: "Its membership is selected through a shared institutional path rather than by unilateral presidential choice." },
          { title: "Protected tenure", article: "Art. XII", text: "Members cannot simply be fired for political inconvenience. Removal follows constitutional procedures." },
        ],
      },
      {
        key: "powers",
        label: "Powers",
        summary: "What the Commission can investigate, prosecute, and enforce.",
        items: [
          { title: "Corruption and abuse investigations", article: "Arts. VIII, XII", text: "The Commission can investigate bribery, corruption, anti-subversion conduct, and other public-integrity offenses." },
          { title: "Independent prosecution", article: "Arts. III, VIII, XII", text: "It can bring cases without waiting for ordinary executive political approval." },
          { title: "Constitutional-order protection", article: "Arts. VI, XII", text: "Its mandate includes defending the constitutional order against electoral sabotage, foreign influence, and anti-subversion conduct." },
        ],
      },
      {
        key: "limits",
        label: "Limits",
        summary: "What the Commission is not allowed to become.",
        items: [
          { title: "No free-floating police power", article: "Art. XII", text: "The Commission is not a general domestic-security agency. Its authority is tied to defined constitutional offenses and public-integrity functions." },
          { title: "Still subject to courts", article: "Arts. IV, XII", text: "Its actions remain reviewable in court. Constitutional process does not disappear because the target is politically powerful." },
          { title: "Cannot rewrite policy by prosecution", article: "Arts. VIII, XII", text: "The Commission enforces the constitutional order; it does not become a substitute legislature." },
        ],
      },
      {
        key: "protections",
        label: "Anti-capture protections",
        summary: "What happens if someone tries to paralyze, defund, or capture it.",
        items: [
          { title: "Continuity protections", article: "Arts. XII, XIX", text: "The constitutional design includes startup and continuity backstops so the Commission cannot be quietly switched off during transition or sabotage." },
          { title: "Removal limits", article: "Art. XII", text: "Commission members cannot be removed by ordinary executive displeasure. Constitutional removal procedures still apply." },
          { title: "Institutional sabotage is itself unconstitutional", article: "Arts. VI, XII, XIX", text: "Attempts to destroy records, disable operations, or block lawful functioning can themselves trigger constitutional consequences." },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar categorías de la Comisión de Rendición de Cuentas",
    note: "Esta guía separa la composición, poderes, límites y protecciones contra captura de la Comisión para que el lector vea tanto lo que puede hacer como lo que no puede llegar a ser.",
    categories: [
      {
        key: "composition",
        label: "Composición y nombramiento",
        summary: "Cómo se integra la Comisión y cómo se la protege del control de una sola persona.",
        items: [
          { title: "Órgano colegiado", article: "Art. XII", text: "La Comisión no es un fiscal único. Es un órgano constitucional con mandatos fijos, estructura colegiada y reglas de nombramiento que impiden el control personal." },
          { title: "Vía de nombramiento compartida", article: "Art. XII", text: "Sus integrantes se seleccionan mediante una vía institucional compartida y no por decisión presidencial unilateral." },
          { title: "Mandato protegido", article: "Art. XII", text: "Sus miembros no pueden ser destituidos simplemente por conveniencia política. La remoción sigue procedimientos constitucionales." },
        ],
      },
      {
        key: "powers",
        label: "Poderes",
        summary: "Qué puede investigar, procesar y hacer cumplir la Comisión.",
        items: [
          { title: "Investigaciones de corrupción y abuso", article: "Arts. VIII, XII", text: "La Comisión puede investigar soborno, corrupción, conducta antisubversiva y otros delitos de integridad pública." },
          { title: "Procesamiento independiente", article: "Arts. III, VIII, XII", text: "Puede presentar casos sin esperar aprobación política ordinaria del ejecutivo." },
          { title: "Protección del orden constitucional", article: "Arts. VI, XII", text: "Su mandato incluye defender el orden constitucional frente a sabotaje electoral, influencia extranjera y conducta antisubversiva." },
        ],
      },
      {
        key: "limits",
        label: "Límites",
        summary: "En qué no puede convertirse la Comisión.",
        items: [
          { title: "Sin poder policial general", article: "Art. XII", text: "La Comisión no es una agencia general de seguridad interior. Su autoridad está ligada a delitos constitucionales definidos y funciones de integridad pública." },
          { title: "Sigue sujeta a los tribunales", article: "Arts. IV, XII", text: "Sus actos siguen siendo revisables judicialmente. El proceso constitucional no desaparece porque el objetivo sea políticamente poderoso." },
          { title: "No puede reescribir políticas mediante procesos", article: "Arts. VIII, XII", text: "La Comisión hace cumplir el orden constitucional; no se convierte en una legislatura sustituta." },
        ],
      },
      {
        key: "protections",
        label: "Protecciones contra la captura",
        summary: "Qué pasa si alguien intenta paralizarla, desfinanciarla o capturarla.",
        items: [
          { title: "Protecciones de continuidad", article: "Arts. XII, XIX", text: "El diseño constitucional incluye salvaguardas de arranque y continuidad para que la Comisión no pueda apagarse silenciosamente durante una transición o sabotaje." },
          { title: "Límites a la remoción", article: "Art. XII", text: "Los miembros de la Comisión no pueden ser removidos por simple disgusto del ejecutivo. Siguen aplicando los procedimientos constitucionales de remoción." },
          { title: "El sabotaje institucional es inconstitucional", article: "Arts. VI, XII, XIX", text: "Los intentos de destruir registros, desactivar operaciones o bloquear el funcionamiento legal pueden generar por sí mismos consecuencias constitucionales." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "筛选问责委员会类别",
    note: "本指南将委员会的构成、权力、限制与防俘获保护分开展示，让读者同时看到它能做什么，以及它不能变成什么。",
    categories: [
      {
        key: "composition",
        label: "构成与任命",
        summary: "委员会如何组建，以及如何避免被单一人物控制。",
        items: [
          { title: "多成员机构", article: "第十二条", text: "委员会不是单一检察官，而是一个具有固定任期、多成员结构和防个人控制任命规则的宪法机关。" },
          { title: "共享任命路径", article: "第十二条", text: "其成员通过共享的制度程序产生，而不是由总统单方面决定。" },
          { title: "受保护任期", article: "第十二条", text: "成员不能因为政治不便就被简单解职。罢免仍须遵循宪法程序。" },
        ],
      },
      {
        key: "powers",
        label: "权力",
        summary: "委员会可以调查、起诉和执行什么。",
        items: [
          { title: "腐败与滥权调查", article: "第八条、第十二条", text: "委员会可以调查贿赂、腐败、反颠覆行为以及其他公共廉政犯罪。" },
          { title: "独立起诉", article: "第三条、第八条、第十二条", text: "它可以在不等待行政部门普通政治批准的情况下提起案件。" },
          { title: "保护宪法秩序", article: "第六条、第十二条", text: "其职责包括防止选举破坏、外国影响和反颠覆行为侵害宪法秩序。" },
        ],
      },
      {
        key: "limits",
        label: "限制",
        summary: "委员会不能变成什么。",
        items: [
          { title: "不是一般性警察权机关", article: "第十二条", text: "委员会不是一般性的国内安全机构。它的权力受限于明确的宪法犯罪和公共廉政职能。" },
          { title: "仍受法院约束", article: "第四条、第十二条", text: "其行为仍可由法院审查。目标即使政治上强大，宪法程序也不会消失。" },
          { title: "不能靠起诉改写政策", article: "第八条、第十二条", text: "委员会执行宪法秩序，但不能取代立法机关自行制定政策。" },
        ],
      },
      {
        key: "protections",
        label: "防俘获保护",
        summary: "如果有人试图使其瘫痪、断供或俘获，会发生什么。",
        items: [
          { title: "连续性保护", article: "第十二条、第十九条", text: "宪法设计包含启动与连续性后备机制，因此委员会不能在交接或破坏中被悄悄关闭。" },
          { title: "罢免限制", article: "第十二条", text: "委员会成员不能因行政部门不满而被普通方式解职。仍须适用宪法罢免程序。" },
          { title: "制度性破坏本身违宪", article: "第六条、第十二条、第十九条", text: "试图销毁记录、瘫痪运作或阻断合法功能，本身就可能触发宪法后果。" },
        ],
      },
    ],
  },
};

export function accountabilityDataForLocale(locale) {
  return ACCOUNTABILITY_GUIDE[locale] || ACCOUNTABILITY_GUIDE.en;
}

export const REMOVAL_GUIDE = {
  en: {
    all: "All",
    filterLabel: "Filter by officer type",
    note: "Each table covers one officer type. Every row is one distinct removal path.",
    pathLabel: "Path",
    triggerLabel: "Who triggers",
    decidesLabel: "Who decides",
    thresholdLabel: "Threshold",
    outcomeLabel: "Outcome",
    categories: [
      {
        key: "president",
        label: "President",
        paths: [
          { path: "Impeachment", trigger: "House (simple majority vote)", decides: "Regional Assembly trial", threshold: "2/3 of Regional Assembly", outcome: "Removal; optional disqualification from future office", article: "Art. III §10" },
          { path: "ACC prosecution", trigger: "Accountability Commission", decides: "Federal court (proceeds after leaving office)", threshold: "Criminal conviction", outcome: "Criminal penalties; certain offenses cannot be pardoned", article: "Art. III §15" },
          { path: "Recall", trigger: "Citizens — petition signed by 20% of registered voters across 35+ states, collected within 90 days", decides: "National referendum", threshold: "60% of votes cast + 60% voter turnout", outcome: "Immediate removal; Vice President becomes President", article: "Art. III §14" },
        ],
      },
      {
        key: "congress",
        label: "Members of Congress",
        paths: [
          { path: "Expulsion", trigger: "Chamber member or ethics finding", decides: "The relevant chamber", threshold: "2/3 of chamber", outcome: "Removal from seat", article: "Art. II §5.3" },
          { path: "Automatic removal", trigger: "Final criminal conviction (no vote needed)", decides: "Courts — no chamber action required", threshold: "Conviction of bribery, fraud, electoral subversion, or related corruption offenses", outcome: "Automatic removal upon exhaustion of all appeals", article: "Art. II §5.5(a)" },
          { path: "Recall", trigger: "Citizens — petition by 20% of prior-election votes, collected within 120 days", decides: "District or state recall election", threshold: "Majority of votes cast + 40% turnout", outcome: "Removal; special election held within 90 days", article: "Art. I §13" },
        ],
      },
      {
        key: "judges",
        label: "Federal Judges",
        paths: [
          { path: "Impeachment", trigger: "House — after Judicial Conduct Board investigation and public hearings", decides: "Regional Assembly trial", threshold: "2/3 of Regional Assembly", outcome: "Removal from office", article: "Art. IV §8.1" },
          { path: "Suspension (not removal)", trigger: "Active felony indictment for official-duty offense", decides: "Automatic — no vote required", threshold: "Indictment", outcome: "Suspended from duties with pay pending trial outcome", article: "Art. IV §8.3" },
          { path: "JCB discipline", trigger: "Complaint to Judicial Conduct Board", decides: "Judicial Conduct Board", threshold: "Board finding of misconduct", outcome: "Censure, required recusal, mandatory training, or referral for impeachment", article: "Art. IV §7.2" },
        ],
      },
      {
        key: "organs",
        label: "Constitutional Organs",
        paths: [
          { path: "ACC member — impeachment", trigger: "House of Representatives", decides: "Regional Assembly trial", threshold: "2/3 of Regional Assembly", outcome: "Removal from office", article: "Art. XII §3.6" },
          { path: "EC member — impeachment", trigger: "House of Representatives", decides: "Regional Assembly trial", threshold: "2/3 of Regional Assembly", outcome: "Removal from office", article: "Art. XII §2.6" },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar por tipo de funcionario",
    note: "Cada tabla cubre un tipo de funcionario. Cada fila es un camino de destitución distinto.",
    pathLabel: "Camino",
    triggerLabel: "Quién lo activa",
    decidesLabel: "Quién decide",
    thresholdLabel: "Umbral",
    outcomeLabel: "Resultado",
    categories: [
      {
        key: "president",
        label: "Presidente",
        paths: [
          { path: "Juicio político", trigger: "Cámara (mayoría simple)", decides: "Juicio en la Asamblea Regional", threshold: "2/3 de la Asamblea Regional", outcome: "Destitución; inhabilitación opcional para cargos futuros", article: "Art. III §10" },
          { path: "Procesamiento por la CRC", trigger: "Comisión de Rendición de Cuentas", decides: "Tribunal federal (tras abandonar el cargo)", threshold: "Condena penal", outcome: "Penas penales; ciertos delitos no pueden ser indultados", article: "Art. III §15" },
          { path: "Revocación", trigger: "Ciudadanos — petición firmada por el 20% de los votantes registrados en 35+ estados, en 90 días", decides: "Referéndum nacional", threshold: "60% de los votos emitidos + 60% de participación", outcome: "Destitución inmediata; el Vicepresidente asume la Presidencia", article: "Art. III §14" },
        ],
      },
      {
        key: "congress",
        label: "Miembros del Congreso",
        paths: [
          { path: "Expulsión", trigger: "Miembro de la cámara o hallazgo ético", decides: "La cámara correspondiente", threshold: "2/3 de la cámara", outcome: "Pérdida del escaño", article: "Art. II §5.3" },
          { path: "Remoción automática", trigger: "Condena penal firme (sin votación requerida)", decides: "Tribunales — sin acción de la cámara", threshold: "Condena por soborno, fraude, subversión electoral u otras ofensas corruptas", outcome: "Remoción automática al agotarse todos los recursos", article: "Art. II §5.5(a)" },
          { path: "Revocación", trigger: "Ciudadanos — petición del 20% de votos de la elección anterior, en 120 días", decides: "Elección de revocación en el distrito o estado", threshold: "Mayoría de votos emitidos + 40% de participación", outcome: "Destitución; elección especial en 90 días", article: "Art. I §13" },
        ],
      },
      {
        key: "judges",
        label: "Jueces federales",
        paths: [
          { path: "Juicio político", trigger: "Cámara — tras investigación de la JCJ y audiencias públicas", decides: "Juicio en la Asamblea Regional", threshold: "2/3 de la Asamblea Regional", outcome: "Destitución del cargo", article: "Art. IV §8.1" },
          { path: "Suspensión (no destitución)", trigger: "Acusación penal activa por delito en funciones", decides: "Automático — sin votación requerida", threshold: "Acusación formal", outcome: "Suspensión de funciones con sueldo hasta el resultado del juicio", article: "Art. IV §8.3" },
          { path: "Disciplina de la JCJ", trigger: "Queja ante la Junta de Conducta Judicial", decides: "Junta de Conducta Judicial", threshold: "Hallazgo de mala conducta", outcome: "Censura, recusación obligatoria, formación o remisión para destitución", article: "Art. IV §7.2" },
        ],
      },
      {
        key: "organs",
        label: "Órganos constitucionales",
        paths: [
          { path: "Miembro de la CRC — juicio político", trigger: "Cámara de Representantes", decides: "Juicio en la Asamblea Regional", threshold: "2/3 de la Asamblea Regional", outcome: "Destitución del cargo", article: "Art. XII §3.6" },
          { path: "Miembro de la CE — juicio político", trigger: "Cámara de Representantes", decides: "Juicio en la Asamblea Regional", threshold: "2/3 de la Asamblea Regional", outcome: "Destitución del cargo", article: "Art. XII §2.6" },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "按官员类型筛选",
    note: "每张表涵盖一类官员。每行代表一条独立的罢免路径。",
    pathLabel: "路径",
    triggerLabel: "谁触发",
    decidesLabel: "谁决定",
    thresholdLabel: "门槛",
    outcomeLabel: "结果",
    categories: [
      {
        key: "president",
        label: "总统",
        paths: [
          { path: "弹劾", trigger: "众议院（简单多数）", decides: "地区议会审判", threshold: "地区议会2/3多数", outcome: "免职；可另行投票禁止担任未来公职", article: "第三条 §10" },
          { path: "问责委员会起诉", trigger: "问责委员会", decides: "联邦法院（离任后进行）", threshold: "刑事定罪", outcome: "刑事处罚；特定罪行不可赦免", article: "第三条 §15" },
          { path: "公民罢免", trigger: "公民联署——35个以上州各至少1%、总计20%登记选民在90天内签名", decides: "全国公民投票", threshold: "60%有效票 + 60%投票率", outcome: "立即免职；副总统继任总统", article: "第三条 §14" },
        ],
      },
      {
        key: "congress",
        label: "国会议员",
        paths: [
          { path: "驱逐", trigger: "议院成员或道德调查结论", decides: "相关议院", threshold: "议院2/3多数", outcome: "失去席位", article: "第二条 §5.3" },
          { path: "自动免职", trigger: "终审刑事定罪（无需投票）", decides: "法院——无需议院行动", threshold: "贿赂、欺诈、选举颠覆或相关腐败罪行定罪", outcome: "上诉穷尽后自动免职", article: "第二条 §5.5(a)" },
          { path: "选民罢免", trigger: "公民联署——上次选举得票的20%，120天内收集", decides: "选区或州罢免选举", threshold: "有效票过半 + 40%投票率", outcome: "免职；90天内举行补选", article: "第一条 §13" },
        ],
      },
      {
        key: "judges",
        label: "联邦法官",
        paths: [
          { path: "弹劾", trigger: "众议院——经司法行为委员会调查及公开听证后", decides: "地区议会审判", threshold: "地区议会2/3多数", outcome: "免职", article: "第四条 §8.1" },
          { path: "停职（非免职）", trigger: "因职务行为被正式起诉重罪", decides: "自动——无需投票", threshold: "正式起诉", outcome: "带薪停职直至审判结果", article: "第四条 §8.3" },
          { path: "司法行为委员会处分", trigger: "向司法行为委员会投诉", decides: "司法行为委员会", threshold: "委员会认定存在不当行为", outcome: "谴责、强制回避、强制培训或移送弹劾", article: "第四条 §7.2" },
        ],
      },
      {
        key: "organs",
        label: "宪法机关",
        paths: [
          { path: "问责委员会委员——弹劾", trigger: "众议院", decides: "地区议会审判", threshold: "地区议会2/3多数", outcome: "免职", article: "第十二条 §3.6" },
          { path: "选举委员会委员——弹劾", trigger: "众议院", decides: "地区议会审判", threshold: "地区议会2/3多数", outcome: "免职", article: "第十二条 §2.6" },
        ],
      },
    ],
  },
};

export function removalDataForLocale(locale) {
  return REMOVAL_GUIDE[locale] || REMOVAL_GUIDE.en;
}

function removalRows(paths) {
  return paths
    .map(
      (p) => `
        <tr>
          <th scope="row">${p.path}</th>
          <td class="congress-cell">${p.trigger}</td>
          <td class="congress-cell">${p.decides}</td>
          <td class="congress-cell congress-cell--draft">${p.threshold}</td>
          <td class="congress-cell">${p.outcome}</td>
          <td class="congress-cell congress-cell--note">${p.article}</td>
        </tr>
      `
    )
    .join("");
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

export const PRESIDENTIAL_POWERS_GUIDE = {
  en: {
    all: "All",
    filterLabel: "Filter presidential power categories",
    note: "Each row compares one presidential power or limit in the current U.S. Constitution and in this draft.",
    categories: [
      {
        key: "core",
        label: "Core executive powers",
        rows: [
          { feature: "Veto", current: "President may veto legislation; no constitutional decision deadline beyond the pocket-veto doctrine", draft: "President may veto legislation, but must sign or veto within 15 days and there is no pocket veto", note: "The draft keeps the veto but removes the recess-based pocket-veto loophole." },
          { feature: "Executive orders", current: "Not expressly defined in the constitutional text", draft: "Expressly authorized but limited to directing the executive branch, implementing law, and exercising vested constitutional powers", note: "The draft constitutionalizes both the power and its limits." },
          { feature: "Executive-order override", current: "No direct legislative disapproval mechanism in the Constitution", draft: "Disapproval by a majority of both chambers voids the order", note: "Adds a constitutional legislative backstop against unilateral executive action." },
        ],
      },
      {
        key: "appointments",
        label: "Appointments and administration",
        rows: [
          { feature: "Confirmation delay", current: "Senate can block nominations indefinitely by inaction", draft: "Regional Assembly inaction for 90 days results in deemed confirmation", note: "Prevents nomination deadlock from becoming a veto by silence." },
          { feature: "Acting officials", current: "Mostly governed by statute", draft: "Acting official may serve only 45 days without a pending nomination; rejected nominees cannot rotate back into the same acting post", note: "Closes a common executive evasion path." },
          { feature: "Removing independent regulators", current: "Depends heavily on doctrine and statute", draft: "Heads of independent agencies may be removed only for cause", note: "Makes insulation from political command constitutionally clearer." },
        ],
      },
      {
        key: "emergency",
        label: "Emergency and war powers",
        rows: [
          { feature: "National emergency", current: "No constitutional approval timetable", draft: "Regional Assembly must approve within 30 days or the declaration lapses automatically", note: "Emergency power exists only inside a timed constitutional chain." },
          { feature: "Commander in Chief", current: "Broadly stated; war-initiation boundaries rely heavily on practice and statute", draft: "Commander in Chief power exists within Article XVI limits; initiating war still belongs to Congress", note: "The draft keeps military command but narrows unilateral war-making." },
          { feature: "Domestic deployment", current: "Mainly statutory and historically elastic", draft: "Domestic military deployment is limited by express constitutional rules in Article XVI", note: "Moves key anti-domestic-force rules into constitutional text." },
        ],
      },
      {
        key: "accountability",
        label: "Accountability limits",
        rows: [
          { feature: "Pardons", current: "Very broad federal pardon power", draft: "No self-pardon, no pardon of co-conspirators in the President's own misconduct, publication and justification required, and timing restrictions apply", note: "The draft keeps clemency but narrows its abuse potential." },
          { feature: "Criminal immunity", current: "Modern doctrine has recognized broad presidential immunity claims", draft: "No categorical immunity for official acts; indictment may proceed while in office, with trial stayed until departure", note: "Official power is not a shield against criminal law." },
          { feature: "Removal and recall", current: "Impeachment only", draft: "Impeachment remains, but recall and ACC-driven criminal accountability are also part of the constitutional system", note: "The presidency is still powerful, but no longer politically untouchable between elections." },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar categorías de poder presidencial",
    note: "Cada fila compara un poder o límite presidencial en la Constitución actual de EE. UU. y en este borrador.",
    categories: [
      {
        key: "core",
        label: "Poderes ejecutivos básicos",
        rows: [
          { feature: "Veto", current: "El Presidente puede vetar legislación; no hay plazo constitucional claro de decisión más allá de la doctrina del veto de bolsillo", draft: "El Presidente puede vetar legislación, pero debe firmar o vetar en 15 días y no existe veto de bolsillo", note: "El borrador mantiene el veto pero elimina la escapatoria del receso." },
          { feature: "Órdenes ejecutivas", current: "No están definidas expresamente en el texto constitucional", draft: "Se autorizan expresamente, pero limitadas a dirigir el poder ejecutivo, ejecutar la ley y ejercer poderes constitucionales conferidos", note: "El borrador constitucionaliza tanto el poder como sus límites." },
          { feature: "Revocación legislativa de órdenes ejecutivas", current: "No existe un mecanismo constitucional directo de desaprobación", draft: "La desaprobación por mayoría de ambas cámaras deja sin efecto la orden", note: "Añade una válvula constitucional frente a la acción ejecutiva unilateral." },
        ],
      },
      {
        key: "appointments",
        label: "Nombramientos y administración",
        rows: [
          { feature: "Retraso en confirmaciones", current: "El Senado puede bloquear nominaciones indefinidamente por inacción", draft: "La inacción de la Asamblea Regional durante 90 días produce confirmación tácita", note: "Evita que el silencio se convierta en veto." },
          { feature: "Funcionarios interinos", current: "Se rigen sobre todo por ley ordinaria", draft: "Un interino solo puede servir 45 días sin nominación pendiente; un nominado rechazado no puede volver al mismo cargo interino", note: "Cierra una vía común de evasión ejecutiva." },
          { feature: "Remoción de reguladores independientes", current: "Depende mucho de doctrina y estatuto", draft: "Los jefes de agencias independientes solo pueden ser removidos por causa", note: "Aclara constitucionalmente el blindaje frente al mando político." },
        ],
      },
      {
        key: "emergency",
        label: "Emergencia y guerra",
        rows: [
          { feature: "Emergencia nacional", current: "No hay calendario constitucional de aprobación", draft: "La Asamblea Regional debe aprobar en 30 días o la declaración caduca automáticamente", note: "El poder de emergencia existe solo dentro de una cadena constitucional temporizada." },
          { feature: "Comandante en Jefe", current: "Formulación amplia; los límites para iniciar guerra dependen mucho de práctica y estatuto", draft: "La jefatura militar existe dentro de los límites del Artículo XVI; iniciar la guerra sigue siendo potestad del Congreso", note: "El borrador conserva el mando militar pero estrecha la guerra unilateral." },
          { feature: "Despliegue interno", current: "Principalmente estatutario y históricamente elástico", draft: "El despliegue militar interno queda limitado por reglas constitucionales expresas del Artículo XVI", note: "Lleva reglas clave al texto constitucional." },
        ],
      },
      {
        key: "accountability",
        label: "Límites de rendición de cuentas",
        rows: [
          { feature: "Indultos", current: "Poder de indulto federal muy amplio", draft: "No hay autoindulto, no se puede indultar a coconspiradores en la propia conducta presidencial, y se exige publicación, justificación y límites temporales", note: "El borrador conserva la clemencia pero reduce su potencial de abuso." },
          { feature: "Inmunidad penal", current: "La doctrina moderna ha reconocido amplias reclamaciones de inmunidad presidencial", draft: "No existe inmunidad categórica por actos oficiales; puede haber acusación durante el cargo, con el juicio suspendido hasta dejarlo", note: "El poder oficial no es un escudo frente al derecho penal." },
          { feature: "Remoción y revocación", current: "Solo juicio político", draft: "Se mantiene el juicio político, pero también forman parte del sistema la revocación y la responsabilidad penal impulsada por la CRC", note: "La presidencia sigue siendo fuerte, pero deja de ser intocable entre elecciones." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "筛选总统权力类别",
    note: "每一行比较当前美国宪法下的总统权力或限制，与本草案中的对应安排。",
    categories: [
      {
        key: "core",
        label: "核心行政权力",
        rows: [
          { feature: "否决权", current: "总统可以否决立法；除口袋否决理论外，宪法没有明确决定期限", draft: "总统可以否决立法，但必须在15天内签署或否决，且不存在口袋否决", note: "草案保留否决权，但去除了利用休会拖死法案的空间。" },
          { feature: "行政命令", current: "宪法正文未明确界定", draft: "明文授权，但仅限于指挥行政部门、执行现有法律和行使宪法赋予的权力", note: "草案把权力本身及其边界都写入了宪法。" },
          { feature: "立法机关否决行政命令", current: "宪法中没有直接的立法否决机制", draft: "两院多数通过不赞成决议即可使该命令失效", note: "为单边行政行为增加了宪法性制衡。" },
        ],
      },
      {
        key: "appointments",
        label: "任命与行政管理",
        rows: [
          { feature: "确认拖延", current: "参议院可通过不作为无限期阻挠提名", draft: "地区议会90天不作为即视为确认", note: "防止沉默变成事实上的否决。" },
          { feature: "代理官员", current: "主要由普通法律规定", draft: "若无待审提名，代理官员任职不得超过45天；被否决者不得轮回同一代理岗位", note: "堵住常见的行政规避路径。" },
          { feature: "独立监管机构负责人罢免", current: "高度依赖判例与法律", draft: "独立机构负责人只能因故罢免", note: "更清楚地把免受政治指挥的保护上升为宪法规则。" },
        ],
      },
      {
        key: "emergency",
        label: "紧急与战争权力",
        rows: [
          { feature: "国家紧急状态", current: "没有宪法规定的批准时间表", draft: "地区议会必须在30天内批准，否则声明自动失效", note: "紧急权力只能存在于一条有时限的宪法链条之内。" },
          { feature: "三军统帅", current: "表述宽泛；开战边界主要依赖实践和法律", draft: "统帅权受第十六条限制；发动战争仍属于国会", note: "草案保留军事指挥，但收窄单边开战空间。" },
          { feature: "国内部署军队", current: "主要依赖法定规则，历史上弹性很大", draft: "国内军事部署受到第十六条明确宪法规则限制", note: "把关键的反国内军事滥用规则写入了宪法。" },
        ],
      },
      {
        key: "accountability",
        label: "问责限制",
        rows: [
          { feature: "赦免权", current: "联邦赦免权非常广泛", draft: "不得自我赦免，不得赦免与总统自身不当行为有关的共谋者，且必须公开说明理由并受时间限制", note: "草案保留宽赦，但压缩其被滥用的空间。" },
          { feature: "刑事豁免", current: "现代判例承认过宽泛的总统豁免主张", draft: "对官方行为不存在类别性豁免；在任时可被起诉，审判可待离任后进行", note: "官方权力不能成为逃避刑法的护盾。" },
          { feature: "免职与罢免", current: "只有弹劾", draft: "除弹劾外，公民罢免和问责委员会推动的刑事追责也属于宪法结构的一部分", note: "总统仍然强大，但不再在选举之间不可触及。" },
        ],
      },
    ],
  },
};

export function presidentialPowersDataForLocale(locale) {
  return PRESIDENTIAL_POWERS_GUIDE[locale] || PRESIDENTIAL_POWERS_GUIDE.en;
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
