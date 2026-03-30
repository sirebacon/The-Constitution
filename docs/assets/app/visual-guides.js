const RIGHTS_GUIDE = {
  en: {
    all: "All",
    filterLabel: "Filter rights categories",
    note: "Tap a category to focus on one part of the rights structure.",
    categories: [
      {
        key: "political",
        label: "Political rights",
        summary: "Voting, officeholding, petition, recall, initiative, and democratic participation.",
        items: [
          { title: "Vote and political participation", article: "Articles I, IX", text: "Protects voting access, equal political membership, and participation in federal democratic life." },
          { title: "Run for office", article: "Articles I, III, IX", text: "Protects access to elected office subject to constitutional qualifications rather than caste restrictions." },
          { title: "Recall and referendum", article: "Articles I, III", text: "Builds public democratic correction mechanisms into the constitutional structure." },
        ],
      },
      {
        key: "civil",
        label: "Civil liberties",
        summary: "Speech, press, assembly, religion, privacy, movement, and conscience.",
        items: [
          { title: "Speech, press, and assembly", article: "Article V", text: "Protects political expression and public dissent as core democratic liberties." },
          { title: "Religion and conscience", article: "Article V", text: "Protects free exercise while keeping the state institutionally neutral." },
          { title: "Privacy and movement", article: "Article V", text: "Protects personal life, bodily autonomy, movement, and freedom from arbitrary intrusion." },
        ],
      },
      {
        key: "process",
        label: "Due process",
        summary: "Fair process in arrest, trial, punishment, detention, and emergency conditions.",
        items: [
          { title: "Criminal procedure", article: "Article V", text: "Protects notice, counsel, impartial adjudication, and safeguards for accused persons." },
          { title: "Habeas corpus and detention limits", article: "Article V", text: "Protects against indefinite or lawless detention, including under emergency pressure." },
          { title: "Fair legal process", article: "Articles V, IX", text: "Requires due process before the state can impose major status loss or punishment." },
        ],
      },
      {
        key: "equality",
        label: "Equality",
        summary: "Equal citizenship, equal protection, and anti-discrimination guarantees.",
        items: [
          { title: "Equal protection", article: "Article V", text: "Protects against unequal treatment and discriminatory state action." },
          { title: "Equal citizenship", article: "Article IX", text: "Rejects second-class citizenship and protects full political membership." },
          { title: "Status-based non-discrimination", article: "Articles V, IX", text: "Protects equality across sex, identity, orientation, and citizenship status." },
        ],
      },
      {
        key: "digital",
        label: "Digital rights",
        summary: "Modern privacy, access, and anti-surveillance protections for networked life.",
        items: [
          { title: "Digital privacy", article: "Article V", text: "Protects communications, data, and digital effects against unlawful intrusion." },
          { title: "Internet access and civic participation", article: "Article V", text: "Recognizes network access as tied to participation in modern democratic life." },
          { title: "Protection against digital suppression", article: "Articles V, VI", text: "Constrains coercive digital suppression and abuse of civic information systems." },
        ],
      },
      {
        key: "social",
        label: "Social and economic rights",
        summary: "Healthcare, education, housing, labor, and child welfare floors.",
        items: [
          { title: "Healthcare", article: "Article XVIII", text: "Guarantees access to basic and emergency care as a public constitutional duty." },
          { title: "Education and child welfare", article: "Article XVIII", text: "Secures education and child-protection floors as conditions of equal citizenship." },
          { title: "Housing and work", article: "Article XVIII", text: "Recognizes minimum social and economic guarantees tied to dignity and democratic membership." },
        ],
      },
      {
        key: "nonderogable",
        label: "Non-derogable rights",
        summary: "Rights that remain protected even under emergency conditions.",
        items: [
          { title: "Core liberty floor", article: "Article V", text: "Protects basic anti-torture, due process, and anti-disappearance principles against suspension." },
          { title: "Democratic floor", article: "Articles V, XI", text: "Prevents emergencies from lawfully extinguishing the core democratic order." },
          { title: "Judicial enforceability", article: "Articles IV, V", text: "Keeps emergency rights review inside the constitutional order rather than outside it." },
        ],
      },
    ],
  },
  es: {
    all: "Todo",
    filterLabel: "Filtrar categorías de derechos",
    note: "Pulsa una categoría para centrarte en una parte de la estructura de derechos.",
    categories: [
      {
        key: "political",
        label: "Derechos políticos",
        summary: "Voto, acceso a cargos, petición, revocación, iniciativa y participación democrática.",
        items: [
          { title: "Voto y participación política", article: "Artículos I, IX", text: "Protege el acceso al voto, la membresía política igualitaria y la participación en la vida democrática federal." },
          { title: "Acceso a cargos públicos", article: "Artículos I, III, IX", text: "Protege el acceso a los cargos electivos sujeto a requisitos constitucionales y no a restricciones de casta." },
          { title: "Revocación e iniciativa", article: "Artículos I, III", text: "Incorpora mecanismos democráticos de corrección pública dentro de la propia estructura constitucional." },
        ],
      },
      {
        key: "civil",
        label: "Libertades civiles",
        summary: "Expresión, prensa, reunión, religión, privacidad, movimiento y conciencia.",
        items: [
          { title: "Expresión, prensa y reunión", article: "Artículo V", text: "Protege la expresión política y el disenso público como libertades democráticas centrales." },
          { title: "Religión y conciencia", article: "Artículo V", text: "Protege el libre ejercicio mientras mantiene la neutralidad institucional del Estado." },
          { title: "Privacidad y movimiento", article: "Artículo V", text: "Protege la vida personal, la autonomía corporal, el movimiento y la libertad frente a intrusiones arbitrarias." },
        ],
      },
      {
        key: "process",
        label: "Debido proceso",
        summary: "Garantías procesales frente al arresto, el juicio, el castigo, la detención y la emergencia.",
        items: [
          { title: "Procedimiento penal", article: "Artículo V", text: "Protege la notificación, la asistencia letrada, la adjudicación imparcial y las garantías de las personas acusadas." },
          { title: "Hábeas corpus y límites a la detención", article: "Artículo V", text: "Protege contra la detención indefinida o arbitraria, incluso bajo presión de emergencia." },
          { title: "Proceso jurídico justo", article: "Artículos V, IX", text: "Exige debido proceso antes de que el Estado pueda imponer una pérdida grave de estatus o un castigo." },
        ],
      },
      {
        key: "equality",
        label: "Igualdad",
        summary: "Ciudadanía igual, igual protección y garantías antidiscriminatorias.",
        items: [
          { title: "Igual protección", article: "Artículo V", text: "Protege contra el trato desigual y la acción estatal discriminatoria." },
          { title: "Ciudadanía igualitaria", article: "Artículo IX", text: "Rechaza la ciudadanía de segunda clase y protege la membresía política plena." },
          { title: "No discriminación por estatus", article: "Artículos V, IX", text: "Protege la igualdad frente a discriminación por sexo, identidad, orientación o condición de ciudadanía." },
        ],
      },
      {
        key: "digital",
        label: "Derechos digitales",
        summary: "Privacidad, acceso y protección frente a vigilancia en la vida conectada.",
        items: [
          { title: "Privacidad digital", article: "Artículo V", text: "Protege comunicaciones, datos y efectos digitales frente a intrusiones ilícitas." },
          { title: "Acceso a internet y participación cívica", article: "Artículo V", text: "Reconoce el acceso a la red como parte de la participación en la vida democrática moderna." },
          { title: "Protección frente a la supresión digital", article: "Artículos V, VI", text: "Limita la supresión coercitiva en el entorno digital y el abuso de sistemas cívicos de información." },
        ],
      },
      {
        key: "social",
        label: "Derechos sociales y económicos",
        summary: "Pisos de atención médica, educación, vivienda, trabajo y bienestar infantil.",
        items: [
          { title: "Atención médica", article: "Artículo XVIII", text: "Garantiza el acceso a la atención básica y de emergencia como deber público constitucional." },
          { title: "Educación y bienestar infantil", article: "Artículo XVIII", text: "Asegura pisos de educación y protección infantil como condiciones de ciudadanía igualitaria." },
          { title: "Vivienda y trabajo", article: "Artículo XVIII", text: "Reconoce garantías sociales y económicas mínimas ligadas a la dignidad y la membresía democrática." },
        ],
      },
      {
        key: "nonderogable",
        label: "Derechos no derogables",
        summary: "Derechos que siguen protegidos incluso en condiciones de emergencia.",
        items: [
          { title: "Piso básico de libertad", article: "Artículo V", text: "Protege principios básicos contra la tortura, la desaparición y la suspensión del debido proceso." },
          { title: "Piso democrático", article: "Artículos V, XI", text: "Impide que una emergencia extinga lícitamente el núcleo del orden democrático." },
          { title: "Exigibilidad judicial", article: "Artículos IV, V", text: "Mantiene la revisión judicial de derechos de emergencia dentro del orden constitucional." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部",
    filterLabel: "筛选权利类别",
    note: "点击某一类别，可聚焦查看权利结构中的一个部分。",
    categories: [
      {
        key: "political",
        label: "政治权利",
        summary: "投票、参选、请愿、罢免、倡议与民主参与。",
        items: [
          { title: "投票与政治参与", article: "第一条、第九条", text: "保护投票可及性、平等政治成员资格，以及参与联邦民主生活的权利。" },
          { title: "担任公职", article: "第一条、第三条、第九条", text: "保护在宪法资格限制下竞选公职，而不是受制于身份等级限制。" },
          { title: "罢免与公民倡议", article: "第一条、第三条", text: "把公众民主纠偏机制直接嵌入宪法结构之中。" },
        ],
      },
      {
        key: "civil",
        label: "公民自由",
        summary: "言论、新闻、集会、宗教、隐私、迁徙与良心自由。",
        items: [
          { title: "言论、新闻与集会", article: "第五条", text: "将政治表达与公共异议保护为核心民主自由。" },
          { title: "宗教与良心自由", article: "第五条", text: "保护自由信仰，同时保持国家制度上的中立。" },
          { title: "隐私与迁徙", article: "第五条", text: "保护私人生活、身体自主、迁徙自由以及免受任意侵扰。" },
        ],
      },
      {
        key: "process",
        label: "正当程序",
        summary: "在逮捕、审判、惩罚、拘禁与紧急状态中的程序保障。",
        items: [
          { title: "刑事程序", article: "第五条", text: "保护通知、律师帮助、公正裁判以及被告人的程序保障。" },
          { title: "人身保护令与拘禁限制", article: "第五条", text: "防止无限期或无法律依据的拘禁，包括在紧急压力下。" },
          { title: "公正法律程序", article: "第五条、第九条", text: "要求国家在施加重大身份剥夺或处罚前遵守正当程序。" },
        ],
      },
      {
        key: "equality",
        label: "平等",
        summary: "平等公民资格、平等保护与反歧视保障。",
        items: [
          { title: "平等保护", article: "第五条", text: "保护个人免受不平等待遇和歧视性国家行为。" },
          { title: "平等公民资格", article: "第九条", text: "拒绝二等公民地位，保护完整的政治成员资格。" },
          { title: "基于身份的非歧视", article: "第五条、第九条", text: "在性别、身份、取向与公民资格地位上保护平等。" },
        ],
      },
      {
        key: "digital",
        label: "数字权利",
        summary: "面向网络时代的隐私、接入与反监控保障。",
        items: [
          { title: "数字隐私", article: "第五条", text: "保护通信、数据和数字财产免受非法侵扰。" },
          { title: "互联网接入与公民参与", article: "第五条", text: "承认网络接入与现代民主参与密切相关。" },
          { title: "防止数字压制", article: "第五条、第六条", text: "限制强制性的数字压制和对公民信息系统的滥用。" },
        ],
      },
      {
        key: "social",
        label: "社会与经济权利",
        summary: "医疗、教育、住房、劳动与儿童福祉底线。",
        items: [
          { title: "医疗保障", article: "第十八条", text: "将获得基本与紧急医疗服务确立为公共宪法义务。" },
          { title: "教育与儿童福祉", article: "第十八条", text: "将教育与儿童保护底线作为平等公民资格的条件。" },
          { title: "住房与工作", article: "第十八条", text: "承认与尊严和民主成员资格相关的最低社会经济保障。" },
        ],
      },
      {
        key: "nonderogable",
        label: "不可减损权利",
        summary: "即使在紧急状态下仍然受到保护的权利。",
        items: [
          { title: "核心自由底线", article: "第五条", text: "保护反酷刑、反失踪和正当程序等基本原则，不得暂停。" },
          { title: "民主底线", article: "第五条、第十一条", text: "防止紧急状态合法消灭民主秩序的核心结构。" },
          { title: "司法可执行性", article: "第四条、第五条", text: "确保紧急状态下的权利审查仍处于宪法秩序之内。" },
        ],
      },
    ],
  },
};

const EMERGENCY_GUIDE = {
  en: {
    all: "All paths",
    ordinary: "Ordinary path",
    lapse: "Lapse path",
    abuse: "Abuse path",
    filterLabel: "Filter emergency lifecycle paths",
    note: "Follow the ordinary approval path, the automatic-lapse path, or the abuse path where emergency power is stretched beyond lawful limits.",
    sections: [
      {
        key: "ordinary",
        label: "Ordinary constitutional path",
        summary: "Emergency power exists only inside a timed and reviewable constitutional chain.",
        steps: [
          { title: "Declaration", meta: "Day 0 · Article III §5.1", text: "The President may declare a national emergency only in response to an imminent threat requiring action faster than the ordinary legislative process permits." },
          { title: "Immediate but limited powers", meta: "Day 0 · Article III §5.2–§5.3", text: "The declaration activates only the narrow emergency powers the Constitution and ordinary law allow. It cannot suspend rights except as separately authorized." },
          { title: "Submission to the Regional Assembly", meta: "Within 48 hours · Article III §5.4", text: "The declaration must be submitted to the Regional Assembly within 48 hours for approval or rejection." },
          { title: "Approval window", meta: "By Day 30 · Article III §5.4", text: "The Regional Assembly must approve or reject the declaration within 30 days. This vote is constitutionally mandatory." },
          { title: "Renewal path", meta: "Successive 30-day periods · Article III §5.5", text: "If approved, the declaration may be renewed in successive 30-day periods. It cannot continue past 180 days without a 2/3 vote of both chambers." },
          { title: "Termination", meta: "Any time · Article III §5.6", text: "The emergency ends when its period expires, when either chamber votes to terminate it, or when the President declares it over." },
        ],
      },
      {
        key: "lapse",
        label: "Automatic lapse path",
        summary: "The system is designed so a missed approval deadline kills the declaration automatically.",
        steps: [
          { title: "No approval", meta: "Day 30 · Article III §5.4", text: "If the Regional Assembly does not approve the declaration within 30 days, the emergency lapses automatically at the end of the thirtieth day." },
          { title: "Dependent measures become void", meta: "Immediate · Article III §5.4", text: "All powers, directives, suspensions, deployments, or restrictions that depend on the declaration become void unless separately authorized by ordinary law." },
          { title: "Judicial certificate", meta: "Immediate · Article III §5.4 / Article IV §2.7", text: "The Chief Justice or designated judicial officer must issue a public certificate stating that the declaration has expired. Failure to issue that certificate does not preserve the emergency." },
          { title: "Immediate standing", meta: "Immediate · Article III §5.4", text: "Any person still subject to enforcement after lapse has immediate standing to seek relief in federal court." },
          { title: "No shell-game redeclaration", meta: "60-day lockout · Article III §5.4", text: "A substantially similar emergency cannot simply be re-declared for 60 days unless materially new circumstances are certified and survive expedited judicial review." },
        ],
      },
      {
        key: "abuse",
        label: "Abuse and review path",
        summary: "If emergency power is stretched, constitutional review, rights limits, and accountability mechanisms continue operating.",
        steps: [
          { title: "Rights floor remains", meta: "Article III §5.3 / Article V §14", text: "An emergency declaration does not itself suspend rights. Non-derogable rights remain protected even under emergency conditions." },
          { title: "Courts remain open", meta: "Article IV §9.7 / §10 / Article V §1.3", text: "Emergency orders remain subject to judicial review, transparency requirements, and expedited treatment where the Constitution requires it." },
          { title: "High-impact directives can be fast-tracked", meta: "Article IV §9.6A", text: "If the executive uses emergency or unilateral authority in a sweeping way, affected parties can seek direct accelerated review." },
          { title: "Either chamber may terminate", meta: "Article III §5.6", text: "Emergency power is not locked in once approved. A majority of either chamber can terminate the declaration." },
          { title: "Defiance remains punishable", meta: "Article III §15 / Article XII", text: "Executive defiance, unlawful continuation, or rights violations still trigger accountability and may support removal or prosecution." },
        ],
      },
    ],
  },
  es: {
    all: "Todas las rutas",
    ordinary: "Ruta ordinaria",
    lapse: "Ruta de caducidad",
    abuse: "Ruta de abuso",
    filterLabel: "Filtrar rutas del ciclo de emergencia",
    note: "Sigue la ruta ordinaria de aprobación, la ruta de caducidad automática o la ruta de abuso cuando el poder de emergencia se estira más allá de sus límites legales.",
    sections: [
      {
        key: "ordinary",
        label: "Ruta constitucional ordinaria",
        summary: "El poder de emergencia solo existe dentro de una cadena constitucional temporizada y revisable.",
        steps: [
          { title: "Declaración", meta: "Día 0 · Artículo III §5.1", text: "El Presidente solo puede declarar una emergencia nacional en respuesta a una amenaza inminente que requiera actuar más rápido de lo que permite el proceso legislativo ordinario." },
          { title: "Poderes inmediatos pero limitados", meta: "Día 0 · Artículo III §5.2–§5.3", text: "La declaración activa solo los poderes de emergencia limitados que permiten la Constitución y la ley ordinaria. No puede suspender derechos salvo autorización separada." },
          { title: "Remisión a la Asamblea Regional", meta: "Dentro de 48 horas · Artículo III §5.4", text: "La declaración debe remitirse a la Asamblea Regional dentro de 48 horas para su aprobación o rechazo." },
          { title: "Ventana de aprobación", meta: "Antes del día 30 · Artículo III §5.4", text: "La Asamblea Regional debe aprobar o rechazar la declaración en 30 días. Esa votación es constitucionalmente obligatoria." },
          { title: "Ruta de renovación", meta: "Períodos sucesivos de 30 días · Artículo III §5.5", text: "Si se aprueba, la declaración puede renovarse por períodos sucesivos de 30 días. No puede continuar más allá de 180 días sin un voto de 2/3 de ambas cámaras." },
          { title: "Terminación", meta: "En cualquier momento · Artículo III §5.6", text: "La emergencia termina cuando expira su período, cuando cualquiera de las cámaras vota por terminarla o cuando el Presidente declara que ha terminado." },
        ],
      },
      {
        key: "lapse",
        label: "Ruta de caducidad automática",
        summary: "El sistema está diseñado para que la falta de aprobación extinga automáticamente la declaración.",
        steps: [
          { title: "Sin aprobación", meta: "Día 30 · Artículo III §5.4", text: "Si la Asamblea Regional no aprueba la declaración dentro de 30 días, la emergencia caduca automáticamente al final del trigésimo día." },
          { title: "Las medidas dependientes quedan sin efecto", meta: "Inmediato · Artículo III §5.4", text: "Todos los poderes, directivas, suspensiones, despliegues o restricciones que dependan de la declaración quedan sin efecto, salvo autorización independiente de la ley ordinaria." },
          { title: "Certificación judicial", meta: "Inmediato · Artículo III §5.4 / Artículo IV §2.7", text: "El Presidente del Tribunal Supremo o la autoridad judicial designada debe emitir una certificación pública de que la declaración ha expirado. La falta de certificado no preserva la emergencia." },
          { title: "Legitimación inmediata", meta: "Inmediato · Artículo III §5.4", text: "Toda persona que siga sometida a medidas tras la caducidad tiene legitimación inmediata para acudir a los tribunales federales." },
          { title: "No re-declaración de cobertura", meta: "Bloqueo de 60 días · Artículo III §5.4", text: "No puede redeclararse una emergencia sustancialmente igual durante 60 días salvo que existan circunstancias materialmente nuevas y superen revisión judicial acelerada." },
        ],
      },
      {
        key: "abuse",
        label: "Ruta de abuso y revisión",
        summary: "Si el poder de emergencia se estira, siguen operando la revisión constitucional, los límites de derechos y los mecanismos de rendición de cuentas.",
        steps: [
          { title: "El piso de derechos permanece", meta: "Artículo III §5.3 / Artículo V §14", text: "La declaración de emergencia no suspende por sí sola los derechos. Los derechos no derogables permanecen protegidos incluso en emergencia." },
          { title: "Los tribunales siguen abiertos", meta: "Artículo IV §9.7 / §10 / Artículo V §1.3", text: "Las órdenes de emergencia siguen sujetas a revisión judicial, requisitos de transparencia y tramitación acelerada cuando la Constitución lo exige." },
          { title: "Las directivas de alto impacto pueden ir por vía rápida", meta: "Artículo IV §9.6A", text: "Si el ejecutivo usa autoridad de emergencia o unilateral de forma amplia, las personas afectadas pueden solicitar revisión acelerada directa." },
          { title: "Cualquiera de las cámaras puede terminarla", meta: "Artículo III §5.6", text: "El poder de emergencia no queda blindado una vez aprobado. Una mayoría de cualquiera de las cámaras puede terminar la declaración." },
          { title: "La desobediencia sigue siendo punible", meta: "Artículo III §15 / Artículo XII", text: "La desobediencia ejecutiva, la continuación ilícita o las violaciones de derechos siguen activando responsabilidad y pueden fundamentar destitución o enjuiciamiento." },
        ],
      },
    ],
  },
  "zh-Hans": {
    all: "全部路径",
    ordinary: "通常路径",
    lapse: "失效路径",
    abuse: "滥用路径",
    filterLabel: "筛选紧急权力路径",
    note: "你可以查看通常批准路径、自动失效路径，或当紧急权力被拉伸到法定边界之外时的滥用路径。",
    sections: [
      {
        key: "ordinary",
        label: "通常宪法路径",
        summary: "紧急权力只能存在于一条有时限且可审查的宪法链条之内。",
        steps: [
          { title: "宣布紧急状态", meta: "第 0 天 · 第三条 §5.1", text: "总统只有在面临迫在眉睫、且必须快于普通立法程序作出回应的威胁时，才能宣布国家紧急状态。" },
          { title: "即时但受限的权力", meta: "第 0 天 · 第三条 §5.2–§5.3", text: "宣布仅激活宪法和普通法律允许的有限紧急权力。除非有单独授权，否则不得暂停权利。" },
          { title: "提交地区议会", meta: "48 小时内 · 第三条 §5.4", text: "该声明必须在 48 小时内提交地区议会批准或否决。" },
          { title: "批准窗口", meta: "第 30 天前 · 第三条 §5.4", text: "地区议会必须在 30 天内批准或否决该声明。这一表决是宪法强制要求的。" },
          { title: "续期路径", meta: "连续 30 天期间 · 第三条 §5.5", text: "一旦获批，紧急状态可按连续 30 天期间续期。未经两院各 2/3 同意，不得超过 180 天。" },
          { title: "终止", meta: "任何时候 · 第三条 §5.6", text: "紧急状态会在授权期届满、任一议院投票终止、或总统书面宣布结束时终止。" },
        ],
      },
      {
        key: "lapse",
        label: "自动失效路径",
        summary: "制度被设计为：一旦未获批准，声明会自动失效。",
        steps: [
          { title: "未获批准", meta: "第 30 天 · 第三条 §5.4", text: "如果地区议会未在 30 天内批准该声明，紧急状态将在第 30 天结束时自动失效。" },
          { title: "依附措施失效", meta: "立即 · 第三条 §5.4", text: "所有依赖该声明的权力、指令、暂停、部署或限制都会失效，除非它们另有普通法律依据。" },
          { title: "司法证明", meta: "立即 · 第三条 §5.4 / 第四条 §2.7", text: "首席大法官或指定司法官必须发布公开证明，说明该声明已经届满。未发布证明并不会维持紧急状态。" },
          { title: "立即诉权", meta: "立即 · 第三条 §5.4", text: "任何人在紧急状态失效后若仍被继续执行相关措施，都立即有资格向联邦法院寻求救济。" },
          { title: "不得用同一事实重新宣布", meta: "60 天锁定期 · 第三条 §5.4", text: "在 60 天内，不得基于大体相同的事实重新宣布紧急状态，除非出现实质性新情况，并通过加速司法审查。" },
        ],
      },
      {
        key: "abuse",
        label: "滥用与审查路径",
        summary: "如果紧急权力被拉伸使用，宪法审查、权利限制和问责机制仍然继续运作。",
        steps: [
          { title: "权利底线仍然存在", meta: "第三条 §5.3 / 第五条 §14", text: "紧急状态声明本身不会自动暂停权利。不可减损权利在紧急状态下仍受保护。" },
          { title: "法院仍然开放", meta: "第四条 §9.7 / §10 / 第五条 §1.3", text: "紧急命令仍然受司法审查、透明度要求，以及宪法规定的加速程序约束。" },
          { title: "高影响指令可走快速通道", meta: "第四条 §9.6A", text: "如果行政部门以紧急或单边权力作出广泛影响的指令，受影响者可以请求直接加速审查。" },
          { title: "任一议院都可以终止", meta: "第三条 §5.6", text: "一旦获批并不意味着紧急权力不可撤销。任一议院的多数都可以终止该声明。" },
          { title: "抗命仍会被追责", meta: "第三条 §15 / 第十二条", text: "行政抗命、违法延续或权利侵害仍会触发问责，并可能支持罢免或起诉。" },
        ],
      },
    ],
  },
};

function dataForLocale(locale) {
  return RIGHTS_GUIDE[locale] || RIGHTS_GUIDE.en;
}

function emergencyDataForLocale(locale) {
  return EMERGENCY_GUIDE[locale] || EMERGENCY_GUIDE.en;
}

function rightsCards(categories) {
  return categories
    .map(
      (category) => `
        <section class="rights-category" data-rights-category="${category.key}">
          <header class="rights-category__header">
            <div>
              <div class="eyebrow">${category.label}</div>
              <h2 class="rights-category__title">${category.label}</h2>
            </div>
            <p class="rights-category__summary">${category.summary}</p>
          </header>
          <div class="rights-grid">
            ${category.items
              .map(
                (item) => `
                  <article class="rights-card">
                    <h3>${item.title}</h3>
                    <p>${item.text}</p>
                    <div class="rights-card__meta">${item.article}</div>
                  </article>
                `
              )
              .join("")}
          </div>
        </section>
      `
    )
    .join("");
}

export function renderVisualGuide(doc, siteData) {
  if (doc.slug === "rights-at-a-glance") {
    const data = dataForLocale(siteData.locale);
    return `
      <section class="visual-guide visual-guide--rights" aria-labelledby="visual-guide-title">
        <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
          <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
          ${data.categories
            .map(
              (category) =>
                `<button class="filter-chip" type="button" data-guide-filter="${category.key}">${category.label}</button>`
            )
            .join("")}
        </div>
        <p class="visual-guide__note">${data.note}</p>
        <div class="visual-guide__body">
          ${rightsCards(data.categories)}
        </div>
      </section>
    `;
  }

  if (doc.slug === "emergency-powers-lifecycle") {
    const data = emergencyDataForLocale(siteData.locale);
    return `
      <section class="visual-guide visual-guide--emergency" aria-labelledby="visual-guide-title">
        <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
          <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
          <button class="filter-chip" type="button" data-guide-filter="ordinary">${data.ordinary}</button>
          <button class="filter-chip" type="button" data-guide-filter="lapse">${data.lapse}</button>
          <button class="filter-chip" type="button" data-guide-filter="abuse">${data.abuse}</button>
        </div>
        <p class="visual-guide__note">${data.note}</p>
        <div class="visual-guide__body">
          ${data.sections
            .map(
              (section) => `
                <section class="rights-category emergency-flow" data-rights-category="${section.key}">
                  <header class="rights-category__header">
                    <div>
                      <div class="eyebrow">${section.label}</div>
                      <h2 class="rights-category__title">${section.label}</h2>
                    </div>
                    <p class="rights-category__summary">${section.summary}</p>
                  </header>
                  <ol class="emergency-steps">
                    ${section.steps
                      .map(
                        (step, index) => `
                          <li class="emergency-step">
                            <div class="emergency-step__index">${index + 1}</div>
                            <div class="emergency-step__body">
                              <h3>${step.title}</h3>
                              <div class="rights-card__meta">${step.meta}</div>
                              <p>${step.text}</p>
                            </div>
                          </li>
                        `
                      )
                      .join("")}
                  </ol>
                </section>
              `
            )
            .join("")}
        </div>
      </section>
    `;
  }

  return "";
}

export function activateVisualGuide(doc, container) {
  if (!["rights-at-a-glance", "emergency-powers-lifecycle"].includes(doc.slug) || !container) return;
  const buttons = [...container.querySelectorAll("[data-guide-filter]")];
  const categories = [...container.querySelectorAll("[data-rights-category]")];
  if (!buttons.length || !categories.length) return;

  function applyFilter(filter) {
    buttons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.guideFilter === filter);
    });
    categories.forEach((section) => {
      const show = filter === "all" || section.dataset.rightsCategory === filter;
      section.hidden = !show;
    });
  }

  buttons.forEach((button) => {
    button.addEventListener("click", () => applyFilter(button.dataset.guideFilter));
  });
}
