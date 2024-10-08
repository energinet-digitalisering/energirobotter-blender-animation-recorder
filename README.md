# Energirobotter Blender Animation Recorder

Blender addon for recording local angles of armature during each animation frame to CSV file. 

The name of the addon is simplified to `AnimationRecorder`.


## Development Setup With VSCode

It is recommended to install Python dependencies in a virtual environment, like pipenv or Anaconda. Install dependencies with (examples with Miniconda):
```
conda create -n energirobotter_blender_animation_recorder python=3.11
pip3 install -r requirements.txt
```

In VSCode download the extension `Blender Development` by Jaques Lucke. 

### Blender Deployment

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
