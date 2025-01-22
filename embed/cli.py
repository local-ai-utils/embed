import fire
from .main import generate_embeddings

def embed(text: str):
    """
    Generate embeddings for the provided text prompt.
    
    Args:
        text (str): The text to generate embeddings for
    """
    return generate_embeddings(text)

def main():
    fire.Fire(embed)

if __name__ == '__main__':
    main()