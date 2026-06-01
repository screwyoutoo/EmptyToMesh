When you Import Vroid models in blender, Their Colliders are empty spheres.
Empty spheres lack world axis size attributes.
Wiggle2 addon's Collision system seemingly does not respond to empty objects when assigned but it reacts to mesh objects.
I wanted to keep official colliders without having to manually parent objects to model so I made this with AI to automatically convert Empty objects to meshes in exact same location and size.
you do not need to select the objects to be active object, this addon converts All empties to mesh spheres at the moment.
NOTE: Consider using this script on a fresh blender scene, not your actual project.

Instructions:
Simply add the addon like any other addon you install in blender preferences.
After Adding, There's no GUI because your N-panel is probably already populated. It is accessible through F3 search function only.
Search: "Convert Empties To Mesh" to find it. Done. Now wiggle2 reacts to body colliders.
New created meshes are placed on a new collection named "Col".
<img width="762" height="468" alt="g1" src="https://github.com/user-attachments/assets/380a1fd6-5f1d-403c-837c-116d02757496" />
<img width="721" height="363" alt="g2" src="https://github.com/user-attachments/assets/b8cd7fc8-b48b-4e58-95ab-703e7dbc1f7f" />
<img width="683" height="395" alt="g3" src="https://github.com/user-attachments/assets/5cb8679f-bfcc-4132-abe7-02e6a006e188" />

