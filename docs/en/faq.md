# FAQ

## Participation

??? question "Where do onsite stages take place? Do we need to go to a field?"

    No. All onsite stages are held **in the NEWUU laboratory** on the university
    campus. Field trips with robots to orchards, greenhouses, or farms **are not
    planned**. Tasks are reproduced on a training arena with artificial beds, plant
    mock-ups, and **artificial fruit**.

??? question "Why does the documentation say 'orchard' and 'harvest' if everything is at the university?"

    This is the competition's **applied scenario**: algorithms must solve tasks
    close to real agriculture, but in a controlled laboratory setup. The simulator
    and arena model a field and sorting table; objects are props, not live crops.

??? question "Do I need my own robot or a powerful computer?"

    No. The first stage runs entirely in the simulator on your laptop — any machine
    with Docker works, including Mac on Apple Silicon and Windows. A discrete GPU is
    not required. Access to real Unitree Go2 and G1 robots is granted to teams that
    advance to the second stage.

??? question "What level of preparation is required?"

    Confident Python is enough. Knowledge of ROS 2, computer vision, or robotics is a
    plus, but the Starter Kit is designed so you can learn along the way: basic
    examples for both tracks already work; you improve them rather than write from
    scratch.

??? question "Can I participate alone?"

    Recommended team size is two to four people: usually one handles perception,
    another control and integration. Individual applications are allowed, but load on
    one person becomes noticeable at stages two and three.

??? question "Can I switch tracks during the season?"

    No, the track is chosen for the entire season. Stage tasks within a track are
    connected, and switching would reset the team's progress.

??? question "What languages is the competition held in?"

    Working languages are Uzbek and Russian. Technical documentation and code are in
    English, as is standard in the industry. The full **English site mirror** is at
    [/en/](/en/) (language selector in the header); **Russian** is the default at [/](/).

---

## Technical questions

??? question "The simulator does not open in the browser"

    Check that the container is running with port mapping `-p 6080:6080` and that the
    port is not used by another application. The address is exactly
    `http://localhost:6080`, without `https`. On corporate machines the port may be
    blocked by a firewall.

??? question "Everything is slow, the simulator stutters"

    The simulator renders on the CPU, so on weaker machines the picture may not be
    smooth. This does not affect the result: physics runs at a fixed step, and the
    judging run is deterministic. For comfortable work, disable the 3D view and use
    the robot camera stream.

??? question "Can I work without Docker by installing everything locally?"

    You can, but we do not support that scenario. The combination of CycloneDDS,
    ROS 2, and Python versions is matched to robot firmware, and any mismatch will
    surface at the real hardware stage. The judging run is always executed in the
    standard container anyway.

??? question "Can I use Isaac Sim instead of MuJoCo?"

    Yes, if you have an x86 machine with an NVIDIA GPU. Participant code does not
    change when switching simulators — both speak over the same DDS bus. Note that
    stage 1 judging runs in the standard environment.

??? question "Why does the Go2 example not work on G1?"

    Platforms use different message types: Go2 — `unitree_go`, G1 — `unitree_hg`. A
    copied example will run and may not even raise an error, but data will not
    match. See [Stack](stack.md) for details.

??? question "Can I control hand fingers directly, bypassing presets?"

    Yes, the `g1.hand.set_joints()` method accepts arbitrary finger positions.
    Presets are a convenient starting point, not a limitation. Remember that
    control is positional: there is no force feedback in the base API.

---

## Solutions and scoring

??? question "Can I use third-party code and pretrained models?"

    Yes, if they are open libraries and models with compatible licenses — list them
    in your report. Your engineering work is evaluated: fine-tuning on the agro
    dataset, integration, and reliability. See [Scoring](scoring.md) for details.

??? question "What if the solution works in simulation but not on the robot?"

    That is normal and, in essence, the main engineering task of stage two. The gap
    between model and reality — sensor noise, lighting, grip, latency — is exactly
    what separates a working robot from a polished demo. The stage includes time for
    calibration and test runs.

??? question "How many attempts are allowed per run?"

    The scenario is run several times, and a stable result counts, not the best
    attempt. The exact number of attempts is defined in the stage rules.

---

!!! question "Didn't find an answer?"

    Contact the organizers: [robotics@newuu.uz](mailto:robotics@newuu.uz)
    or open a discussion in the
    [competition repository](https://github.com/NewUU-engineering/unitree-contest).
