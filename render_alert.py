bl_info = {
    "name": "Render Complete Alert",
    "blender": (2, 80, 0),
    "category": "Render",
    "version": (1, 0, 0),
    "description": "Play an alert sound when rendering is complete.",
}

import bpy
import os
import platform

def play_alert_sound():
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.MessageBeep()
    elif system == "Darwin":
        os.system("afplay /System/Library/Sounds/Glass.aiff")
    else:
        os.system("paplay /usr/share/sounds/freedesktop/stereo/complete.oga")

def render_complete_handler(scene):
    print("レンダリングが完了しました！")
    play_alert_sound()

class RENDER_OT_EnableAlert(bpy.types.Operator):
    """Enable Render Complete Alert"""
    bl_idname = "render.enable_alert"
    bl_label = "Enable Render Complete Alert"

    def execute(self, context):
        if render_complete_handler not in bpy.app.handlers.render_complete:
            bpy.app.handlers.render_complete.append(render_complete_handler)
        self.report({'INFO'}, "Render complete alert enabled")
        return {'FINISHED'}

class RENDER_OT_DisableAlert(bpy.types.Operator):
    """Disable Render Complete Alert"""
    bl_idname = "render.disable_alert"
    bl_label = "Disable Render Complete Alert"

    def execute(self, context):
        if render_complete_handler in bpy.app.handlers.render_complete:
            bpy.app.handlers.render_complete.remove(render_complete_handler)
        self.report({'INFO'}, "Render complete alert disabled")
        return {'FINISHED'}

class RENDER_PT_AlertPanel(bpy.types.Panel):
    """Render Complete Alert Panel"""
    bl_label = "Render Complete Alert"
    bl_idname = "RENDER_PT_alert_panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"

    def draw(self, context):
        layout = self.layout
        layout.operator(RENDER_OT_EnableAlert.bl_idname, text="Enable Alert")
        layout.operator(RENDER_OT_DisableAlert.bl_idname, text="Disable Alert")

def register():
    bpy.utils.register_class(RENDER_OT_EnableAlert)
    bpy.utils.register_class(RENDER_OT_DisableAlert)
    bpy.utils.register_class(RENDER_PT_AlertPanel)

def unregister():
    bpy.utils.unregister_class(RENDER_OT_EnableAlert)
    bpy.utils.unregister_class(RENDER_OT_DisableAlert)
    bpy.utils.unregister_class(RENDER_PT_AlertPanel)

if __name__ == "__main__":
    register()
