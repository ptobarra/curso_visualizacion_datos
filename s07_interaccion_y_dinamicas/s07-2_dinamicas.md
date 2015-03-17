% Dinámicas en visual analytics
% Juan Morales del Olmo
% 17 de marzo de 2015

# Dinámicas para el análisis visual

## Taxonomías de tareas

Muchas propuestas. Por ejemplo:


<div class="multicolumn">
<div>
* 7 tareas [Shneiderman, 96][]
	- Overview
	- Zoom
	- Filter
	- Details-on-demand
	- Relate
	- History
	- Extract
</div>
<div>
* 10 tareas [Stasko, 05][]
	- Retrieve Value
	- Filter
	- Compute Derived Value
	- Find Extremum
	- Sort
	- Determine Range
	- Characterize Distribution
	- Find Anomalies
	- Cluster
	- Correlate
	</div>
</div>

## [Heer y Shneiderman, 2012][]

<div class="multicolumn">

Especificación de datos y vistas
:   - Visualizar
	- Filtrar
	- Ordenar
	- Derivar

Manipulación de las vistas
:   - Seleccionar
	- Navegar
	- Coordinar
	- Organizar

Proceso y procedencia
:   - Registrar
	- Anotar
	- Compartir
	- Guiar

----------

12 tareas en 3 grupos

</div>

<http://queue.acm.org/detail.cfm?id=2146416>



# Visualizar

## Visualizar - Charts

![Excel](../rsc/images/visualizar-chart.png)

## Charts - Programando
<iframe width="100%" height="800" src="http://www.highcharts.com/demo/line-basic" frameborder="1" allowfullscreen>
![[http://www.highcharts.com/demo/line-basic](http://www.highcharts.com/demo/line-basic)](../rsc/images/link.png)

</iframe>

## Visualizar - Flujo de datos

![VisTrails](../rsc/images/vistrails.png)

## Visualizar - Flujo de datos

![Knime](../rsc/images/knime-wf.png)

## Flujo de datos - Programando

<iframe width="100%" height="800" src="http://www.vtk.org/Wiki/VTK/Examples/Cxx/Filters/GaussianSplat" frameborder="1" allowfullscreen>
![[http://www.vtk.org/Wiki/VTK/Examples/Cxx/Filters/GaussianSplat](http://www.vtk.org/Wiki/VTK/Examples/Cxx/Filters/GaussianSplat)](../rsc/images/link.png)

</iframe>

## Visualizar - Gramáticas

![Tableau](../rsc/images/tableau-grammar.jpg)

## Gramáticas - Programando

<iframe width="100%" height="800" src="http://trifacta.github.io/vega/editor/" frameborder="1" allowfullscreen>
![[http://trifacta.github.io/vega/editor/](http://trifacta.github.io/vega/editor/)](../rsc/images/link.png)

</iframe>

# Filtrar

## Filtrar

* Normalmente no se quiere ver toda la información a la vez

* Muy relacionado con la tarea de **Seleccionar**

## Filtrar - Queries dinámicas

![Dinamic Queries](../rsc/images/query-selectors.png)

## Visualizaciones como filtros


![[Crossfilter](<http://square.github.io/crossfilter/>)](../rsc/images/crossfilter.png)





# Ordenar
## Ordenar
<iframe width="100%" height="800" src="http://bl.ocks.org/mbostock/raw/3885705/" frameborder="1" allowfullscreen>
![[http://bl.ocks.org/mbostock/raw/3885705/](http://bl.ocks.org/mbostock/raw/3885705/)](../rsc/images/link.png)

</iframe>

# Derivar

## Hermanar con análisis de datos 

![Outlier detection](../rsc/images/plot_outlier_detection.png)

# Seleccionar

## Selección directa (brushing)

<iframe width="100%" height="800" src="http://bl.ocks.org/mbostock/raw/4063663/" frameborder="1" allowfullscreen>
![[http://bl.ocks.org/mbostock/raw/4063663/](http://bl.ocks.org/mbostock/raw/4063663/)](../rsc/images/link.png)

</iframe>

## Selección directa (lasso)

<iframe width="100%" height="800" src="http://bl.ocks.org/GerHobbelt/raw/3732612/" frameborder="1" allowfullscreen>
![[http://bl.ocks.org/GerHobbelt/raw/3732612/](http://bl.ocks.org/GerHobbelt/raw/3732612/)](../rsc/images/link.png)

</iframe>

## Selección indirecta
<iframe width="100%" height="800" src="http://bl.ocks.org/mbostock/raw/5180185/" frameborder="1" allowfullscreen>
![[http://bl.ocks.org/mbostock/raw/5180185/](http://bl.ocks.org/mbostock/raw/5180185/)](../rsc/images/link.png)

</iframe>

# Navegar

## Navegar es mover la cámara 

* Se usa la metáfora de la cámara.
 
	* En visualizaciones en 3D, la metáfora es directa. **Navegación geométrica**
	
	* En visualizaciones en 2D también puede serlo. (Pan and Zoom) **Navegación geométrica**

* Si cambiamos la representación (diferente de cambiar la proyección)
  de los items según se mueve la cámara estaremos hablando de
  **navegación semántica**

* La navegación se puede considerar una forma de filtrar items

## Zoom geométrico
<iframe width="100%" height="800" src="http://bl.ocks.org/mbostock/raw/3680958/" frameborder="1" allowfullscreen>
![[http://bl.ocks.org/mbostock/raw/3680958/](http://bl.ocks.org/mbostock/raw/3680958/)](../rsc/images/link.png)

</iframe>

## Zoom semántico
<iframe width="100%" height="800" src="http://bl.ocks.org/mbostock/raw/3681006/" frameborder="1" allowfullscreen>
![[http://bl.ocks.org/mbostock/raw/3681006/](http://bl.ocks.org/mbostock/raw/3681006/)](../rsc/images/link.png)

</iframe>

## Foco más contexto

<iframe width="100%" height="800" src="http://bl.ocks.org/mbostock/raw/1667367/" frameborder="1" allowfullscreen>
![[http://bl.ocks.org/mbostock/raw/1667367/](http://bl.ocks.org/mbostock/raw/1667367/)](../rsc/images/link.png)

</iframe>

## Distorsión ojo de pez

<iframe width="100%" height="800" src="http://bost.ocks.org/mike/fisheye/" frameborder="1" allowfullscreen>
![[http://bost.ocks.org/mike/fisheye/](http://bost.ocks.org/mike/fisheye/)](../rsc/images/link.png)

</iframe>

# Coordinar

## Small mulitples views

![Small multiples](../rsc/images/small-multiples.png)

## Vistas múltiples coordinadas

<iframe width="640" height="480" src="http://www.youtube.com/embed/Tzsv6wkZoiQ?rel=0&start=84&end=107" frameborder="1" allowfullscreen>
![[http://www.youtube.com/embed/Tzsv6wkZoiQ?rel=0&start=84&end=107](http://www.youtube.com/embed/Tzsv6wkZoiQ?rel=0&start=84&end=107)](../rsc/images/link.png)

</iframe>

## Brushing and linking

<iframe width="100%" height="800" src="http://bl.ocks.org/mbostock/raw/4063663/" frameborder="1" allowfullscreen>
![[http://bl.ocks.org/mbostock/raw/4063663/](http://bl.ocks.org/mbostock/raw/4063663/)](../rsc/images/link.png)

</iframe>

# Organizar

## Organizar

![GGobi](../rsc/images/ggobi.png)

# Registrar

## Registrar

* Cuando se presenta el resultado de un análisis lo habitual es que se pida **poder explicar** todos los pasos que han llevado a la conclusión

* Si se obtienen datos de **múltiples fuentes** es necesario conocer de dónde vino qué

* Las herramientas de **análisis exploratorio** fomentan la visualización
  de cientos de vistas y configuraciones diferentes. Algunas de ellas
  darán lugar a la creación de **hipótesis**. Tener un **registro** de todo el
  proceso es necesario para no pasar nada por alto.

# Anotar

## Anotar

* El analista debe ser capaz de describir sus ideas o hallazgos en el mismo sitio que surgen
* Permitir resaltar elementos destacados
* Básico para comunicar los resultados

![Anotaciones *in-situ*](../rsc/images/anotaciones.png)

# Compartir

## Compartir

* Exportar las vistas para los informes
* Poder exportar o guardar todos los ajustes para regresar a la visualización concreta
* Interactuar varios analistas a la vez sobre la misma herramienta

# Guiar

## Guiar

<iframe width="100%" height="800" src="http://www.nytimes.com/interactive/2013/02/04/science/girls-lead-in-science-exam-but-not-in-the-united-states.html" frameborder="1" allowfullscreen>
![[http://www.nytimes.com/interactive/2013/02/04/science/girls-lead-in-science-exam-but-not-in-the-united-states.html](http://www.nytimes.com/interactive/2013/02/04/science/girls-lead-in-science-exam-but-not-in-the-united-states.html)](../rsc/images/link.png)

</iframe>








[Shneiderman, 96]: http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=545307&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D545307

[Stasko, 05]: http://www.cc.gatech.edu/~john.stasko/papers/infovis05.pdf

[Heer y Shneiderman, 2012]: https://queue.acm.org/detail.cfm?id=2146416
