#!/bin/bash
pandoc -t revealjs -s s07_interaccion_y_dinamicas.md -V transition="linear" -V theme="simple" --smart -c style.css --template=template.revealjs -o s7.html
