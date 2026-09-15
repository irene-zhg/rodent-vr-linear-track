# Looping Virtual Reality Linear Track with Telemetry Data Pipeline
A closed-loop, custom-scripted virtual reality linear track built in Unreal Engine 5.7. that logs real-time telemetry data. Designed for rodent spatial navigational and behavioural experiments with limited electromagnetic interference and low-latency data processing. 

## Table of Contents
1. [Project Demo](#demo)
2. [Core VR Environment Features](#core-VR-environment-features)
3. [Blueprint Architecture](#blueprint-architecture)
4. [Telemetry Data Pipeline](#telemetry-data-pipeline)
5. [Applications & Impact](#applications-&-impact)
6. [Limitations](#limitations)
7. [Next Steps](#next-steps)

## Project Demo
- insert video from presentation
- 1. Name file
  2. Play project
  3. Slide computer mouse sensor along track, clicking M for marker
  4. Convert saved telemetry file using code
  5. View telemetry data 

## Core VR Environment Features
- Custom file naming variable
- Looping teleportation w/ 3s delay
- Distinct wall patterns/decals
- Distance amplifier
- Telemetry Logger per 60 hz/set frame w/ backup telemetry logger in chunks to protect against data lost
- Experimental marker

## VR Blueprint Architecture
- Insert scripting diagrams with captions

## Telemetry Data Pipeline
- see uploaded sav to csv conversion code
- data recorded (time/position/displacement)

## Applications & Impact
- reduced EMI "noise" when used with tech like ephys = greater spike detection, more robust data collection and analysis
- easier to incorporate future modification/do so without coding

## Limitations
- Currently only editable on UE5.7; but executable/attached packaged exe file works anywhere

## Next Steps
- incorporating lick sensor to enable behavioural/mem encoding experiments
- clinical translation/parallel environments to pair with VR headset (Quest) + EEG
