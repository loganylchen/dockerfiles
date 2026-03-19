# Meeko

Interface for AutoDock

## Description

Meeko prepares the input for AutoDock and processes its output. It is developed alongside AutoDock-GPU and AutoDock-Vina. Meeko parameterizes both small organic molecules (ligands) and proteins and nucleic acids (receptors).

## Usage

### Prepare Ligand

```bash
mk_prepare_ligand.py -i molecule.sdf -o molecule.pdbqt
```

### Prepare Receptor

```bash
# Basic preparation
mk_prepare_receptor.py -i receptor.pdb -o receptor.pdbqt

# With flexible sidechain
mk_prepare_receptor.py -i receptor.pdb -o my_receptor -j -p -f A:42
```

### Export Results

```bash
mk_export.py vina_results.pdbqt -j my_receptor.json -s lig_docked.sdf -p rec_docked.pdb
```

## Python API

```python
from meeko import MoleculePreparation

# Prepare a molecule
mol_prep = MoleculePreparation()
mol_prep.prepare(molecule)
```

## Documentation

- Official docs: https://meeko.readthedocs.io

## Version

- 0.7.1

## References

- GitHub: https://github.com/forlilab/Meeko
- PyPI: https://pypi.org/project/meeko/
