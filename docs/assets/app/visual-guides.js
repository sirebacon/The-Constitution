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

const POWER_GUIDE = {
  en: {
    all: "All links",
    electoral: "Democratic input",
    checks: "Institutional checks",
    accountability: "Accountability",
    filterLabel: "Filter power distribution links",
    note: "This map shows where democratic authority enters the system and how each institution is constrained by another part of the constitutional order.",
    nodes: [
      { key: "people", label: "The People", summary: "Democratic source of election, recall, ratification, and political legitimacy." },
      { key: "house", label: "House of Representatives", summary: "Popular chamber for legislation, impeachment initiation, and public democratic accountability." },
      { key: "assembly", label: "Regional Assembly", summary: "Second chamber for confirmations, emergency approval, impeachment trial, and treaty functions." },
      { key: "president", label: "President", summary: "Executes law, directs the executive branch, and operates under timed and reviewable constitutional limits." },
      { key: "courts", label: "Courts", summary: "Exercise constitutional review, adjudication, and judicial enforcement of the constitutional order." },
      { key: "ec", label: "Electoral Commission", summary: "Protects election administration, ballot integrity, and campaign-finance enforcement." },
      { key: "acc", label: "Accountability Commission", summary: "Investigates, prosecutes, and protects the constitutional order against corruption and anti-subversion conduct." },
    ],
    links: [
      { category: "electoral", from: "people", to: "house", label: "elect", meta: "Article I" },
      { category: "electoral", from: "people", to: "president", label: "elect", meta: "Articles I, III" },
      { category: "electoral", from: "people", to: "president", label: "recall", meta: "Article III §14" },
      { category: "electoral", from: "people", to: "house", label: "petition and initiative", meta: "Article I" },
      { category: "checks", from: "house", to: "president", label: "impeach", meta: "Articles II, III" },
      { category: "checks", from: "assembly", to: "president", label: "try and remove", meta: "Articles II, III" },
      { category: "checks", from: "assembly", to: "president", label: "approve emergencies", meta: "Article III §5.4" },
      { category: "checks", from: "president", to: "courts", label: "nominate", meta: "Articles III, IV" },
      { category: "checks", from: "assembly", to: "courts", label: "confirm nominations", meta: "Article IV" },
      { category: "checks", from: "courts", to: "president", label: "review directives", meta: "Article IV §9" },
      { category: "checks", from: "courts", to: "house", label: "review laws", meta: "Article IV §9" },
      { category: "checks", from: "house", to: "courts", label: "impeach judges", meta: "Articles II, IV" },
      { category: "checks", from: "assembly", to: "courts", label: "remove on conviction", meta: "Articles II, IV" },
      { category: "accountability", from: "ec", to: "house", label: "certify and administer elections", meta: "Articles I, XII" },
      { category: "accountability", from: "ec", to: "president", label: "certify election process", meta: "Articles I, XII" },
      { category: "accountability", from: "ec", to: "house", label: "enforce campaign finance", meta: "Articles VII, XII" },
      { category: "accountability", from: "acc", to: "president", label: "investigate and prosecute", meta: "Articles VIII, XII" },
      { category: "accountability", from: "acc", to: "house", label: "investigate members", meta: "Articles VIII, XII" },
      { category: "accountability", from: "acc", to: "courts", label: "investigate judicial misconduct", meta: "Articles IV, XII" },
      { category: "accountability", from: "courts", to: "ec", label: "review commission action", meta: "Articles I, IV, XII" },
      { category: "accountability", from: "courts", to: "acc", label: "review constitutional action", meta: "Articles IV, XII" },
    ],
  },
  es: {
    all: "Todos los vínculos",
    electoral: "Entrada democrática",
    checks: "Controles institucionales",
    accountability: "Rendición de cuentas",
    filterLabel: "Filtrar vínculos de distribución del poder",
    note: "Este mapa muestra por dónde entra la autoridad democrática en el sistema y cómo cada institución queda limitada por otra parte del orden constitucional.",
    nodes: [
      { key: "people", label: "El Pueblo", summary: "Fuente democrática de elección, revocación, ratificación y legitimidad política." },
      { key: "house", label: "Cámara de Representantes", summary: "Cámara popular para legislar, iniciar destituciones y sostener la responsabilidad democrática pública." },
      { key: "assembly", label: "Asamblea Regional", summary: "Segunda cámara para confirmaciones, aprobación de emergencias, juicios políticos y funciones en tratados." },
      { key: "president", label: "Presidente", summary: "Ejecuta la ley, dirige el poder ejecutivo y opera bajo límites constitucionales temporizados y revisables." },
      { key: "courts", label: "Tribunales", summary: "Ejercen control constitucional, adjudicación y ejecución judicial del orden constitucional." },
      { key: "ec", label: "Comisión Electoral", summary: "Protege la administración electoral, la integridad de la papeleta y la aplicación del financiamiento de campañas." },
      { key: "acc", label: "Comisión de Rendición de Cuentas", summary: "Investiga, procesa y protege el orden constitucional frente a corrupción y conducta antisubversiva." },
    ],
    links: [
      { category: "electoral", from: "people", to: "house", label: "elige", meta: "Artículo I" },
      { category: "electoral", from: "people", to: "president", label: "elige", meta: "Artículos I, III" },
      { category: "electoral", from: "people", to: "president", label: "revoca", meta: "Artículo III §14" },
      { category: "electoral", from: "people", to: "house", label: "petición e iniciativa", meta: "Artículo I" },
      { category: "checks", from: "house", to: "president", label: "acusa", meta: "Artículos II, III" },
      { category: "checks", from: "assembly", to: "president", label: "juzga y remueve", meta: "Artículos II, III" },
      { category: "checks", from: "assembly", to: "president", label: "aprueba emergencias", meta: "Artículo III §5.4" },
      { category: "checks", from: "president", to: "courts", label: "nomina", meta: "Artículos III, IV" },
      { category: "checks", from: "assembly", to: "courts", label: "confirma nominaciones", meta: "Artículo IV" },
      { category: "checks", from: "courts", to: "president", label: "revisa directivas", meta: "Artículo IV §9" },
      { category: "checks", from: "courts", to: "house", label: "revisa leyes", meta: "Artículo IV §9" },
      { category: "checks", from: "house", to: "courts", label: "acusa a jueces", meta: "Artículos II, IV" },
      { category: "checks", from: "assembly", to: "courts", label: "remueve tras condena", meta: "Artículos II, IV" },
      { category: "accountability", from: "ec", to: "house", label: "certifica y administra elecciones", meta: "Artículos I, XII" },
      { category: "accountability", from: "ec", to: "president", label: "certifica el proceso electoral", meta: "Artículos I, XII" },
      { category: "accountability", from: "ec", to: "house", label: "aplica financiamiento de campañas", meta: "Artículos VII, XII" },
      { category: "accountability", from: "acc", to: "president", label: "investiga y procesa", meta: "Artículos VIII, XII" },
      { category: "accountability", from: "acc", to: "house", label: "investiga a miembros", meta: "Artículos VIII, XII" },
      { category: "accountability", from: "acc", to: "courts", label: "investiga conducta judicial", meta: "Artículos IV, XII" },
      { category: "accountability", from: "courts", to: "ec", label: "revisa la acción de la comisión", meta: "Artículos I, IV, XII" },
      { category: "accountability", from: "courts", to: "acc", label: "revisa la acción constitucional", meta: "Artículos IV, XII" },
    ],
  },
  "zh-Hans": {
    all: "全部联系",
    electoral: "民主输入",
    checks: "制度制衡",
    accountability: "问责",
    filterLabel: "筛选权力分配联系",
    note: "这张图展示民主权威从何进入制度，以及每个机构如何受到宪法秩序中其他部分的约束。",
    nodes: [
      { key: "people", label: "人民", summary: "选举、罢免、批准与政治正当性的民主来源。" },
      { key: "house", label: "众议院", summary: "承担立法、启动弹劾与公共民主问责的民选议院。" },
      { key: "assembly", label: "地区议会", summary: "负责确认、紧急状态批准、弹劾审判与条约职能的第二议院。" },
      { key: "president", label: "总统", summary: "执行法律、领导行政部门，并受有时限且可审查的宪法限制。" },
      { key: "courts", label: "法院", summary: "行使违宪审查、裁判以及对宪法秩序的司法执行。" },
      { key: "ec", label: "选举委员会", summary: "保护选举管理、选票完整性与竞选资金执法。" },
      { key: "acc", label: "问责委员会", summary: "调查、起诉并保护宪法秩序免受腐败与反颠覆行为侵害。" },
    ],
    links: [
      { category: "electoral", from: "people", to: "house", label: "选举", meta: "第一条" },
      { category: "electoral", from: "people", to: "president", label: "选举", meta: "第一条、第三条" },
      { category: "electoral", from: "people", to: "president", label: "罢免", meta: "第三条 §14" },
      { category: "electoral", from: "people", to: "house", label: "请愿与倡议", meta: "第一条" },
      { category: "checks", from: "house", to: "president", label: "提出弹劾", meta: "第二条、第三条" },
      { category: "checks", from: "assembly", to: "president", label: "审判并罢免", meta: "第二条、第三条" },
      { category: "checks", from: "assembly", to: "president", label: "批准紧急状态", meta: "第三条 §5.4" },
      { category: "checks", from: "president", to: "courts", label: "提名", meta: "第三条、第四条" },
      { category: "checks", from: "assembly", to: "courts", label: "确认提名", meta: "第四条" },
      { category: "checks", from: "courts", to: "president", label: "审查行政指令", meta: "第四条 §9" },
      { category: "checks", from: "courts", to: "house", label: "审查法律", meta: "第四条 §9" },
      { category: "checks", from: "house", to: "courts", label: "弹劾法官", meta: "第二条、第四条" },
      { category: "checks", from: "assembly", to: "courts", label: "定罪后罢免", meta: "第二条、第四条" },
      { category: "accountability", from: "ec", to: "house", label: "认证并管理选举", meta: "第一条、第十二条" },
      { category: "accountability", from: "ec", to: "president", label: "认证选举程序", meta: "第一条、第十二条" },
      { category: "accountability", from: "ec", to: "house", label: "执行竞选资金规则", meta: "第七条、第十二条" },
      { category: "accountability", from: "acc", to: "president", label: "调查并起诉", meta: "第八条、第十二条" },
      { category: "accountability", from: "acc", to: "house", label: "调查议员", meta: "第八条、第十二条" },
      { category: "accountability", from: "acc", to: "courts", label: "调查司法失当", meta: "第四条、第十二条" },
      { category: "accountability", from: "courts", to: "ec", label: "审查委员会行为", meta: "第一条、第四条、第十二条" },
      { category: "accountability", from: "courts", to: "acc", label: "审查宪法行为", meta: "第四条、第十二条" },
    ],
  },
};

function dataForLocale(locale) {
  return RIGHTS_GUIDE[locale] || RIGHTS_GUIDE.en;
}

function emergencyDataForLocale(locale) {
  return EMERGENCY_GUIDE[locale] || EMERGENCY_GUIDE.en;
}

function powerDataForLocale(locale) {
  return POWER_GUIDE[locale] || POWER_GUIDE.en;
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

const CONGRESS_COMPARISON = {
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

function congressDataForLocale(locale) {
  return CONGRESS_COMPARISON[locale] || CONGRESS_COMPARISON.en;
}

const REMOVAL_GUIDE = {
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

function removalDataForLocale(locale) {
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

const ELECTIONS_GUIDE = {
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

function electionsDataForLocale(locale) {
  return ELECTIONS_GUIDE[locale] || ELECTIONS_GUIDE.en;
}

function congressRows(rows) {
  return rows
    .map(
      (row) => `
        <tr>
          <th scope="row">${row.feature}</th>
          <td class="congress-cell congress-cell--current">${row.current}</td>
          <td class="congress-cell congress-cell--draft">${row.draft}</td>
          ${row.note ? `<td class="congress-cell congress-cell--note">${row.note}</td>` : "<td></td>"}
        </tr>
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

  if (doc.slug === "power-distribution") {
    const data = powerDataForLocale(siteData.locale);
    return `
      <section class="visual-guide visual-guide--power" aria-labelledby="visual-guide-title">
        <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
          <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
          <button class="filter-chip" type="button" data-guide-filter="electoral">${data.electoral}</button>
          <button class="filter-chip" type="button" data-guide-filter="checks">${data.checks}</button>
          <button class="filter-chip" type="button" data-guide-filter="accountability">${data.accountability}</button>
        </div>
        <p class="visual-guide__note">${data.note}</p>
        <div class="visual-guide__body">
          <section class="power-map">
            <div class="power-map__grid">
              ${data.nodes
                .map(
                  (node) => `
                    <article class="power-node" data-power-node="${node.key}">
                      <div class="eyebrow">${node.label}</div>
                      <h2 class="rights-category__title">${node.label}</h2>
                      <p class="rights-category__summary">${node.summary}</p>
                    </article>
                  `
                )
                .join("")}
            </div>
          </section>
          <section class="rights-category">
            <header class="rights-category__header">
              <div class="eyebrow">${data.all}</div>
              <h2 class="rights-category__title">${data.all}</h2>
            </header>
            <div class="rights-grid rights-grid--links">
              ${data.links
                .map(
                  (link) => `
                    <article class="rights-card power-link" data-rights-category="${link.category}">
                      <h3>${link.label}</h3>
                      <p>${data.nodes.find((node) => node.key === link.from).label} → ${data.nodes.find((node) => node.key === link.to).label}</p>
                      <div class="rights-card__meta">${link.meta}</div>
                    </article>
                  `
                )
                .join("")}
            </div>
          </section>
        </div>
      </section>
    `;
  }

  if (doc.slug === "removal-pathways") {
    const data = removalDataForLocale(siteData.locale);
    return `
      <section class="visual-guide visual-guide--removal" aria-labelledby="visual-guide-title">
        <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
          <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
          ${data.categories.map((cat) => `<button class="filter-chip" type="button" data-guide-filter="${cat.key}">${cat.label}</button>`).join("")}
        </div>
        <p class="visual-guide__note">${data.note}</p>
        <div class="visual-guide__body">
          ${data.categories.map((cat) => `
            <section class="rights-category congress-section" data-rights-category="${cat.key}">
              <header class="rights-category__header">
                <h2 class="rights-category__title">${cat.label}</h2>
              </header>
              <div class="congress-table-wrapper">
                <table class="congress-table">
                  <thead>
                    <tr>
                      <th scope="col">${data.pathLabel}</th>
                      <th scope="col">${data.triggerLabel}</th>
                      <th scope="col">${data.decidesLabel}</th>
                      <th scope="col" class="congress-cell--draft">${data.thresholdLabel}</th>
                      <th scope="col">${data.outcomeLabel}</th>
                      <th scope="col" class="congress-cell--note">§</th>
                    </tr>
                  </thead>
                  <tbody>${removalRows(cat.paths)}</tbody>
                </table>
              </div>
            </section>
          `).join("")}
        </div>
      </section>
    `;
  }

  if (doc.slug === "how-elections-work") {
    const data = electionsDataForLocale(siteData.locale);
    return `
      <section class="visual-guide visual-guide--elections" aria-labelledby="visual-guide-title">
        <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
          <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
          ${data.categories.map((cat) => `<button class="filter-chip" type="button" data-guide-filter="${cat.key}">${cat.label}</button>`).join("")}
        </div>
        <p class="visual-guide__note">${data.note}</p>
        <div class="visual-guide__body">
          ${data.categories.map((cat) => `
            <section class="rights-category" data-rights-category="${cat.key}">
              <header class="rights-category__header">
                <h2 class="rights-category__title">${cat.label}</h2>
                <p class="rights-category__summary">${cat.summary}</p>
              </header>
              <div class="rights-grid">
                ${cat.items.map((item) => `
                  <article class="rights-card">
                    <h3>${item.title}</h3>
                    <p>${item.text}</p>
                    <div class="rights-card__meta">${item.article}</div>
                  </article>
                `).join("")}
              </div>
            </section>
          `).join("")}
        </div>
      </section>
    `;
  }

  if (doc.slug === "congress-comparison") {
    const data = congressDataForLocale(siteData.locale);
    const currentLabel = siteData.locale === "zh-Hans" ? "现行制度" : siteData.locale === "es" ? "Actual" : "Current";
    const draftLabel = siteData.locale === "zh-Hans" ? "本草案" : siteData.locale === "es" ? "Este borrador" : "This draft";
    const whyLabel = siteData.locale === "zh-Hans" ? "说明" : siteData.locale === "es" ? "Por qué" : "Why";
    const featureLabel = siteData.locale === "zh-Hans" ? "特征" : siteData.locale === "es" ? "Característica" : "Feature";
    return `
      <section class="visual-guide visual-guide--congress" aria-labelledby="visual-guide-title">
        <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
          <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
          ${data.categories
            .map(
              (cat) =>
                `<button class="filter-chip" type="button" data-guide-filter="${cat.key}">${cat.label}</button>`
            )
            .join("")}
        </div>
        <p class="visual-guide__note">${data.note}</p>
        <div class="visual-guide__body">
          ${data.categories
            .map(
              (cat) => `
                <section class="rights-category congress-section" data-rights-category="${cat.key}">
                  <header class="rights-category__header">
                    <h2 class="rights-category__title">${cat.label}</h2>
                  </header>
                  <div class="congress-table-wrapper">
                    <table class="congress-table">
                      <thead>
                        <tr>
                          <th scope="col">${featureLabel}</th>
                          <th scope="col" class="congress-cell--current">${currentLabel}</th>
                          <th scope="col" class="congress-cell--draft">${draftLabel}</th>
                          <th scope="col" class="congress-cell--note">${whyLabel}</th>
                        </tr>
                      </thead>
                      <tbody>${congressRows(cat.rows)}</tbody>
                    </table>
                  </div>
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
  if (!["rights-at-a-glance", "emergency-powers-lifecycle", "power-distribution", "congress-comparison", "removal-pathways", "how-elections-work"].includes(doc.slug) || !container) return;
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
