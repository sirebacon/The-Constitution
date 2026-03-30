from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
CONTENT_DIR = DOCS_DIR / "content"
ASSETS_DIR = DOCS_DIR / "assets"
TRANSLATIONS_DIR = ROOT / "translation" / "translations"

LOCALE_LABELS = {
    "en": "English",
    "es": "Español",
    "zh-Hans": "中文（简体）",
}

SITE_TITLES = {
    "en": "Constitution of the United States of America",
    "es": "Constitución de los Estados Unidos de América",
    "zh-Hans": "美利坚合众国宪法",
}

NAV_GROUP_LABELS = {
    "en": {
        "start_here": "Start Here",
        "visual_guides": "Visual Guides",
        "constitution": "The Constitution",
        "clause_notes": "Clause Notes",
        "commentary": "Commentary",
        "research": "Research",
        "contributing": "Contributing",
    },
    "es": {
        "start_here": "Empieza aquí",
        "visual_guides": "Guías visuales",
        "constitution": "La Constitución",
        "clause_notes": "Notas de cláusulas",
        "commentary": "Comentario",
        "research": "Investigación",
        "contributing": "Contribuir",
    },
    "zh-Hans": {
        "start_here": "从这里开始",
        "visual_guides": "可视化指南",
        "constitution": "宪法",
        "clause_notes": "条款注释",
        "commentary": "评注",
        "research": "研究",
        "contributing": "贡献指南",
    },
}

OVERVIEW_SUBTITLES = {
    "en": "A modern replacement draft built around democratic legitimacy, anti-authoritarian safeguards, and readable constitutional architecture.",
    "es": "Un borrador moderno de reemplazo construido en torno a la legitimidad democrática, las salvaguardas anti-autoritarias y una arquitectura constitucional legible.",
    "zh-Hans": "一份围绕民主正当性、反威权保障与清晰宪法结构而设计的现代替代性宪法草案。",
}

GROUP_LABELS = {
    "en": {
        "overview": "Overview",
        "guides": "Guides",
        "visual_guides": "Visual Guides",
        "research": "Research",
        "commentary": "Commentary",
        "clause_notes": "Clause Notes",
        "constitution": "Constitution",
    },
    "es": {
        "overview": "Resumen",
        "guides": "Guías",
        "visual_guides": "Guías visuales",
        "research": "Investigación",
        "commentary": "Comentario",
        "clause_notes": "Notas de cláusulas",
        "constitution": "Constitución",
    },
    "zh-Hans": {
        "overview": "概览",
        "guides": "指南",
        "visual_guides": "可视化指南",
        "research": "研究",
        "commentary": "评注",
        "clause_notes": "条款注释",
        "constitution": "宪法",
    },
}

PAGE_METADATA = {
    "index": {
        "en": ("Constitution Index", "Master index and drafting status"),
        "es": ("Índice de la Constitución", "Índice principal y estado de redacción"),
        "zh-Hans": ("宪法索引", "总索引与起草状态"),
    },
    "overview": {
        "en": ("Project Overview", "High-level explanation of the constitutional model"),
        "es": ("Resumen del proyecto", "Explicación general del modelo constitucional"),
        "zh-Hans": ("项目概览", "对本宪法模型的高层说明"),
    },
    "overview-zh": {
        "en": ("Project Overview (中文)", "Chinese-language overview of the constitutional model"),
        "es": ("Resumen del proyecto (中文)", "Resumen en chino del modelo constitucional"),
        "zh-Hans": ("项目概览（中文）", "以中文介绍本宪法模型"),
    },
    "comparison": {
        "en": ("Comparison", "Comparison with the current U.S. Constitution"),
        "es": ("Comparación", "Comparación con la Constitución actual de Estados Unidos"),
        "zh-Hans": ("比较", "与现行美国宪法的比较"),
    },
    "rationale": {
        "en": ("Design Rationale", "Why the major structural choices were made"),
        "es": ("Justificación del diseño", "Por qué se adoptaron las principales decisiones estructurales"),
        "zh-Hans": ("设计理由", "为何做出这些主要结构选择"),
    },
    "scorecard": {
        "en": ("Scorecard", "Current quality assessment and next targets"),
        "es": ("Puntuación", "Evaluación actual de calidad y próximos objetivos"),
        "zh-Hans": ("评分卡", "当前质量评估与下一步目标"),
    },
    "findings": {
        "en": ("Simulation Findings", "What the simulator is currently showing"),
        "es": ("Resultados de simulación", "Lo que actualmente muestra el simulador"),
        "zh-Hans": ("模拟结果", "模拟器当前显示的结果"),
    },
    "finalization-plan": {
        "en": ("Finalization Plan", "Current remaining work and near-finalization sequence"),
        "es": ("Plan de finalización", "Trabajo restante y secuencia para cerrar el borrador"),
        "zh-Hans": ("定稿计划", "当前剩余工作与接近定稿的顺序"),
    },
    "how-testing-works": {
        "en": ("How Testing Works", "How the simulator stress-tests the draft and what its results mean"),
        "es": ("Cómo funciona la validación", "Cómo el simulador somete el borrador a pruebas de esfuerzo y qué significan sus resultados"),
        "zh-Hans": ("测试如何运作", "模拟器如何对草案进行压力测试，以及这些结果意味着什么"),
    },
    "how-to-write-simulation-tests": {
        "en": ("How To Write Simulation Tests", "A contributor guide for creating new scenario tests, handlers, and follow-up report updates"),
        "es": ("Cómo escribir pruebas de simulación", "Guía para contribuir nuevos escenarios, controladores y actualizaciones posteriores"),
        "zh-Hans": ("如何编写模拟测试", "用于创建新情景测试、处理器和后续报告更新的贡献者指南"),
    },
    "rights-at-a-glance": {
        "en": ("Rights At A Glance", "A visual guide to the constitution's major rights categories and protections"),
        "es": ("Derechos de un vistazo", "Guía visual de las principales categorías de derechos y protecciones de la constitución"),
        "zh-Hans": ("权利一览", "对本宪法主要权利类别与保障的可视化导览"),
    },
    "emergency-powers-lifecycle": {
        "en": ("Emergency Powers Lifecycle", "A visual guide to how emergency declarations begin, narrow, lapse, and terminate"),
        "es": ("Ciclo de los poderes de emergencia", "Guía visual de cómo las declaraciones de emergencia comienzan, se limitan, caducan y terminan"),
        "zh-Hans": ("紧急权力生命周期", "对应急状态如何启动、收窄、失效与终止的可视化导览"),
    },
    "power-distribution": {
        "en": ("How Power Is Distributed", "A visual guide to the main institutions, democratic inputs, and accountability links in the constitutional system"),
        "es": ("Cómo se distribuye el poder", "Guía visual de las principales instituciones, entradas democráticas y vínculos de rendición de cuentas del sistema constitucional"),
        "zh-Hans": ("权力如何分配", "对本宪法体系中主要机构、民主输入与问责联系的可视化导览"),
    },
    "congress-comparison": {
        "en": ("Congress: Then vs. Now", "A side-by-side comparison of the current U.S. Congress and the legislature in this draft — what changed, what stayed, and why"),
        "es": ("El Congreso: antes y ahora", "Comparación del Congreso de EE. UU. actual y la legislatura en este borrador — qué cambió, qué se mantuvo y por qué"),
        "zh-Hans": ("国会：今昔对比", "对比当前美国国会与本草案立法机构——有何变化、有何保留及其原因"),
    },
    "removal-pathways": {
        "en": ("How Officials Are Removed", "Every path for removing a federal official — who triggers it, who decides, the vote threshold, and what happens after"),
        "es": ("Cómo se destituye a los funcionarios", "Cada camino para destituir a un funcionario federal: quién lo activa, quién decide, el umbral de votación y qué sucede después"),
        "zh-Hans": ("如何罢免官员", "罢免联邦官员的每条路径——谁触发、谁决定、投票门槛以及后续结果"),
    },
    "how-elections-work": {
        "en": ("How Elections Work", "What is different about federal elections under this constitution — voting methods, registration, integrity protections, and recall"),
        "es": ("Cómo funcionan las elecciones", "Qué tiene de diferente las elecciones federales bajo esta constitución: métodos de votación, registro, protecciones de integridad y revocación"),
        "zh-Hans": ("选举如何运作", "本宪法下联邦选举有何不同——投票方式、选民登记、诚信保护与罢免机制"),
    },
    "amendment-process": {
        "en": ("The Amendment Process", "How this constitution can be changed — Track 1 vs Track 2, the pre-clearance gate, and what eleven provisions cannot be amended under any process"),
        "es": ("El proceso de enmienda", "Cómo puede modificarse esta constitución — Vía 1 vs Vía 2, el control previo y las once disposiciones que no pueden enmendarse bajo ningún proceso"),
        "zh-Hans": ("修宪程序", "本宪法如何修改——路径一与路径二对比、预审批关卡，以及十一项在任何程序下均不可修改的条款"),
    },
    "accountability-commission": {
        "en": ("The Accountability Commission", "What the ACC is, what it can do, what it cannot do, and how it is protected from capture, defunding, or shutdown"),
        "es": ("La Comisión de Rendición de Cuentas", "Qué es la CRC, qué puede hacer, qué no puede hacer y cómo está protegida frente a la captura, la desfinanciación o el cierre"),
        "zh-Hans": ("问责委员会", "问责委员会是什么、能做什么、不能做什么，以及如何防止其被控制、断资或关闭"),
    },
    "presidential-powers-comparison": {
        "en": ("Presidential Powers: Then vs. Now", "A side-by-side comparison of the current U.S. presidency and the presidency in this draft — what remains strong, what narrows, and what new checks apply"),
        "es": ("Poderes presidenciales: antes y ahora", "Comparación de la presidencia actual de EE. UU. y la presidencia en este borrador — qué sigue siendo fuerte, qué se estrecha y qué nuevos controles se aplican"),
        "zh-Hans": ("总统权力：今昔对比", "对比当前美国总统职位与本草案中的总统职位——哪些权力仍然强、哪些被收窄，以及新增了哪些制衡"),
    },
    "how-a-bill-becomes-law": {
        "en": ("How A Bill Becomes Law", "The legislative path from bicameral passage to signature, veto override, or deadlock resolution"),
        "es": ("Cómo un proyecto se convierte en ley", "La ruta legislativa desde la aprobación bicameral hasta la firma, la anulación del veto o la resolución del bloqueo"),
        "zh-Hans": ("法案如何成为法律", "从两院通过到签署、否决推翻或僵局解决的立法路径"),
    },
    "election-to-transfer-of-power": {
        "en": ("From Election To Transfer Of Power", "How the system moves from voting to certification to a lawful transfer of power"),
        "es": ("De la elección a la transferencia del poder", "Cómo el sistema pasa de la votación a la certificación y a una transferencia legal del poder"),
        "zh-Hans": ("从选举到权力交接", "制度如何从投票走向认证，再到合法的权力交接"),
    },
    "how-rights-are-enforced": {
        "en": ("How Rights Are Enforced", "How constitutional rights claims move through courts, expedited review, and emergency backstops"),
        "es": ("Cómo se hacen exigibles los derechos", "Cómo las reclamaciones de derechos constitucionales avanzan por los tribunales, la revisión acelerada y las salvaguardas de emergencia"),
        "zh-Hans": ("权利如何得到执行", "宪法权利主张如何经过法院、加速审查与紧急状态后备机制"),
    },
}

COMMENTARY_OVERVIEW_METADATA = {
    "commentary-overview": {
        "en": ("Using Commentary Notes", "How the website separates constitutional text from explanatory notes"),
        "es": ("Cómo usar las notas de comentario", "Cómo el sitio separa el texto constitucional de las notas explicativas"),
        "zh-Hans": ("如何使用评注", "网站如何将宪法正文与说明性注释分开"),
    },
    "commentary-choices": {
        "en": ("Why Keep Commentary Separate?", "Why the constitutional text stays clean while design notes stay public"),
        "es": ("¿Por qué mantener separado el comentario?", "Por qué el texto constitucional se mantiene limpio mientras las notas de diseño siguen siendo públicas"),
        "zh-Hans": ("为什么要将评注分开？", "为何保持宪法正文简洁，同时公开设计说明"),
    },
    "commentary-peaceful-use": {
        "en": ("Peaceful Civic Use", "How the project defines its peaceful civic purpose and contribution boundaries"),
        "es": ("Uso cívico pacífico", "Cómo el proyecto define su propósito cívico pacífico y los límites de contribución"),
        "zh-Hans": ("和平公民用途", "项目如何界定其和平公民目的与贡献边界"),
    },
}

CLAUSE_METADATA = {
    "clause-unamendable-core": {
        "en": ("Clause Note: The Unamendable Core", "Why some democratic foundations are intentionally placed beyond amendment"),
        "es": ("Nota de cláusula: el núcleo irreformable", "Por qué algunos fundamentos democráticos se sitúan deliberadamente más allá de la reforma"),
        "zh-Hans": ("条款注释：不可修宪核心", "为何有些民主基础被有意置于修宪之外"),
    },
    "clause-naturalized-president": {
        "en": ("Clause Note: Naturalized Citizens And The Presidency", "Why the draft rejects a natural-born-only presidency"),
        "es": ("Nota de cláusula: ciudadanía naturalizada y presidencia", "Por qué el borrador rechaza que la presidencia se limite a ciudadanos nativos"),
        "zh-Hans": ("条款注释：归化公民与总统职位", "为何本草案拒绝仅限出生公民担任总统"),
    },
    "clause-high-impact-directives": {
        "en": ("Clause Note: Fast-Track Review For High-Impact Directives", "Why major presidential directives receive a narrow fast-track path"),
        "es": ("Nota de cláusula: revisión acelerada de directivas de alto impacto", "Por qué las grandes directivas presidenciales reciben una vía rápida y limitada"),
        "zh-Hans": ("条款注释：高影响总统指令的快速审查", "为何重大总统指令适用一条狭窄的快速审查路径"),
    },
    "clause-supreme-court-delay": {
        "en": ("Clause Note: Supreme Court Delay Backstop", "Why expedited constitutional cases cannot be frozen indefinitely by nondecision"),
        "es": ("Nota de cláusula: respaldo frente a la demora de la Corte Suprema", "Por qué los casos constitucionales urgentes no pueden quedar congelados indefinidamente por falta de decisión"),
        "zh-Hans": ("条款注释：最高法院拖延的后备机制", "为何紧急宪法案件不能因不作决定而被无限期冻结"),
    },
    "clause-term-limits": {
        "en": ("Clause Note: Presidential Term Limits", "Why presidential term limits remain part of this safer presidential design"),
        "es": ("Nota de cláusula: límites de mandato presidencial", "Por qué los límites de mandato siguen siendo parte de este diseño presidencial más seguro"),
        "zh-Hans": ("条款注释：总统任期限制", "为何任期限制仍是这一更安全总统制设计的一部分"),
    },
    "clause-constitutional-organs": {
        "en": ("Clause Note: Why Constitutional Organs Exist", "Why some democratic functions are kept outside ordinary partisan control"),
        "es": ("Nota de cláusula: por qué existen los órganos constitucionales", "Por qué algunas funciones democráticas quedan fuera del control partidista ordinario"),
        "zh-Hans": ("条款注释：为何设立宪法机关", "为何某些民主职能被置于日常党派控制之外"),
    },
    "clause-healthcare-floor": {
        "en": ("Clause Note: The Healthcare Floor", "Why the Constitution protects access to basic and emergency healthcare without fixing one program model"),
        "es": ("Nota de cláusula: el piso de atención médica", "Por qué la Constitución protege el acceso a la atención básica y de emergencia sin fijar un único modelo"),
        "zh-Hans": ("条款注释：医疗保障底线", "为何宪法保障基本与紧急医疗服务的可及性，但不固定为单一制度模式"),
    },
    "clause-war-powers-backstop": {
        "en": ("Clause Note: War Powers Backstops", "Why unauthorized force triggers concrete constitutional consequences instead of open-ended drift"),
        "es": ("Nota de cláusula: salvaguardas de poderes de guerra", "Por qué el uso no autorizado de la fuerza genera consecuencias constitucionales concretas"),
        "zh-Hans": ("条款注释：战争权力后备机制", "为何未经授权的武力使用会触发具体的宪法后果，而不是无限漂移"),
    },
    "clause-political-speech-floor": {
        "en": ("Clause Note: Political Speech And Democratic Dissent", "Why political expression receives especially strong protection in a democracy-defending constitution"),
        "es": ("Nota de cláusula: expresión política y disenso democrático", "Por qué la expresión política recibe una protección especialmente fuerte en una constitución que defiende la democracia"),
        "zh-Hans": ("条款注释：政治表达与民主异议", "为何政治表达在一部保卫民主的宪法中获得特别强的保护"),
    },
    "clause-peaceful-transfer": {
        "en": ("Clause Note: Peaceful Transfer Of Power", "Why lawful transfer of power is protected as a constitutional core commitment rather than a political norm"),
        "es": ("Nota de cláusula: transferencia pacífica del poder", "Por qué la transferencia legal del poder se protege como compromiso constitucional central"),
        "zh-Hans": ("条款注释：和平移交权力", "为何合法的权力移交被保护为核心宪法承诺，而不只是政治惯例"),
    },
    "clause-campaign-finance-equality": {
        "en": ("Clause Note: Campaign Finance And Political Equality", "Why constitutional democracy permits strong limits on political money without freezing one permanent regulatory model"),
        "es": ("Nota de cláusula: financiación de campañas e igualdad política", "Por qué la democracia constitucional permite límites fuertes al dinero político sin congelarlo en un único modelo regulatorio permanente"),
        "zh-Hans": ("条款注释：竞选资金与政治平等", "为何宪政民主可以对政治金钱设定强限制，而不冻结为单一永久监管模式"),
    },
    "clause-federalism-floor": {
        "en": ("Clause Note: Federalism And The Democratic Floor", "Why state autonomy is preserved within a democratic floor rather than treated as absolute"),
        "es": ("Nota de cláusula: federalismo y piso democrático", "Por qué la autonomía estatal se preserva dentro de un piso democrático y no como algo absoluto"),
        "zh-Hans": ("条款注释：联邦制与民主底线", "为何州自治是在民主底线内被保留，而不是被视为绝对"),
    },
    "clause-citizenship-revocation": {
        "en": ("Clause Note: Citizenship Revocation And Due Process", "Why loss of citizenship requires an explicit constitutional process floor before it can take effect"),
        "es": ("Nota de cláusula: revocación de ciudadanía y debido proceso", "Por qué la pérdida de ciudadanía requiere un piso procesal constitucional explícito antes de surtir efecto"),
        "zh-Hans": ("条款注释：撤销国籍与正当程序", "为何丧失国籍在生效前必须满足明确的宪法程序底线"),
    },
    "clause-anti-corruption": {
        "en": ("Clause Note: Anti-Corruption And Anti-Capture", "Why corruption and institutional capture are treated as constitutional threats rather than ordinary policy failures"),
        "es": ("Nota de cláusula: anticorrupción y anticaptura", "Por qué la corrupción y la captura institucional se tratan como amenazas constitucionales y no como fallas políticas ordinarias"),
        "zh-Hans": ("条款注释：反腐败与反俘获", "为何腐败和制度俘获被视为宪法威胁，而不只是普通政策失败"),
    },
}


PAGE_SOURCES = [
    ("index", "Constitution Index", ROOT / "CONSTITUTION.md", "Overview", "Master index and drafting status"),
    ("overview", "Project Overview", ROOT / "design-notes" / "constitutional-overview.md", "Overview", "High-level explanation of the constitutional model"),
    ("overview-zh", "Project Overview (中文)", ROOT / "design-notes" / "constitutional-overview.zh.md", "Overview", "Chinese-language overview of the constitutional model"),
    ("comparison", "Comparison", ROOT / "design-notes" / "comparison.md", "Overview", "Comparison with the current U.S. Constitution"),
    ("rationale", "Design Rationale", ROOT / "design-notes" / "rationale.md", "Overview", "Why the major structural choices were made"),
    ("scorecard", "Scorecard", ROOT / "design-notes" / "scorecard.md", "Overview", "Current quality assessment and next targets"),
    ("how-testing-works", "How Testing Works", ROOT / "design-notes" / "how-testing-works.md", "Overview", "How the simulator stress-tests the draft and what its results mean"),
    ("how-to-write-simulation-tests", "How To Write Simulation Tests", ROOT / "design-notes" / "how-to-write-simulation-tests.md", "Overview", "A contributor guide for creating new scenario tests, handlers, and follow-up report updates"),
    ("findings", "Simulation Findings", ROOT / "design-notes" / "simulation-findings.md", "Research", "What the simulator is currently showing"),
    ("finalization-plan", "Finalization Plan", ROOT / "design-notes" / "finalization-plan.md", "Research", "Current remaining work and near-finalization sequence"),
]

VISUAL_GUIDE_SOURCES = [
    (
        "rights-at-a-glance",
        "Rights At A Glance",
        ROOT / "visual-guides" / "rights-at-a-glance.md",
        "Visual Guides",
        "A visual guide to the constitution's major rights categories and protections",
    ),
    (
        "emergency-powers-lifecycle",
        "Emergency Powers Lifecycle",
        ROOT / "visual-guides" / "emergency-powers-lifecycle.md",
        "Visual Guides",
        "A visual guide to how emergency declarations begin, narrow, lapse, and terminate",
    ),
    (
        "power-distribution",
        "How Power Is Distributed",
        ROOT / "visual-guides" / "power-distribution.md",
        "Visual Guides",
        "A visual guide to the main institutions, democratic inputs, and accountability links in the constitutional system",
    ),
    (
        "congress-comparison",
        "Congress: Then vs. Now",
        ROOT / "visual-guides" / "congress-comparison.md",
        "Visual Guides",
        "A side-by-side comparison of the current U.S. Congress and the legislature in this draft",
    ),
    (
        "removal-pathways",
        "How Officials Are Removed",
        ROOT / "visual-guides" / "removal-pathways.md",
        "Visual Guides",
        "Every path for removing a federal official — who triggers it, who decides, the vote threshold, and what happens after",
    ),
    (
        "how-elections-work",
        "How Elections Work",
        ROOT / "visual-guides" / "how-elections-work.md",
        "Visual Guides",
        "What is different about federal elections under this constitution — voting methods, registration, integrity protections, and recall",
    ),
    (
        "amendment-process",
        "The Amendment Process",
        ROOT / "visual-guides" / "amendment-process.md",
        "Visual Guides",
        "How this constitution can be changed — Track 1 vs Track 2, pre-clearance, and what cannot be amended under any process",
    ),
    (
        "accountability-commission",
        "The Accountability Commission",
        ROOT / "visual-guides" / "accountability-commission.md",
        "Visual Guides",
        "What the ACC is, what it can do, what it cannot do, and how it is protected from capture, defunding, or shutdown",
    ),
    (
        "presidential-powers-comparison",
        "Presidential Powers: Then vs. Now",
        ROOT / "visual-guides" / "presidential-powers-comparison.md",
        "Visual Guides",
        "A side-by-side comparison of the current U.S. presidency and the presidency in this draft",
    ),
    (
        "how-a-bill-becomes-law",
        "How A Bill Becomes Law",
        ROOT / "visual-guides" / "how-a-bill-becomes-law.md",
        "Visual Guides",
        "The legislative path from bicameral passage to signature, veto override, or deadlock resolution",
    ),
    (
        "election-to-transfer-of-power",
        "From Election To Transfer Of Power",
        ROOT / "visual-guides" / "election-to-transfer-of-power.md",
        "Visual Guides",
        "How the system moves from voting to certification to a lawful transfer of power",
    ),
    (
        "how-rights-are-enforced",
        "How Rights Are Enforced",
        ROOT / "visual-guides" / "how-rights-are-enforced.md",
        "Visual Guides",
        "How rights claims move through courts, accelerated review, and emergency backstops",
    ),
]

GUIDE_SLUGS = {"how-testing-works", "how-to-write-simulation-tests"}
OVERVIEW_SLUGS = {"index", "overview", "overview-zh", "comparison", "scorecard"}
RESEARCH_SLUGS = {"rationale", "findings", "finalization-plan"}
POLICY_SLUGS = {"commentary-peaceful-use"}
HOMEPAGE_FEATURED = {
    "project_use": "commentary-peaceful-use",
    "testing": "how-testing-works",
}

COMMENTARY_OVERVIEW_SOURCES = [
    ("commentary-overview", "Using Commentary Notes", ROOT / "commentary" / "overview" / "using-commentary-notes.md", "Commentary", "How the website separates constitutional text from explanatory notes"),
    ("commentary-choices", "Why Keep Commentary Separate?", ROOT / "commentary" / "overview" / "why-commentary-is-separate.md", "Commentary", "Why the constitutional text stays clean while design notes stay public"),
    ("commentary-peaceful-use", "Peaceful Civic Use", ROOT / "commentary" / "overview" / "peaceful-civic-use.md", "Commentary", "How the project defines its peaceful civic purpose and contribution boundaries"),
]

CLAUSE_COMMENTARY_SOURCES = [
    (
        "clause-unamendable-core",
        "Clause Note: The Unamendable Core",
        ROOT / "commentary" / "clauses" / "unamendable-core.md",
        "Clause Notes",
        "Why some democratic foundations are intentionally placed beyond amendment",
        ["xi-amendments"],
    ),
    (
        "clause-naturalized-president",
        "Clause Note: Naturalized Citizens And The Presidency",
        ROOT / "commentary" / "clauses" / "naturalized-president.md",
        "Clause Notes",
        "Why the draft rejects a natural-born-only presidency",
        ["iii-executive", "ix-citizenship-membership"],
    ),
    (
        "clause-high-impact-directives",
        "Clause Note: Fast-Track Review For High-Impact Directives",
        ROOT / "commentary" / "clauses" / "high-impact-directives.md",
        "Clause Notes",
        "Why major presidential directives receive a narrow fast-track path",
        ["iii-executive", "iv-judiciary"],
    ),
    (
        "clause-supreme-court-delay",
        "Clause Note: Supreme Court Delay Backstop",
        ROOT / "commentary" / "clauses" / "supreme-court-delay-backstop.md",
        "Clause Notes",
        "Why expedited constitutional cases cannot be frozen indefinitely by nondecision",
        ["iv-judiciary"],
    ),
    (
        "clause-term-limits",
        "Clause Note: Presidential Term Limits",
        ROOT / "commentary" / "clauses" / "presidential-term-limits.md",
        "Clause Notes",
        "Why presidential term limits remain part of this safer presidential design",
        ["iii-executive"],
    ),
    (
        "clause-constitutional-organs",
        "Clause Note: Why Constitutional Organs Exist",
        ROOT / "commentary" / "clauses" / "constitutional-organs.md",
        "Clause Notes",
        "Why some democratic functions are kept outside ordinary partisan control",
        ["xii-constitutional-organs", "xix-ratification-transition"],
    ),
    (
        "clause-healthcare-floor",
        "Clause Note: The Healthcare Floor",
        ROOT / "commentary" / "clauses" / "healthcare-floor.md",
        "Clause Notes",
        "Why the Constitution protects access to basic and emergency healthcare without fixing one program model",
        ["xviii-social-economic-rights"],
    ),
    (
        "clause-war-powers-backstop",
        "Clause Note: War Powers Backstops",
        ROOT / "commentary" / "clauses" / "war-powers-backstop.md",
        "Clause Notes",
        "Why unauthorized force triggers concrete constitutional consequences instead of open-ended drift",
        ["xvi-war-powers-national-security"],
    ),
    (
        "clause-political-speech-floor",
        "Clause Note: Political Speech And Democratic Dissent",
        ROOT / "commentary" / "clauses" / "political-speech-floor.md",
        "Clause Notes",
        "Why political expression receives especially strong protection in a democracy-defending constitution",
        ["v-rights", "vi-integrity"],
    ),
    (
        "clause-peaceful-transfer",
        "Clause Note: Peaceful Transfer Of Power",
        ROOT / "commentary" / "clauses" / "peaceful-transfer.md",
        "Clause Notes",
        "Why lawful transfer of power is protected as a constitutional core commitment rather than a political norm",
        ["vi-integrity", "xix-ratification-transition"],
    ),
    (
        "clause-campaign-finance-equality",
        "Clause Note: Campaign Finance And Political Equality",
        ROOT / "commentary" / "clauses" / "campaign-finance-equality.md",
        "Clause Notes",
        "Why constitutional democracy permits strong limits on political money without freezing one permanent regulatory model",
        ["vii-campaign-finance"],
    ),
    (
        "clause-federalism-floor",
        "Clause Note: Federalism And The Democratic Floor",
        ROOT / "commentary" / "clauses" / "federalism-floor.md",
        "Clause Notes",
        "Why state autonomy is preserved within a democratic floor rather than treated as absolute",
        ["x-federalism"],
    ),
    (
        "clause-citizenship-revocation",
        "Clause Note: Citizenship Revocation And Due Process",
        ROOT / "commentary" / "clauses" / "citizenship-revocation.md",
        "Clause Notes",
        "Why loss of citizenship requires an explicit constitutional process floor before it can take effect",
        ["ix-citizenship-membership"],
    ),
    (
        "clause-anti-corruption",
        "Clause Note: Anti-Corruption And Anti-Capture",
        ROOT / "commentary" / "clauses" / "anti-corruption.md",
        "Clause Notes",
        "Why corruption and institutional capture are treated as constitutional threats rather than ordinary policy failures",
        ["viii-government-ethics", "xiii-federal-agencies", "vi-integrity"],
    ),
]

SCORECARD_KEYS = {
    "preamble": "Preamble",
    "I-electoral-system.md": "Article I — Electoral System",
    "II-legislature.md": "Article II — Legislature",
    "III-executive.md": "Article III — Executive",
    "IV-judiciary.md": "Article IV — Judiciary",
    "V-rights.md": "Article V — Civil and Political Rights",
    "VI-integrity.md": "Article VI — Democratic Integrity",
    "VII-campaign-finance.md": "Article VII — Campaign Finance and Political Money",
    "VIII-government-ethics.md": "Article VIII — Government Ethics",
    "IX-citizenship-membership.md": "Article IX — Citizenship and National Membership",
    "X-federalism.md": "Article X — Federalism and the States",
    "XI-amendments.md": "Article XI — Amendments",
    "XII-constitutional-organs.md": "Article XII — Constitutional Organs",
    "XIII-federal-agencies.md": "Article XIII — Federal Agencies",
    "XIV-taxation-public-revenue.md": "Article XIV — Taxation and Public Revenue",
    "XV-budget-public-credit-appropriations.md": "Article XV — Budget, Public Credit, and Appropriations",
    "XVI-war-powers-national-security.md": "Article XVI — War Powers and National Security",
    "XVII-foreign-policy-national-security.md": "Article XVII — Foreign Policy and National Security",
    "XVIII-social-economic-rights.md": "Article XVIII — Social, Economic, and Affirmative Rights",
    "XIX-ratification-transition.md": "Article XIX — Ratification and Transition",
}


ARTICLE_ORDER = [
    "I-electoral-system.md",
    "II-legislature.md",
    "III-executive.md",
    "IV-judiciary.md",
    "V-rights.md",
    "VI-integrity.md",
    "VII-campaign-finance.md",
    "VIII-government-ethics.md",
    "IX-citizenship-membership.md",
    "X-federalism.md",
    "XI-amendments.md",
    "XII-constitutional-organs.md",
    "XIII-federal-agencies.md",
    "XIV-taxation-public-revenue.md",
    "XV-budget-public-credit-appropriations.md",
    "XVI-war-powers-national-security.md",
    "XVII-foreign-policy-national-security.md",
    "XVIII-social-economic-rights.md",
    "XIX-ratification-transition.md",
]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def homepage_section_items() -> dict[str, list[str]]:
    return {
        "start_here": ["overview", "comparison"],
        "visual_guides": ["rights-at-a-glance", "emergency-powers-lifecycle", "power-distribution", "congress-comparison", "removal-pathways", "how-elections-work", "amendment-process", "accountability-commission", "presidential-powers-comparison", "how-a-bill-becomes-law", "election-to-transfer-of-power", "how-rights-are-enforced"],
        "constitution": ["index", "preamble"] + [slugify(filename.replace(".md", "")) for filename in ARTICLE_ORDER],
        "clause_notes": [
            "clause-unamendable-core",
            "clause-naturalized-president",
            "clause-high-impact-directives",
            "clause-supreme-court-delay",
            "clause-term-limits",
            "clause-constitutional-organs",
            "clause-healthcare-floor",
            "clause-war-powers-backstop",
            "clause-political-speech-floor",
            "clause-peaceful-transfer",
            "clause-campaign-finance-equality",
            "clause-federalism-floor",
            "clause-citizenship-revocation",
            "clause-anti-corruption",
        ],
        "commentary": ["commentary-overview", "commentary-choices", "commentary-peaceful-use"],
        "research": ["scorecard", "rationale", "findings", "finalization-plan"],
        "contributing": ["how-testing-works", "how-to-write-simulation-tests"],
    }


def extract_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def extract_status(markdown: str) -> str | None:
    match = re.search(r"\*\*Status:\*\*\s*`?\[\s*([A-Z]+)\s*\]`?", markdown)
    return match.group(1) if match else None


def extract_summary(markdown: str) -> str:
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if line.strip() == "## Scope":
            collected: list[str] = []
            for follow in lines[index + 1 :]:
                if follow.startswith("## "):
                    break
                if not follow.strip() or follow.strip() == "---":
                    if collected:
                        break
                    continue
                collected.append(follow.strip())
            if collected:
                return " ".join(collected)
    paragraphs = [
        line.strip()
        for line in lines
        if line.strip()
        and not line.startswith("#")
        and line.strip() != "---"
        and not line.startswith("**Status:**")
        and not line.startswith(">")
    ]
    return paragraphs[0] if paragraphs else ""


def extract_headings(markdown: str) -> list[dict[str, str | int]]:
    headings: list[dict[str, str | int]] = []
    for line in markdown.splitlines():
        if line.startswith("## "):
            text = line[3:].strip()
            headings.append({"level": 2, "text": text, "anchor": slugify(text)})
        elif line.startswith("### "):
            text = line[4:].strip()
            headings.append({"level": 3, "text": text, "anchor": slugify(text)})
    return headings


def plain_text(markdown: str) -> str:
    text = markdown
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_>#-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def copy_source(source: Path) -> str:
    relative = source.relative_to(ROOT)
    target = CONTENT_DIR / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    return relative.as_posix()


def available_locales() -> list[str]:
    locales = ["en"]
    if TRANSLATIONS_DIR.exists():
        locales.extend(
            sorted(
                path.name
                for path in TRANSLATIONS_DIR.iterdir()
                if path.is_dir() and any((path / "articles").glob("*.md"))
            )
        )
    seen: list[str] = []
    for locale in locales:
        if locale not in seen:
            seen.append(locale)
    return seen


def locale_meta(locales: list[str]) -> list[dict[str, str]]:
    return [{"code": locale, "label": LOCALE_LABELS.get(locale, locale)} for locale in locales]


def nav_labels(locale: str) -> dict[str, str]:
    return NAV_GROUP_LABELS.get(locale, NAV_GROUP_LABELS["en"])


def group_label(group_key: str, locale: str) -> str:
    return GROUP_LABELS.get(locale, GROUP_LABELS["en"]).get(group_key, group_key)


def localized_pair(
    metadata: dict[str, dict[str, tuple[str, str]]], slug: str, locale: str, fallback_title: str, fallback_summary: str
) -> tuple[str, str]:
    values = metadata.get(slug, {})
    return values.get(locale) or values.get("en") or (fallback_title, fallback_summary)


def localized_article_source(filename: str, locale: str) -> Path:
    return localized_source(ROOT / "articles" / filename, locale)


def localized_source(source: Path, locale: str) -> Path:
    if locale == "en":
        return source
    relative = source.relative_to(ROOT)
    translated = TRANSLATIONS_DIR / locale / relative
    if translated.exists():
        return translated
    if relative == Path("design-notes/constitutional-overview.md") and locale == "zh-Hans":
        legacy_zh = ROOT / "design-notes" / "constitutional-overview.zh.md"
        if legacy_zh.exists():
            return legacy_zh
    return source


def parse_scorecard_rows(markdown: str) -> dict[str, dict[str, str]]:
    lines = markdown.splitlines()
    in_summary = False
    rows: dict[str, dict[str, str]] = {}
    for line in lines:
        if line.strip() == "### Summary Baseline":
            in_summary = True
            continue
        if in_summary and line.startswith("### "):
            break
        if not in_summary or not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().split("|")[1:-1]]
        if len(parts) != 6 or parts[0] == "Area" or parts[0].startswith("------"):
            continue
        rows[parts[0]] = {
            "score": parts[1],
            "status": parts[2],
            "strength": parts[3],
            "weakness": parts[4],
            "next": parts[5],
        }
    return rows


def build_manifest(locale: str, locales: list[str]) -> dict[str, object]:
    scorecard_md = (ROOT / "design-notes" / "scorecard.md").read_text()
    scorecard = parse_scorecard_rows(scorecard_md)
    aggregate = json.loads((ROOT / "simulation" / "reports" / "aggregate.json").read_text())

    docs: list[dict[str, object]] = []

    preamble_path = ROOT / "preamble.md"
    localized_preamble_path = localized_source(preamble_path, locale)
    preamble_md = localized_preamble_path.read_text()
    preamble_rel = copy_source(localized_preamble_path)
    preamble_score = scorecard.get(SCORECARD_KEYS["preamble"], {})
    docs.append(
        {
            "slug": "preamble",
            "title": {"en": "Preamble", "es": "Preámbulo", "zh-Hans": "序言"}.get(locale, "Preamble"),
            "group": group_label("constitution", locale),
            "kind": "preamble",
            "content_type": "constitution_text",
            "source": preamble_rel,
            "status": extract_status(preamble_md),
            "summary": extract_summary(preamble_md),
            "headings": extract_headings(preamble_md),
            "search_text": plain_text(preamble_md),
            "score": preamble_score.get("score"),
            "score_status": preamble_score.get("status"),
        }
    )

    for filename in ARTICLE_ORDER:
        source = localized_article_source(filename, locale)
        markdown = source.read_text()
        relative = copy_source(source)
        title = extract_title(markdown, filename)
        score = scorecard.get(SCORECARD_KEYS[filename], {})
        docs.append(
            {
                "slug": slugify(filename.replace(".md", "")),
                "title": title,
                "group": group_label("constitution", locale),
                "kind": "article",
                "content_type": "constitution_text",
                "source": relative,
                "status": extract_status(markdown),
                "summary": extract_summary(markdown),
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
                "score": score.get("score"),
                "score_status": score.get("status"),
                "source_locale": locale if source != ROOT / "articles" / filename else "en",
            }
        )

    for slug, title, source, group, fallback_summary in PAGE_SOURCES:
        if slug == "overview-zh" and locale == "zh-Hans":
            continue
        source = localized_source(source, locale)
        markdown = source.read_text()
        relative = copy_source(source)
        score = scorecard.get(title, {})
        localized_title, localized_summary = localized_pair(PAGE_METADATA, slug, locale, title, fallback_summary)
        docs.append(
            {
                "slug": slug,
                "title": localized_title,
                "group": group_label("overview" if group == "Overview" else "research", locale),
                "kind": "note",
                "content_type": (
                    "guide"
                    if slug in GUIDE_SLUGS
                    else "research"
                    if slug in RESEARCH_SLUGS
                    else "overview"
                ),
                "source": relative,
                "status": extract_status(markdown),
                "summary": localized_summary if locale != "en" else extract_summary(markdown) or fallback_summary,
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
                "score": score.get("score"),
                "score_status": score.get("status"),
            }
        )

    for slug, title, source, group, fallback_summary in VISUAL_GUIDE_SOURCES:
        source = localized_source(source, locale)
        markdown = source.read_text()
        relative = copy_source(source)
        localized_title, localized_summary = localized_pair(PAGE_METADATA, slug, locale, title, fallback_summary)
        docs.append(
            {
                "slug": slug,
                "title": localized_title,
                "group": group_label("visual_guides", locale),
                "kind": "note",
                "content_type": "visual_guide",
                "source": relative,
                "status": extract_status(markdown),
                "summary": localized_summary if locale != "en" else extract_summary(markdown) or fallback_summary,
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
            }
        )

    for slug, title, source, group, fallback_summary in COMMENTARY_OVERVIEW_SOURCES:
        source = localized_source(source, locale)
        markdown = source.read_text()
        relative = copy_source(source)
        localized_title, localized_summary = localized_pair(
            COMMENTARY_OVERVIEW_METADATA, slug, locale, title, fallback_summary
        )
        docs.append(
            {
                "slug": slug,
                "title": localized_title,
                "group": group_label("commentary", locale),
                "kind": "commentary",
                "content_type": "policy" if slug in POLICY_SLUGS else "commentary_overview",
                "source": relative,
                "status": extract_status(markdown),
                "summary": localized_summary if locale != "en" else extract_summary(markdown) or fallback_summary,
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
            }
        )

    for slug, title, source, group, fallback_summary, related_slugs in CLAUSE_COMMENTARY_SOURCES:
        source = localized_source(source, locale)
        markdown = source.read_text()
        relative = copy_source(source)
        localized_title, localized_summary = localized_pair(CLAUSE_METADATA, slug, locale, title, fallback_summary)
        docs.append(
            {
                "slug": slug,
                "title": localized_title,
                "group": group_label("clause_notes", locale),
                "kind": "commentary",
                "content_type": "commentary_clause",
                "source": relative,
                "status": extract_status(markdown),
                "summary": localized_summary if locale != "en" else extract_summary(markdown) or fallback_summary,
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
                "related_slugs": related_slugs,
            }
        )

    for filename in ARTICLE_ORDER:
        source = localized_source(ROOT / "commentary" / "articles" / filename, locale)
        if not source.exists():
            continue
        markdown = source.read_text()
        relative = copy_source(source)
        article_slug = slugify(filename.replace(".md", ""))
        commentary_slug = f"notes-{article_slug}"
        localized_article_markdown = localized_article_source(filename, locale).read_text()
        article_title = extract_title(localized_article_markdown, filename)
        notes_suffix = {"en": "Notes", "es": "Notas", "zh-Hans": "注释"}.get(locale, "Notes")
        summary_fallback = {
            "en": f"Explanatory notes for {article_title}",
            "es": f"Notas explicativas para {article_title}",
            "zh-Hans": f"{article_title}的说明性注释",
        }.get(locale, f"Explanatory notes for {article_title}")
        docs.append(
            {
                "slug": commentary_slug,
                "title": f"{article_title} {notes_suffix}",
                "group": group_label("commentary", locale),
                "kind": "commentary",
                "content_type": "commentary_article",
                "source": relative,
                "status": extract_status(markdown),
                "summary": summary_fallback if locale != "en" else extract_summary(markdown) or summary_fallback,
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
                "companion_slug": article_slug,
                "companion_kind": "article",
            }
        )

    commentary_by_article = {
        doc["companion_slug"]: doc["slug"]
        for doc in docs
        if doc.get("kind") == "commentary" and doc.get("companion_slug")
    }
    for doc in docs:
        if doc["kind"] in {"article", "preamble"} and doc["slug"] in commentary_by_article:
            doc["companion_slug"] = commentary_by_article[doc["slug"]]
            doc["companion_kind"] = "commentary"

    overview = {
        "title": SITE_TITLES.get(locale, SITE_TITLES["en"]),
        "subtitle": OVERVIEW_SUBTITLES.get(locale, OVERVIEW_SUBTITLES["en"]),
        "article_count": len(ARTICLE_ORDER),
        "scenario_count": aggregate["scenario_count"],
        "overall_score": scorecard.get("Overall Draft", {}).get("score"),
        "overall_status": scorecard.get("Overall Draft", {}).get("status"),
        "unresolved_obligations": aggregate["totals"]["unresolved_obligations"],
        "top_strength": scorecard.get("Overall Draft", {}).get("strength"),
        "top_weakness": scorecard.get("Overall Draft", {}).get("weakness"),
    }

    labels = nav_labels(locale)
    section_items = homepage_section_items()
    homepage_sections = [
        {"key": key, "title": labels[key], "items": items}
        for key, items in section_items.items()
    ]

    navigation = [
        {"group": labels["start_here"], "items": section_items["start_here"]},
        {"group": labels["visual_guides"], "items": section_items["visual_guides"]},
        {"group": labels["constitution"], "items": section_items["constitution"]},
        {"group": labels["clause_notes"], "items": section_items["clause_notes"]},
        {"group": labels["commentary"], "items": section_items["commentary"]},
        {"group": labels["research"], "items": section_items["research"]},
        {"group": labels["contributing"], "items": section_items["contributing"]},
    ]

    return {
        "generated_at": aggregate.get("generated_at", ""),
        "locale": locale,
        "locales": locale_meta(locales),
        "overview": overview,
        "homepage": {
            "sections": homepage_sections,
            "featured": HOMEPAGE_FEATURED,
        },
        "navigation": navigation,
        "docs": docs,
    }


def write_manifest(manifest: dict[str, object], locale: str) -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    filename = "site-data.json" if locale == "en" else f"site-data.{locale}.json"
    (ASSETS_DIR / filename).write_text(json.dumps(manifest, indent=2))


def main() -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    if CONTENT_DIR.exists():
        for child in CONTENT_DIR.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    locales = available_locales()
    for locale in locales:
        manifest = build_manifest(locale, locales)
        write_manifest(manifest, locale)


if __name__ == "__main__":
    main()
