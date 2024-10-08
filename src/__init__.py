import os
import platform
import subprocess
import sys

import bpy
from bpy.utils import register_class, unregister_class

# Addon metadata
bl_info = {
    "name": "EnergirobotterBlenderAnimationRecorder",
    "author": "Energinet",
    "version": (0, 0, 0),
    "blender": (4, 2, 1),
    "location": "Toolbar > EnergirobotterBlenderAnimationRecorder",
    "description": "Record angles of animation at each frame to CSV file.",
    "category": "Animation",
}

############################### Packages ###############################

# Non standard Python packages - "python import name": "pip install name"
packages = {}


def install_package(package):

    if platform.system() == "win32":

        python_exe = os.path.join(sys.prefix, "bin", "python.exe")
        target = os.path.join(sys.prefix, "lib", "site-packages")

        subprocess.call([python_exe, "-m", "ensurepip"])
        subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

        subprocess.call(
            [python_exe, "-m", "pip", "install", "--upgrade", package, "-t", target]
        )

    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


for package_py, package_pip in packages.items():
    try:
        exec("import " + package_py)

    except ModuleNotFoundError:
        print(
            package_py
            + " module not found, installing '"
            + package_pip
            + "' with pip..."
        )

        install_package(package_pip)
        exec("import " + package_py)

        print(package_py + " successfully imported")

print("All packages installed")


############################### Defines ###############################

# Load addon modules
from .animation_recorder import AnimationRecorder, State

# Global objects
recorder = AnimationRecorder()


############################### Scene Properties ###############################


class SceneProperties(bpy.types.PropertyGroup):
    # Defining custom properties to be used by the addon panel

    ...


############################### Operators ###############################


class ANIMATIONRECORDER_OT_RecordAnimation(bpy.types.Operator):
    # Go through animation timeline and get angles from rig, and record to file

    bl_idname = "animation_recorder.record_animation"
    bl_label = "Go through animation timeline and record angles"

    def __init__(self):
        print("Animation recording starting...")

    def __del__(self):
        print("Animation recording ended")

    def modal(self, context, event):
        if event.type == "ESC":
            recorder.set_state_idle()

            self.report({"INFO"}, "ESC key pressed, stopping animation recording")
            return {"FINISHED"}

        if recorder.state == State.IDLE:
            self.report({"INFO"}, "Animation recording finished")
            return {"FINISHED"}

        return {"PASS_THROUGH"}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)

        recorder.record_animation(self.report)

        return {"RUNNING_MODAL"}


############################### Panels ###############################


class ANIMATIONRECORDER_PT_Panel(bpy.types.Panel):
    # Addon panel displaying options

    bl_label = "Animation Recorder"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AnimationRecorder"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout

        layout.row().operator(
            ANIMATIONRECORDER_OT_RecordAnimation.bl_idname,
            text="Record animation",
            icon="PLAY",
        )


############################### Blender Registration ###############################


classes = (
    SceneProperties,
    ANIMATIONRECORDER_OT_RecordAnimation,
    ANIMATIONRECORDER_PT_Panel,
)


def register():
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.scn_prop = bpy.props.PointerProperty(type=SceneProperties)


def unregister():
    for cls in classes:
        unregister_class(cls)

    del bpy.types.Scene.scn_prop


if __name__ == "__main__":

    register()
