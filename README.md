# scivi.web.examples
Examples of the SciVi platform usage, part of SciVi.Tools project

# Essentials
The set of different knowledge bases from various projects is in `kb`. The implementations of corresponding operators
are in `lib`. The typical dataflow diagrams are in `preset`.

# Quick start
1. Compile SciVi:
```
cd scivi.web
npm install
make release
```

2. Install needed Python virtual environment:
```
./setup.py
```

3. Run the server
```
source .venv/bin/activate
./run.sh
```

4. Open some data flow diagram, for example the one to view an ontogenesis of *Titanophoneus potens*.
http://localhost:5555/paleo?preset=titanophone.json.gz

Here, `paleo` is the name of the knowledge base (see subdirectories of `kb`) and `titanophone.json.gz` is the file with
a data flow diagram to open. So, to open one, you have to know the corresponding knowledge base.
