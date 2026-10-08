# UE 5.7 Virtual Reality Linear Track with Telemetry Data Pipeline
A closed-loop, custom-scripted virtual reality (VR) linear track built in Unreal Engine (UE) 5.7 that logs real-time telemetry data. Designed for rodent navigational and behavioural experiments with limited electromagnetic interference (EMI) and low-latency data processing for use alongside electrophysiology. 

## Table of Contents
1. [System Pipeline Demo](#system-pipeline-demo)
2. [Background & Objective](#background-&-objective)
3. [Core VR Environment Features](#core-VR-environment-features)
4. [Blueprint Architecture](#blueprint-architecture)
5. [Pipeline & Repository Usage Guide](#pipeline-&-repository-usage-guide)
7. [Limitations](#limitations)
8. [Application Impact & Future Directions](#application-impact-&-future-directions)

## System Pipeline
### Computer Mouse Sensor &rarr; Unreal Engine &rarr; Telemetry Output
An optical motion sensor (Logitech wireless computer mouse) tracks treadmill movement from a rodent and updates the player position in Unreal Engine. On program exit, an automated final save writes the raw telemetry data to a .sav file. The file is converted to a readable .csv sheet via Python.

https://github.com/user-attachments/assets/a29de731-eb81-4aad-a683-b99e8f6e168a

**In the demo above, the sensor was moved by hand across a surface. For real-time use with a treadmill and the physical setup, see demos [here](demo).**


## Background & Objective
The Zwang Lab studies neuronal circuitry in Alzheimer's Disease by recording electrophysiology from mice with mesh electronics as they navigate a VR linear track. 

The prior setup had two bottlenecks: 

1. **Platform Modification**: The MATLAB-based VR system required extensive, low-level coding for even small modifications.
2. **Electromagnetic Interference (EMI)**: The laser motion sensor introduced significant EMI into data, making it difficult to isolate single-unit neuronal activity.

This pipeline addresses these challenges through:
1. **Unreal Engine**: The environment is built with blueprint scripting, providing a simplified, readable, and visual development platform for rapid configuration and deployment.
2. **Optical Motion Tracking**: An optical motion sensor replaces the laser sensor to reduce EMI.

This pipeline facilitates cleaner recordings and improves downstream data analysis, providing a strong framework for future clinical translation.

## Core VR Environment Features
- **Continuous backup saving**: telemetry is saved 
- **Custom file name**: set via an UE string variable in the editor before starting a session.
- **Experimental keyboard marker**: pressing the 'M' key writes a time-aligned 'MARKER' to the outputted telemetry data to flag any experimental milestones.
- **Looping teleportation**: reaching the end of the track triggers a 3-second delay before the pawn is teleported back to the origin.
- **Restricted locomotion**: forward (y-axis) only, but yaw, pitch, and roll can be enabled with scripting edits.
- **Visual Landmarks**: 5 distinct visual wall patterns built from UE materials, enabling spatial memory encoding and position learning.

## Blueprint Architecture
Isolated photos of the game mode, kinetics, and teleportation scripting sections are included under blueprints [here](assets/blueprints).

![Complete Blueprint Scripting](assets/blueprints/complete-scripting.png)

## Pipeline & Repository Usage Guideline
Usage requires Unreal Engine 5.7 Editor and Python.

**Launching a Session**
1. Open the source project inside UE 5.7.
2. Select BP_XRPawn in viewport > Details Panel > Default > CustomFileName.
3. Edit trial name.
4. Click play to start session, click once to begin hands-free movement using the sensor. Telemetry logs data continuously into the system RAM at the specified frame rate limit.
5. Press esc inside the game viewport window to close the application. Exiting executes the final storage write as a .sav file inside Saved/SaveGames/.

**Telemetry Data Post-Processing**
1. Edit input and output path in src/UECoordinateConverter.py.
2. Open terminal and run src/UECoordinateConverter.py and enter custom session file name when prompted.
3. Script outputs the readable csv file directly into specified path with the following columns:
- Timestamp_Sec
- Player_X, Y, Z: 3D coordinate tracking path vectors (in cm)
- Player_Yaw: Body/head orientation tracking angle (degrees)
- Displacement

## Limitations
- Built and tested on UE 5.7: have had challenges with migrating to other versions and maintaining functionality
- SerialCOM plugin does not work in UE 5.7 which prevents hardware integration with microcontrollers like Arduino, actively troubleshooting integration

## Application Impact & Future Directions
- Recording precision: lower system EMI lowers Root Mean Squared (RMS) baseline noise, improving spike-sorting precision and single-unit data processing
- Clinical translation: UE's built-in XR compatibility allows for environments to be easily translated for parallel clinical studies with EEG
- Microcontroller integration: integrate serialCOM for UE 5.7 to add hardwire such as a lick sensor for reward experiments
