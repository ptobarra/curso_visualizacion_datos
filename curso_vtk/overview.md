% VTK
% Juan Morales del Olmo
% 3 de mayo de 2016


# Overview #

## ¿Qué es VTK? ##

* Visualization Toolkit
* Creada para el proyecto "Visible Humand"
* Creada por Kitware. Totalmente OpenSource.
* Libería de visualización de datos científicos en C++ 
* Bindings para otros lenguajes como Python


--------------------------------------------------------------------------

## Arquitectura

- Pipeline de Datos --> Pipeline Gráfico

- SetInputConnection()
- GetOutputPort()

- Cada filtro cachea salida
	- Update y Modified

--------------------------------------------------------------------------

## Pipeline

![](rsc/pipeline.svg)

--------------------------------------------------------------------------

## Sources

- Punto de inicio de los datos

- Leídos desde archivos (Readers)
	- Formatos poligonales: [ObjReader](http://www.vtk.org/doc/release/6.3/html/classvtkOBJReader.html)
	- Imágenes: [PNGReader](http://www.vtk.org/doc/release/6.3/html/classvtkPNGReader.html)

- Datos Generados
	- Cuerpos 3D: [vtkSphereSource](http://www.vtk.org/doc/release/6.3/html/classvtkSphereSource.html)
	- Funciones Implícitas: [vtkSphere](http://www.vtk.org/doc/release/6.3/html/classvtkSphere.html)

--------------------------------------------------------------------------

## Cell Types 

![](rsc/celltypes.png)

--------------------------------------------------------------------------

## Data Objects 

![](rsc/datatypes.jpg)

--------------------------------------------------------------------------

## Filters

- Modifican los DataObjects

- Su uso es opcional, pero gran parte de la potencia de VTK está en
  los filtros

- Pueden transformar de unos tipos a otros: [MarchingCubes](http://www.vtk.org/doc/release/6.3/html/classvtkMarchingCubes.html)

--------------------------------------------------------------------------

## Mappers

- Unen el pipeline de datos al de visualizacíón

- Controlan la visibilidad de los escalares:
		- mapper.ScalarVisibilityOff()

- Controlan el mapping de colorres>
		- mapper.SetLookupTable(lut)
	
--------------------------------------------------------------------------

## Actors

- Posicionan al elemento en la escena

- Controlan algunas propiedades visuales:
	- `SetOpacity`		
	- `SetColor`	
	- `SetDiffuseColor`
	- `SetLineWidth`

--------------------------------------------------------------------------

## Renderers

- Controlan el proceso de renderizado

- Contienen los actores a renderizar

- Contienen las luces y la cámara activa

--------------------------------------------------------------------------

## WindowRenderer

- Abstrae el abrir una ventana en las diferentes plataformas

- No necesario si el render es OffScreen y se quiere guardar a disco

--------------------------------------------------------------------------

## WindowRendererInteraction

- Añade posibilidades de interacción a la ventana

- Permite fácil navegación por la escena

- Varios estilos de navegación

- Permite interactuar con Widgets añadidos a la escena

# Programando con VTK

## Hola Mundo

```
coneSource = vtk.vtkConeSource()
coneSource.SetResolution(10)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(coneSource.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
 
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
 
renderWindow.Render()
renderWindowInteractor.Start()
```

## Ejercicios

- Completa los [ejercicios](rsc/codigo/Enunciado+Ejercicios.html) propuestos


