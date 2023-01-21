def print_models (unprinted_designs,completed_models):
    while unprinted_designs: 
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design.title()}")
        completed_models.append(current_design)
        
def show_completed_models (completed_models):
    print("\nShowing all completed models: ")
    for completed_model in completed_models: 
        print(completed_model.title())