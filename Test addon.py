bl_info = {
    "name": "My Test Addon",
    "author": "Jacob",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "3d veiw > F3 > Search > Monkey grid",
    "description": "Adds monkeys in rows",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object",
}
import bpy



class MESH_OT_MONKEY_grid(bpy.types.Operator):
    """The Tool Tip"""
    bl_idname = 'mesh.monkey_grid'
    bl_label = 'Monkey Grid'
    bl_options = {"REGISTER", "UNDO"}
    
    count_x: bpy.props.IntProperty(
        name="X", 
        description="Number of monkeys in the x-direction",
        default=3,
        min=0, soft_max=10,
    )
    count_y: bpy.props.IntProperty(
        name="Y", 
        description="Number of monkeys in the Y-direction",
        default=3,
        min=0, soft_max=10,
    )
    size: bpy.props.FloatProperty(
        name="Size",
        description="Size of each monkey",
        default=0.5,
        min=0, soft_max=1,
    )
    

    def execute(self, context):
        for idx in range(self.count_x * self.count_y ):
            x= idx % self.count_x
            y= idx //self.count_x
            bpy.ops.mesh.primitive_monkey_add( 
            size=self.size,
            location=(x,y, 1))
    
            
        
        return {'FINISHED'}
    

class VEIW3D_PT_monkey_grid(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Monkeys'
    bl_label = 'Grid'
    
    def draw(self, context):
        self.layout.operator('mesh.monkey_grid',
             text= 'Default grid',
             icon= 'MONKEY')
        
    
    
    
def register():
    bpy.utils.register_class(MESH_OT_MONKEY_grid)
    bpy.utils.register_class(VEIW3D_PT_monkey_grid)
    
def unregister():
    bpy.utils.unregister_class(MESH_OT_MONKEY_grid)
    bpy.utils.unregister_class(VEIW3D_PT_monkey_grid)

if __name__ == '__main__':
	register()
    

      
      
      
      
      
      
        


    
