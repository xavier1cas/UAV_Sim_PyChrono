import pychrono as chrono
import builtins

# Some global settings
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'shapes/'

if hasattr(builtins, 'exported_system_relpath'):
    shapes_dir = builtins.exported_system_relpath + shapes_dir

exported_items = []

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('Total_Body_sub-1')
body_1.SetPos(chrono.ChVector3d(0.0,0.0,0.0))
body_1.SetRot(chrono.ChQuaterniond(1.0,0.0,0.0,0.0))
body_1.SetMass(1.6192098341509984)
body_1.SetInertiaXX(chrono.ChVector3d(0.012250488040487789,0.011707272348066677,0.011726460980231598))
body_1.SetInertiaXY(chrono.ChVector3d(-0.0006349503545381315,8.416911654144232e-07,3.3865411371690895e-06))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(0.00782071598512143,-0.01850977113682776,-4.94191891404891e-05),chrono.ChQuaterniond(0,0,1,0)))

body_1_1_shape = chrono.ChVisualShapeModelFile()
body_1_1_shape.SetFilename(shapes_dir +'Total_Body_sub.obj')
body_1_1_shape.SetColor(chrono.ChColor(0.1, 0.1, 0.1))
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model
body_1.AddCollisionModel(chrono.ChCollisionModel())

# Collision material
mat_1 = chrono.ChContactMaterialNSC()
mr = chrono.ChMatrix33d()
mr[0,0]=1.0; mr[0,1]=0.0; mr[0,2]=0.0; 
mr[1,0]=0.0; mr[1,1]=6.123233995736766e-17; mr[1,2]=1.0; 
mr[2,0]=0.0; mr[2,1]=-1.0; mr[2,2]=6.123233995736766e-17; 
collshape = chrono.ChCollisionShapeBox(mat_1,0.23145987416302546,0.24489553447165766,0.09475000010000002)
body_1.GetCollisionModel().AddShape(collshape,chrono.ChFramed(chrono.ChVector3d(0.00727006291848727,0.014875000050000009,9.108310599274614e-19), mr))

mr = chrono.ChMatrix33d()
mr[0,0]=1.0; mr[0,1]=0.0; mr[0,2]=0.0; 
mr[1,0]=0.0; mr[1,1]=6.123233995736766e-17; mr[1,2]=1.0; 
mr[2,0]=0.0; mr[2,1]=-1.0; mr[2,2]=6.123233995736766e-17; 
collshape = chrono.ChCollisionShapeBox(mat_1,0.2450000000000001,0.37324312395177706,0.016)
body_1.GetCollisionModel().AddShape(collshape,chrono.ChFramed(chrono.ChVector3d(0.0,-0.23514,-1.439817241757543e-17), mr))

body_1.EnableCollision(True)

exported_items.append(body_1)

# Rigid body part
body_7 = chrono.ChBodyAuxRef()
body_7.SetName('box_big_200x200x100-1')
body_7.SetPos(chrono.ChVector3d(0,-215.5e-3,0))
body_7.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_7.SetMass(0.356678398800002)
body_7.SetInertiaXX(chrono.ChVector3d(0.00230806584511846,0.00384657830287282,0.00230806584511845))
body_7.SetInertiaXY(chrono.ChVector3d(5.36017556566241e-19,3.00555792072242e-19,-1.57466153292409e-18))
body_7.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-1.46498601287635e-16,0.0343231818337972,1.96114607702853e-17),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 

# mesh_for_visualization_3 = chrono.ChTriangleMeshConnected()
# mesh_for_visualization_3.LoadWavefrontMesh(shapes_dir + 'body_7_1.obj')
# visualization_shape_3 = chrono.ChVisualShapeTriangleMesh()
# visualization_shape_3.SetMesh(mesh_for_visualization_3)
# visualization_shape_3.SetWireframe(True)
# body_7.AddVisualShape(visualization_shape_3)

body_7_1_shape = chrono.ChVisualShapeModelFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_shape.SetOpacity(0.3)
body_7.AddVisualShape(body_7_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_7.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_7 = chrono.ChContactMaterialNSC()
mat_7.SetRollingFriction(0.01) # 0.01
mat_7.SetSpinningFriction(0.01) # 0.01
# Create a triangle mesh collision shape
mesh_for_collision = chrono.ChTriangleMeshConnected()
mesh_for_collision.LoadWavefrontMesh(shapes_dir + 'body_7_1.obj')
triangle_shape = chrono.ChCollisionShapeTriangleMesh(
    mat_7,                   # contact material
    mesh_for_collision,      # the mesh
    False,                   # is it static?
    False)                   # is it convex?
body_7.GetCollisionModel().AddShape(triangle_shape)
body_7.EnableCollision(True)

exported_items.append(body_7)



# Mate constraint: Coincident29 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: drone_big_box-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: box_big_200x200x100-1 ,  SW ref.type:2 (2)
link_17 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.0949999999999987,-0.225500000000002,0.179999999999999)
cB = chrono.ChVector3d(-1.31722055646533e-43,-0.225500000000002,-1.00893489431387e-43)
dA = chrono.ChVector3d(0,1,0)
dB = chrono.ChVector3d(0,-1,0)
link_17.Initialize(body_1,body_7,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Coincident29")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.0949999999999987,-0.225500000000002,0.179999999999999)
cB = chrono.ChVector3d(-1.31722055646533e-43,-0.225500000000002,-1.00893489431387e-43)
dA = chrono.ChVector3d(0,1,0)
dB = chrono.ChVector3d(0,-1,0)
link_18.SetFlipped(True)
link_18.Initialize(body_1,body_7,False,cA,cB,dA,dB)
link_18.SetName("Coincident29")
exported_items.append(link_18)


# Mate constraint: Coincident30 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_0 , SW name: drone_big_box-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_0 , SW name: box_big_200x200x100-1 ,  SW ref.type:4 (4)
link_19 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0,0,0)
cB = chrono.ChVector3d(-1.31722055646533e-43,-0.225500000000002,-1.00893489431387e-43)
dA = chrono.ChVector3d(-6.98296267768627e-15,0,-1)
dB = chrono.ChVector3d(0,0,1)
link_19.Initialize(body_1,body_7,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident30")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0,0,0)
cB = chrono.ChVector3d(-1.31722055646533e-43,-0.225500000000002,-1.00893489431387e-43)
dA = chrono.ChVector3d(-6.98296267768627e-15,0,-1)
dB = chrono.ChVector3d(0,0,1)
link_20.SetFlipped(True)
link_20.Initialize(body_1,body_7,False,cA,cB,dA,dB)
link_20.SetName("Coincident30")
exported_items.append(link_20)


# Mate constraint: Coincident31 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_0 , SW name: drone_big_box-1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_0 , SW name: box_big_200x200x100-1 ,  SW ref.type:4 (4)
link_21 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0,0,0)
cB = chrono.ChVector3d(-1.31722055646533e-43,-0.225500000000002,-1.00893489431387e-43)
dA = chrono.ChVector3d(-1,0,6.98296267768627e-15)
dB = chrono.ChVector3d(1,0,0)
link_21.Initialize(body_1,body_7,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Coincident31")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0,0,0)
cB = chrono.ChVector3d(-1.31722055646533e-43,-0.225500000000002,-1.00893489431387e-43)
dA = chrono.ChVector3d(-1,0,6.98296267768627e-15)
dB = chrono.ChVector3d(1,0,0)
link_22.SetFlipped(True)
link_22.Initialize(body_1,body_7,False,cA,cB,dA,dB)
link_22.SetName("Coincident31")
exported_items.append(link_22)


# Auxiliary marker (coordinate system feature)
marker_0_1 = chrono.ChMarker()
marker_0_1.SetName('Coordinate System1')
body_0.AddMarker(marker_0_1)
marker_0_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.0878554539951735,0.0430000000000000034,-0.10844776723582883),chrono.ChQuaterniond(0.707106781186545,-0.70710678118655,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_2 = chrono.ChMarker()
marker_0_2.SetName('Coordinate System2')
body_0.AddMarker(marker_0_2)
marker_0_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.0878554539951735,0.0430000000000000034,-0.10844776723582883),chrono.ChQuaterniond(0.707106781186545,-0.70710678118655,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_3 = chrono.ChMarker()
marker_0_3.SetName('Coordinate System3')
body_0.AddMarker(marker_0_3)
marker_0_3.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.0878554539951735,0.0430000000000000037,0.1084477672358288),chrono.ChQuaterniond(0.707106781186545,-0.70710678118655,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_4 = chrono.ChMarker()
marker_0_4.SetName('Coordinate System4')
body_0.AddMarker(marker_0_4)
marker_0_4.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.0878554539951735,0.0430000000000000034,0.10844776723582879),chrono.ChQuaterniond(0.707106781186545,-0.70710678118655,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_5 = chrono.ChMarker()
marker_0_5.SetName('Coordinate System5')
body_0.AddMarker(marker_0_5)
marker_0_5.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.08785545399517357,-0.029999999999999995,-0.1084477672358288),chrono.ChQuaterniond(0.707106781186545,-0.70710678118655,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_6 = chrono.ChMarker()
marker_0_6.SetName('Coordinate System6')
body_0.AddMarker(marker_0_6)
marker_0_6.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.08785545399517357,-0.029999999999999995,-0.1084477672358288),chrono.ChQuaterniond(0.707106781186545,-0.70710678118655,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_7 = chrono.ChMarker()
marker_0_7.SetName('Coordinate System7')
body_0.AddMarker(marker_0_7)
marker_0_7.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.08785545399517354,-0.029999999999999995,0.10844776723582883),chrono.ChQuaterniond(0.707106781186545,-0.70710678118655,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_8 = chrono.ChMarker()
marker_0_8.SetName('Coordinate System8')
body_0.AddMarker(marker_0_8)
marker_0_8.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.08785545399517354,-0.029999999999999995,0.10844776723582883),chrono.ChQuaterniond(0.707106781186545,-0.70710678118655,0,0)))
