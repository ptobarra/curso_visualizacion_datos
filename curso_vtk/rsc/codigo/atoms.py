import vtk
import string

def readPoints(filename):
    points = vtk.vtkPoints()
    file = open(filename)

    line = file.readline()
    while line:
        data = string.split(line)

        if data and data[0] != '#':
            x, y, z = float(data[0]), float(data[1]), float(data[2])
            points.InsertNextPoint(x, y, z)
        line = file.readline()
    return points;

def readScalars(filename):
    scalars = vtk.vtkFloatArray()
    file = open(filename)

    line = file.readline()
    while line:
        data = string.split(line)
        if data and data[0] != '#':
            x= float(data[0])
            scalars.InsertNextValue(x)
        line = file.readline()
    return scalars;


def readConnections(filename):
    connections=vtk.vtkCellArray()
    file = open(filename)

    line = file.readline()
    while line:
        data = string.split(line)
        if data and data[0] != '#':
            a, b = int(data[0]), int(data[1])
            connections.InsertNextCell(2)
            connections.InsertCellPoint(a)
            connections.InsertCellPoint(b)
        line = file.readline()
    return connections


# Read the data into a vtkPolyData using the functions in ReadPoints.py
data = vtk.vtkPolyData()

data.SetPoints(readPoints("../../data/atoms-coordinates.txt"))
data.GetPointData().SetScalars(readScalars("../../data/atoms-radius.txt"))
data.SetLines(readConnections("../../data/atoms-connections.txt"))

# Put spheres at each point in the dataset.
# The size and color of a sphere is determined by the
# scalar value (radius) of the corresponding point.

ball = vtk.vtkSphereSource()
ball.SetRadius(0.25)
ball.SetThetaResolution(8)
ball.SetPhiResolution(8)

ballGlyph = vtk.vtkGlyph3D()
ballGlyph.SetInputData(data)
ballGlyph.SetSourceConnection(ball.GetOutputPort())
ballGlyph.SetScaleModeToScaleByScalar()
ballGlyph.SetColorModeToColorByScalar()
ballGlyph.SetScaleFactor(2.0)

colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(0.37, 1.0, 1.0, 1.0)
colorTransferFunction.AddRGBPoint(0.68, 1.0, 1.0, 0.0)
colorTransferFunction.AddRGBPoint(0.73, 0.0, 0.0, 1.0)
colorTransferFunction.AddRGBPoint(0.74, 1.0, 0.0, 0.0)
colorTransferFunction.AddRGBPoint(0.77, 0.0, 0.0, 1.0)
colorTransferFunction.AddRGBPoint(2.0, 0.0, 1.0, 0.0)

ballMapper = vtk.vtkPolyDataMapper()
ballMapper.SetInputConnection(ballGlyph.GetOutputPort())
ballMapper.SetLookupTable(colorTransferFunction)

ballActor = vtk.vtkActor()
ballActor.SetMapper(ballMapper)

#Create tubes between connected molecules
tubeFilter = vtk.vtkTubeFilter()
tubeFilter.SetInputData(data)
tubeFilter.SetRadius(0.15)
tubeFilter.SetNumberOfSides(7)

tubeMapper = vtk.vtkPolyDataMapper()
tubeMapper.SetInputConnection(tubeFilter.GetOutputPort())

# We want to be able to set the color ourselves!
tubeMapper.ScalarVisibilityOff()

tubeActor = vtk.vtkActor()
tubeActor.SetMapper(tubeMapper)
tubeActor.GetProperty().SetColor(0.8,0.8,0.8)

tubeActor.GetProperty().SetSpecularColor(1, 1, 1)
tubeActor.GetProperty().SetSpecular(0.3)
tubeActor.GetProperty().SetSpecularPower(20)
tubeActor.GetProperty().SetAmbient(0.2)
tubeActor.GetProperty().SetDiffuse(0.8)

# A Bounding box
outlineData = vtk.vtkOutlineFilter()
outlineData.SetInputConnection(ballGlyph.GetOutputPort())

outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outlineData.GetOutputPort())

outlineActor = vtk.vtkActor()
outlineActor.SetMapper(outlineMapper)
outlineActor.GetProperty().SetColor(0, 0, 0)

# Create the Renderer, Window and Interator
ren = vtk.vtkRenderer()
ren.AddActor(ballActor)
ren.AddActor(outlineActor)
ren.AddActor(tubeActor)
ren.SetBackground(0.4, 0.4, 0.4)

#vtk_show(ren)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetWindowName("Atoms")
renWin.SetSize(600, 600)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()
