# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XDMF Reader'
tp8faultxdmf = XDMFReader(FileNames=['/import/freenas-m-05-seissol/dli/Alaska2021/result1/tp8-fault.xdmf'])
tp8faultxdmf.CellArrayStatus = ['ASl', 'DS', 'Mud', 'PSR', 'P_f', 'P_n', 'Pn0', 'RT', 'SRd', 'SRs', 'Sld', 'Sls', 'StV', 'T_d', 'T_s', 'Td0', 'Tmp', 'Ts0', 'Vr', 'partition', 'u_n']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on tp8faultxdmf
tp8faultxdmf.GridStatus = ['step_000000000000', 'step_000000000001', 'step_000000000002', 'step_000000000003', 'step_000000000004', 'step_000000000005', 'step_000000000006', 'step_000000000007', 'step_000000000008', 'step_000000000009', 'step_000000000010', 'step_000000000011', 'step_000000000012', 'step_000000000013', 'step_000000000014', 'step_000000000015', 'step_000000000016', 'step_000000000017', 'step_000000000018', 'step_000000000019', 'step_000000000020', 'step_000000000021', 'step_000000000022', 'step_000000000023', 'step_000000000024', 'step_000000000025', 'step_000000000026', 'step_000000000027', 'step_000000000028', 'step_000000000029', 'step_000000000030', 'step_000000000031', 'step_000000000032', 'step_000000000033', 'step_000000000034', 'step_000000000035', 'step_000000000036', 'step_000000000037', 'step_000000000038', 'step_000000000039', 'step_000000000040', 'step_000000000041', 'step_000000000042', 'step_000000000043', 'step_000000000044', 'step_000000000045', 'step_000000000046', 'step_000000000047', 'step_000000000048', 'step_000000000049', 'step_000000000050', 'step_000000000051', 'step_000000000052', 'step_000000000053', 'step_000000000054', 'step_000000000055', 'step_000000000056', 'step_000000000057', 'step_000000000058', 'step_000000000059', 'step_000000000060', 'step_000000000061', 'step_000000000062', 'step_000000000063', 'step_000000000064', 'step_000000000065', 'step_000000000066', 'step_000000000067', 'step_000000000068', 'step_000000000069', 'step_000000000070', 'step_000000000071', 'step_000000000072', 'step_000000000073', 'step_000000000074', 'step_000000000075', 'step_000000000076', 'step_000000000077', 'step_000000000078', 'step_000000000079', 'step_000000000080', 'step_000000000081', 'step_000000000082', 'step_000000000083', 'step_000000000084', 'step_000000000085', 'step_000000000086', 'step_000000000087', 'step_000000000088', 'step_000000000089', 'step_000000000090', 'step_000000000091', 'step_000000000092', 'step_000000000093', 'step_000000000094', 'step_000000000095', 'step_000000000096', 'step_000000000097', 'step_000000000098', 'step_000000000099', 'step_000000000100', 'step_000000000101', 'step_000000000102', 'step_000000000103', 'step_000000000104', 'step_000000000105', 'step_000000000106', 'step_000000000107', 'step_000000000108', 'step_000000000109', 'step_000000000110', 'step_000000000111', 'step_000000000112', 'step_000000000113', 'step_000000000114', 'step_000000000115', 'step_000000000116', 'step_000000000117', 'step_000000000118', 'step_000000000119', 'step_000000000120', 'step_000000000121', 'step_000000000122', 'step_000000000123', 'step_000000000124', 'step_000000000125', 'step_000000000126', 'step_000000000127', 'step_000000000128', 'step_000000000129', 'step_000000000130', 'step_000000000131', 'step_000000000132', 'step_000000000133', 'step_000000000134', 'step_000000000135', 'step_000000000136', 'step_000000000137', 'step_000000000138', 'step_000000000139', 'step_000000000140']

# get active view
renderView2 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView2.ViewSize = [1482, 799]

# show data in view
tp8faultxdmfDisplay = Show(tp8faultxdmf, renderView2)

# get color transfer function/color map for 'partition'
partitionLUT = GetColorTransferFunction('partition')

# get opacity transfer function/opacity map for 'partition'
partitionPWF = GetOpacityTransferFunction('partition')

# trace defaults for the display properties.
tp8faultxdmfDisplay.Representation = 'Surface'
tp8faultxdmfDisplay.AmbientColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.ColorArrayName = ['CELLS', 'partition']
tp8faultxdmfDisplay.LookupTable = partitionLUT
tp8faultxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
tp8faultxdmfDisplay.SelectOrientationVectors = 'None'
tp8faultxdmfDisplay.ScaleFactor = 33890.296636
tp8faultxdmfDisplay.SelectScaleArray = 'partition'
tp8faultxdmfDisplay.GlyphType = 'Arrow'
tp8faultxdmfDisplay.GlyphTableIndexArray = 'partition'
tp8faultxdmfDisplay.GaussianRadius = 1694.5148318
tp8faultxdmfDisplay.SetScaleArray = [None, '']
tp8faultxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
tp8faultxdmfDisplay.OpacityArray = [None, '']
tp8faultxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
tp8faultxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
tp8faultxdmfDisplay.SelectionCellLabelFontFile = ''
tp8faultxdmfDisplay.SelectionPointLabelFontFile = ''
tp8faultxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
tp8faultxdmfDisplay.ScalarOpacityFunction = partitionPWF
tp8faultxdmfDisplay.ScalarOpacityUnitDistance = 5114.894452155798

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tp8faultxdmfDisplay.OSPRayScaleFunction.Points = [2.984462091089798e-15, 0.0, 0.5, 0.0, 10.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tp8faultxdmfDisplay.ScaleTransferFunction.Points = [2.984462091089798e-15, 0.0, 0.5, 0.0, 10.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tp8faultxdmfDisplay.OpacityTransferFunction.Points = [2.984462091089798e-15, 0.0, 0.5, 0.0, 10.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tp8faultxdmfDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.DataAxesGrid.XTitleFontFile = ''
tp8faultxdmfDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.DataAxesGrid.YTitleFontFile = ''
tp8faultxdmfDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.DataAxesGrid.ZTitleFontFile = ''
tp8faultxdmfDisplay.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.DataAxesGrid.XLabelFontFile = ''
tp8faultxdmfDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.DataAxesGrid.YLabelFontFile = ''
tp8faultxdmfDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tp8faultxdmfDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.PolarAxes.PolarAxisTitleFontFile = ''
tp8faultxdmfDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.PolarAxes.PolarAxisLabelFontFile = ''
tp8faultxdmfDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
tp8faultxdmfDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tp8faultxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView2.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
tp8faultxdmfDisplay.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView2.Update()

animationScene1.GoToLast()

# set scalar coloring
ColorBy(tp8faultxdmfDisplay, ('CELLS', 'ASl'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partitionLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
tp8faultxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tp8faultxdmfDisplay.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'ASl'
aSlLUT = GetColorTransferFunction('ASl')

# get opacity transfer function/opacity map for 'ASl'
aSlPWF = GetOpacityTransferFunction('ASl')

# get color legend/bar for aSlLUT in view renderView2
aSlLUTColorBar = GetScalarBar(aSlLUT, renderView2)

# change scalar bar placement
aSlLUTColorBar.WindowLocation = 'AnyLocation'
aSlLUTColorBar.Position = [0.7402159244264508, 0.12515644555694622]

# Rescale transfer function
aSlLUT.RescaleTransferFunction(6.98731798968e-21, 30.0)

# Rescale transfer function
aSlPWF.RescaleTransferFunction(6.98731798968e-21, 30.0)

# current camera placement for renderView2
renderView2.CameraPosition = [1496115.0223949999, -1918312.73642, 883947.9748654438]
renderView2.CameraFocalPoint = [1496115.0223949999, -1918312.73642, -33313.93432615]
renderView2.CameraParallelScale = 237404.8514458834

# save screenshot
SaveScreenshot('/import/freenas-m-05-seissol/dli/Alaska2021/Asl-tp8.jpeg', renderView2, ImageResolution=[1482, 799])

# set scalar coloring
ColorBy(tp8faultxdmfDisplay, ('CELLS', 'Pn0'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(aSlLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
tp8faultxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tp8faultxdmfDisplay.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'Pn0'
pn0LUT = GetColorTransferFunction('Pn0')

# get opacity transfer function/opacity map for 'Pn0'
pn0PWF = GetOpacityTransferFunction('Pn0')

# rescale color and/or opacity maps used to exactly fit the current data range
tp8faultxdmfDisplay.RescaleTransferFunctionToDataRange(False, True)

# get color legend/bar for pn0LUT in view renderView2
pn0LUTColorBar = GetScalarBar(pn0LUT, renderView2)

# change scalar bar placement
pn0LUTColorBar.WindowLocation = 'AnyLocation'
pn0LUTColorBar.Position = [0.7658569500674763, 0.08260325406758447]

# set scalar coloring
ColorBy(tp8faultxdmfDisplay, ('CELLS', 'Td0'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pn0LUT, renderView2)

# rescale color and/or opacity maps used to include current data range
tp8faultxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tp8faultxdmfDisplay.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'Td0'
td0LUT = GetColorTransferFunction('Td0')

# get opacity transfer function/opacity map for 'Td0'
td0PWF = GetOpacityTransferFunction('Td0')

# rescale color and/or opacity maps used to exactly fit the current data range
tp8faultxdmfDisplay.RescaleTransferFunctionToDataRange(False, True)

# get color legend/bar for td0LUT in view renderView2
td0LUTColorBar = GetScalarBar(td0LUT, renderView2)

# change scalar bar placement
td0LUTColorBar.WindowLocation = 'AnyLocation'
td0LUTColorBar.Position = [0.7604588394062078, 0.0763454317897372]
td0LUTColorBar.ScalarBarLength = 0.33000000000000007

# set scalar coloring
ColorBy(tp8faultxdmfDisplay, ('CELLS', 'Pn0'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(td0LUT, renderView2)

# rescale color and/or opacity maps used to include current data range
tp8faultxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tp8faultxdmfDisplay.SetScalarBarVisibility(renderView2, True)

# current camera placement for renderView2
renderView2.CameraPosition = [1496115.0223949999, -1918312.73642, 883947.9748654438]
renderView2.CameraFocalPoint = [1496115.0223949999, -1918312.73642, -33313.93432615]
renderView2.CameraParallelScale = 237404.8514458834

# save screenshot
SaveScreenshot('/import/freenas-m-05-seissol/dli/Alaska2021/Pn0-tp8.jpeg', renderView2, ImageResolution=[1482, 799])

#### saving camera placements for all active views

# current camera placement for renderView2
renderView2.CameraPosition = [1496115.0223949999, -1918312.73642, 883947.9748654438]
renderView2.CameraFocalPoint = [1496115.0223949999, -1918312.73642, -33313.93432615]
renderView2.CameraParallelScale = 237404.8514458834

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).