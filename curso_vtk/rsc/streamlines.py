# Streamlines

from vtk import *
import math

reader = vtkStructuredPointsReader()
reader.SetFileName("../data/Wind.vtk")
reader.Update()

# The range and bounds of the data
a,b = reader.GetOutput().GetScalarRange()
xmi, xma, ymi, yma, zmi, zma = reader.GetOutput().GetBounds()

# Color Transfer Function
ctf = vtkLookupTable()
ctf.SetHueRange(0.667, 0.0)
ctf.SetValueRange(1.0, 1.0)
ctf.SetSaturationRange(1.0, 1.0)
ctf.SetTableRange(a,b)

# A plane for the seeds
plane = vtkPlaneSource()
plane.SetOrigin(xmi,math.ceil(ymi),zmi)
plane.SetPoint1(xma,math.ceil(ymi),zmi)
plane.SetPoint2(xmi,math.ceil(ymi),zma)
plane.SetXResolution(100)
plane.SetYResolution(100)

# Streamlines
stream = vtkStreamLine()
stream.SetSourceConnection(plane.GetOutputPort())
stream.SetInputConnection(reader.GetOutputPort())
stream.SetIntegrationDirectionToForward()
stream.SetIntegrator(vtkRungeKutta4())
stream.SetStepLength(0.01)

streamMapper = vtkPolyDataMapper()
streamMapper.SetLookupTable(ctf)
streamMapper.SetInputConnection(stream.GetOutputPort())
streamMapper.SetScalarRange(a,b)
streamActor = vtkActor()
streamActor.SetMapper(streamMapper)
streamActor.GetProperty().SetLineWidth(3.0)

# Add an outline
outline = vtkOutlineFilter()
outline.SetInputConnection(reader.GetOutputPort())

outlineMapper = vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())
outlineActor = vtkActor()

outlineActor.SetMapper(outlineMapper)
outlineActor.GetProperty().SetDiffuseColor(0.8, 0.8, 0.8)
outlineActor.GetProperty().SetLineWidth(2.0)

# Create the Renderer, Window and Interator
ren = vtkRenderer()
ren.SetBackground(0.2, 0.2, 0.2)
ren.AddActor(streamActor)
ren.AddActor(outlineActor)

renWin = vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetWindowName("Wind as Streamlines")
renWin.SetSize(500, 500)

iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()
