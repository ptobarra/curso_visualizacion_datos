import vtk
import math

reader = vtk.vtkStructuredPointsReader()
reader.SetFileName("../data/Wind.vtk")
reader.Update()

# The range and bounds of the data
a,b = reader.GetOutput().GetScalarRange()
xmi, xma, ymi, yma, zmi, zma = reader.GetOutput().GetBounds()

# Color Transfer Function
ctf = vtk.vtkLookupTable()
ctf.SetHueRange(0.0, 0.0)
ctf.SetValueRange(1.0, 1.0)
ctf.SetSaturationRange(0.2, 1.0)
ctf.SetTableRange(a,b)

# A plane for the seeds
plane = vtk.vtkPlaneSource()
plane.SetOrigin(xmi,math.ceil(ymi),zmi)
plane.SetPoint1(xma,math.ceil(ymi),zmi)
plane.SetPoint2(xmi,math.ceil(ymi),zma)
plane.SetXResolution(20)
plane.SetYResolution(10)

# Streamlines
stream = vtk.vtkStreamLine()
stream.SetSourceConnection(plane.GetOutputPort())
stream.SetInputConnection(reader.GetOutputPort())
stream.SetIntegrationDirectionToForward()
stream.SetStepLength(0.01)

streamMapper = vtk.vtkPolyDataMapper()
streamMapper.SetLookupTable(ctf)
streamMapper.SetInputConnection(stream.GetOutputPort())
streamMapper.SetScalarRange(a,b)
streamActor = vtk.vtkActor()
streamActor.SetMapper(streamMapper)
streamActor.GetProperty().SetLineWidth(2)

# Add an outline
outline = vtk.vtkOutlineFilter()
outline.SetInputConnection(reader.GetOutputPort())

outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())
outlineActor = vtk.vtkActor()

outlineActor.SetMapper(outlineMapper)
outlineActor.GetProperty().SetDiffuseColor(0.8, 0.8, 0.8)
outlineActor.GetProperty().SetLineWidth(2.0)

# Create the Renderer, Window and Interator
ren = vtk.vtkRenderer()
ren.SetBackground(0.2, 0.2, 0.2)
ren.AddActor(streamActor)
ren.AddActor(outlineActor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(500, 500)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()
