#!/bin/bash

if [[ "$1" != "clean" ]]; then
    pdflatex master-thesis
    biber master-thesis
    pdflatex master-thesis
    pdflatex master-thesis
else
    rm -f master-thesis.{aux,log,pdf,bcf,blg,run.xml,bbl,tct,toc}
fi
