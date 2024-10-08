# Energirobotter Blender Animation Recorder

Blender addon for recording local angles of armature during each animation frame to CSV file. 

The name of the addon is simplified to `AnimationRecorder`.

There are two ways to install/use this addon. Installing like a normal Blender addon, or in a development environment with VSCode. 

## Setup

### Installing Blender Addon
In Blender, navigate to `Edit > Preferences... > Add-Ons`.

Press `Install`.

Navigate to the addon .zip file, click `Install Add-on`.

### Development Setup With VSCode

#### Requirements
Tested with:

- Ubuntu 22.04
- Blender 4.2.1
- Python 3.11.7 (Blender intepreter verision)
- VSCode

#### Dependencies

It is recommended to install Python dependencies in a virtual environment, like pipenv or Anaconda. Install dependencies with (examples with Miniconda):
```
conda create -n energirobotter_blender_animation_recorder python=3.11
pip3 install -r requirements.txt
```

In VSCode download the extension `Blender Development` by Jaques Lucke. 

#### Blender Deployment

> If addon is already installed normally in Blender through `.zip` file, disable it first.

Activate environment from terminal and open VSCode:
```
conda activate energirobotter_blender_animation_recorder
code src/
```
> NOTE: You must open VSCode in the same directory as the `__init__.py` file, otherwise the extension won't see the addon. Here this is `src/`.

Start Blender  from VSCode with `Ctrl + Shift + P` and search for `Blender: Start`. Use the location of your Blender install. 
> If there is an error, check out [this video](https://youtu.be/YUytEtaVrrc?t=469) for how to fix it.

From here you can use `Ctrl + Shift + P` and choose `Blender: Reload Addons` to update Addons in Blender.

> NOTE: The `__init__.py` file is the addon entry point from Blender, so all Blender classes should be registered here. This is only an affect of the VSCode Blender extension.


## Usage

1. Create animation with a rig, name all bones in the rig appropriate names. These are the names used for logging. 

2. Find the AnimationRecorder tab in the N Panel (if not visible press N).

3. Press `Record animation`. This will quickly go through each frame until the end frame, recording all bone's local angles to a CSV file.

4. The CSV file is saved next to you Blender project, and will be overwritten if not moved/renamed before next recording.  
