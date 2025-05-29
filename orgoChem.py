import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw

def draw_molecule_from_name(name):
    try:
        # Get compound data from PubChem
        compound = pcp.get_compounds(name, 'name')
        if not compound:
            print(f"Could not find molecule for name: {name}")
            return
        
        smiles = compound[0].isomeric_smiles
        print(f"SMILES for {name}: {smiles}")

        # Convert SMILES to RDKit molecule
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print("Error converting SMILES to molecule.")
            return
        
        # Draw molecule
        img = Draw.MolToImage(mol, size=(300, 300))
        img.show()
        
    except Exception as e:
        print(f"Error: {e}")

# Example usage
draw_molecule_from_name("butanol");
draw_molecile_from_name("ethanol");
