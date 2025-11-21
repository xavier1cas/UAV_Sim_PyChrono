# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: D:\Virginia-Tech-PhD\PHD_research\PyChrono\UAV_CAD_Models\Q4\PyChronoAssembly\UAV_Assembly_pychrono.SLDASM


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
body_1.SetName('Propeller-2')
body_1.SetPos(chrono.ChVectorD(-0.202459825780886,0.0273700000000012,0.134579864496243))
body_1.SetRot(chrono.ChQuaternionD(0.707106781186545,-0.70710678118655,-1.32308232789105e-16,-6.10015203643817e-17))
# body_1.SetMass(0.00541929141423071)
# body_1.SetInertiaXX(chrono.ChVectorD(4.81635001652512e-07,1.1442973805553e-05,1.1009339485845e-05))
# body_1.SetInertiaXY(chrono.ChVectorD(-1.20189792658221e-15,-1.92999877761758e-06,3.97142243513157e-16))
body_1.SetMass(1e-12) # Modified by Xavier, the original is in the lines above
body_1.SetInertiaXX(chrono.ChVectorD(1e-12,1e-12,1e-12)) # Modified by Xavier, the original is in the lines above
body_1.SetInertiaXY(chrono.ChVectorD(0,0,0)) # Modified by Xavier, the original is in the lines above
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.91230583801852e-11,5.61998649220364e-12,0.00128496582935105),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
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
visualization_shape1.SetColor(chrono.ChColor(0, 1, 0))
body_1.AddVisualShape(visualization_shape1)

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Propeller-4')
body_2.SetPos(chrono.ChVectorD(0.202459825780885,0.02737,-0.134579864496244))
body_2.SetRot(chrono.ChQuaternionD(0.707106781186545,-0.70710678118655,-1.32308232789105e-16,-6.10015203643817e-17))
# body_2.SetMass(0.00541929141423071)
# body_2.SetInertiaXX(chrono.ChVectorD(4.81635001652512e-07,1.1442973805553e-05,1.1009339485845e-05))
# body_2.SetInertiaXY(chrono.ChVectorD(-1.20189792658221e-15,-1.92999877761758e-06,3.97142243513157e-16))
body_2.SetMass(1e-12) # Modified by Xavier, the original is in the lines above
body_2.SetInertiaXX(chrono.ChVectorD(1e-12,1e-12,1e-12)) # Modified by Xavier, the original is in the lines above
body_2.SetInertiaXY(chrono.ChVectorD(0,0,0)) # Modified by Xavier, the original is in the lines above
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.91230583801852e-11,5.61998649220364e-12,0.00128496582935105),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
# body_1_1_shape = chrono.ChObjFileShape() 
# body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
# body_2.AddVisualShape(body_1_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))
body_2.AddVisualShape(visualization_shape1)

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Propeller-1')
body_3.SetPos(chrono.ChVectorD(0.202459825780885,0.0273700000000012,0.134579864496244))
body_3.SetRot(chrono.ChQuaternionD(0.707106781186545,-0.70710678118655,-1.32308232789105e-16,-6.10015203643817e-17))
# body_3.SetMass(0.00541929141423071)
# body_3.SetInertiaXX(chrono.ChVectorD(4.81635001652512e-07,1.1442973805553e-05,1.1009339485845e-05))
# body_3.SetInertiaXY(chrono.ChVectorD(-1.20189792658221e-15,-1.92999877761758e-06,3.97142243513157e-16))
body_3.SetMass(1e-12) # Modified by Xavier, the original is in the lines above
body_3.SetInertiaXX(chrono.ChVectorD(1e-12,1e-12,1e-12)) # Modified by Xavier, the original is in the lines above
body_3.SetInertiaXY(chrono.ChVectorD(0,0,0)) # Modified by Xavier, the original is in the lines above
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.91230583801852e-11,5.61998649220364e-12,0.00128496582935105),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
# body_1_1_shape = chrono.ChObjFileShape() 
# body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
# body_3.AddVisualShape(body_1_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))
body_3.AddVisualShape(visualization_shape1)

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Propeller-3')
body_4.SetPos(chrono.ChVectorD(-0.202459825780886,0.0273699999999999,-0.134579864496245))
body_4.SetRot(chrono.ChQuaternionD(0.706959700526014,-0.706959700526019,0.0144215752317702,0.0144215752317702))
# body_4.SetMass(0.00541929141423071)
# body_4.SetInertiaXX(chrono.ChVectorD(4.99865489797599e-07,1.14247433174079e-05,1.1009339485845e-05))
# body_4.SetInertiaXY(chrono.ChVectorD(4.46652220884193e-07,-1.92839315887399e-06,7.87089982995217e-08))
body_4.SetMass(1e-12) # Modified by Xavier, the original is in the lines above
body_4.SetInertiaXX(chrono.ChVectorD(1e-12,1e-12,1e-12)) # Modified by Xavier, the original is in the lines above
body_4.SetInertiaXY(chrono.ChVectorD(0,0,0)) # Modified by Xavier, the original is in the lines above
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.91230583801852e-11,5.61998649220364e-12,0.00128496582935105),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
# body_1_1_shape = chrono.ChObjFileShape() 
# body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
# body_4.AddVisualShape(body_1_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))
body_4.AddVisualShape(visualization_shape1)

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('Box_200x200x100-1')
body_5.SetPos(chrono.ChVectorD(-2.55871712706579e-17,-0.2088,2.19008838842072e-17))
body_5.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_5.SetMass(0.356294160000001)
body_5.SetInertiaXX(chrono.ChVectorD(0.00230557943592284,0.00384243450096,0.00230557943592284))
body_5.SetInertiaXY(chrono.ChVectorD(0,0,-4.72485565890289e-20))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0,0.0343231818337971,0),chrono.ChQuaternionD(1,0,0,0)))

# # Visualization shape 
# body_5_1_shape = chrono.ChObjFileShape() 
# body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
# body_5.AddVisualShape(body_5_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))

# Attach a visualization shape
# First load a .obj from disk into a ChTriangleMeshConnected:
mesh_for_visualization5 = chrono.ChTriangleMeshConnected()
mesh_for_visualization5.LoadWavefrontMesh(shapes_dir +'body_5_1.obj')
# Now the  triangle mesh is inserted in a ChTriangleMeshShape visualization asset, 
# and added to the body
visualization_shape5 = chrono.ChTriangleMeshShape()
visualization_shape5.SetMesh(mesh_for_visualization5)
# visualization_shape5.SetWireframe(True)
visualization_shape5.SetColor(chrono.ChColor(0.1, 0.1, 0.1))
body_5.AddVisualShape(visualization_shape5)

# Collision material 
mat_5 = chrono.ChMaterialSurfaceNSC()

# Collision shapes 
body_5.GetCollisionModel().ClearModel()

# Triangle mesh collision shape 
body_5_1_collision_mesh = chrono.ChTriangleMeshConnected.CreateFromWavefrontFile(shapes_dir + 'body_5_1_collision.obj', False, True) 
mr = chrono.ChMatrix33D()
mr[0,0]=1; mr[1,0]=0; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=1 
body_5_1_collision_mesh.Transform(chrono.ChVectorD(0, 0, 0), mr) 
body_5.GetCollisionModel().AddTriangleMesh(mat_5, body_5_1_collision_mesh, False, False, chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(chrono.ChQuaternionD(1,0,0,0)), sphereswept_r) 
body_5.GetCollisionModel().BuildModel()
body_5.SetCollide(True)

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('UAV_Assembly_part_single-1')
body_6.SetPos(chrono.ChVectorD(0,0,0))
body_6.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_6.SetMass(0.725155689894245)
body_6.SetInertiaXX(chrono.ChVectorD(0.00281476025893015,0.00776849449509212,0.00662126607982517))
body_6.SetInertiaXY(chrono.ChVectorD(-3.01324974056602e-05,-9.38857838027414e-06,-4.4113720829106e-06))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.00412025498024158,-0.0378957456822676,-0.000167739309237873),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjFileShape() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6.AddVisualShape(body_6_1_shape, chrono.ChFrameD(chrono.ChVectorD(0,0,0), chrono.ChQuaternionD(1,0,0,0)))

# # Attach a visualization shape
# # First load a .obj from disk into a ChTriangleMeshConnected:
# mesh_for_visualization6 = chrono.ChTriangleMeshConnected()
# mesh_for_visualization6.LoadWavefrontMesh(shapes_dir +'body_6_1.obj')
# # Now the  triangle mesh is inserted in a ChTriangleMeshShape visualization asset, 
# # and added to the body
# visualization_shape6 = chrono.ChTriangleMeshShape()
# visualization_shape6.SetMesh(mesh_for_visualization6)
# # visualization_shape6.SetWireframe(True)
# visualization_shape6.SetColor(chrono.ChColor(0.1, 0.1, 0.1))
# body_6.AddVisualShape(visualization_shape6)


# Collision material 
mat_6 = chrono.ChMaterialSurfaceNSC()

# Collision shapes 
body_6.GetCollisionModel().ClearModel()
mr = chrono.ChMatrix33D()
mr[0,0]=-1; mr[1,0]=-3.19029604777344E-17; mr[2,0]=-1.27611841910938E-16 
mr[0,1]=-9.25185853854297E-17; mr[1,1]=3.33066907387547E-15; mr[2,1]=1 
mr[0,2]=-3.1902960477734E-17; mr[1,2]=1; mr[2,2]=-3.33066907387547E-15 
body_6.GetCollisionModel().AddBox(mat_6, 0.2175,0.15,0.0355,chrono.ChVectorD(-4.05008083264838E-17,-0.00149999999999994,3.49720252756924E-17),mr)
mr = chrono.ChMatrix33D()
mr[0,0]=1; mr[1,0]=4.67265582754696E-17; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=-3.3831423014075E-15; mr[2,1]=-1 
mr[0,2]=-4.67265582754696E-17; mr[1,2]=1; mr[2,2]=-3.3831423014075E-15 
body_6.GetCollisionModel().AddBox(mat_6, 0.1485,0.1005,0.0359,chrono.ChVectorD(-2.94330590577183E-17,-0.0728999999999999,2.53245462190461E-16),mr)
body_6.GetCollisionModel().BuildModel()
body_6.SetCollide(True)

exported_items.append(body_6)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Propeller-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.202459825780886,0.0338700000000008,0.134579864496244)
dA = chrono.ChVectorD(1.87112097223968e-16,-1,3.22335161018178e-15)
cB = chrono.ChVectorD(0.202459825780885,0.023443222215258,0.134579864496244)
dB = chrono.ChVectorD(-1.87112097223969e-16,1,-3.22335161018178e-15)
link_1.SetFlipped(True)
link_1.Initialize(body_6,body_3,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.202459825780886,0.0338700000000008,0.134579864496244)
cB = chrono.ChVectorD(0.202459825780885,0.023443222215258,0.134579864496244)
dA = chrono.ChVectorD(1.87112097223968e-16,-1,3.22335161018178e-15)
dB = chrono.ChVectorD(-1.87112097223969e-16,1,-3.22335161018178e-15)
link_2.Initialize(body_6,body_3,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Propeller-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.202459825780886,0.0238700000000008,0.134579864496244)
cB = chrono.ChVectorD(0.202459825780885,0.0238700000000011,0.134579864496244)
dA = chrono.ChVectorD(-5.55111512312578e-17,1,-3.22953809397064e-15)
dB = chrono.ChVectorD(1.00842919799282e-16,-1,3.23856319376527e-15)
link_3.Initialize(body_6,body_3,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident5")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.202459825780886,0.0238700000000008,0.134579864496244)
dA = chrono.ChVectorD(-5.55111512312578e-17,1,-3.22953809397064e-15)
cB = chrono.ChVectorD(0.202459825780885,0.0238700000000011,0.134579864496244)
dB = chrono.ChVectorD(1.00842919799282e-16,-1,3.23856319376527e-15)
link_4.SetFlipped(True)
link_4.Initialize(body_6,body_3,False,cA,cB,dA,dB)
link_4.SetName("Coincident5")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Propeller-2 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.202459825780886,0.0338700000000007,0.134579864496244)
dA = chrono.ChVectorD(1.87112097223968e-16,-1,3.22335161018178e-15)
cB = chrono.ChVectorD(-0.202459825780886,0.023443222215258,0.134579864496243)
dB = chrono.ChVectorD(-1.87112097223969e-16,1,-3.22335161018178e-15)
link_5.SetFlipped(True)
link_5.Initialize(body_6,body_1,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.202459825780886,0.0338700000000007,0.134579864496244)
cB = chrono.ChVectorD(-0.202459825780886,0.023443222215258,0.134579864496243)
dA = chrono.ChVectorD(1.87112097223968e-16,-1,3.22335161018178e-15)
dB = chrono.ChVectorD(-1.87112097223969e-16,1,-3.22335161018178e-15)
link_6.Initialize(body_6,body_1,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Propeller-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.202459825780886,0.0238700000000007,0.134579864496244)
cB = chrono.ChVectorD(-0.202459825780886,0.0238700000000011,0.134579864496243)
dA = chrono.ChVectorD(-5.55111512312578e-17,1,-3.22953809397064e-15)
dB = chrono.ChVectorD(1.00842919799282e-16,-1,3.23856319376527e-15)
link_7.Initialize(body_6,body_1,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident6")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.202459825780886,0.0238700000000007,0.134579864496244)
dA = chrono.ChVectorD(-5.55111512312578e-17,1,-3.22953809397064e-15)
cB = chrono.ChVectorD(-0.202459825780886,0.0238700000000011,0.134579864496243)
dB = chrono.ChVectorD(1.00842919799282e-16,-1,3.23856319376527e-15)
link_8.SetFlipped(True)
link_8.Initialize(body_6,body_1,False,cA,cB,dA,dB)
link_8.SetName("Coincident6")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Propeller-3 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.202459825780886,0.0338699999999996,-0.134579864496244)
dA = chrono.ChVectorD(1.87112097223968e-16,-1,3.22335161018178e-15)
cB = chrono.ChVectorD(-0.202459825780885,0.0234432222152568,-0.134579864496244)
dB = chrono.ChVectorD(-1.8711209722397e-16,1,-3.22335161018176e-15)
link_9.SetFlipped(True)
link_9.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.202459825780886,0.0338699999999996,-0.134579864496244)
cB = chrono.ChVectorD(-0.202459825780885,0.0234432222152568,-0.134579864496244)
dA = chrono.ChVectorD(1.87112097223968e-16,-1,3.22335161018178e-15)
dB = chrono.ChVectorD(-1.8711209722397e-16,1,-3.22335161018176e-15)
link_10.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Propeller-4 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.202459825780886,0.0338699999999997,-0.134579864496244)
dA = chrono.ChVectorD(1.87112097223968e-16,-1,3.22335161018178e-15)
cB = chrono.ChVectorD(0.202459825780886,0.0234432222152568,-0.134579864496244)
dB = chrono.ChVectorD(-1.87112097223969e-16,1,-3.22335161018178e-15)
link_11.SetFlipped(True)
link_11.Initialize(body_6,body_2,False,cA,cB,dA,dB)
link_11.SetName("Concentric4")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.202459825780886,0.0338699999999997,-0.134579864496244)
cB = chrono.ChVectorD(0.202459825780886,0.0234432222152568,-0.134579864496244)
dA = chrono.ChVectorD(1.87112097223968e-16,-1,3.22335161018178e-15)
dB = chrono.ChVectorD(-1.87112097223969e-16,1,-3.22335161018178e-15)
link_12.Initialize(body_6,body_2,False,cA,cB,dA,dB)
link_12.SetName("Concentric4")
exported_items.append(link_12)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Propeller-4 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.202459825780886,0.0238699999999996,-0.134579864496244)
cB = chrono.ChVectorD(0.202459825780886,0.0238699999999999,-0.134579864496244)
dA = chrono.ChVectorD(-5.55111512312578e-17,1,-3.22953809397064e-15)
dB = chrono.ChVectorD(1.00842919799282e-16,-1,3.23856319376527e-15)
link_13.Initialize(body_6,body_2,False,cA,cB,dB)
link_13.SetDistance(0)
link_13.SetName("Coincident8")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.202459825780886,0.0238699999999996,-0.134579864496244)
dA = chrono.ChVectorD(-5.55111512312578e-17,1,-3.22953809397064e-15)
cB = chrono.ChVectorD(0.202459825780886,0.0238699999999999,-0.134579864496244)
dB = chrono.ChVectorD(1.00842919799282e-16,-1,3.23856319376527e-15)
link_14.SetFlipped(True)
link_14.Initialize(body_6,body_2,False,cA,cB,dA,dB)
link_14.SetName("Coincident8")
exported_items.append(link_14)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Propeller-3 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.202459825780886,0.0238699999999996,-0.134579864496244)
cB = chrono.ChVectorD(-0.202459825780885,0.0238699999999999,-0.134579864496244)
dA = chrono.ChVectorD(-5.55111512312578e-17,1,-3.22953809397064e-15)
dB = chrono.ChVectorD(1.01535046614456e-16,-1,3.24206875893968e-15)
link_15.Initialize(body_6,body_4,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident9")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.202459825780886,0.0238699999999996,-0.134579864496244)
dA = chrono.ChVectorD(-5.55111512312578e-17,1,-3.22953809397064e-15)
cB = chrono.ChVectorD(-0.202459825780885,0.0238699999999999,-0.134579864496244)
dB = chrono.ChVectorD(1.01535046614456e-16,-1,3.24206875893968e-15)
link_16.SetFlipped(True)
link_16.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_16.SetName("Coincident9")
exported_items.append(link_16)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Box_200x200x100-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(2.85729165729834e-18,-0.1088,3.62630214477719e-16)
cB = chrono.ChVectorD(-2.55871712706579e-17,-0.1088,2.19008838842072e-17)
dA = chrono.ChVectorD(2.33632791377348e-17,-1,3.34862044118906e-15)
dB = chrono.ChVectorD(0,1,0)
link_17.Initialize(body_6,body_5,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Coincident10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(2.85729165729834e-18,-0.1088,3.62630214477719e-16)
dA = chrono.ChVectorD(2.33632791377348e-17,-1,3.34862044118906e-15)
cB = chrono.ChVectorD(-2.55871712706579e-17,-0.1088,2.19008838842072e-17)
dB = chrono.ChVectorD(0,1,0)
link_18.SetFlipped(True)
link_18.Initialize(body_6,body_5,False,cA,cB,dA,dB)
link_18.SetName("Coincident10")
exported_items.append(link_18)


# Mate constraint: Distance1 [MateDistanceDim] type:5 align:0 flip:True
#   Entity 0: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Box_200x200x100-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.1485,-0.1088,0.1005)
cB = chrono.ChVectorD(-0.1,-0.1088,0.1)
dA = chrono.ChVectorD(-7.76816855591655e-32,3.32494788514936e-15,1)
dB = chrono.ChVectorD(0,0,1)
link_19.Initialize(body_6,body_5,False,cA,cB,dB)
link_19.SetDistance(0.0005)
link_19.SetName("Distance1")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.1485,-0.1088,0.1005)
dA = chrono.ChVectorD(-7.76816855591655e-32,3.32494788514936e-15,1)
cB = chrono.ChVectorD(-0.1,-0.1088,0.1)
dB = chrono.ChVectorD(0,0,1)
link_20.Initialize(body_6,body_5,False,cA,cB,dA,dB)
link_20.SetName("Distance1")
exported_items.append(link_20)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: Box_200x200x100-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: UAV_Assembly_part_single-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.1,-0.1088,0.1)
cB = chrono.ChVectorD(0.1485,-0.1088,0.1005)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,2.77555756156289e-17,-9.29428878634636e-32)
link_21.Initialize(body_5,body_6,False,cA,cB,dB)
link_21.SetDistance(-0.0485)
link_21.SetName("Distance3")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.1,-0.1088,0.1)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.1485,-0.1088,0.1005)
dB = chrono.ChVectorD(1,2.77555756156289e-17,-9.29428878634636e-32)
link_22.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_22.SetName("Distance3")
exported_items.append(link_22)


# Auxiliary marker (coordinate system feature)
marker_0_1 =chrono.ChMarker()
marker_0_1.SetName('Coordinate System1')
body_0.AddMarker(marker_0_1)
marker_0_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.202459825780885,0.0273700000000008,0.134579864496243),chrono.ChQuaternionD(0.707106781186546,0.707106781186549,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_2 =chrono.ChMarker()
marker_0_2.SetName('Coordinate System2')
body_0.AddMarker(marker_0_2)
marker_0_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.202459825780886,0.0273700000000008,0.134579864496243),chrono.ChQuaternionD(0.707106781186546,0.707106781186549,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_3 =chrono.ChMarker()
marker_0_3.SetName('Coordinate System3')
body_0.AddMarker(marker_0_3)
marker_0_3.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.202459825780886,0.0273699999999996,-0.134579864496244),chrono.ChQuaternionD(0.707106781186546,0.707106781186549,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_4 =chrono.ChMarker()
marker_0_4.SetName('Coordinate System4')
body_0.AddMarker(marker_0_4)
marker_0_4.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.202459825780885,0.0273699999999997,-0.134579864496244),chrono.ChQuaternionD(0.707106781186546,0.707106781186549,0,0)))
