from typing import Optional, Dict, List

def structure_to_xyz(
    smiles:Optional[str]=None,
    inchi:Optional[str]=None, 
    output_file:Optional[str]=None):
    """
    Convert an InChI string to a .xyz file with atomic coordinates.

    :param smiles: smiles string of the molecule.
    :param inchi: InChI string of the molecule.
    :param output_file: Path to the output .xyz file.
    """

    from rdkit import Chem
    from openbabel import openbabel
    import os
    # Convert InChI to RDKit molecule
    if inchi is not None:
        mol = Chem.MolFromInchi(inchi)
        if mol is None:
            raise ValueError(f"Invalid InChI string {inchi}")
        # Convert RDKit molecule to SMILES
        smiles = Chem.MolToSmiles(mol)

    # Use Open Babel to convert SMILES to XYZ
    obConversion = openbabel.OBConversion()
    obConversion.SetInAndOutFormats("smi", "xyz")

    obmol = openbabel.OBMol()
    obConversion.ReadString(obmol, smiles)
    obmol.AddHydrogens()

    # Optimize the geometry
    builder = openbabel.OBBuilder()
    builder.Build(obmol)

    # Write to XYZ file
    obConversion.WriteFile(obmol, output_file)