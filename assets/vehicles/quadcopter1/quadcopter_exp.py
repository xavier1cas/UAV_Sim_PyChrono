# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: D:\Virginia-Tech-PhD\PHD_research\PyChrono\UAV_CAD_Models\Q4\Assem2.SLDASM

# Quad Copter Motors enumeration and Global reference frame (Reference frame acquired by SolidWorks)
#
# 4                  1
# -                  -
#   \    forward   / 
#    \      ^ X   /
#     \     |    /
#      \____|___/
#      |    |   |
#      |    |   |
#      |    |   |
#      |   O|___|______> Z right
#      |   Y up |
#      |        |
#      |________|
#      /        \
#     /          \
#    /            \
# 3 /              \ 2
# -                  -
#

import pychrono as chrono 
import builtins 

# some global settings: 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'quadcopter1_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Box_200x200x100-1')
body_1.SetPos(chrono.ChVectorD(0,-0.20913,-3.47590732374625e-15))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(0.751000000000001)
body_1.SetInertiaXX(chrono.ChVectorD(0.00426689349755881,0.00711851666666668,0.00426689349755882))
body_1.SetInertiaXY(chrono.ChVectorD(-4.80530715356197e-18,-2.43174143902709e-18,1.23780725515736e-18))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(2.43144632504112e-16,0.0283688415446072,-6.31609121787493e-17),chrono.ChQuaternionD(1,0,0,0)))

# # Visualization shape 
# body_1_1_shape = chrono.ChObjFileShape() 
# body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
# body_1.AddVisualShape(body_1_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))

# Attach a visualization shape
# First load a .obj from disk into a ChTriangleMeshConnected:
mesh_for_visualization1 = chrono.ChTriangleMeshConnected()
mesh_for_visualization1.LoadWavefrontMesh(shapes_dir +'body_1_1.obj')
# Now the  triangle mesh is inserted in a ChTriangleMeshShape visualization asset, 
# and added to the body
visualization_shape1 = chrono.ChTriangleMeshShape()
visualization_shape1.SetMesh(mesh_for_visualization1)
# visualization_shape1.SetWireframe(True)
visualization_shape1.SetColor(chrono.ChColor(0, 0, 0))
body_1.AddVisualShape(visualization_shape1)

# Collision material 
mat_1 = chrono.ChMaterialSurfaceNSC()

# Collision shapes 
body_1.GetCollisionModel().ClearModel()

# Triangle mesh collision shape 
body_1_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_1_1_collision.obj', False, True) 
mr = chrono.ChMatrix33D()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_1_1_collision_mesh.Transform(chrono.ChVectorD(0, 0, 0), mr) 
body_1.GetCollisionModel().AddTriangleMesh(mat_1, body_1_1_collision_mesh, False, False, chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(chrono.ChQuaternionD(1,0,0,0)), sphereswept_r) 
body_1.GetCollisionModel().BuildModel()
body_1.SetCollide(True)

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Propeller.step-1')
body_2.SetPos(chrono.ChVectorD(0.202466406708586,0.0308700000000001,0.134834820978301))
body_2.SetRot(chrono.ChQuaternionD(1,0,0,0))
# body_2.SetMass(0.00598816719490141)
# body_2.SetInertiaXX(chrono.ChVectorD(5.32193366608095e-07,1.2644169847229e-05,1.21650159081775e-05))
# body_2.SetInertiaXY(chrono.ChVectorD(1.08640420006801e-15,2.13259531518346e-06,-9.23542300019621e-16))
body_2.SetMass(1e-12) # Modified by Xavier, the original is in the lines above
body_2.SetInertiaXX(chrono.ChVectorD(1e-12,1e-12,1e-12)) # Modified by Xavier, the original is in the lines above
body_2.SetInertiaXY(chrono.ChVectorD(0,0,0)) # Modified by Xavier, the original is in the lines above
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.2968384063405e-10,-0.00221503418857244,9.95629894039621e-11),chrono.ChQuaternionD(1,0,0,0)))

# # Visualization shape 
# body_2_1_shape = chrono.ChObjFileShape() 
# body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
# body_2.AddVisualShape(body_2_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))

# Attach a visualization shape
# First load a .obj from disk into a ChTriangleMeshConnected:
mesh_for_visualization2 = chrono.ChTriangleMeshConnected()
mesh_for_visualization2.LoadWavefrontMesh(shapes_dir +'body_2_1.obj')
# Now the  triangle mesh is inserted in a ChTriangleMeshShape visualization asset, 
# and added to the body
visualization_shape2 = chrono.ChTriangleMeshShape()
visualization_shape2.SetMesh(mesh_for_visualization2)
# visualization_shape1.SetWireframe(True)
visualization_shape2.SetColor(chrono.ChColor(0, 1, 0))
body_2.AddVisualShape(visualization_shape2)

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Propeller.step-2')
body_3.SetPos(chrono.ChVectorD(-0.202453244853185,0.0308700000000001,0.134834820978301))
body_3.SetRot(chrono.ChQuaternionD(1,0,0,0))
# body_3.SetMass(0.00598816719490141)
# body_3.SetInertiaXX(chrono.ChVectorD(5.32193366608095e-07,1.2644169847229e-05,1.21650159081775e-05))
# body_3.SetInertiaXY(chrono.ChVectorD(1.08640420006801e-15,2.13259531518346e-06,-9.23542300019621e-16))
body_3.SetMass(1e-12) # Modified by Xavier, the original is in the lines above
body_3.SetInertiaXX(chrono.ChVectorD(1e-12,1e-12,1e-12)) # Modified by Xavier, the original is in the lines above
body_3.SetInertiaXY(chrono.ChVectorD(0,0,0)) # Modified by Xavier, the original is in the lines above
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.2968384063405e-10,-0.00221503418857244,9.95629894039621e-11),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
# body_2_1_shape = chrono.ChObjFileShape() 
# body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
# body_3.AddVisualShape(body_2_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))

body_3.AddVisualShape(visualization_shape2)

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Propeller.step-3')
body_4.SetPos(chrono.ChVectorD(-0.202453244853185,0.0308700000000001,-0.134324908014187))
body_4.SetRot(chrono.ChQuaternionD(1,0,0,0))
# body_4.SetMass(0.00598816719490141)
# body_4.SetInertiaXX(chrono.ChVectorD(5.32193366608095e-07,1.2644169847229e-05,1.21650159081775e-05))
# body_4.SetInertiaXY(chrono.ChVectorD(1.08640420006801e-15,2.13259531518346e-06,-9.23542300019621e-16))
body_4.SetMass(1e-12) # Modified by Xavier, the original is in the lines above
body_4.SetInertiaXX(chrono.ChVectorD(1e-12,1e-12,1e-12)) # Modified by Xavier, the original is in the lines above
body_4.SetInertiaXY(chrono.ChVectorD(0,0,0)) # Modified by Xavier, the original is in the lines above
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.2968384063405e-10,-0.00221503418857244,9.95629894039621e-11),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
# body_2_1_shape = chrono.ChObjFileShape() 
# body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
# body_4.AddVisualShape(body_2_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))

body_4.AddVisualShape(visualization_shape2)

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('Propeller.step-4')
body_5.SetPos(chrono.ChVectorD(0.202466406708586,0.0308700000000001,-0.134324908014187))
body_5.SetRot(chrono.ChQuaternionD(1,0,0,0))
# body_5.SetMass(0.00598816719490141)
# body_5.SetInertiaXX(chrono.ChVectorD(5.32193366608095e-07,1.2644169847229e-05,1.21650159081775e-05))
# body_5.SetInertiaXY(chrono.ChVectorD(1.08640420006801e-15,2.13259531518346e-06,-9.23542300019621e-16))
body_5.SetMass(1e-12) # Modified by Xavier, the original is in the lines above
body_5.SetInertiaXX(chrono.ChVectorD(1e-12,1e-12,1e-12)) # Modified by Xavier, the original is in the lines above
body_5.SetInertiaXY(chrono.ChVectorD(0,0,0)) # Modified by Xavier, the original is in the lines above
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.2968384063405e-10,-0.00221503418857244,9.95629894039621e-11),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
# body_2_1_shape = chrono.ChObjFileShape() 
# body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
# body_5.AddVisualShape(body_2_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))

body_5.AddVisualShape(visualization_shape2)

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('UAV_body-1')
body_6.SetPos(chrono.ChVectorD(0,0,0))
body_6.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_6.SetMass(14.5630237498979)
body_6.SetInertiaXX(chrono.ChVectorD(0.110866327214873,0.278989170666085,0.211714416089775))
body_6.SetInertiaXY(chrono.ChVectorD(-8.25507590738186e-06,-1.39380405417335e-05,-6.17436142134492e-06))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.000282253166443781,-0.0252566607780662,0.000264109795016584),chrono.ChQuaternionD(1,0,0,0)))
body_6.SetBodyFixed(True)

# Visualization shape 
body_6_1_shape = chrono.ChObjFileShape() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6.AddVisualShape(body_6_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))

# Collision material 
mat_6 = chrono.ChMaterialSurfaceNSC()

# Collision shapes 
body_6.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=-1; mr[1,0]=-4.66480262447545E-17; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=-1.38087440873776E-16; mr[2,1]=1 
mr[0,2]=-4.66480262447545E-17; mr[1,2]=1; mr[2,2]=1.38087440873776E-16 
body_6.GetCollisionModel().AddBox(mat_6, 0.14875,0.1005,0.034,chrono.ChVectorD(6.58092770186422E-06,-0.07513,0.000254956482058177),mr)
mr = chrono.ChMatrix33D()
mr[0,0]=0; mr[1,0]=-9.25185853854297E-17; mr[2,0]=1 
mr[0,1]=1; mr[1,1]=3.19029604777344E-17; mr[2,1]=0 
mr[0,2]=-3.19029604777344E-17; mr[1,2]=1; mr[2,2]=9.25185853854297E-17 
body_6.GetCollisionModel().AddBox(mat_6, 0.15,0.2175,0.0375,chrono.ChVectorD(6.58092770050458E-06,-0.00362999999999999,0.000254956482056898),mr)
body_6.GetCollisionModel().BuildModel()
body_6.SetCollide(True)

exported_items.append(body_6)




# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Propeller.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.202466406708586,0.0234432222152569,0.134834820978301)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0.202466406708586,0.03387,0.134834820978301)
dB = chrono.ChVectorD(-4.41406746732548e-18,-1,-9.38975150022512e-17)
link_1.SetFlipped(True)
link_1.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_1.SetName("Concentric6")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.202466406708586,0.0234432222152569,0.134834820978301)
cB = chrono.ChVectorD(0.202466406708586,0.03387,0.134834820978301)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(-4.41406746732548e-18,-1,-9.38975150022512e-17)
link_2.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_2.SetName("Concentric6")
exported_items.append(link_2)


# Mate constraint: Coincident31 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Propeller.step-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.202466406708586,0.02387,0.134834820978301)
cB = chrono.ChVectorD(0.202466406708586,0.02387,0.134834820978301)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,9.54097911787244e-17)
link_3.Initialize(body_2,body_6,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident31")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.202466406708586,0.02387,0.134834820978301)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(0.202466406708586,0.02387,0.134834820978301)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,9.54097911787244e-17)
link_4.SetFlipped(True)
link_4.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_4.SetName("Coincident31")
exported_items.append(link_4)


# Mate constraint: Concentric7 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: Propeller.step-4 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.202466406708586,0.0234432222152569,-0.134324908014187)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0.202466406708586,0.03387,-0.134324908014187)
dB = chrono.ChVectorD(-4.41406746732548e-18,-1,-9.38975150022512e-17)
link_5.SetFlipped(True)
link_5.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_5.SetName("Concentric7")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.202466406708586,0.0234432222152569,-0.134324908014187)
cB = chrono.ChVectorD(0.202466406708586,0.03387,-0.134324908014187)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(-4.41406746732548e-18,-1,-9.38975150022512e-17)
link_6.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_6.SetName("Concentric7")
exported_items.append(link_6)


# Mate constraint: Coincident32 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: Propeller.step-4 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.202466406708586,0.02387,-0.134324908014187)
cB = chrono.ChVectorD(0.202466406708586,0.02387,-0.134324908014187)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,9.54097911787244e-17)
link_7.Initialize(body_5,body_6,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident32")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.202466406708586,0.02387,-0.134324908014187)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(0.202466406708586,0.02387,-0.134324908014187)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,9.54097911787244e-17)
link_8.SetFlipped(True)
link_8.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_8.SetName("Coincident32")
exported_items.append(link_8)


# Mate constraint: Concentric8 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: Propeller.step-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.202453244853185,0.0234432222152569,-0.134324908014187)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(-0.202453244853185,0.03387,-0.134324908014187)
dB = chrono.ChVectorD(-4.41406746732548e-18,-1,-9.38975150022512e-17)
link_9.SetFlipped(True)
link_9.Initialize(body_4,body_6,False,cA,cB,dA,dB)
link_9.SetName("Concentric8")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.202453244853185,0.0234432222152569,-0.134324908014187)
cB = chrono.ChVectorD(-0.202453244853185,0.03387,-0.134324908014187)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(-4.41406746732548e-18,-1,-9.38975150022512e-17)
link_10.Initialize(body_4,body_6,False,cA,cB,dA,dB)
link_10.SetName("Concentric8")
exported_items.append(link_10)


# Mate constraint: Coincident33 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: Propeller.step-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.202453244853185,0.02387,-0.134324908014187)
cB = chrono.ChVectorD(-0.202453244853185,0.02387,-0.134324908014187)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,9.54097911787244e-17)
link_11.Initialize(body_4,body_6,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident33")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.202453244853185,0.02387,-0.134324908014187)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(-0.202453244853185,0.02387,-0.134324908014187)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,9.54097911787244e-17)
link_12.SetFlipped(True)
link_12.Initialize(body_4,body_6,False,cA,cB,dA,dB)
link_12.SetName("Coincident33")
exported_items.append(link_12)


# Mate constraint: Concentric9 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Propeller.step-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.202453244853185,0.0234432222152569,0.134834820978301)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(-0.202453244853185,0.03387,0.134834820978301)
dB = chrono.ChVectorD(-4.41406746732548e-18,-1,-9.38975150022512e-17)
link_13.SetFlipped(True)
link_13.Initialize(body_3,body_6,False,cA,cB,dA,dB)
link_13.SetName("Concentric9")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.202453244853185,0.0234432222152569,0.134834820978301)
cB = chrono.ChVectorD(-0.202453244853185,0.03387,0.134834820978301)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(-4.41406746732548e-18,-1,-9.38975150022512e-17)
link_14.Initialize(body_3,body_6,False,cA,cB,dA,dB)
link_14.SetName("Concentric9")
exported_items.append(link_14)


# Mate constraint: Coincident34 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Propeller.step-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.202453244853185,0.02387,0.134834820978301)
cB = chrono.ChVectorD(-0.202453244853185,0.02387,0.134834820978301)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,9.54097911787244e-17)
link_15.Initialize(body_3,body_6,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident34")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.202453244853185,0.02387,0.134834820978301)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(-0.202453244853185,0.02387,0.134834820978301)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,9.54097911787244e-17)
link_16.SetFlipped(True)
link_16.Initialize(body_3,body_6,False,cA,cB,dA,dB)
link_16.SetName("Coincident34")
exported_items.append(link_16)


# Mate constraint: Coincident35 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Box_200x200x100-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:4 (4)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,-0.20913,-3.47590732374625e-15)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,1)
link_17.Initialize(body_1,body_6,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Coincident35")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,-0.20913,-3.47590732374625e-15)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_18.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_18.SetName("Coincident35")
exported_items.append(link_18)


# Mate constraint: Coincident37 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Box_200x200x100-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,-0.10913,-3.47590732374625e-15)
cB = chrono.ChVectorD(3.12871797220931e-18,-0.10913,-1.0550916138563e-17)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(2.33240131223772e-17,-1,-1.03565580655332e-16)
link_19.Initialize(body_1,body_6,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident37")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,-0.10913,-3.47590732374625e-15)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(3.12871797220931e-18,-0.10913,-1.0550916138563e-17)
dB = chrono.ChVectorD(2.33240131223772e-17,-1,-1.03565580655332e-16)
link_20.SetFlipped(True)
link_20.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_20.SetName("Coincident37")
exported_items.append(link_20)


# Mate constraint: Coincident38 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Box_200x200x100-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:4 (4)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,-0.20913,-3.47590732374625e-15)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_21.Initialize(body_1,body_6,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Coincident38")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,-0.20913,-3.47590732374625e-15)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_22.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_22.SetName("Coincident38")
exported_items.append(link_22)


# Mate constraint: Coincident39 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name:  , SW name: Assem2 ,  SW ref.type:4 (4)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_23.Initialize(body_6,body_0,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Coincident39")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_24.Initialize(body_6,body_0,False,cA,cB,dA,dB)
link_24.SetName("Coincident39")
exported_items.append(link_24)


# Mate constraint: Coincident40 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name:  , SW name: Assem2 ,  SW ref.type:4 (4)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,1)
link_25.Initialize(body_6,body_0,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Coincident40")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_26.Initialize(body_6,body_0,False,cA,cB,dA,dB)
link_26.SetName("Coincident40")
exported_items.append(link_26)


# Mate constraint: Coincident43 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_body-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name:  , SW name: Assem2 ,  SW ref.type:4 (4)

link_27 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_27.Initialize(body_6,body_0,False,cA,cB,dB)
link_27.SetDistance(0)
link_27.SetName("Coincident43")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,1,0)
link_28.Initialize(body_6,body_0,False,cA,cB,dA,dB)
link_28.SetName("Coincident43")
exported_items.append(link_28)


# Auxiliary marker (coordinate system feature)
marker_0_1 =chrono.ChMarker()
marker_0_1.SetName('Coordinate System1')
body_0.AddMarker(marker_0_1)
marker_0_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.202466406708586,0.03387,0.134834820978301),chrono.ChQuaternionD(0.707106781186546,-0.707106781186549,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_2 =chrono.ChMarker()
marker_0_2.SetName('Coordinate System2')
body_0.AddMarker(marker_0_2)
marker_0_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.202453244853185,0.03387,0.134834820978301),chrono.ChQuaternionD(0.707106781186546,-0.707106781186549,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_3 =chrono.ChMarker()
marker_0_3.SetName('Coordinate System3')
body_0.AddMarker(marker_0_3)
marker_0_3.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.202453244853185,0.03387,-0.134324908014187),chrono.ChQuaternionD(0.707106781186546,-0.707106781186549,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_4 =chrono.ChMarker()
marker_0_4.SetName('Coordinate System4')
body_0.AddMarker(marker_0_4)
marker_0_4.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.202466406708586,0.03387,-0.134324908014187),chrono.ChQuaternionD(0.707106781186546,-0.707106781186549,0,0)))
