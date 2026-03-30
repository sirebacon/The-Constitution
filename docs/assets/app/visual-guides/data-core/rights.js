export const RIGHTS_GUIDE = {
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

export function rightsDataForLocale(locale) {
  return RIGHTS_GUIDE[locale] || RIGHTS_GUIDE.en;
}
