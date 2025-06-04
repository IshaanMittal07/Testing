from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw

# Define common organic reactions using SMARTS
REACTIONS = {
    "addition": "[C:1]=[C:2].[H][Cl]>>[C:1]([H])[C:2]([Cl])",
    "substitution": "[C:1][Br].[OH-]>>[C:1][OH].[Br-]",
    "elimination": "[C:1][CH2][Br]>>[C:1]=[CH2].[HBr]"
}

def get_products(reactant_smiles, reaction_type):
    if reaction_type not in REACTIONS:
        return f"Reaction type '{reaction_type}' not supported."

    reaction_smarts = REACTIONS[reaction_type]
    rxn = AllChem.ReactionFromSmarts(reaction_smarts)

    reactant = Chem.MolFromSmiles(reactant_smiles)
    if not reactant:
        return "Invalid reactant SMILES."

    products = rxn.RunReactants((reactant,))
    
    if not products:
        return "No products formed."

    product_smiles = [Chem.MolToSmiles(p[0]) for p in products]
    return product_smiles

# Example usage
reactant = "C=C"  # ethene
reaction_type = "addition"

products = get_products(reactant, reaction_type)
print(f"Products of {reaction_type} reaction: {products}")
