# Competition rules

!!! warning "Draft edition"

    This document is under review by the organizing committee. Items marked
    **[pending approval]** contain preliminary values and may change before
    publication of the official edition. After approval, this mark will be removed
    and the edition date will be recorded.

---

## 1. General provisions

**1.1.** These rules define the procedure for organizing and conducting the national
robotics and artificial intelligence competition **AgroTech Robotics Challenge**
(hereinafter — the Competition).

**1.2.** The Organizer of the Competition is the New Uzbekistan University
Engineering School (hereinafter — the Organizer).

**1.3.** Objectives of the Competition:

- develop competencies in robotics, computer vision, and machine learning among
  students of the Republic of Uzbekistan;
- apply modern robotic platforms to practical agriculture tasks;
- build a developer community around open robotics tools.

**1.4.** The Competition is held on Unitree Go2 (quadruped robot) and Unitree G1
(humanoid robot) platforms in two independent tracks.

**1.5.** The official Competition website, where rules, calendar, results, and all
changes are published, is
[newuu-engineering.github.io/unitree-contest](https://newuu-engineering.github.io/unitree-contest/).

---

## 2. Terms and definitions

**Track** — a Competition direction defined by the robotic platform. Tracks are
described in [Tracks](tracks/index.md).

**Stage** — a part of the Competition season with its own tasks and procedure.
Stages are described in [Stages](stages.md).

**Solution** — software code prepared by the team to perform the stage task,
together with supporting materials.

**Run** — a single execution of the team's solution under stage conditions with
results recorded by judges.

**Judging script** — Organizer software that runs the solution in the standard
environment and calculates scores.

**Starter Kit** — the set of tools provided by the Organizer, described in
[Starter Kit](starter-kit.md).

**Intervention** — any human action that affects task execution by the robot during
a run.

---

## 3. Participants

**3.1.** Students of higher education institutions and colleges of the Republic of
Uzbekistan may participate. **[pending approval]**

**3.2.** The Competition is team-based. Recommended team size is two to four people.
Individual applications are allowed. **[pending approval]**

**3.3.** Each participant may belong to only one team.

**3.4.** The team chooses one track at registration. Track changes during the season
are not allowed.

**3.5.** The team appoints a captain — the sole person authorized to communicate with
the Organizer and submit appeals in disputed situations.

**3.6.** The team may involve an academic advisor. The advisor is not part of the
team, does not participate in runs, and does not affect scoring.

**3.7.** The number of teams from one institution is not limited.
**[pending approval]**

---

## 4. Registration and admission

**4.1.** Registration is conducted electronically on the Competition website within
the dates specified in the calendar.

**4.2.** Registration includes: team name, chosen track, roster with institution for
each member, captain contact details.

**4.3.** Roster changes are allowed until registration closes. After the first stage
starts, the roster is fixed; participant replacement is possible only by Organizer
decision for a valid reason.

**4.4.** The Organizer may deny admission to a team whose application contains false
information.

---

## 5. Stage 1. Qualifier

**5.1.** The stage is held remotely. Teams develop the solution in the Starter Kit
environment on their own equipment.

**5.2.** Minimum team equipment requirements are described in [Quick start](quickstart.md).
A robot or discrete GPU is not required.

**5.3.** The solution is submitted as a repository with the structure described in
[Starter Kit](starter-kit.md). The entry point is `main.py`.

**5.4.** The solution must run in the Organizer's standard container. Additional
dependencies are listed in `requirements.txt` and must install without internet
access during the run.

**5.5.** A team report of up to five pages describing the approach and listing
external components used is attached to the solution.

**5.6.** Solutions submitted after the deadline are not scored. The team is
responsible for the operability of the submitted solution.

**5.7.** Scoring is performed by the judging script on scenes identical for all
teams, with a fixed random seed. The solution is run several times; a stable result
counts. **[pending approval: number of runs]**

**5.8.** Teams with the highest scores advance to the second stage, within the
established quota. **[pending approval: quota per track]**

**5.9.** Stage results are published on the Competition website with a score breakdown
by criteria.

---

## 6. Stage 2. Semifinal

**6.1.** The stage is held onsite in the Organizer's robotics laboratory on the New
Uzbekistan University campus. Off-site trips are not provided. At least two team
members must be present. **[pending approval]**

**6.2.** Each team is assigned a time slot including preparation, calibration, and
scored runs. The schedule is published in advance.

**6.3.** Before scored runs, teams receive shared time for testing in the Organizer's
laboratory. **[pending approval: duration]**

**6.4.** Work with the real robot is conducted only in the presence of a judge and
within the assigned slot.

**6.5.** During a scored run, team members remain outside the work zone. Any action
that affects task execution is recorded as an intervention and counted in scoring.

**6.6.** The judge may stop a run at any time if there is a threat to people or
equipment. A run stopped for this reason may be repeated by judge decision if the
cause is not related to the team's solution.

**6.7.** The team must ensure graceful shutdown in the solution: the robot must enter
a safe state on error, not continue moving.

**6.8.** Modification of robot hardware is prohibited. Installation of additional
sensors is allowed only with written Organizer consent and only using standard
mounts.

---

## 7. Stage 3. Final

**7.1.** The final is held publicly. Performance order is determined by draw.

**7.2.** The final scenario includes dynamically changing conditions. Specific
conditions are communicated to teams no later than one week before the final.
**[pending approval: deadline]**

**7.3.** In the Unitree G1 track, the final includes work with the teleoperation kit.
The team may choose one of the strategies described in
[Track 2](tracks/g1.md) — both count equally.

**7.4.** Performance time is limited. Exceeding the limit stops the run; the result
achieved at the moment of stop is counted. **[pending approval: time limit]**

---

## 8. Scoring and winners

**8.1.** Criteria and weights are given in [Scoring](scoring.md).

**8.2.** Winners are determined separately for each track.

**8.3.** In case of a tie, the team with the higher autonomy score takes precedence;
if still tied — the team with the shorter scenario completion time.

**8.4.** Jury composition is published before the second stage starts. A jury member
affiliated with a team's institution does not score that team.

**8.5.** Awards and prize fund. **[pending approval]**

---

## 9. Fair play rules

**9.1.** Open libraries, frameworks, and pretrained models with licenses permitting
such use are allowed. All external components are listed in the team report.

**9.2.** The following is prohibited:

- presenting another team's code as your own solution;
- tuning the solution to a specific judging scene while bypassing general logic
  (for example, using hard-coded object coordinates instead of detection);
- interfering with the judging script, environment, or equipment;
- obstructing other teams.

**9.3.** Violation of section 9.2 results in removal of the solution from scoring; for
repeated or serious violations — team disqualification by Organizer decision.

**9.4.** Teams are responsible for compliance with licenses of components used.

---

## 10. Safety

!!! danger "Required reading before stage two"

    Unitree Go2 and G1 are robotic systems with high-power actuators. Failure to
    follow the rules below creates injury risk.

**10.1.** Only participants who completed Organizer briefing may work with robots.
Briefing is held on the day of arrival at the NEWUU laboratory.

**10.2.** People may not enter the work zone while the robot is moving. Work zone
boundaries are marked by the Organizer.

**10.3.** Emergency stop is held by the judge and must be accessible throughout the
run.

**10.4.** Unitree G1 operates exclusively on a safety harness. Harness disconnection
is not allowed under any circumstances.

**10.5.** Switching software to the real robot DDS domain is performed only in the
Organizer's laboratory and only with judge permission. The rule and its rationale
are described in
[Stack: safety rules](stack.md#safety-rules).

**10.6.** Connecting, disconnecting, and charging robot batteries independently is
prohibited. These operations are performed by Organizer staff.

**10.7.** If the robot behaves abnormally, the participant must immediately notify
the judge and must not attempt to stop the robot physically.

---

## 11. Disputes

**11.1.** An appeal for result review is submitted in writing by the team captain
within two hours after run results are published. **[pending approval: deadline]**

**11.2.** The appeal is reviewed by an appeals commission consisting of an Organizer
representative and at least two jury members.

**11.3.** The appeals commission decision is final.

**11.4.** Situations not covered by these rules are resolved by Organizer decision.

---

## 12. Rights to solutions

**12.1.** Copyright in solutions belongs to the developing teams.

**12.2.** The team grants the Organizer the right to use solution materials (code,
reports, run recordings) for non-commercial purposes: publishing results, covering
the Competition, and in educational materials.

**12.3.** The Organizer recommends, but does not require, teams to publish solutions
under an open license after the season ends.

---

## 13. Rule changes

**13.1.** The Organizer may amend these rules. Changes take effect upon publication
on the Competition website.

**13.2.** Changes affecting conditions of an already started stage are made only to
correct errors and ambiguities and are communicated to all teams.

**13.3.** The edition published on the website is authoritative.

---

!!! info "Questions about the rules"

    Send to [robotics@newuu.uz](mailto:robotics@newuu.uz). Answers to common questions
    are collected in [FAQ](faq.md).
