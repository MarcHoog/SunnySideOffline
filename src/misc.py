import os


def clean_up_sprite_names(path: str):
    """Clean up the sprite names in the sprite sheet"""
    for file in os.listdir(path): 
        
        new_name = file.split('_')[1] + '.png' 
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
                
                
                
if __name__ == "__main__":
    clean_up_sprite_names('src/content/assets/characters/goblin')