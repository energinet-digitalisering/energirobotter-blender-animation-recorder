from enum import Enum
import mathutils
import numpy as np

import bpy


class State(Enum):
    IDLE = 0
    RECORDING = 1


class AnimationRecorder:

    def __init__(self):

        self.state = State.IDLE

    def __del__(self):
        self.set_state_idle()

    def set_state_idle(self):
        self.state = State.IDLE

    def get_bone_names(self):

        names = []

        for bone in bpy.context.active_object.pose.bones:
            names.append(bone.name)

        return names

    # Helper functions from rigify plugin
    def get_pose_matrix_in_other_space(self, mat, pose_bone):
        """Returns the transform matrix relative to pose_bone's current
        transform space. In other words, presuming that mat is in
        armature space, slapping the returned matrix onto pose_bone
        should give it the armature-space transforms of mat.
        """

        rest = pose_bone.bone.matrix_local.copy()
        rest_inv = rest.inverted()

        if pose_bone.parent != None:
            par_mat = pose_bone.parent.matrix.copy()
            par_inv = par_mat.inverted()
            par_rest = pose_bone.parent.bone.matrix_local.copy()
        else:
            par_mat = mathutils.Matrix()
            par_inv = mathutils.Matrix()
            par_rest = mathutils.Matrix()

        # Get matrix in bone's current transform space
        smat = rest_inv @ (par_rest @ (par_inv @ mat))

        return smat

    def get_bones_rotation(self, pose_bone, axis):

        mat = self.get_pose_matrix_in_other_space(pose_bone.matrix, pose_bone)

        if axis == 0:
            return mat.to_euler().x
        elif axis == 1:
            return mat.to_euler().y
        elif axis == 2:
            return mat.to_euler().z

    def angle_of_bone(self, bone):

        # Get unconstrained axis
        axis_rot = (np.array(bone.lock_rotation) == False).nonzero()[0][0]

        return np.rad2deg(self.get_bones_rotation(bone, axis_rot))

    def angles_of_bones(self):

        data = []

        for bone in bpy.context.active_object.pose.bones:
            data.append(self.angle_of_bone(bone))

        return data

    def record_animation(self, report_blender):

        if not self.state == State.RECORDING:
            self.state = State.RECORDING

            bpy.data.scenes["Scene"].frame_set(0)

            # Iterate through all animation frames
            while self.state == State.RECORDING:
                bpy.data.scenes["Scene"].frame_set(
                    bpy.data.scenes["Scene"].frame_current + 1
                )

                # Record data
                print(bpy.data.scenes["Scene"].frame_current)
                self.angles_of_bones()

                # Break loop at end of animation
                if (
                    bpy.data.scenes["Scene"].frame_current
                    >= bpy.data.scenes["Scene"].frame_end
                ):
                    break

            report_blender({"INFO"}, "End of animation")

            self.state = State.IDLE

        else:
            report_blender({"INFO"}, "Animation is already in progress")
