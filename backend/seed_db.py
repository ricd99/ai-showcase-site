from database import SessionLocal, engine, Base
from models import Project

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data
db.query(Project).delete()

# Add initial projects
projects = [
    Project(
        title="Micrograd",
        short_description="A tiny autograd engine implementing backpropagation",
        detailed_description="Built a scalar-valued autograd engine from scratch, following Andrej Karpathy's micrograd tutorial. Implements automatic differentiation for building and training neural networks with a PyTorch-like API. Includes forward and backward passes, gradient computation, and a simple neural network implementation.",
        image_url="https://via.placeholder.com/400x300?text=Micrograd",
        tech_stack=["Python", "NumPy", "Matplotlib"],
    ),
    Project(
        title="Makemore - Bigram Model",
        short_description="Character-level language model using bigrams",
        detailed_description="Implemented a bigram character-level language model that predicts the next character based on the previous one. Trained on a dataset of names to generate new, realistic-sounding names. Explored probability distributions and sampling techniques.",
        image_url="https://via.placeholder.com/400x300?text=Makemore+Bigram",
        tech_stack=["Python", "PyTorch", "Matplotlib"],
    ),
    Project(
        title="Makemore - MLP",
        short_description="Multi-layer perceptron for name generation",
        detailed_description="Built a multi-layer perceptron (MLP) neural network for character-level language modeling. Improved upon the bigram model by considering multiple previous characters. Implemented batch normalization, weight initialization strategies, and explored the training dynamics of deep networks.",
        image_url="https://via.placeholder.com/400x300?text=Makemore+MLP",
        tech_stack=["Python", "PyTorch", "NumPy"],
    ),
    Project(
        title="GPT from Scratch",
        short_description="Transformer-based language model implementation",
        detailed_description="Implemented a GPT-style transformer model from scratch, including multi-head self-attention, positional encodings, and layer normalization. Trained on character-level text data to generate coherent sequences. Explored attention mechanisms and the architecture that powers modern LLMs.",
        image_url="https://via.placeholder.com/400x300?text=GPT",
        tech_stack=["Python", "PyTorch", "Transformers"],
    ),
    Project(
        title="Neural Network Visualizer",
        short_description="Interactive visualization of neural network training",
        detailed_description="Created an interactive web application to visualize how neural networks learn. Shows forward propagation, backpropagation, weight updates, and decision boundaries in real-time. Helps build intuition for how gradient descent optimizes neural networks.",
        image_url="https://via.placeholder.com/400x300?text=NN+Visualizer",
        tech_stack=["Python", "JavaScript", "D3.js", "Flask"],
    ),
    Project(
        title="Tokenizer Implementation",
        short_description="BPE tokenizer built from scratch",
        detailed_description="Implemented Byte Pair Encoding (BPE) tokenization algorithm used in GPT models. Includes training vocabulary from text corpus, encoding/decoding text, and handling special tokens. Essential understanding for working with modern language models.",
        image_url="https://via.placeholder.com/400x300?text=Tokenizer",
        tech_stack=["Python", "Regex"],
    ),
]

for project in projects:
    db.add(project)

db.commit()
db.close()

print("Database seeded successfully!")
