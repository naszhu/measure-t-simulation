import pdfplumber
import os
import sys
from pathlib import Path
import io

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            # Extract text from first few pages to identify the model
            for page in pdf.pages[:10]:  # First 10 pages usually contain model info
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def identify_model_type(text):
    """Identify which transformation type the model uses."""
    text_lower = text.lower()
    
    # Kernel transformation indicators
    kernel_keywords = ['similarity', 'gaussian', 'kernel', 'echo intensity', 'feature matching', 
                      'overlap', 'spreading activation', 'stochastic', 'sampling', 'rem', 
                      'minerva', 'nairne', 'gomez', 'dell', 'usher', 'mcclelland', 'leaky accumulator']
    
    # Push-forward indicators
    pushforward_keywords = ['context drift', 'temporal compression', 'phase transformation', 
                           'position transformation', 'compression', 'tcm', 'simple', 'oscillator',
                           'temporal ratio', 'start-end', 'henson', 'cru', 'logan', 'brown',
                           'deterministic', 'evolution', 'transformation']
    
    # Density change indicators
    density_keywords = ['weighting', 'weight', 'primacy', 'novelty', 'sob', 'todam', 'murdock',
                       'chaining', 'sequential', 'position-based', 'decay', 'rehearsal',
                       'lewandowsky', 'farrell', 'radon-nikodym', 'density']
    
    kernel_score = sum(1 for kw in kernel_keywords if kw in text_lower)
    pushforward_score = sum(1 for kw in pushforward_keywords if kw in text_lower)
    density_score = sum(1 for kw in density_keywords if kw in text_lower)
    
    max_score = max(kernel_score, pushforward_score, density_score)
    if max_score == 0:
        return None
    
    if kernel_score == max_score:
        return 'kernel'
    elif pushforward_score == max_score:
        return 'pushforward'
    else:
        return 'density'

def main():
    reading_stm_dir = r"g:\My Drive\shulai@iu.edu 2022-09-04 14 28\IUB\QUALS\Reading_STM"
    
    pdf_files = sorted(list(Path(reading_stm_dir).glob("*.pdf")))
    
    print(f"Found {len(pdf_files)} PDF files\n")
    
    models_by_type = {'kernel': [], 'pushforward': [], 'density': []}
    
    # Process each PDF
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}] Processing: {pdf_file.name[:60]}...")
        try:
            text = extract_text_from_pdf(str(pdf_file))
            
            # Look for model-related keywords
            keywords = ['model', 'Model', 'kernel', 'Kernel', 'push-forward', 'density', 'measure', 
                       'activation', 'retrieval', 'encoding', 'context', 'similarity', 'weighting',
                       'transformation', 'TCM', 'REM', 'SIMPLE', 'SOB', 'TODAM', 'CRU', 'primacy',
                       'chaining', 'oscillator', 'temporal', 'position']
            
            if any(keyword.lower() in text.lower() for keyword in keywords):
                model_type = identify_model_type(text)
                if model_type:
                    models_by_type[model_type].append((pdf_file.name, text[:1000]))
                    print(f"  -> {model_type.upper()} transformation model")
                else:
                    print(f"  -> Modeling paper (type unclear)")
            else:
                print(f"  -> Not a modeling paper")
        except Exception as e:
            print(f"  -> Error: {str(e)[:50]}")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY:")
    print(f"Kernel transformation models: {len(models_by_type['kernel'])}")
    print(f"Push-forward models: {len(models_by_type['pushforward'])}")
    print(f"Density change models: {len(models_by_type['density'])}")
    
    return models_by_type

if __name__ == "__main__":
    models_by_type = main()

