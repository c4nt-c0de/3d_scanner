# 3D Photogrammetry Scanner
This project is a work in progress.
3D photogrammetry scanning system powered by Python, Flask, stepper motors, and a Raspberry Pi 4B. Designed for precise small object capture and subsequent 3D model reconstruction.

## Showcase
Example images of a rock taken with the test setup.
![Test Run - Rock Showcase](showcase_results/test_run_imgs_rock.gif)

### Proof of Concept Result
[🌐 Open Interactive 3D Model Viewer](https://c4nt-c0de.github.io/3d_scanner/viewer.html)

First 3D model result. The object was photographed only in one orientation, but the level of detail is promising (3D model obtained with RealityScan software).

## Hardware Stack
- **Microcontroller / Compute:** Raspberry Pi
- **Camera:** Raspberry Pi Camera v3 (for high-resolution image capture)
- **Stepper Motor:** NEMA 17 stepper motor for precise rotational positioning
- **Motor Driver:** BIGTREETECH TMC2209 driver for quiet and smooth microstepping control

## Software Stack
- **Control & Automation:** Python, Flask (web interface for triggering and managing scans)
- **Reconstruction:** Processed and reconstructed using photogrammetry software RealityScan for now, as it is the fastest and quite convenient. We will see if an implementation of some reconstruction algorithm is practical with this setup.

## Features
- Automated rotation and image capture workflow.
- Clean web-based interface for remote triggering.
- Structured output directory management for raw capture data ready for photogrammetry pipelines.
