from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_warrantless_surveillance_conducted(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article V Section 5.3", "Article XVII Section 4.7", "Article XV Section 6.5"})
    state.add_violation(
        "warrantless_domestic_surveillance",
        "rights_suppression",
        "Intelligence agency",
        "Intelligence agency conducts warrantless surveillance targeting a domestic political organization, in violation of Article V Section 5.3, Article XVII Section 4.7, and the prohibition on using classified appropriations for domestic political surveillance under Article XV Section 6.5.",
        "Article V Section 5.3, Article XVII Section 4.7, and Article XV Section 6.5",
        day,
    )
    state.add_obligation(
        "court_halt_surveillance",
        "Federal courts",
        "order an immediate halt to the warrantless domestic surveillance operation",
        "Article V Section 5.3 and Article XVII Section 4.7",
        day,
        day + 5,
        severity="high",
    )


def handle_court_orders_surveillance_halt(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_halt_surveillance",
        day,
        "ordered an immediate halt to the warrantless domestic surveillance and referred the matter to the Accountability Commission",
    )
    state.add_obligation(
        "agency_comply_surveillance_halt",
        "Intelligence agency",
        "cease the warrantless domestic surveillance operation in compliance with the court order",
        "Article V Section 5.3 and Article XVII Section 4.7",
        day,
        day + 2,
        severity="high",
    )


def handle_agency_complies_with_surveillance_halt(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "agency_comply_surveillance_halt",
        day,
        "ceased the warrantless domestic surveillance operation in compliance with the court order",
    )


def handle_emergency_used_to_restrict_protected_speech(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 5.3", "Article V"})
    message = "Executive branch uses an emergency declaration to restrict protected expression, in violation of the absolute bar on overriding Article V rights through emergency powers."
    state.add_violation(
        "emergency_rights_suppression",
        "rights_suppression",
        "Executive branch",
        message,
        "Article III Section 5.3(f) and Article V",
        day,
    )
    state.add_obligation(
        "court_void_emergency_rights_restriction",
        "Federal courts",
        "void the emergency-based restriction on protected expression",
        "Article III Section 5.3(f) and Article V",
        day,
        day + 2,
        severity="high",
    )


def handle_court_voids_emergency_rights_restriction(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_void_emergency_rights_restriction",
        day,
        "voided the emergency-based restriction on protected expression",
    )


def handle_president_suspends_habeas_corpus_by_executive_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 5.7", "Article V Section 1"})
    state.add_violation(
        "executive_habeas_suspension",
        "rights_suppression",
        "President",
        "President suspends the privilege of the writ of habeas corpus by executive order. This power belongs exclusively to Congress under Article III Section 5.7 and may not be exercised by the President alone.",
        "Article III Section 5.7",
        day,
    )
    state.add_obligation(
        "court_void_habeas_suspension",
        "Federal courts",
        "void the executive habeas suspension immediately",
        "Article III Section 5.7 and Article V Section 1",
        day,
        day + 2,
        severity="high",
    )


def handle_court_voids_habeas_suspension(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_void_habeas_suspension",
        day,
        "voided the executive habeas suspension and restored access to the writ",
    )


def handle_budget_deadline_missed(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article XV Section 3.2", "Article XV Section 3.3", "Article XV Section 3.4"})
    state.add_entry(
        day,
        "event",
        "Congress has not enacted appropriations legislation by October 1. The automatic continuing resolution takes effect at 98% of prior-year enacted levels.",
        "Article XV Section 3.2",
    )
    state.add_entry(
        day,
        "outcome",
        "The government may not shut down for lack of appropriations. The automatic continuing resolution is self-executing and requires no further legislative or executive action to take effect.",
        "Article XV Section 3.2 and Section 3.3",
    )


def handle_executive_attempts_selective_cr_funding(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_violation(
        "executive_selective_cr_funding",
        "executive_defiance",
        "Executive branch",
        "Executive branch attempts to alter funding ratios, withhold appropriated funds, or selectively apply funding levels under the automatic continuing resolution.",
        "Article XV Section 3.4",
        day,
    )
    state.add_obligation(
        "court_review_cr_manipulation",
        "Federal courts",
        "review the executive branch's selective CR funding manipulation on an expedited basis",
        "Article XV Section 3.4",
        day,
        day + 5,
        severity="high",
    )


def handle_court_blocks_cr_manipulation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_review_cr_manipulation",
        day,
        "issued an expedited order blocking the executive branch's selective application of the automatic continuing resolution",
    )


def handle_government_targets_political_speech(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.provisions.update({"Article V Section 2.1", "Article V Section 2.6"})
    state.add_violation(
        "political_speech_restriction",
        "rights_suppression",
        "Executive branch",
        "Government issues an order restricting or penalizing political expression based on its political content or viewpoint, in violation of the highest-protection category of Article V Section 2.6.",
        "Article V Section 2.1 and Section 2.6",
        day,
    )
    state.add_obligation(
        "court_void_speech_restriction",
        "Federal courts",
        "void the unconstitutional restriction on political speech",
        "Article V Section 2.1 and Section 2.6",
        day,
        day + 3,
        severity="high",
    )


def handle_court_voids_political_speech_restriction(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_void_speech_restriction",
        day,
        "voided the restriction on political speech on expedited review",
    )
    state.add_entry(
        day,
        "outcome",
        "Political speech receives the highest level of constitutional protection under Article V Section 2.6. Laws targeting speech based on political content or viewpoint are void.",
        "Article V Section 2.1 and Section 2.6",
    )


def handle_state_enacts_discriminatory_classification(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    characteristic = details.get("characteristic", "a protected characteristic")
    state.provisions.update({"Article V Section 6.2", "Article V Section 7.2"})
    state.add_violation(
        "state_equal_protection_violation",
        "rights_suppression",
        "State government",
        f"State enacts a law that classifies persons on the basis of {characteristic}. Such classifications are presumptively unconstitutional under Article V Section 7.2 and must satisfy strict scrutiny.",
        "Article V Section 6.2 and Section 7.2",
        day,
    )
    state.add_obligation(
        "court_apply_strict_scrutiny_to_state_law",
        "Federal courts",
        "apply strict scrutiny and void the discriminatory state classification if it fails",
        "Article V Section 6.2 and Section 7.2",
        day,
        day + 30,
        severity="high",
    )


def handle_court_voids_discriminatory_state_law(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_apply_strict_scrutiny_to_state_law",
        day,
        "applied strict scrutiny and voided the discriminatory state classification for failure to serve a compelling interest by the least restrictive means",
    )
    state.add_entry(
        day,
        "outcome",
        "The state law is void under Article V Section 6.2 and Section 7.2. The rights floor applies to state governments; no state law may reduce or eliminate rights guaranteed by Article V.",
        "Article V Section 1.5, Section 6.2, and Section 7.2",
    )


def handle_congress_votes_nationwide_rights_suspension(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.provisions.update({"Article V Section 1.3", "Article V Section 14.3"})
    state.add_entry(
        day,
        "event",
        "Congress passes a 2/3 vote in both chambers to suspend specific rights during the declared emergency, applicable nationwide. A judicial finding that the suspension is narrowly tailored is also required under Article V Section 1.3 before the suspension takes effect.",
        "Article V Section 1.3",
    )
    state.add_obligation(
        "court_finding_rights_suspension_narrowness",
        "D.C. Circuit Court of Appeals",
        "determine whether the proposed nationwide rights suspension is narrowly tailored, necessary, and supported by a judicial finding that the emergency itself affects the entire nation as required by Article V Section 14.3",
        "Article V Section 1.3 and Section 14.3",
        day,
        day + 3,
        severity="high",
    )


def handle_court_rejects_rights_suspension_finding(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_finding_rights_suspension_narrowness",
        day,
        "declined to issue the required judicial finding because the proposed suspension is not narrowly tailored to the affected area and population",
    )
    state.add_violation(
        "overbroad_rights_suspension_void",
        "rights_suppression",
        "Congress",
        "Congress attempted a nationwide rights suspension that is not narrowly tailored to a geographic area or population directly affected by the emergency, in violation of Article V Section 1.3 and Section 14.3. Without the required judicial finding, the suspension does not take effect.",
        "Article V Section 1.3 and Section 14.3",
        day,
    )
    state.add_entry(
        day,
        "outcome",
        "The proposed suspension is void. A nationwide suspension requires a judicial finding that the emergency itself affects the entire nation. The court declined to make that finding.",
        "Article V Section 1.3 and Section 14.3",
    )


def handle_agency_purchases_data_to_circumvent_warrant(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.provisions.update({"Article V Section 10.3", "Article V Section 5.3"})
    state.add_violation(
        "data_purchase_warrant_circumvention",
        "rights_suppression",
        "Government agency",
        "Government agency purchases personal data from a private data broker — including location data, communications metadata, and association records — in order to obtain information it would need a warrant to collect directly, in violation of Article V Section 10.3.",
        "Article V Section 10.3 and Section 5.3",
        day,
    )
    state.add_obligation(
        "court_apply_warrant_requirement_to_purchased_data",
        "Federal courts",
        "apply the warrant requirement to the purchased data under Article V Section 10.3 and suppress any evidence derived from it",
        "Article V Section 10.3 and Section 5.3",
        day,
        day + 14,
        severity="high",
    )


def handle_court_applies_warrant_requirement_to_purchased_data(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_apply_warrant_requirement_to_purchased_data",
        day,
        "treated the purchased data as government-obtained under Article V Section 10.3 and suppressed it as collected without a warrant",
    )
    state.add_entry(
        day,
        "outcome",
        "Data purchased from a private entity to circumvent the warrant requirement is treated as government-obtained for all constitutional purposes under Article V Section 10.3. The warrant requirement cannot be evaded by routing collection through a commercial intermediary.",
        "Article V Section 10.3 and Section 5.3",
    )


def handle_state_sponsors_school_prayer(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.provisions.update({"Article V Section 3.2", "Article V Section 3.3", "Article V Section 3.4"})
    state.add_violation(
        "state_school_prayer_sponsorship",
        "rights_suppression",
        "Public school officials",
        "Public school officials organize or lead prayer in an official capacity and pressure students to participate, violating the no-establishment, neutrality, and school-specific religion rules of Article V.",
        "Article V Section 3.2, Section 3.3, and Section 3.4",
        day,
    )
    state.add_obligation(
        "court_enjoin_school_prayer_sponsorship",
        "Federal courts",
        "enjoin the official prayer practice and require religious neutrality in the public school",
        "Article V Section 3.2, Section 3.3, and Section 3.4",
        day,
        day + 14,
        severity="high",
    )


def handle_court_enjoins_school_prayer_sponsorship(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_enjoin_school_prayer_sponsorship",
        day,
        "enjoined the official prayer practice, barred school-led religious activity, and reaffirmed that student religious expression may remain voluntary and private on the same terms as other student expression",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article V protects both religious freedom and government neutrality: officials may not sponsor religion, but students retain their own private religious liberty.",
        "Article V Section 3.1 through Section 3.4",
    )


def handle_state_forces_medical_procedure_without_sufficient_justification(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    procedure = details.get("procedure", "a medical procedure")
    state.provisions.update({"Article V Section 4.1", "Article V Section 4.2", "Article V Section 4.3"})
    state.add_violation(
        "bodily_autonomy_violation",
        "rights_suppression",
        "State government",
        f"State law compels {procedure} without a sufficiently tailored public-health justification, medical exemption structure, or individualized necessity. Article V protects bodily autonomy and bars compulsory medical decision-making absent a compelling interest pursued by the least restrictive means.",
        "Article V Section 4.1, Section 4.2, and Section 4.3",
        day,
    )
    state.add_obligation(
        "court_block_forced_medical_procedure",
        "Federal courts",
        "block enforcement of the compulsory medical procedure law unless the state satisfies Article V's strict bodily-autonomy and public-health requirements",
        "Article V Section 4.1 and Section 4.2",
        day,
        day + 10,
        severity="high",
    )


def handle_court_blocks_forced_medical_procedure(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_block_forced_medical_procedure",
        day,
        "blocked enforcement of the compulsory medical-procedure law after finding that the state had not shown a sufficiently tailored public-health necessity or adequate medical exemptions",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates Article V's bodily-autonomy rule: the government cannot compel medical decisions merely by invoking public welfare in the abstract.",
        "Article V Section 4.1 and Section 4.2",
    )


def handle_state_refuses_parental_recognition_based_on_family_structure(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    family = details.get("family", "a lawfully formed family")
    state.provisions.update({"Article V Section 4.1", "Article V Section 4.3", "Article V Section 7.2"})
    state.add_violation(
        "family_autonomy_parental_recognition_violation",
        "rights_suppression",
        "State government",
        f"State officials refuse to recognize the parental status of {family} solely because of the sex, gender, or family structure of the parents. Article V protects family formation and parental recognition from unjustified government interference and bars discriminatory classifications affecting family status.",
        "Article V Section 4.1, Section 4.3, and Section 7.2",
        day,
    )
    state.add_obligation(
        "court_restore_parental_recognition",
        "Federal or state courts",
        "restore lawful parental recognition and enjoin enforcement of the discriminatory family-status rule",
        "Article V Section 4.3 and Section 7.2",
        day,
        day + 21,
        severity="high",
    )


def handle_court_restores_parental_recognition(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_restore_parental_recognition",
        day,
        "restored parental recognition, barred enforcement of the discriminatory family-status rule, and held that family decisions may not be denied legal effect because of the sex, gender, or sexual orientation of the parents",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article V protects family autonomy in substance, not only marriage in name. The state may not deny legal parental recognition to an otherwise lawful family on discriminatory grounds.",
        "Article V Section 4.3 and Section 7.2",
    )


def handle_government_throttles_internet_access_for_political_punishment(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    target = details.get("target", "a disfavored political association")
    state.provisions.update({"Article V Section 10.6", "Article V Section 2.6"})
    state.add_violation(
        "political_internet_access_punishment",
        "rights_suppression",
        "Government",
        f"Government officials deny, throttle, or otherwise degrade internet access for {target} because of political views or associations. Article V forbids using internet access as punishment, political coercion, or discrimination based on political viewpoint.",
        "Article V Section 10.6 and Section 2.6",
        day,
    )
    state.add_obligation(
        "court_restore_internet_access",
        "Federal courts",
        "order prompt restoration of nondiscriminatory internet access and bar the politically punitive restriction",
        "Article V Section 10.6 and Section 2.6",
        day,
        day + 10,
        severity="high",
    )


def handle_court_restores_internet_access(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_restore_internet_access",
        day,
        "ordered prompt restoration of nondiscriminatory internet access and barred the politically punitive restriction",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that the right to internet access is not symbolic. Government may not use throttling or denial of access as a political punishment or coercive tool.",
        "Article V Section 10.6 and Section 2.6",
    )


HANDLERS = {
    "warrantless_surveillance_conducted": handle_warrantless_surveillance_conducted,
    "court_orders_surveillance_halt": handle_court_orders_surveillance_halt,
    "agency_complies_with_surveillance_halt": handle_agency_complies_with_surveillance_halt,
    "emergency_used_to_restrict_protected_speech": handle_emergency_used_to_restrict_protected_speech,
    "court_voids_emergency_rights_restriction": handle_court_voids_emergency_rights_restriction,
    "president_suspends_habeas_corpus_by_executive_order": handle_president_suspends_habeas_corpus_by_executive_order,
    "court_voids_habeas_suspension": handle_court_voids_habeas_suspension,
    "budget_deadline_missed": handle_budget_deadline_missed,
    "executive_attempts_selective_cr_funding": handle_executive_attempts_selective_cr_funding,
    "court_blocks_cr_manipulation": handle_court_blocks_cr_manipulation,
    "government_targets_political_speech": handle_government_targets_political_speech,
    "court_voids_political_speech_restriction": handle_court_voids_political_speech_restriction,
    "state_enacts_discriminatory_classification": handle_state_enacts_discriminatory_classification,
    "court_voids_discriminatory_state_law": handle_court_voids_discriminatory_state_law,
    "congress_votes_nationwide_rights_suspension": handle_congress_votes_nationwide_rights_suspension,
    "court_rejects_rights_suspension_finding": handle_court_rejects_rights_suspension_finding,
    "agency_purchases_data_to_circumvent_warrant": handle_agency_purchases_data_to_circumvent_warrant,
    "court_applies_warrant_requirement_to_purchased_data": handle_court_applies_warrant_requirement_to_purchased_data,
    "state_sponsors_school_prayer": handle_state_sponsors_school_prayer,
    "court_enjoins_school_prayer_sponsorship": handle_court_enjoins_school_prayer_sponsorship,
    "state_forces_medical_procedure_without_sufficient_justification": handle_state_forces_medical_procedure_without_sufficient_justification,
    "court_blocks_forced_medical_procedure": handle_court_blocks_forced_medical_procedure,
    "state_refuses_parental_recognition_based_on_family_structure": handle_state_refuses_parental_recognition_based_on_family_structure,
    "court_restores_parental_recognition": handle_court_restores_parental_recognition,
    "government_throttles_internet_access_for_political_punishment": handle_government_throttles_internet_access_for_political_punishment,
    "court_restores_internet_access": handle_court_restores_internet_access,
}
