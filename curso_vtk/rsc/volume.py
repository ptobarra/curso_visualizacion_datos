import vtk

reader = vtk.vtkTIFFReader()
reader.SetFileName("../data/asymmetric.tif")

reader.Update()
a,b = reader.GetOutput().GetScalarRange()
print a, b

opacityTransferFunction = vtk.vtkPiecewiseFunction()
opacityTransferFunction.AddPoint(0, 0.0)
opacityTransferFunction.AddPoint(1, 1.0)

palette = vtk.vtkColorSeries()
colorTransferFunction = vtk.vtkDiscretizableColorTransferFunction()
for i in range(int(b)):
    r, g, b = palette.GetColorRepeating(i)
    print r, g, b
    colorTransferFunction.AddRGBPoint(i, r / 255.0, g / 255.0, b / 255.0)

volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(colorTransferFunction)
volumeProperty.SetScalarOpacity(opacityTransferFunction)

compositeFunction = vtk.vtkVolumeRayCastCompositeFunction()
volumeMapper = vtk.vtkVolumeRayCastMapper()
volumeMapper.SetVolumeRayCastFunction(compositeFunction)
volumeMapper.SetInputConnection(reader.GetOutputPort())

volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

# Create the Renderer, Window and Interator
ren = vtk.vtkRenderer()
ren.AddVolume(volume)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(500, 500)

reader2 = vtk.vtkTIFFReader()
reader2.SetFileName("../data/One-third_resolution_stack.tif")
reader2.Update()

plane = vtk.vtkImagePlaneWidget()
plane.SetInputData(reader2.GetOutput())
plane.SetSliceIndex(25)
plane.SetPlaneOrientationToXAxes()
plane.SetPlaneOrientationToYAxes()
plane.SetPlaneOrientationToZAxes()

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

iren.Initialize()

plane.SetInteractor(iren)
plane.EnabledOn()

iren.Start()
