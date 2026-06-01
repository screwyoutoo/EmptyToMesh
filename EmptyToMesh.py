# ##### BEGIN GPL LICENSE BLOCK #####
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Empty To Mesh",
    "author": "screwyoutoo",
    "version": (1, 2, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Object > Convert Empties to Mesh",
    "description": "Converts sphere-displayed empties to UV sphere meshes for physics collisions",
    "category": "Object",
}

import bpy
from bpy.props import StringProperty


class OBJECT_OT_convert_empties_to_mesh(bpy.types.Operator):
    """Convert sphere empties to mesh, parent to empties, hide empties, store meshes in a collection"""
    bl_idname = "object.convert_empties_to_mesh"
    bl_label = "Convert Empties to Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    collection_name: StringProperty(
        name="Collection Name",
        default="Col"
    )

    def execute(self, context):
        sphere_empties = [obj for obj in bpy.data.objects
                          if obj.type == 'EMPTY' and obj.empty_display_type == 'SPHERE']

        if not sphere_empties:
            self.report({'WARNING'}, "No sphere empties found")
            return {'CANCELLED'}

        # Ensure the Col collection exists
        coll_name = self.collection_name
        if coll_name in bpy.data.collections:
            target_coll = bpy.data.collections[coll_name]
        else:
            target_coll = bpy.data.collections.new(coll_name)
            context.scene.collection.children.link(target_coll)

        converted = 0
        for empty in sphere_empties:
            radius = empty.empty_display_size
            name = empty.name

            # Create sphere at origin with correct radius
            bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=(0, 0, 0))
            sphere = context.active_object
            sphere.name = name

            # Parent sphere to empty FIRST
            sphere.parent = empty

            # Now set local transform to zero → sphere sits exactly at empty's position
            sphere.location = (0, 0, 0)
            sphere.rotation_euler = (0, 0, 0)
            sphere.scale = (1, 1, 1)

            # Move to Col collection
            for col in sphere.users_collection:
                col.objects.unlink(sphere)
            target_coll.objects.link(sphere)

            # Hide the empty (keep it)
            empty.hide_viewport = True
            empty.hide_render = True

            converted += 1

        self.report({'INFO'}, f"Converted {converted} sphere empties to mesh. Meshes in '{coll_name}' collection.")
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_convert_empties_to_mesh.bl_idname, text="Convert Empties to Mesh")


def register():
    bpy.utils.register_class(OBJECT_OT_convert_empties_to_mesh)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_convert_empties_to_mesh)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()