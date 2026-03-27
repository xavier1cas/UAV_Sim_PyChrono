# PyChrono model automatically generated using Chrono::SolidWorks add-in
# Assembly: C:\Users\Luca\Downloads\Duy Ann's drone\Simplified Quadcopter\Full Assembly - Chrono Export Ready.SLDASM


import pychrono as chrono 
import builtins 

# Some global settings 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'QuadCopter_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0 = chrono.ChBodyAuxRef()
body_0.SetName('SLDW_GROUND')
body_0.SetFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1 = chrono.ChBodyAuxRef()
body_1.SetName('Drone without Propellers Reduced-1')
body_1.SetPos(chrono.ChVector3d(-0.0231698366600012,-0.0262602429219341,0.0494258119007119))
body_1.SetRot(chrono.ChQuaterniond(1,0,0,0))
body_1.SetMass(1.0429123913637)
body_1.SetInertiaXX(chrono.ChVector3d(0.004086594862673,0.006065073700399,0.00356507620399933))
body_1.SetInertiaXY(chrono.ChVector3d(-8.65500570940336e-07,4.0877004416229e-06,1.15603516033095e-05))
body_1.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(2.4741168574083e-05,-0.00409801756839977,-0.00149597132200055),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChVisualShapeModelFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

# Collision Model

body_1.AddCollisionModel(chrono.ChCollisionModel())

# Collision material 
mat_1 = chrono.ChContactMaterialNSC()
mr = chrono.ChMatrix33d()
mr[0,0]=1; mr[1,0]=-2.01644647513419E-08; mr[2,0]=0 
mr[0,1]=0; mr[1,1]=-1; mr[2,1]=0 
mr[0,2]=0; mr[1,2]=0; mr[2,2]=-1 
collshape = chrono.ChCollisionShapeBox(mat_1,0.265753701921236,0.133095441991417,0.230005914172354)
body_1.GetCollisionModel().AddShape(collshape,chrono.ChFramed(chrono.ChVector3d(-4.22642035258214E-09,0.00754771611314055,-0.00171129479013446), mr))
body_1.EnableCollision(True)

exported_items.append(body_1)



# Rigid body part
body_2 = chrono.ChBodyAuxRef()
body_2.SetName('Propeller CCW-1')
body_2.SetPos(chrono.ChVector3d(0.0875453596480283,0.00426475707806556,0.146328076660421))
body_2.SetRot(chrono.ChQuaterniond(0.809417880545532,1.41303371262534e-15,-0.587233083752251,-1.02515667673614e-15))
body_2.SetMass(0.00327419527181132)
body_2.SetInertiaXX(chrono.ChVector3d(1.05212304772093e-06,2.0805510195381e-06,1.05226174825666e-06))
body_2.SetInertiaXY(chrono.ChVector3d(5.30885592471638e-11,2.68970924289033e-10,4.26912762462803e-11))
body_2.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(7.3315602583064e-06,-0.0084495854885684,-7.75309113946039e-06),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_2)



# Rigid body part
body_3 = chrono.ChBodyAuxRef()
body_3.SetName('Propeller CW-2')
body_3.SetPos(chrono.ChVector3d(0.116644914904978,-0.00273524292193397,0.00581948251984933))
body_3.SetRot(chrono.ChQuaterniond(0.999285632094842,1.85882240111642e-15,-0.0377918706709853,-2.38672616109981e-17))
body_3.SetMass(0.00327626318826267)
body_3.SetInertiaXX(chrono.ChVector3d(1.0525637132744e-06,2.08159752619688e-06,1.05291394457523e-06))
body_3.SetInertiaXY(chrono.ChVector3d(-1.11777930680591e-11,1.05622308041431e-10,3.17919424989842e-12))
body_3.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0330369529154692,0.00139763186282363,-0.0509441435522752),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_3)



# Rigid body part
body_4 = chrono.ChBodyAuxRef()
body_4.SetName('Propeller CCW-2')
body_4.SetPos(chrono.ChVector3d(-0.133885032968031,0.00426475707806624,-0.0474764528589973))
body_4.SetRot(chrono.ChQuaterniond(0.600023804625506,1.04748595835581e-15,-0.799982145977479,-1.39656136704403e-15))
body_4.SetMass(0.00327419527181132)
body_4.SetInertiaXX(chrono.ChVector3d(1.0524177191718e-06,2.0805510195381e-06,1.05196707680578e-06))
body_4.SetInertiaXY(chrono.ChVector3d(6.79172689153183e-11,1.62435163221808e-10,5.30893337311602e-12))
body_4.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(7.3315602583064e-06,-0.0084495854885684,-7.75309113946039e-06),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChVisualShapeModelFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_4.AddVisualShape(body_2_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_4)



# Rigid body part
body_5 = chrono.ChBodyAuxRef()
body_5.SetName('Propeller CW-1')
body_5.SetPos(chrono.ChVector3d(-0.108482306059853,-0.00273524292193426,0.0911742707202222))
body_5.SetRot(chrono.ChQuaterniond(0.482487797827288,8.56013361035306e-16,0.875902691483349,1.65016104995787e-15))
body_5.SetMass(0.00327626318826267)
body_5.SetInertiaXX(chrono.ChVector3d(1.05289038651475e-06,2.08159752619688e-06,1.05258727133488e-06))
body_5.SetInertiaXY(chrono.ChVector3d(4.11892582571888e-12,1.37302075401133e-10,-1.08666822900627e-11))
body_5.SetFrameCOMToRef(chrono.ChFramed(chrono.ChVector3d(-0.0330369529154692,0.00139763186282363,-0.0509441435522752),chrono.ChQuaterniond(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChVisualShapeModelFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_5.AddVisualShape(body_3_1_shape, chrono.ChFramed(chrono.ChVector3d(0,0,0), chrono.ChQuaterniond(1,0,0,0)))

exported_items.append(body_5)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Drone without Propellers Reduced-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_2 , SW name: Propeller CCW-1 ,  SW ref.type:1 (1)
link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.0875453596480283,-0.00626024292193443,0.146328076660421)
dA = chrono.ChVector3d(0,1,3.49148133884313e-15)
cB = chrono.ChVector3d(0.0875453596480283,-0.00627274292193444,0.146328076660421)
dB = chrono.ChVector3d(-2.31727890908672e-30,1,3.49148133884313e-15)
link_1.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.0875453596480283,-0.00626024292193443,0.146328076660421)
cB = chrono.ChVector3d(0.0875453596480283,-0.00627274292193444,0.146328076660421)
dA = chrono.ChVector3d(0,1,3.49148133884313e-15)
dB = chrono.ChVector3d(-2.31727890908672e-30,1,3.49148133884313e-15)
link_2.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Drone without Propellers Reduced-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Propeller CCW-1 ,  SW ref.type:2 (2)
link_3 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.0879805065506803,-0.00626024292193444,0.148789914829983)
cB = chrono.ChVector3d(0.0875453596480283,-0.00626024292193444,0.146328076660421)
dA = chrono.ChVector3d(0,1,3.49148133884313e-15)
dB = chrono.ChVector3d(2.31727890908672e-30,-1,-3.49148133884313e-15)
link_3.Initialize(body_1,body_2,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.0879805065506803,-0.00626024292193444,0.148789914829983)
dA = chrono.ChVector3d(0,1,3.49148133884313e-15)
cB = chrono.ChVector3d(0.0875453596480283,-0.00626024292193444,0.146328076660421)
dB = chrono.ChVector3d(2.31727890908672e-30,-1,-3.49148133884313e-15)
link_4.SetFlipped(True)
link_4.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Drone without Propellers Reduced-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_4 , SW name: Propeller CCW-2 ,  SW ref.type:1 (1)
link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.133885032968031,-0.00626024292193376,-0.0474764528589974)
dA = chrono.ChVector3d(-4.73316543132607e-30,1,3.49148133884313e-15)
cB = chrono.ChVector3d(-0.133885032968031,-0.00626024292193376,-0.0474764528589974)
dB = chrono.ChVector3d(-1.81449275547396e-30,1,3.49148133884313e-15)
link_5.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.133885032968031,-0.00626024292193376,-0.0474764528589974)
cB = chrono.ChVector3d(-0.133885032968031,-0.00626024292193376,-0.0474764528589974)
dA = chrono.ChVector3d(-4.73316543132607e-30,1,3.49148133884313e-15)
dB = chrono.ChVector3d(-1.81449275547396e-30,1,3.49148133884313e-15)
link_6.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Drone without Propellers Reduced-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Propeller CCW-2 ,  SW ref.type:2 (2)
link_7 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.134320179870683,-0.00626024292193375,-0.0499382910285594)
cB = chrono.ChVector3d(-0.133885032968031,-0.00626024292193376,-0.0474764528589974)
dA = chrono.ChVector3d(-4.73316543132607e-30,1,3.49148133884313e-15)
dB = chrono.ChVector3d(1.81449275547396e-30,-1,-3.49148133884313e-15)
link_7.Initialize(body_1,body_4,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.134320179870683,-0.00626024292193375,-0.0499382910285594)
dA = chrono.ChVector3d(-4.73316543132607e-30,1,3.49148133884313e-15)
cB = chrono.ChVector3d(-0.133885032968031,-0.00626024292193376,-0.0474764528589974)
dB = chrono.ChVector3d(1.81449275547396e-30,-1,-3.49148133884313e-15)
link_8.SetFlipped(True)
link_8.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Drone without Propellers Reduced-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_5 , SW name: Propeller CW-1 ,  SW ref.type:1 (1)
link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.133885032968025,-0.00626024292193443,0.146328076660429)
dA = chrono.ChVector3d(-5.78530007598221e-17,1,3.5994194142832e-15)
cB = chrono.ChVector3d(-0.133885032968025,-0.00626024292193447,0.146328076660429)
dB = chrono.ChVector3d(9.27963283560063e-17,-1,-3.71679301303149e-15)
link_9.SetFlipped(True)
link_9.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(-0.133885032968025,-0.00626024292193443,0.146328076660429)
cB = chrono.ChVector3d(-0.133885032968025,-0.00626024292193447,0.146328076660429)
dA = chrono.ChVector3d(-5.78530007598221e-17,1,3.5994194142832e-15)
dB = chrono.ChVector3d(9.27963283560063e-17,-1,-3.71679301303149e-15)
link_10.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Drone without Propellers Reduced-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Propeller CW-1 ,  SW ref.type:2 (2)
link_11 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(-0.136346871137587,-0.00626024292193443,0.145892929757777)
cB = chrono.ChVector3d(-0.133885032968025,-0.00626024292193447,0.146328076660429)
dA = chrono.ChVector3d(-5.78530007598221e-17,1,3.5994194142832e-15)
dB = chrono.ChVector3d(9.27963283560063e-17,-1,-3.71679301303149e-15)
link_11.Initialize(body_1,body_5,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident3")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(-0.136346871137587,-0.00626024292193443,0.145892929757777)
dA = chrono.ChVector3d(-5.78530007598221e-17,1,3.5994194142832e-15)
cB = chrono.ChVector3d(-0.133885032968025,-0.00626024292193447,0.146328076660429)
dB = chrono.ChVector3d(9.27963283560063e-17,-1,-3.71679301303149e-15)
link_12.SetFlipped(True)
link_12.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_12.SetName("Coincident3")
exported_items.append(link_12)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Drone without Propellers Reduced-1 ,  SW ref.type:1 (1)
#   Entity 1: C::E name: body_3 , SW name: Propeller CW-2 ,  SW ref.type:1 (1)
link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.0875453596480235,-0.00626024292193376,-0.0474764528590191)
dA = chrono.ChVector3d(6.95232737629598e-17,1,3.39066411694182e-15)
cB = chrono.ChVector3d(0.0875453596480234,-0.00626024292193377,-0.0474764528590192)
dB = chrono.ChVector3d(9.27963283560056e-17,-1,-3.71679301303149e-15)
link_13.SetFlipped(True)
link_13.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_13.SetName("Concentric4")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(True, True, False, False, False, False)
cA = chrono.ChVector3d(0.0875453596480235,-0.00626024292193376,-0.0474764528590191)
cB = chrono.ChVector3d(0.0875453596480234,-0.00626024292193377,-0.0474764528590192)
dA = chrono.ChVector3d(6.95232737629598e-17,1,3.39066411694182e-15)
dB = chrono.ChVector3d(9.27963283560056e-17,-1,-3.71679301303149e-15)
link_14.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_14.SetName("Concentric4")
exported_items.append(link_14)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Drone without Propellers Reduced-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Propeller CW-2 ,  SW ref.type:2 (2)
link_15 = chrono.ChLinkMateDistanceZ()
cA = chrono.ChVector3d(0.0900071978175855,-0.00626024292193376,-0.0470413059563673)
cB = chrono.ChVector3d(0.0875453596480234,-0.00626024292193377,-0.0474764528590192)
dA = chrono.ChVector3d(6.95232737629598e-17,1,3.39066411694182e-15)
dB = chrono.ChVector3d(9.27963283560056e-17,-1,-3.71679301303149e-15)
link_15.Initialize(body_1,body_3,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident4")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVector3d(0.0900071978175855,-0.00626024292193376,-0.0470413059563673)
dA = chrono.ChVector3d(6.95232737629598e-17,1,3.39066411694182e-15)
cB = chrono.ChVector3d(0.0875453596480234,-0.00626024292193377,-0.0474764528590192)
dB = chrono.ChVector3d(9.27963283560056e-17,-1,-3.71679301303149e-15)
link_16.SetFlipped(True)
link_16.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_16.SetName("Coincident4")
exported_items.append(link_16)


# Auxiliary marker (coordinate system feature)
marker_0_1 = chrono.ChMarker()
marker_0_1.SetName('Coordinate System1')
body_0.AddMarker(marker_0_1)
marker_0_1.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.133885032968031,-0.00626024292193376,-0.0474764528589974),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_2 = chrono.ChMarker()
marker_0_2.SetName('Coordinate System2')
body_0.AddMarker(marker_0_2)
marker_0_2.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.0875453596480235,-0.00626024292193376,-0.0474764528590191),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_3 = chrono.ChMarker()
marker_0_3.SetName('Coordinate System3')
body_0.AddMarker(marker_0_3)
marker_0_3.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(0.0875453596480283,-0.00626024292193444,0.146328076660421),chrono.ChQuaterniond(1,0,0,0)))

# Auxiliary marker (coordinate system feature)
marker_0_4 = chrono.ChMarker()
marker_0_4.SetName('Coordinate System4')
body_0.AddMarker(marker_0_4)
marker_0_4.ImposeAbsoluteTransform(chrono.ChFramed(chrono.ChVector3d(-0.133885032968025,-0.00626024292193444,0.146328076660429),chrono.ChQuaterniond(1,0,0,0)))
