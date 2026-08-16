echo "Enter the name of the file"

pdflatex -interaction=nonstopmode -halt-on-error example.tex \
  && pdftocairo -svg example.pdf figures/example.svg

rm -rf example.pdf